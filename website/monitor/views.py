import json
import datetime
import re
import random
import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.views.generic import DetailView
from django.views.generic.detail import BaseDetailView
from django.core.cache import cache

from device.models import Device
from device.mixins import ConnectSFMixins
from monitor.models import HardwareData, BandwidthData, PortBound, TemperatureData


class MonitorMixin:
    def _get_object_values(self, device):
        """获得对象的字典形式"""
        b = device.__dict__.copy()
        b.pop('_state')
        b.pop('create_time')
        b.pop('device_id')
        b.pop('_device_cache')
        return {
            'create_time':device.create_time.strftime('%H:%M'),
            'value': b
        }

    def _get_now_time(self,_last_time):
        if _last_time:
            return _last_time
        else:
            return datetime.datetime.now()

    def _last_time(self, data_objects, count, timedelta, _last_time=None):
        if data_objects:
            # 返回最后一条的数据创建时间
            return data_objects[count - 1].create_time
        else:
            # 当没有一条数据时返回当前时间的一分钟以前
            return self._get_now_time(_last_time) + datetime.timedelta(minutes=timedelta - timedelta * 2)

    def _get_limit_data(self,_last_time,*args):
        """判断是否是搜索页面使用，因为普通获取和搜索的排序方式不同"""
        data_objects = args[0]
        count = args[1]
        limit = args[2]
        if _last_time:
            # 返回靠近_last_time时间的值
            return data_objects[0:limit]
        else:
            # 取出queryset最后多少条数据  小 << 大
            return data_objects[count - limit:count]
    
    def _append_object_data(self, data_objects):
        """如果没有数据则返回的是一个空列表"""
        return [self._get_object_values(device) for device in data_objects]

    def get_monitor_data(self, data_objects, limit, timedelta=1, _last_time=None):
        """返回监控数据的列表字典，如果对象不够则生成占位"""
        count = data_objects.count()
        if count >= limit:
            return [self._get_object_values(device) for device in self._get_limit_data(_last_time,*(data_objects,count,limit))]
        else:
            _step = timedelta
            last_time = self._last_time(data_objects=data_objects, count=count, timedelta=timedelta, _last_time=_last_time)
            result = self._append_object_data(data_objects)
            # 当数据不够时，使用最后一个对象的时间或者当前的时间来创建占位值
            for _ in range(limit - count):
                # 获得时间
                t = last_time  + datetime.timedelta(minutes=timedelta)
                result.append({'value':0, 'create_time': t.strftime('%H:%M')})
                timedelta += _step
            return result


class MonitorView(LoginRequiredMixin, MonitorMixin, ConnectSFMixins, DetailView):
    """监控视图"""
    model = Device
    template_name = 'monitor.html'


    def get_context_data(self, **kwargs): 
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)
        # 硬件数据
        hardware_data_objects = self.object.monitor_hardwaredata_related.all()
        hardware_data = self.get_monitor_data(hardware_data_objects, 20, 1)
        # 监控首页默认显示第一个绑定端口的流量
        port_object = self.object.monitor_portbound_related.first()
        if port_object:
            bandwidth_data_objects = self.object.monitor_bandwidthdata_related.filter(port=port_object)
        else:
            bandwidth_data_objects = Device.objects.none()
        bandwidth_data = self.get_monitor_data(bandwidth_data_objects, 10, 10)
        # 温度数据
        temperature_data_objects = self.object.monitor_temperaturedata_related.all()
        temperature_data = self.get_monitor_data(temperature_data_objects, 20, 1)
        # 获得当前对象的已绑定端口列表
        ports_of_bound = [port_object.port for port_object in self.object.monitor_portbound_related.all()]
        # 获得当前对象的所有端口配置
        ports = cache.get(self.object.ip + '_port')
        context.update({
            'hardware_data': hardware_data,
            'bandwidth_data': bandwidth_data,
            'temperature_data': temperature_data,
            'devices': Device.objects.order_by('ip'),
            # 排除已绑定的端口
            'ports': [port for port in ports if port[0] not in ports_of_bound],
            'ports_of_bound': ports_of_bound
        })
        return context


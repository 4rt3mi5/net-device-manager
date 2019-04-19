import re
import datetime
import json

from django.views.generic.detail import BaseDetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.core.cache import cache
from django.http import JsonResponse


from device.models import Device
from device.mixins import ConnectSFMixins
from monitor.models import PortBound
from monitor.views import MonitorMixin
from website.settings import BASE_DIR


class GetPort(LoginRequiredMixin, ConnectSFMixins, BaseDetailView):
    """获得设备端口信息"""
    model = Device

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        port = cache.get(self.object.ip + '_port')
        update = request.GET.get('update')
        if update == 'true' or port is None:
            if self.object.ip == '172.16.111.1':
                port = self.ssh_execute_command(command=['display interface brief'])
            else:
                port = self.telnet_execute_command(device=self.object, command=['display interface brief'])
            if isinstance(port, dict):
                return JsonResponse({'error': []})
            ports = []
            for block in port.split('\r\n'):
                line = re.split(r' +', block)
                if len(line) > 5:
                    format_port = [s for s in line if s]
                    if 'up' in format_port[1] and 'up' in format_port[2] and 'Vlanif' not in format_port[0]:
                        ports.append(format_port)
            cache.set(self.object.ip + '_port', ports, 60 * 60 * 24 * 30)
            return JsonResponse({'port': ports})
        else:
            return JsonResponse({'port': port})


class BoundPort(LoginRequiredMixin, BaseDetailView):
    """绑定端口到设备"""
    model = Device

    def get(self, request, *args, **kwargs):
        port = request.GET.get('port')
        obj = PortBound.objects.create(device=self.get_object(), port=port)
        return JsonResponse({'msg': 'success', 'id': obj.id})

    
class GetNewMonitorData(LoginRequiredMixin, BaseDetailView):
    """获得最新的一条信息"""
    model =Device

    def get_hardware_new_data(self, last_data_object, last_time):
        hardware_no_data = {
            'time': '00:00',
            'cpu': 0,
            'memory': 0,
        }
        if last_data_object:
            last_object_time = last_data_object.create_time.strftime('%H:%M')
            if last_time == '00:00' or self.object.monitor_hardwaredata_related.count() < 20 or last_time == last_object_time:
                new_data = hardware_no_data
            else:
                new_data = {
                        'time': last_object_time,
                        'cpu': last_data_object.cpu,
                        'memory': last_data_object.memory,
                    }
        else:
            new_data = hardware_no_data
        return new_data

    def get_temperature_new_data(self, last_data_object, last_time):
        temperature_no_data = {
            'time': '00:00',
            'current': 0,
            'upper': 0,
        }
        if last_data_object:
            last_object_time = last_data_object.create_time.strftime('%H:%M')
            if last_time == '00:00' or self.object.monitor_temperaturedata_related.count() < 20 or last_time == last_object_time:
                new_data = temperature_no_data
            else:
                new_data = {
                        'time': last_object_time,
                        'current': last_data_object.current,
                        'upper': last_data_object.upper,
                    }
        else:
            new_data = temperature_no_data
        return new_data

    def get_bandwidth_new_data(self, last_data_object, last_time):
        bandwidth_no_data = {
            'time': '00:00',
            'upload': 0,
            'download': 0,
        }
        if last_data_object:
            last_object_time = last_data_object.create_time.strftime('%H:%M')
            if last_time == '00:00' or self.object.monitor_bandwidthdata_related.count() < 10 or last_time == last_object_time:
                new_data = bandwidth_no_data
            else:
                new_data = {
                    'time': last_object_time,
                    'upload': last_data_object.upload,
                    'download': last_data_object.download,
                }
        else:
            new_data = bandwidth_no_data
        return new_data

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        data_type = request.GET.get('type')
        last_time = request.GET.get('last_time')
        
        if data_type == 'hardware':
            last_data_object = self.object.monitor_hardwaredata_related.last()
            new_data = self.get_hardware_new_data(last_data_object, last_time)
        elif data_type == 'temperature':
            last_data_object = self.object.monitor_temperaturedata_related.last()
            new_data = self.get_temperature_new_data(last_data_object, last_time)
        elif data_type == 'bandwidth':
            port = request.GET.get('port')
            port_of_bound_object = self.object.monitor_portbound_related.get(port=port)
            last_data_object = self.object.monitor_bandwidthdata_related.filter(port=port_of_bound_object).last()
            new_data = self.get_bandwidth_new_data(last_data_object, last_time)
        return JsonResponse(new_data)


class GetDataRange(LoginRequiredMixin, MonitorMixin, BaseDetailView):
    """获得多少条时间数据"""
    model = Device

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        from_time = request.GET.get('from_time')
        node_length = request.GET.get('node_length')
        data_type = request.GET.get('type')
        _now_date = datetime.datetime.now().strftime('%Y-%m-%d')
        format_time = datetime.datetime.strptime(_now_date + from_time, '%Y-%m-%d%H:%M')
        if data_type == 'hardware':
            data_objects = self.object.monitor_hardwaredata_related.filter(create_time__lte=format_time)
            search_result_data = self.get_monitor_data(data_objects,int(node_length),1)
        elif data_type == 'temperature':
            data_objects = self.object.monitor_temperaturedata_related.filter(create_time__lte=format_time)
            search_result_data = self.get_monitor_data(data_objects,int(node_length),1)
        elif data_type == 'bandwidth':
            port = request.GET.get('port')
            port_of_bound_object = self.get_object().monitor_portbound_related.get(port=port)
            data_objects = self.object.monitor_bandwidthdata_related.filter(create_time__lt=format_time,port=port_of_bound_object)
            search_result_data = self.get_monitor_data(data_objects,int(node_length),10)
        return JsonResponse({'search_result_data':search_result_data})


class GetPortData(LoginRequiredMixin, MonitorMixin, BaseDetailView):
    """获得新端口数据"""
    model = Device

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        labels_length = request.GET.get('labels_length')
        port = request.GET.get('port')
        ports_of_bound_object = self.get_object().monitor_portbound_related.get(port=port)
        data_objects = self.object.monitor_bandwidthdata_related.filter(port=ports_of_bound_object)
        port_data = self.get_monitor_data(data_objects,int(labels_length),10)
        return JsonResponse({'port_data':port_data})



class SearchTimeRange(LoginRequiredMixin, MonitorMixin, BaseDetailView):
    """搜索时间范围"""
    model = Device

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        from_time = request.GET.get('from_time')
        data_type = request.GET.get('type')
        lables_length = request.GET.get('labels_length')
        format_time = datetime.datetime.strptime(from_time,'%Y-%m-%d %H:%M')
        if data_type == 'hardware':
            data_objects = self.object.monitor_hardwaredata_related.filter(create_time__gte=format_time)
            search_result_data = self.get_monitor_data(data_objects,int(lables_length),1,format_time)
        elif data_type == 'temperature':
            data_objects = self.object.monitor_temperaturedata_related.filter(create_time__gte=format_time)
            search_result_data = self.get_monitor_data(data_objects,int(lables_length),1,format_time)
        elif data_type == 'bandwidth':
            port = request.GET.get('port')
            port_of_bound_object = self.get_object().monitor_portbound_related.get(port=port)
            data_objects = self.object.monitor_bandwidthdata_related.filter(create_time__gt=format_time,port=port_of_bound_object)
            search_result_data = self.get_monitor_data(data_objects,int(lables_length),10,format_time)
        return JsonResponse({'search_result_data':search_result_data})


class ChangeThreshold(LoginRequiredMixin, BaseDetailView):
    """更改阈值"""
    model = Device

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        count = request.GET.get('count')
        cpu = request.GET.get('cpu')
        memory = request.GET.get('memory')
        upload = request.GET.get('upload')
        download = request.GET.get('download')
        temperature = request.GET.get('temperature')
        current_config = json.loads(self.object.config)
        current_config.get('threshold')['count'] = count
        current_config.get('threshold')['cpu'] = cpu
        current_config.get('threshold')['upload'] = upload
        current_config.get('threshold')['download'] = download
        current_config.get('threshold')['memory'] = memory
        current_config.get('threshold')['temp'] = temperature
        self.object.config = json.dumps(current_config)
        self.object.save()
        return JsonResponse(current_config)


class CleanData(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        with open(BASE_DIR + '/time.txt') as f:
            time = f.readlines()
        return JsonResponse({'data': time})
        

    def post(self, requst, *args, **kwargs):
        with open(BASE_DIR + '/time.txt', 'w') as f:
            time = requst.POST.get('time')
            f.write(time)
        return JsonResponse({'msg':'更改成功'})
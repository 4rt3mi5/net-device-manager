from django.db import models
from django.utils.translation import ugettext_lazy as _

from device.models import Device


class PortBound(models.Model):
    """绑定需要监控数据流量的端口"""
    port = models.CharField(verbose_name=_('端口'), max_length=64)
    device = models.ForeignKey(verbose_name=_('设备'), to=Device, to_field='id', on_delete=models.CASCADE,
                               related_name='%(app_label)s_%(class)s_related')
    create_time = models.DateTimeField(verbose_name=_('创建时间'), auto_now_add=True)

    class Meta:
        db_table = 'ndm_port_bound'

    def __str__(self):
        return '{}'.format(self.port)

    def __repr__(self):
        return '{}'.format(self.port)


class BaseMonitorData(models.Model):
    device = models.ForeignKey(verbose_name=_('设备'), to=Device, to_field='id',
        related_name='%(app_label)s_%(class)s_related', on_delete=models.CASCADE)
    create_time = models.DateTimeField(verbose_name=_('创建时间'), auto_now_add=True)

    def __repr__(self):
        return self.device.ip

    class Meta:
        abstract = True
        ordering = ['-created_time']


class HardwareData(BaseMonitorData):
    cpu = models.IntegerField(verbose_name=_('cpu使用率'))
    memory = models.IntegerField(verbose_name=_('内存使用率'))

    class Meta:
        db_table = 'ndm_monitor_hardware'


class BandwidthData(BaseMonitorData):
    upload = models.FloatField(verbose_name=_('上传速率'), default=0.0)
    download = models.FloatField(verbose_name=_('下载速率'), default=0.0)
    port = models.ForeignKey(verbose_name=_('端口'), to=PortBound, to_field='id',
                        related_name='%(app_label)s_%(class)s_related', on_delete=models.CASCADE)

    class Meta:
        db_table = 'ndm_monitor_bandwidth'


class TemperatureData(BaseMonitorData):
    current = models.IntegerField(verbose_name=_('当前温度'))
    upper = models.IntegerField(verbose_name=_('最高温度'))

    class Meta:
        db_table = 'ndm_monitor_temperature'


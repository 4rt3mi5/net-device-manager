import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _

from device.models import Device


class RunningConfig(models.Model):
    id = models.UUIDField(verbose_name=_(
        'ID'), default=uuid.uuid4, primary_key=True)
    config = models.TextField(verbose_name=_('配置信息'))
    device = models.ForeignKey(verbose_name=_('设备'), to=Device, to_field='id', on_delete=models.CASCADE,
                               related_name='%(app_label)s_%(class)s_related')
    create_time = models.DateTimeField(
        verbose_name=_('创建时间'), auto_now_add=True)

    class Meta:
        ordering = ['create_time']
        db_table = 'ndm_running_config'

    def __str__(self):
        return '{}'.format(self.id)

    def __repr__(self):
        return '{}'.format(self.id)

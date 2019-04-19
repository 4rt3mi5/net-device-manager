import uuid
import json


from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.cache import cache


class DeviceGroup(models.Model):
    id = models.UUIDField(verbose_name=_('Id'), default=uuid.uuid4, primary_key=True)
    name = models.CharField(verbose_name=_('名称'), max_length=128)
    create_time = models.DateTimeField(verbose_name=_('创建时间'), auto_now_add=True)
    comment = models.TextField(verbose_name=_('备注'), null=True, blank=True)

    class Meta:
        db_table = 'ndm_device_group'
        verbose_name = '设备组'
        verbose_name_plural = '设备组'

    def __repr__(self):
        return '%s' % self.name

    def __str__(self):
        return '%s' % self.name


class DeviceType(models.Model):
    id = models.UUIDField(verbose_name=_('Id'), default=uuid.uuid4, primary_key=True)
    name = models.CharField(verbose_name=_('名称'), max_length=128)
    create_time = models.DateTimeField(verbose_name=_('创建时间'), auto_now_add=True)
    comment = models.TextField(verbose_name=_('备注'), null=True, blank=True)

    class Meta:
        db_table = 'ndm_device_type'
        verbose_name = '设备类型'
        verbose_name_plural = '设备类型'

    def __repr__(self):
        return '%s' % self.name

    def __str__(self):
        return '%s' % self.name


class Device(models.Model):
    id = models.UUIDField(verbose_name=_('ID'), default=uuid.uuid4, primary_key=True)
    ip = models.GenericIPAddressField(verbose_name=_('IP地址'), unique=True)
    username = models.CharField(verbose_name=_('用户名'), max_length=128)
    password = models.CharField(verbose_name=_('密码'), max_length=128)
    group = models.ForeignKey(verbose_name=_('组'), to=DeviceGroup, to_field='id', on_delete=models.CASCADE,
                              related_name='%(app_label)s_%(class)s_related')
    alias = models.CharField(verbose_name=_('别名'), max_length=255, null=True, blank=True)
    create_time = models.DateTimeField(verbose_name=_('创建时间'), auto_now_add=True)
    type = models.ForeignKey(verbose_name=_('型号'), to=DeviceType, to_field='id', on_delete=models.CASCADE,
                              related_name='%(app_label)s_%(class)s_related')
    config = models.TextField(verbose_name=_('配置信息'), default=json.dumps(
        {'threshold':{'cpu':80,'memory':80,'upload':80,'download':80,'temp':80,'count':3}}))
    comment = models.TextField(verbose_name=_('备注'), null=True, blank=True)

    class Meta:
        db_table = 'ndm_device'
        verbose_name = '设备'
        verbose_name_plural = '设备'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.alias:
            self.alias = self.ip
        super().save()

    def get_status(self):
        return True if cache.get(self.ip) else False

    def __repr__(self):
        return '{ip} ({alias})'.format(ip=self.ip, alias=self.alias)

    def __str__(self):
        return '{ip} ({alias})'.format(ip=self.ip, alias=self.alias)
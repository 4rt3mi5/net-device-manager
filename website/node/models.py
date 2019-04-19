import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Node(models.Model):
    DEVICE_TYPE = (
        ('router', '路由器'),
        ('switch', '交换机'),
        ('firewall', '防火墙'),
        ('internet', '广域网'),
        ('lan', '局域网'),
        ('ac', '上网行为管理'),
        ('wlc', '无线控制器'),
        ('sslvpn', 'SSLVPN')
    )
    id = models.UUIDField(verbose_name=_('Id'), default=uuid.uuid4, primary_key=True)
    name = models.CharField(verbose_name=_('节点名称'), max_length=128, help_text=_('英文大小写'))
    show_name = models.CharField(verbose_name=_('显示名称'), max_length=128)
    hint = models.CharField(verbose_name=_('提示信息'), max_length=128, help_text=_('鼠标放到节点时的提示信息，默认ip地址'))
    x = models.IntegerField(verbose_name=_('X 坐标'), default=100)
    y = models.IntegerField(verbose_name=_('Y 坐标'), default=100)
    type = models.CharField(verbose_name=_('设备类型'), max_length=128, choices=DEVICE_TYPE, default='switch')
    create_time = models.DateTimeField(verbose_name=_('创建时间'), auto_now_add=True)
    comment = models.TextField(verbose_name=_('备注'), null=True, blank=True)

    class Meta:
        db_table = 'ndm_node'
        verbose_name = '节点'
        verbose_name_plural = '节点'

    def __repr__(self):
        return '%s' % self.hint

    def __str__(self):
        return '%s' % self.hint


class NodeConnect(models.Model):
    LINE_TYPE = (
        ('reticle', '网线'),
        ('optical', '光纤')
    )
    id = models.UUIDField(verbose_name=_('Id'), default=uuid.uuid4, primary_key=True)
    ip1 = models.ForeignKey(verbose_name=_('IP1'), to=Node, to_field='id',
        related_name='%(app_label)s_%(class)s_related_ip1', on_delete=models.CASCADE)
    ip2 = models.ForeignKey(verbose_name=_('IP2'), to=Node, to_field='id',
        related_name='%(app_label)s_%(class)s_related_ip2', on_delete=models.CASCADE)
    mode = models.CharField(verbose_name=_('连接介质'), max_length=128, choices=LINE_TYPE, default='reticle')
    create_time = models.DateTimeField(verbose_name=_('创建时间'), auto_now_add=True)
    comment = models.TextField(verbose_name=_('备注'), null=True, blank=True)

    class Meta:
        db_table = 'ndm_node_connect'
        verbose_name = '节点连接'
        verbose_name_plural = '节点连接'

    def __repr__(self):
        return '%s<>%s' % (self.ip1, self.ip2)

    def __str__(self):
        return '%s<>%s' % (self.ip1, self.ip2)

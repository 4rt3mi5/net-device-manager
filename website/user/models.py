import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Loginlog(models.Model):
    id = models.UUIDField(verbose_name=_('ID'), default=uuid.uuid4, primary_key=True)
    username = models.CharField(verbose_name=_('用户名'), max_length=20)
    type = models.CharField(verbose_name=_('登录方式'), default='Web', max_length=24)
    ip = models.GenericIPAddressField(verbose_name=_('登录IP'))
    user_agent = models.CharField(verbose_name=_('用户代理'), max_length=254, blank=True, null=True)
    login_time = models.DateTimeField(verbose_name=_('登录时间'))

    class Meta:
        ordering = ['-login_time']
        db_table = 'ndm_login_log'
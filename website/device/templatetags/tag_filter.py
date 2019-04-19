import time
import datetime
import kombu.five
import json

from django import template
from django.core.cache import cache

register = template.Library()

from node.models import Node


@register.filter
def get_status(ip):
    """获得IP的状态"""
    return cache.get(ip)


@register.filter
def get_nodename(ip):
    """根据ip获得到节点的名称"""
    return Node.objects.get(hint=ip).name


@register.filter
def str_to_dict(s):
    """返回设备配置"""
    return json.loads(s).get('running')


@register.filter
def get_port(ip):
    return cache.get(ip + '_port')


@register.filter
def get_key_value(dict, key):
    """获得字典的值"""
    return dict.get(key)


@register.filter
def get_user(ip):
    return cache.get(ip + '_users')


@register.filter
def get_threshold(config, tp):
    return json.loads(config).get('threshold').get(tp)

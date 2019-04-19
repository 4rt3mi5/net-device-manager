from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, TemplateView
from django.core.cache import cache
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse_lazy

from device.models import Device, DeviceGroup
from device.mixins import ConnectwlcMixins


class DeviceListView(LoginRequiredMixin, ListView):
    """设备列表"""
    model = Device
    template_name = 'device_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        group_id = self.request.GET.get('group-id', None)
        if group_id:
            queryset = queryset.filter(group=group_id)
        return queryset


class DeviceGroupListView(LoginRequiredMixin, ListView):
    """设备组列表"""
    model = DeviceGroup
    template_name = 'group_list.html'


class APListView(LoginRequiredMixin, ConnectwlcMixins, TemplateView):
    """AP列表"""
    template_name = 'ap_list.html'

    def get_context_data(self):
        context = super().get_context_data()
        context.update({
            'ap_list': cache.get('ap_list')
        })
        return context

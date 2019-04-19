from django.views.generic import DetailView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache

from device.models import Device
from config.forms import CreateDeviceUserForm


class DisplayRunningConfigView(LoginRequiredMixin, DetailView):
    """显示运行中的全局配置"""
    model = Device
    template_name = 'running_config.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'devices': Device.objects.all()
        })
        return context
        

class DisplayUsersView(LoginRequiredMixin, DetailView):
    """显示设备的用户列表"""
    model = Device
    template_name = 'd_users.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'users': cache.get(self.object.ip + '_users')
        })
        return context


class CreateUsersView(LoginRequiredMixin, FormView):
    """创建用户"""
    template_name = 'create_users.html'
    form_class = CreateDeviceUserForm

    def get_initial(self):
        return {'level': '15', 'service_type': 'telnet'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'devices': Device.objects.all().order_by('ip').exclude(ip='172.16.111.1')})
        return context

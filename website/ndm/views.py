from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.models import User

from node.models import Node, NodeConnect
from device.models import Device
from website.settings import BASE_DIR


class IndexView(LoginRequiredMixin, TemplateView):
    """首页视图"""
    template_name = 'index.html'

    def get_alert_users(self):
        with open(BASE_DIR + '/users.txt') as f:
            users = f.readlines()
        return users

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'users': User.objects.count(),
            'devices': Device.objects.count(),
            'nodes': Node.objects.all(),
            'nodes_connect': NodeConnect.objects.all(),
            'alert_users': self.get_alert_users(),
        })
        return context


class SettingView(LoginRequiredMixin, TemplateView):
    template_name = "setting.html"

    def get_data(self,filename):
        with open(BASE_DIR + '/' + filename) as f:
            return f.readlines()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        users = self.get_data('users.txt')
        time = self.get_data('time.txt')
        context.update({'users':[user.strip() for user in users],'clean_time':time})
        print(context)
        return context
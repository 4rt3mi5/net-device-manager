import json
import os
import sys
import datetime
import difflib
import uuid

from django.views.generic.detail import BaseDetailView
from django.views.generic import View, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse

from device.models import Device
from config.models import RunningConfig
from device.mixins import ConnectSFMixins
from website.settings import BASE_DIR


class GetConfigDetail(LoginRequiredMixin, ConnectSFMixins, BaseDetailView):
    model = Device

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        _config_object = self.object.config_runningconfig_related.last()
        if not _config_object:
            return JsonResponse({'error': '没有配置信息'})
        detail = model_to_dict(self.object, exclude=['password', 'username'])
        detail['_config_create_time'] = datetime.datetime.strftime(_config_object.create_time, '%Y年%-m月%-d日 %H:%M')
        detail['_config_config'] = json.loads(_config_object.config).get('running')
        detail['_config_id'] = str(_config_object.id)
        return JsonResponse(detail)


class GetRunningConfig(LoginRequiredMixin, ConnectSFMixins, BaseDetailView):
    model = Device

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        update = request.GET.get('update')
        if self.object.config_runningconfig_related.count() == 0 or update == 'true':
            if self.object.ip == '172.16.111.1':
                result = self.ssh_execute_command(command=['dis cu'])
            else:
                result = self.telnet_execute_command(device=self.object, command=['dis cu'])
            if not isinstance(result, dict):
                RunningConfig.objects.create(config=json.dumps({'running':result}), device=self.object)
                return JsonResponse({'running': result})
            else:
                return JsonResponse({'error': result['error']})
        else:
            return JsonResponse(json.loads(self.object.config_runningconfig_related.last().config))
        

class DiffContext(LoginRequiredMixin, View):

    def make_file(self, string):
        fid = str(uuid.uuid4())
        with open(BASE_DIR + '/difftmp/' + fid + '.html','w') as f:
            f.write(string)
        return fid

    def get(self, request, *args, **kwargs):
        conf1 = request.GET.get('conf1')
        conf2 = request.GET.get('conf2')
        if not conf1 or not conf2:
            return JsonResponse({'msg':'参数不正确'})
        obj1 = RunningConfig.objects.get(id=conf1)
        obj2 = RunningConfig.objects.get(id=conf2)
        c1 = json.loads(obj1.config).get('running').split('\r\n')
        c2 = json.loads(obj2.config).get('running').split('\r\n')
        diff = difflib.HtmlDiff()
        fid = self.make_file(diff.make_file(c1, c2))
        return JsonResponse({'uuid': fid})


class ReadDiff(LoginRequiredMixin, TemplateView):

    def get_template_names(self):
        fid = self.request.GET.get('uuid')
        return fid + '.html'

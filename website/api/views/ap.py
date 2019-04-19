import re

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from device.mixins import ConnectwlcMixins
from django.core.cache import cache
from django.http import JsonResponse


class APlist(LoginRequiredMixin, ConnectwlcMixins, View):
    def format_data(self, data):
        lines = data.split('\r\n\r\n')[1].split('---\r\n')[1].split('\r\n')
        blocks = [[s.strip() for s in line.split('  ') if s] for line in lines]
        return blocks

    def get(self, request, *args, **kwargs):
        ap_list = cache.get('ap_list')
        update = request.GET.get('update')
        ap_list = (False if update else ap_list)
        if ap_list:
            self.result = ap_list
        else:
            ap_summary = self.execute_command(command=['show ap summary'])
            ap_lists = ap_summary.get('result')
            if not ap_lists:
                return JsonResponse({'msg':ap_summary.get('error')})
            self.result = self.format_data(ap_lists)
            cache.set('ap_list', self.result, 60 * 10)
        return JsonResponse({'msg': self.result})


class SearchClientAddress(LoginRequiredMixin, ConnectwlcMixins, View):
    """搜索动作，返回数据字典"""

    def get_detail(self, mac_address):
        client_detail = self.execute_command(
            command=['show client detail {mac}'.format(mac=mac_address)])
        data = client_detail.get('result')
        if 'Invalid client MAC address provided' in data:
            return {'error': '无效的Mac或者未找到'}
        sub_string = re.sub(r'\.+', ':', data)
        split_string = sub_string.split('\r\n')
        detail = {}
        for string in split_string:
            if string:
                try:
                    key, value = string.split(':', 1)
                    detail[key.strip()] = value.strip()
                except:
                    continue
        return detail

    def get(self, request, *args, **kwargs):
        mac = request.GET.get('mac')
        detail = self.get_detail(mac)
        return JsonResponse(detail)


class RebootAP(LoginRequiredMixin, ConnectwlcMixins, View):
    """重启AP"""

    def get(self, request, *args, **kwargs):
        ap_name = request.GET.get('ap_name')
        command_result = self.execute_command(
            command=['config ap reset {ap_name}'.format(ap_name=ap_name), 'y'])
        error = command_result.get('error')
        if not error:
            return JsonResponse({'msg': 'true'})
        else:
            return JsonResponse({'msg': error})

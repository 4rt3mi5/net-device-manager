import re

from django.views.generic.detail import BaseDetailView
from django.views.generic.edit import BaseDeleteView, BaseFormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.http import JsonResponse


from device.mixins import ConnectSFMixins
from device.models import Device
from config.forms import CreateDeviceUserForm


class GetUsers(LoginRequiredMixin, ConnectSFMixins, BaseDetailView):
    """连接设备获得到用户信息"""
    model = Device

    def get_users(self, c, show, bi, ei):
        _users = c.execute_command(['display %s' % show])
        users_lines = [line.strip()
                       for line in _users.split('\r\n') if line][bi:ei]
        users_list = [re.split(r' +', user)[0] for user in users_lines]
        users = {}
        for username in users_list:
            user_info = c.execute_command(
                ['display {show} username {username}'.format(show=show, username=username)])
            lines = [line.strip() for line in user_info.split('\r\n') if line]
            line_split = [re.split(r' +: +', block)
                          for block in lines if ':' in block]
            user_detail = {d[0]: d[1] for d in line_split if len(d) == 2}
            user_detail['username'] = username
            users[username] = user_detail
        return users

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        users = cache.get(self.object.ip + '_users')
        update = request.GET.get('update')
        if update == 'true' or users is None:
            # if self.object.ip == '172.16.111.1':
            #     users = self.get_users(self.get_ssh_c(
            #         ip='172.16.111.1', username='admin', password='r6HhEyXhNFYz'), 'manager-user', 5, -2)
            # else:
            users = self.get_users(self.get_telnet_c(
                device=self.object), 'local-user', 4, -3)
            if users.get('error'):
                return JsonResponse({'error': {}})
            cache.set(self.object.ip + '_users', users, 60 * 60 * 24 * 30)
            return JsonResponse({'user': users})
        else:
            return JsonResponse({'user': users})


class DeleteUser(LoginRequiredMixin, ConnectSFMixins, BaseDeleteView):
    """删除设备上的一个用户信息"""
    model = Device

    def get(self, request, *args, **kwargs):
        self.username = request.GET.get('username')
        self.object = self.get_object()
        return self.delete(self, request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        # if self.object.ip == '172.16.111.1':
        #     command = ['sys','aaa','undo manager-user %s' % self.username]
        #     self.ssh_execute_command(command=command)
        # else:
        command = ['sys','aaa','undo local-user %s' % self.username]
        self.telnet_execute_command(device=self.object, command=command)
        return JsonResponse({'msg': 'true'})


class CreateUsers(LoginRequiredMixin, ConnectSFMixins, BaseFormView):
    """批量创建用户"""
    form_class = CreateDeviceUserForm
    # ssh_type = ['api','ssh','ftp','telnet','web','terminal']

    def form_invalid(self, form):
        return JsonResponse({'error': form.errors.as_text()})

    def form_valid(self, form):
        result = {'success': [],'failed': []}
        devices_id = form.cleaned_data.pop('devices').split(',')
        devices_objects = Device.objects.filter(id__in=devices_id[:-1])
        for device_object in devices_objects:
            # if device_object.ip == '172.16.111.1':
            #     if form.cleaned_data.get('service_type') not in self.ssh_type:
            #         ser_type = 'ssh'
            #     else:
            #         ser_type = form.cleaned_data.get('service_type')
            #     r = self.ssh_execute_command(command=['sys', 'aaa','manager-user %s' % form.cleaned_data.get('username'),
            #     'password %s %s' % (form.cleaned_data.get('username'), form.cleaned_data.get('password')),
            #     'level %s' % form.cleaned_data.get('level'),'service-type %s' % ser_type])
            # else:
            r = self.telnet_execute_command(command=['sys','aaa','local-user %s password cipher %s' % (form.cleaned_data.get('username'), form.cleaned_data.get('password')),
            'local-user %s privilege level %s' % (form.cleaned_data.get('username'), form.cleaned_data.get('level')), 
            'local-user %s service-type %s' % (form.cleaned_data.get('username'), form.cleaned_data.get('service_type'))],device=device_object)
            if isinstance(r, dict):
                result['failed'].append(device_object.ip)
            else:
                result['success'].append(device_object.ip)
        return JsonResponse(result)


class ChangePassword(LoginRequiredMixin, ConnectSFMixins, BaseDetailView):
    model = Device

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        self.object = self.get_object()
        # if self.object.ip == '172.16.111.1':
        #     r = self.ssh_execute_command(command=['sys','aaa','manager-user %s' % username,'password cipher %s' % password])
        #     if 'Error: The password you entered does not meet the minimum complexity requirement.' in r:
        #         return JsonResponse({'error':'密码不符合复杂性'})
        # else:
        encryp = 'irreversible-cipher'
        r = self.telnet_execute_command(command=['sys','aaa','local-user %s password %s %s' % (username,encryp,password),
        'local-user %s state active' % username],device=self.object)
        if 'The password encryption mode cannot be changed' in r:
            encryp = 'cipher'
            twor = self.telnet_execute_command(command=['sys','aaa','local-user %s password %s %s' % (username,encryp,password),
            'local-user %s state active' % username],device=self.object)
            if 'error' in twor:
                return JsonResponse({'error':r})
        return JsonResponse({'msg':'更新密码成功'})
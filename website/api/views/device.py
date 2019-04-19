import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.contrib import messages
from django.utils import timezone
from django.http import StreamingHttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy

from device.models import Device, DeviceGroup, DeviceType


class DevicedExportView(LoginRequiredMixin, View):
    """设备导出"""

    def get(self, request):
        fields = [
            field for field in Device._meta.fields
            if field.name not in ['create_time', 'id']
        ]
        filename = 'devices-{}.json'.format(
            timezone.now().strftime('%Y-%m-%d_%H-%M-%S')
        )
        devices = {
            device.id.__str__(): {
                field.name: (
                    '%s' % getattr(device, field.name) if field.name in ['group', 'type'] else getattr(device, field.name))
                for field in fields
            }
            for device in Device.objects.all()
        }
        response = StreamingHttpResponse(json.dumps(devices))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{filename}"'.format(
            filename=filename)
        return response


class DeviceImportView(LoginRequiredMixin, View):
    """设备导入"""
    redirect_url = reverse_lazy('device_list')

    def post(self, request, content='', errorList=list()):
        try:
            for line in request.FILES['import'].chunks():
                content += line.decode()
            devices = json.loads(content)
        except:
            messages.error(request, '文件解析失败！')
            return HttpResponseRedirect(self.redirect_url)
        for device in devices.values():
            device_group_obj, created_device_group = DeviceGroup.objects.get_or_create(
                name=device.get('group'))
            device_obj, created_device = Device.objects.get_or_create(
                ip=device.get('ip'),
                alias=device.get('alias'),
                defaults={
                    'type': DeviceType.objects.get(name=device.get('type')),
                    'comment': device.get('comment'),
                    'username': device.get('username'),
                    'password': device.get('password'),
                    'group': device_group_obj,
                })
            if not created_device:
                errorList.append(device.get('ip'))
        return HttpResponseRedirect(self.redirect_url)

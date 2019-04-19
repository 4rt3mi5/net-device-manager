from django.contrib import admin
from device.models import Device, DeviceGroup, DeviceType

# Register your models here.

admin.site.register(DeviceGroup)
admin.site.register(DeviceType)


class DeviceDisplayList(admin.ModelAdmin):
    search_fields = ('ip',)
    list_display = ('ip', 'alias', 'group', 'type', 'config')


admin.site.register(Device, DeviceDisplayList)


# class DisplayList(admin.ModelAdmin):
#     search_fields = ('device__ip',)
#     list_display = ('ip', 'monitor_threshold',)

#     def ip(self, obj):
#         return obj.device.ip


# admin.site.register(DeviceGlobalConfig, DisplayList)

from django.conf.urls import url

from device.views import *

urlpatterns = [
    url(r'^list$', DeviceListView.as_view(), name='device_list'),

    url(r'^group-list$', DeviceGroupListView.as_view(), name='group_list'),

    url(r'^ap-list$', APListView.as_view(), name='ap_list'),
]
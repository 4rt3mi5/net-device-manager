from django.conf.urls import url

from node.views import *

urlpatterns = [
    url(r'^list$', NodeListView.as_view(), name='node_list'),
    url(r'^connect-list$', NodeConnectListView.as_view(), name='connect_list'),
]
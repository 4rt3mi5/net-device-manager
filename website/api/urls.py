from django.conf.urls import url

from api.views import device, ap, config, monitor, users, node, alert

urlpatterns = [
    url(r'^device/export$', device.DevicedExportView.as_view()),
    url(r'^device/import$', device.DeviceImportView.as_view()),

    url(r'^ap/search-client$', ap.SearchClientAddress.as_view()),
    url(r'^ap/reboot$', ap.RebootAP.as_view()),
    url(r'^ap/list$', ap.APlist.as_view()),

    url(r'^config/running/(?P<pk>.+)$', config.GetRunningConfig.as_view()),
    url(r'^config/get-detail/(?P<pk>.+)$', config.GetConfigDetail.as_view()),
    url(r'^config/diff$', config.DiffContext.as_view()),

    url(r'^monitor/get-port/(?P<pk>.+)$', monitor.GetPort.as_view()),
    url(r'^monitor/bound-port/(?P<pk>.+)$', monitor.BoundPort.as_view()),
    url(r'^monitor/new-data/(?P<pk>.+)$', monitor.GetNewMonitorData.as_view()),
    url(r'^monitor/get-range/(?P<pk>.+)$', monitor.GetDataRange.as_view()),
    url(r'^monitor/get-port-data/(?P<pk>.+)$', monitor.GetPortData.as_view()),
    url(r'^monitor/search-time/(?P<pk>.+)$', monitor.SearchTimeRange.as_view()),
    url(r'^monitor/tereshold/(?P<pk>.+)$', monitor.ChangeThreshold.as_view()),
    url(r'^monitor/set-clean-data$', monitor.CleanData.as_view()),

    url(r'^d-user/get/(?P<pk>.+)$', users.GetUsers.as_view()),
    url(r'^d-user/delete/(?P<pk>.+)$', users.DeleteUser.as_view()),
    url(r'^d-user/create$', users.CreateUsers.as_view()),
    url(r'^d-user/change-password/(?P<pk>.+)$', users.ChangePassword.as_view()),

    url(r'^node/getall$', node.GetNodeStatus.as_view()),

    url(r'^alert-user/getall$', alert.AlertUsers.as_view()),
    url(r'^alert-user/delete$', alert.DeleteAlertUser.as_view()),
]
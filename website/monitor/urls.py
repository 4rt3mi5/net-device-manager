from django.conf.urls import url
from monitor.views import MonitorView


urlpatterns = [
    url(r'chart/(?P<pk>.+)$', MonitorView.as_view(), name='monitor')
]
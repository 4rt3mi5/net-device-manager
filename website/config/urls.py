from django.conf.urls import url

from config.views import DisplayRunningConfigView, DisplayUsersView, CreateUsersView

urlpatterns = [
    url(r'^running/(?P<pk>.+)$', DisplayRunningConfigView.as_view(), name='running_config'),

    url(r'^show-users/(?P<pk>.+)$', DisplayUsersView.as_view(), name='d_users'),
    url(r'^create-users$', CreateUsersView.as_view(), name='create_users')
]
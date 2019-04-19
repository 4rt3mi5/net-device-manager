from django.conf.urls import url
from user import views

urlpatterns = [
    url(r'^login$', views.UserLoginView.as_view(), name='login'),
    url(r'^logout$', views.UserLogoutView.as_view(), name='logout'),
    url(r'^login-log$', views.LoginlogListView.as_view(), name='login_log'),
]
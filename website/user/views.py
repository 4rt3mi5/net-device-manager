# Create your views here.

import datetime
import time

from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django import forms
from django.db.models import Q
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView

from user.models import Loginlog


class UserLoginView(LoginView):
    """用户登录"""
    template_name = 'login.html'
    success_url = reverse_lazy('index')

    def get_form(self, form_class=AuthenticationForm):
        """返回更改过后的表单"""
        form = super().get_form(form_class)
        form.fields['username'].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Username"
        })
        form.fields['password'].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Password"
        })
        return form

    def get_success_url(self):
        return self.success_url

    def form_invalid(self, form):
        messages.error(self.request, form.errors.as_text())
        return super().form_invalid(form)

    def form_valid(self, form):
        """获得客户端一些访问信息"""
        print(form.cleaned_data)
        user = form.get_user()
        x_forwarded_for = self.request.META.get(
            'HTTP_X_FORWARDED_FOR', '').split(',')
        if x_forwarded_for and x_forwarded_for[0]:
            login_ip = x_forwarded_for[0]
        else:
            login_ip = self.request.META.get('REMOTE_ADDR', '')
        user_agent = self.request.META.get('HTTP_USER_AGENT', '')
        Loginlog.objects.create(username=user.username, ip=login_ip,
                                user_agent=user_agent, login_time=timezone.now())
        return super().form_valid(form)


class UserLogoutView(LoginRequiredMixin, LogoutView):
    """用户注销"""
    template_name = 'logout.html'


class LoginlogListView(LoginRequiredMixin, ListView):
    """登录日志列表"""
    model = Loginlog
    template_name = 'login_log.html'

    def get_queryset(self):
        """搜索关键字及日期的选择"""
        self.username = self.request.GET.get('username', '')
        self.keyword = self.request.GET.get("keyword", '')
        self.date_from = self.request.GET.get('date_from', None)
        self.date_to = self.request.GET.get('date_to', None)

        queryset = super().get_queryset()
        if self.date_from and self.date_to:
            self.date_from_s = datetime.datetime(
                *(time.strptime(self.date_from + ' 00:00:00', "%Y-%m-%d %H:%M:%S"))[:6])
            self.date_to_s = datetime.datetime(*(time.strptime(self.date_to + ' 23:59:59', "%Y-%m-%d %H:%M:%S"))[:6])
            queryset = queryset.filter(
                login_time__gt=self.date_from_s, login_time__lt=self.date_to_s
            )
        if self.username:
            queryset = queryset.filter(username=self.username)
        if self.keyword:
            queryset = queryset.filter(
                Q(ip__contains=self.keyword) |
                Q(username__contains=self.keyword)
            )
        return queryset

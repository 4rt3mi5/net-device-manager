from django import forms
from django.utils.translation import ugettext_lazy as _


service_type = (
    ('8021x', '8021x'), 
    ('bind', 'bind'),
    ('ftp', 'ftp'), 
    ('http', 'http'), 
    ('ppp', 'ppp'),
    ('ssh', 'ssh'), 
    ('telnet', 'telnet'), 
    ('terminal', 'terminal'), 
    ('web', 'web'),
    ('x25-pad', 'x25-pad'), 
)

class CreateDeviceUserForm(forms.Form):
    """创建设备用户"""
    username = forms.CharField(label=_('用户名'), max_length=64, required=True, 
                                widget=forms.TextInput(attrs={'class': 'form-control'}), help_text=_('* required'))
    password = forms.CharField(label=_('密码'), max_length=64, required=True, 
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    level = forms.ChoiceField(label=_('权限等级'), required=True, 
                                widget=forms.Select(attrs={'class': 'form-control'}), help_text=_('level 15 is super'),
                                choices=tuple([(n, 'level %s' % n) for n in range(16)]))
    service_type = forms.ChoiceField(label=_('访问类型'), required=True,
                                widget=forms.Select(attrs={'class': 'form-control'}), help_text=('allow access source type'), 
                                choices=service_type)
    devices = forms.CharField(label=_('设备列表'), required=False, widget=forms.TextInput())
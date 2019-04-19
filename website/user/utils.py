from django.contrib.auth.models import User


def init_usermodel():
    """初始化一个用户"""
    User.objects.create_superuser(username='admin', email='admin@yixia.com', password='yixia123')
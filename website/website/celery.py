from __future__ import absolute_import

import os

from celery import Celery
from django.conf import settings
from celery import platforms

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')

app = Celery('webite', backend='redis://127.0.0.1:6379/0',
             broker='redis://127.0.0.1:6379/0')
app.config_from_object('django.conf:settings')
platforms.C_FORCE_ROOT = True       #允许使用root用户启动uwsgi
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

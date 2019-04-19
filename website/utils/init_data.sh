#!/usr/bin/env bash

python3 ../manage.py shell << EOF
from user.utils import init_usermodel
init_usermodel()
from device.utils import init_typemodel
init_typemodel()
from monitor.utils import init_crontab, init_tasks
init_crontab()
init_tasks()
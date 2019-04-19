import requests
import time

from djcelery.models import CrontabSchedule
from djcelery.models import PeriodicTask


def init_crontab():
    """创建计划时间"""
    CrontabSchedule.objects.create(
        id=1, minute='*/1', hour='*', day_of_week='*', day_of_month='*', month_of_year='*')
    CrontabSchedule.objects.create(
        id=2, minute='*/10', hour='*', day_of_week='*', day_of_month='*', month_of_year='*')
    CrontabSchedule.objects.create(
        id=3, minute='*/30', hour='*', day_of_week='*', day_of_month='*', month_of_year='*')
    CrontabSchedule.objects.create(
        id=4, minute='30', hour='01', day_of_week='*', day_of_month='*', month_of_year='*')
    

def init_tasks():
    """创建任务"""
    PeriodicTask.objects.create(
        name='update hardware usage', 
        task='monitor.tasks.send_hardware_taskgroup', 
        crontab=CrontabSchedule.objects.get(pk=1), 
    )
    PeriodicTask.objects.create(
        name='update bandwidth usage', 
        task='monitor.tasks.send_bandwidth_taskgroup', 
        crontab=CrontabSchedule.objects.get(pk=2), 
    )
    PeriodicTask.objects.create(
        name='update temperature usage', 
        task='monitor.tasks.send_temperature_taskgroup', 
        crontab=CrontabSchedule.objects.get(pk=3), 
    )
    PeriodicTask.objects.create(
        name='clean old monitor data', 
        task='monitor.tasks.clear_monitor_old_data', 
        crontab=CrontabSchedule.objects.get(pk=4), 
    )
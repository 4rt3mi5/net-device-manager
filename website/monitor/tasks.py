import os
import sys
import re
import time
import requests
import json
import datetime

from hashlib import md5
from celery import group
from django.core.cache import cache

from website.celery import app
from monitor.models import HardwareData, BandwidthData, TemperatureData
from device.models import Device
from website.settings import BASE_DIR
sys.path.append(os.path.dirname(BASE_DIR))
from pexssh import Pexssh
from telnet import Telnet


def alert(content):
    """警告信息"""
    url = 'https://oa.yixia.com/v2/api/wx/sendmessage?access_token={token}' 
    timestamp = md5(b'%d' % time.mktime(time.strptime('%s%s%s'%(time.localtime()[:3]), '%Y%m%d'))).hexdigest()
    with open(BASE_DIR + '/users.txt') as f:
            users = f.readlines()
    data = {'to_user': [u.strip() for u in users], 'content': content,}
    result = requests.post(url=url.format(token=timestamp), data=data)
    if result.status_code != 200:
        return result.content


def alert_h(device):
    text = '''
        错误等级： 告警 | 设备IP：{ip} | 超过阈值字段： {field} | 当前最高值： {max} \n
    '''
    hardware_data_objects = device.monitor_hardwaredata_related.all()
    threshold = json.loads(device.config).get('threshold')
    if hardware_data_objects.count() >= int(threshold.get('count')):
        hards = hardware_data_objects.order_by('-create_time')[:int(threshold.get('count'))]
        cpu_usages = [o.cpu for o in hards]
        memory_usages = [o.memory for o in hards]
        if min(cpu_usages) > int(threshold.get('cpu')):
            alert(text.format(ip=device.ip, field='CPU', max=max(cpu_usages)))
        if min(memory_usages) > int(threshold.get('memory')):
            alert(text.format(ip=device.ip, field='MEMORY', max=max(memory_usages)))
        return {'cpu':max(cpu_usages),'memory':max(memory_usages)}


def alert_t(device):
    text = '''
        错误等级： 告警 | 设备IP：{ip} | 超过阈值字段： {field} | 当前最高值： {max} \n
    '''
    temp_data_objects = device.monitor_temperaturedata_related.all()
    threshold = json.loads(device.config).get('threshold')
    if temp_data_objects.count() >= int(threshold.get('count')):
        temps = temp_data_objects.order_by('-create_time')[:int(threshold.get('count'))]
        current = [o.current for o in temps]
        if min(current) > int(threshold.get('temp')):
            alert(text.format(ip=device.ip, field='TEMPERATURE', max=max(current)))
    return {'temperature':max(current)}

        
def alert_b(device):
    text = '''
        错误等级： 告警 | 设备IP：{ip} | 超过阈值字段： {field} | 当前最高值： {max} | 端口： {port} \n
    '''
    ports_obj = device.monitor_portbound_related.all()
    if not ports_obj:
        return {'msg':'未监听端口'}
    for port in ports_obj:
        bandwidth_data_objects = device.monitor_bandwidthdata_related.filter(port=port)
        threshold = json.loads(device.config).get('threshold')
        if bandwidth_data_objects.count() >= int(threshold.get('count')):
            bands = bandwidth_data_objects.order_by('-create_time')[:int(threshold.get('count'))]
            uploads = [o.upload for o in bands]
            downloads = [o.download for o in bands]
            if min(uploads) > int(threshold.get('output')):
                alert(text.format(ip=device.ip, field='OUTPUT', max=max(uploads), port=port.port))
            if min(downloads) > int(threshold.get('input')):
                alert(text.format(ip=device.ip, field='INPUT', max=max(downloads), port=port.port))
    return {'out': max(uploads),'in':max(downloads)}


@app.task
def get_hardware_data(device):
    """获得设备的CPU、内存信息使用率"""
    if device.ip == '172.16.111.1':
        invoke = Pexssh(device=device)
    else:
        invoke = Telnet(device=device)
    cpu_info = invoke.execute_command(['display cpu-usage'])
    memory_info = invoke.execute_command(['display memory-usage'])
    if isinstance(cpu_info, dict) or isinstance(memory_info, dict):
        return {'error': '获取CPU或内存命令执行失败', 'host': device.ip, 'result': [cpu_info, memory_info]}
    cpu_usage = re.findall(r'Usage *:(.+?)%', cpu_info)
    memory_usage = re.findall(r':(.+?)%', memory_info)
    if cpu_usage and memory_usage:
        cpu = (float(cpu_usage[0])if len(cpu_usage)
               == 1 else float(cpu_usage[1]))
        memory = float(memory_usage[0])
        HardwareData.objects.create(device=device, cpu=cpu, memory=memory)
        cache.set(device.ip, True, 120)
        invoke.close()
        msg = alert_h(device=device)
        return {'host': device.ip, 'cpu': cpu, 'memory': memory, 'msg': 'success'}
    return {'error': '正则匹配失败', 'host': device.ip, 'result': [cpu_usage, memory_usage]}


@app.task
def get_bandwidth_data(device):
    """获得端口的带宽使用率"""
    ports_obj = device.monitor_portbound_related.all()
    if not ports_obj:
        return {'host': device.ip, 'msg': '未监听端口'}
    if device.ip == '172.16.111.1':
        invoke = Pexssh(device=device)
    else:
        invoke = Telnet(device=device)
    result = invoke.execute_command(command=['display interface brief'])
    if isinstance(result, dict):
        return {'error': '获取端口带宽命令执行失败', 'host': device.ip, 'result': result}
    ports = {}
    for block in result.split('\r\n'):
        line = re.split(r' +', block)
        if len(line) > 5:
            format_port = [s for s in line if s]
            if 'up' in format_port[1] and 'up' in format_port[2] and 'Vlanif' not in format_port[0]:
                ports[format_port[0]] = format_port
    for port in ports_obj:
        usage_list = ports.get(port.port)
        BandwidthData.objects.create(
            device=device,
            port=port,
            upload=usage_list[4].replace('%', ''),
            download=usage_list[3].replace('%', '')
        )
    invoke.close()
    msg = alert_b(device=device)
    return {'host': device.ip, 'msg': 'success'}


@app.task
def get_temperature(device):
    """获得设备平均温度"""
    current_mean = []
    upper_mean = []
    if device.ip == '172.16.111.1':
        invoke = Pexssh(device=device)
    else:
        invoke = Telnet(device=device)
    temp_info = invoke.execute_command(['display temperature all'])
    if isinstance(temp_info, dict):
        temp_info = invoke.execute_command(['display environment'])
        if isinstance(temp_info, dict):
            return {'error': '结果执行错误', 'result': temp_info, 'host': device.ip}

    lines = [line for line in temp_info.lower().split('\r\n') if not line.strip().startswith('-')]
    newlines = [line for line in lines if 'display' not in line and line and '<' not in line]
    values = [newlines[newlines.index(line):] for line in newlines if 'current' in line or 'lower' in line][0]
    title = values.pop(0).split()
    current = [title.index(n) for n in title if 'current' in n or 'temp(c)' in n][0]
    upper = [title.index(n) for n in title if 'upper' in n or 'high' in n][0]
    for n in values:
        line = n.split()
        try:
            current_mean.append(int(line[current]))
            upper_mean.append(int(line[upper]))
        except:
            continue
    c = sum(current_mean) // len(current_mean)
    u = sum(upper_mean) // len(upper_mean)
    TemperatureData.objects.create(device=device, current=c, upper=u)
    invoke.close()
    msg = alert_t(device=device)
    return {'host': device.ip, 'current':c,'upper':u}


@app.task
def send_hardware_taskgroup():
    """一次性生成多个任务"""
    job = group(get_hardware_data.s(device)
                for device in Device.objects.all())
    job.delay()


@app.task
def send_bandwidth_taskgroup():
    job = group(get_bandwidth_data.s(device)
                for device in Device.objects.all())
    job.delay()


@app.task
def send_temperature_taskgroup():
    job = group(get_temperature.s(device)
                for device in Device.objects.all())
    job.delay()


@app.task
def clear_monitor_old_data():
    """只保留最近几天的监控数据"""
    with open(BASE_DIR + '/time.txt') as f:
        time = f.readlines()
    after_day = datetime.datetime.now() - datetime.timedelta(days=int(time[0]))
    HardwareData.objects.filter(create_time__lte=after_day).delete()
    BandwidthData.objects.filter(create_time__lte=after_day).delete()
    TemperatureData.objects.filter(create_time__lte=after_day).delete()
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
Description:
    ssh连接WLC
"""

import paramiko
import time
import datetime
import re


class Genssh:
    def __init__(self, ip=None, username=None, password=None, port=22, device=None):
        self.ip = ip or device.ip
        self.username = username or device.username
        self.password = password or device.password
        self.port = port
        self.dict = {
            '10.10.24.10': {'end_str': '(Cisco Controller) >', 'paging': 'config paging disable'}
        }
        self.connect = self.__invoke_genssh()

    def __invoke_genssh(self):
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            self.ssh_client.connect(
                hostname=self.ip, username=self.username, password=self.password, port=self.port)
        except paramiko.ssh_exception.NoValidConnectionsError:
            return {'error': '不能连接到主机{hostname}的端口{port}'.format(hostname=self.ip, port=self.port)}
        s = self.ssh_client.invoke_shell()
        s.recv(1024).decode()
        s.send('{username}\n'.format(username=self.username))
        time.sleep(0.5)
        s.recv(1024).decode()
        s.send('{password}\n'.format(password=self.password))
        time.sleep(0.5)
        s.recv(1024).decode()
        s.send(self.dict.get(self.ip).get('paging') + '\n')
        time.sleep(0.5)
        s.recv(1024).decode()
        return s

    def execute_command(self, command=[], close=True):
        if isinstance(self.connect, dict):
            return self.connect
        self.connect.send('{command}\n'.format(command=' \n'.join(command)))
        time.sleep(1)
        result = ""
        while True:
            if self.connect.recv_ready():
                output = self.connect.recv(1024).decode('utf-8')
                result += output
            if self.dict.get(self.ip).get('end_str') in result:
                break
        if close:
            self.ssh_client.close()
        return {'result': result, 'time': datetime.datetime.now()}

    def close(self):
        if not isinstance(self.connect, dict):
            self.ssh_client.close()


if __name__ == '__main__':
    ss = Genssh('10.10.24.10', 'admin', 'admin@123')
    r = ss.execute_command(['show client detail 78:4f:43:7d:fb:b8'])
    print(r)

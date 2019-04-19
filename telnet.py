#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
Description:
    TElnet连接交换机
"""

import re
import socket
import telnetlib
import time
import subprocess


# Telnet连接
class Telnet:
    def __init__(self, ip=None, username=None, password=None, device=None):
        self.ip = ip or device.ip
        self.username = username or device.username
        self.password = password or device.password
        self.errors = [
            'Error: Authentication failed.',
            'Error: Authentication fail',
            'Error: Local authentication is rejected.'
        ]
        self.connect = self.__invoke_telnet()

    def __invoke_telnet(self):
        try:
            t = telnetlib.Telnet(self.ip, timeout=1)
        except socket.timeout:
            return {'error': '连接超时'}
        except ConnectionResetError:
            return {'error': '连接被重置'}
        except OSError:
            return {'error': '网络不可达'}
        except:
            return {'error': '未知错误'}
        t.read_until(b'Username:')
        t.write(self.username.encode() + b'\n')
        t.read_until(b'Password:')
        t.write(self.password.encode() + b'\n')
        time.sleep(1)
        msg = t.read_very_eager().decode()
        for log in self.errors:
            if log in msg:
                return {'error': '账号密码输入错误'}
        t.write(b'screen-length 0 temporary \r\n')
        time.sleep(0.5)
        t.read_very_eager().decode()
        return t

    def execute_command(self, command=[], timeout=1):
        if isinstance(self.connect, dict):
            return self.connect
        self.connect.write('{} \r\n'.format(' \r\n'.join(command)).encode())
        time.sleep(timeout)
        result = self.__get_result()
        if 'Error:' not in result and 'command found' not in result and 'Unrecognized' not in result:
            return result
        else:
            try:
                return {'error': re.findall(r'.+?(Error.+)\r\n', result, re.S)[0]}
            except IndexError:
                return {'error': result}

    def __get_result(self):
        time.sleep(3)
        try:
            result = self.connect.read_very_eager().decode()
        except socket.timeout:
            return {'error': '获取结果超时'}
        return result

    def close(self):
        if not isinstance(self.connect, dict):
            self.connect.close()

    def __del__(self):
        self.close()


if __name__ == '__main__':
    t = Telnet('10.10.10.25', 'yixia', 'anbs,23tyx')
    _temp = t.execute_command(['display temperature all'])
    print(_temp)
    q = subprocess.Popen('echo "%s" | awk \'{print $4}\'' % _temp,stdout=subprocess.PIPE,shell=True)
    print(q.stdout.read())

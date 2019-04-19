#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
Description:
    pexpect连接ssh
"""

import re
import pexpect


class Pexssh:
    def __init__(self, ip=None, username=None, password=None, device=None):
        self.ip = ip or device.ip
        self.username = username or device.username
        self.password = password or device.password
        self.dict = {
            '172.16.111.1': {'end_str': '<USG6500>', 'paging': 'screen-length 0 temporary'}
        }
        self.connect = self.__invoke_pexssh()

    def __invoke_pexssh(self):
        try:
            s = pexpect.spawn(command='ssh {username}@{ip}'.format(
                username=self.username, ip=self.ip), timeout=10)
            s.expect('Password')
            s.sendline(self.password)
        except pexpect.exceptions.TIMEOUT:
            return {'error': '连接超时'}
        try:
            index = s.expect(pattern=[self.dict.get(self.ip).get('end_str')], timeout=2)
            if index == 0:
                s.sendline(self.dict.get(self.ip).get('paging'))
                s.expect(self.dict.get(self.ip).get('end_str'))
                return s
        except pexpect.exceptions.TIMEOUT:
            return {'error': '账号密码错误'}

    def execute_command(self, command=[]):
        if isinstance(self.connect, dict):
            return self.connect
        self.connect.sendline(' \n'.join(command))
        self.connect.expect(self.dict.get(self.ip).get('end_str'))
        return self.connect.before.decode()

    def close(self):
        if not isinstance(self.connect, dict):
            self.connect.close()


if __name__ == '__main__':
    s = Pexssh('172.16.111.1', 'admin', 'r6HhEyXhNFYz')
    _users = s.execute_command(['display manager-user'])
    users_lines = [line.strip() for line in _users.split('\r\n') if line][5:-2]
    users_list = [re.split(r' +',user)[0] for user in users_lines]
    print(users_list)
    users = {}
    for username in users_list:
        user_info = s.execute_command(['display manager-user username {username}'.format(username=username)])
        print(user_info)
        lines = [line.strip() for line in user_info.split('\r\n') if line]
        line_split = [re.split(r' +: +',block) for block in lines if ':' in block]
        user_detail = {d[0]:d[1] for d in line_split if len(d) == 2}
        user_detail['username'] = username
        users[username] = user_detail
    print(users)
    s.close()

import os
import sys

from website.settings import BASE_DIR
sys.path.append(os.path.dirname(BASE_DIR))
from genssh import Genssh
from telnet import Telnet
from pexssh import Pexssh


class ConnectwlcMixins:
    def execute_command(self, ip='10.10.24.10', username='admin', password='admin@123', command=[], close=True):
        gen = Genssh(ip=ip, username=username, password=password)
        result = gen.execute_command(command=command, close=close)
        return result


class ConnectSFMixins:
    def get_ssh_c(self, ip, username, password):
        pex = Pexssh(ip=ip, username=username, password=password)
        return pex

    def get_telnet_c(self, device):
        tel = Telnet(device=device)
        return tel

    def ssh_execute_command(self, ip='172.16.111.1', username='admin', password='r6HhEyXhNFYz', command=[]):
        pex = self.get_ssh_c(ip=ip, username=username, password=password)
        result = pex.execute_command(command=command)
        pex.close()
        return result

    def telnet_execute_command(self, device, command=[], timeout=1):
        tel = self.get_telnet_c(device=device)
        result = tel.execute_command(command=command, timeout=timeout)
        tel.close()
        return result

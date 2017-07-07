# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from ssh_config import get_ssh_config, username, password
import paramiko
import time

for i in range(6):
    cfg = get_ssh_config(i)
    ip = cfg['ip']
    port = cfg['port']
    print "1"
    ssh = paramiko.SSHClient()
    print "2"
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print "3"
    ssh.connect(ip, port, username, password)
    print "4"

    stdin, stdout, stderr = ssh.exec_command("systemctl restart squid.service")
    time.sleep(1)
    stdout.readline()
    ssh.close()

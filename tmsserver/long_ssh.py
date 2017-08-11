#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import paramiko


class Long_ssh(object):
    def __init__(self, hostname, username, password, script,port=22):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.script = script
        self.port = port

    def connection(self):
        paramiko.util.log_to_file('syslogin.log')
        ssh = paramiko.SSHClient()
        # ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=self.hostname, username=self.username, password=self.password)
        stdin, stdout, stderr = ssh.exec_command(self.script)
        result= stdout.read()
        ssh.close()
        return result

#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# import paramiko
#
# hostname='192.168.137.25'
# username='root'
# password='123456'
# paramiko.util.log_to_file('syslogin.log')
#
# ssh=paramiko.SSHClient()
# # ssh.load_system_host_keys()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect(hostname=hostname,username=username,password=password)
# stdin,stdout,stderr=ssh.exec_command('ls|wc -l')
# s,d= stdout.read(),stderr.read()
# print s
# print d
# ssh.close()
from tmsserver import  long_ssh
a = long_ssh.Long_ssh('192.168.137.113','root','123456','ll ')
result,error  = a.connection()
if error :
    print '错误原因是 %s' %(error)
else:
    print result

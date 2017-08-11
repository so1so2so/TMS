#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#!/usr/bin/env python
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
# stdin,stdout,stderr=ssh.exec_command('ls -l')
# s = stdout.read()
# print s
# ssh.close()
from tmsserver import  long_ssh
a = long_ssh.Long_ssh('192.168.137.25','root','123456','ls -l')
a.connection()

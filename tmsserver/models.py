#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Service(models.Model):
    service_id = models.IntegerField(primary_key=True, verbose_name='服务编号')
    service_name = models.CharField(max_length=50, verbose_name='服务名称')
    status = (
        (1, '启动'),
        (2, '未启动')
    )
    service_status = models.IntegerField(choices=status, default=1, verbose_name='服务状态')
    service_address = models.CharField(max_length=128,default=1,verbose_name='服务地址')
    service_script = models.CharField(max_length=128,default=1,verbose_name='脚本名称')
    service_command = models.CharField(max_length=128,default=1,verbose_name='启动命令')
    class Meta:
        verbose_name = u"服务"
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.service_name


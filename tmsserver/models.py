#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from __future__ import unicode_literals
from  DjangoUeditor.forms import UEditorField as UEditorFieldF
from DjangoUeditor.models import UEditorField
from django.db import models
from django import forms

# Create your models here.
class Service(models.Model):
    service_id = models.IntegerField(primary_key=True, verbose_name='服务编号')
    service_name = models.CharField(max_length=50, verbose_name='服务名称')
    status = (
        (1, '启动'),
        (2, '未启动')
    )
    service_status = models.IntegerField(choices=status, default=1, verbose_name='服务状态')
    service_address = models.CharField(max_length=128, default=1, verbose_name='服务地址')
    service_script = models.CharField(max_length=128, default=1, verbose_name='脚本名称')
    service_command = models.CharField(max_length=128, default=1, verbose_name='启动命令')
    service_test = models.EmailField(max_length=128, blank=True, verbose_name='e-mail',null=True)
    service_test2 = models.DateTimeField(max_length=128, blank=True, verbose_name='添加时间')
    service_grep = models.CharField(max_length=128, default=1, verbose_name='服务过滤条件',null=True,blank=True)
    Content=UEditorField(u'内容',width=600, height=300, imagePath="media/ueditor/img/", filePath="media/ueditor/file/", upload_settings={"imageMaxSize":1204000},default=1,blank=True,)
    class Meta:
        verbose_name = u"服务"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.service_name



class Blog(forms.Form):
    # Name = models.CharField(max_length=100, blank=True)
     Description=UEditorFieldF("描述",initial="abc",width=600,height=800)

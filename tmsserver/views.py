#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from django.shortcuts import render
from django.views.generic.base import View
# Create your views here.
from tmsserver.models import Service
from  long_ssh import Long_ssh
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Head_ListView(View):
    def get(self, request):
        service = Service.objects.all()
        return render(
            request, 'index.html',
            {'service': service}
        )

    def post(self, request):
        hostname='192.168.137.113'
        username='root'
        password='123456'
        script =request.POST.get(u'script')
        conn = Long_ssh(hostname,username,password,script)
        resu = conn.connection()
        return render(
            request, 'index.html',
            {'s': resu}
        )

class Send_message(View):
        def post(self,request,service_id):


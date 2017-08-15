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
hostname = '192.168.137.113'
username = 'root'
password = '123456'


class Head_ListView(View):
    def get(self, request):
        service = Service.objects.all()
        return render(
            request, 'index.html',
            {'service': service}
        )

    def post(self, request):
        script = request.POST.get(u'script')
        conn = Long_ssh(hostname, username, password, script)
        retuer, error = conn.connection()
        if error:
            result = error
        else:
            result = retuer
        return render(request, 'index.html',
                      {'result': result,
                       })


class Send_message(View):
    def get(self, request, service_id):
        service = Service.objects.get(service_id=service_id)
        address = service.service_address
        script = service.service_command
        end_script = 'cd' + ' ' + address + '&&' + ' ' + script
        status = service.service_script
        end_status = 'ps aux|grep -v grep|grep'+' '+status
        if end_status:
            print end_status
            conn = Long_ssh(hostname, username, password, end_status)
        # conn2 = Long_ssh(hostname, username, password, end_script)
            retuer, error = conn.connection()
            if error:
                result = error
            else:
                result = retuer
            print result
            return render(request, 'abc.html',
                          {'service': service,
                           'end_script': end_script,
                           'result': result,
                           })


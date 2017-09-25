#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# import urllib
# import urllib2
#
# request = urllib2.Request("http://www.baidu.com")
# response = urllib2.urlopen(request)
# print response.read()

import urllib
import urllib2

user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
headers = { 'User-Agent' : user_agent }

values = {"LoginForm[username]": "so1so2so", "LoginForm[password]": "zhangneng"}
data = urllib.urlencode(values)
url = "http://127.0.0.1:8000/admin/login/?next=/admin/"
request = urllib2.Request(url, data,headers)
response = urllib2.urlopen(request)
print response.read()

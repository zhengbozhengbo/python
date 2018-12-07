# /usr/bin/env   python
# -*- coding:utf-8 -*-

import requests
class 请求1():
    def qingqiu(slef,a):
        url='http://testsupport-be.haofenshu.com/v1/schools/infos'
        pa={'filterInput':'{}'.format(a)}
        head={"Cookie":"yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA",
              "Content-Type":"application/x-www-form-urlencoded",
              "Accepe":"*/*",
              "Accepet-Encoding": "gzip,deflate"}
        responese=requests.get(url=url,headers=head,params=pa)
        jieguo=responese.json()
        print(jieguo)
# /usr/bin/env python
# -*- coding:utf-8 -*-
import requests

class 学校_查询():
    def 学校_快查(self,a):
        url = "http://testsupport-be.haofenshu.com/v1/schools/infos"
        # a=input("》》")
        pa = {"filterInput": "{}".format(a)}
        head = {"Content-Type": "application/x-www-form-urlencoded",
                "Accepet-Encoding": "gzip,deflate",
                "Accpet": "*/*",
                "cookie": "yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA"}
        respones = requests.get(url=url, headers=head, params=pa)
        jieguo = respones.json()  ## 结果字典
        return jieguo
    def 学校_考试快查(self):
        pass
    def 学校_列表(self):
        pass

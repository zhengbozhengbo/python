# /usr/bin/env  python
# -*- coding:utf-8 -*-

import requests
import unittest
class Xuexiao():

    def __init__(self):
        self.url = "http://testsupport-be.haofenshu.com/v1/schools/infos"
        self.head = {"Content-Type": "application/x-www-form-urlencoded",
                "Accepet-Encoding": "gzip,deflate",
                "Accpet": "*/*",
                "cookie": "yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA"}

    def ceshi1(self,a):
        import xlrd
        #a=input("》》")
        f=xlrd.open_workbook("文件名")
        sheet= f.sheets()[0]
        b=sheet.nrows
        for i in range(b):


            pa={"filterInput":"{}".format(a)}
            respones = requests.get(url=self.url, headers=self.head, params=pa)
            html=respones.json()  ## 结果字典
            print(html["msg"])
            #print(respones.text)
            assert html["code"]==0    #断言方式
    def ceshi2(self,a):
        url = "http://testsupport-be.haofenshu.com/v1/schools/infos"
        # a=input("》》")
        pa = {"filterInput": "{}".format(a)}
        head = {"Content-Type": "application/x-www-form-urlencoded",
                "Accepet-Encoding": "gzip,deflate",
                "Accpet": "*/*",
                "cookie": "yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA"}
        respones = requests.get(url=url, headers=head, params=pa)
        html = respones.json()  ## 结果字典
        print(html["msg"])


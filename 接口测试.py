#/usr/bin/env python
# -*- coding:utf-8 -*
from 测试报告 import HTMLTestRunnertest
import time
import xlrd


#接口测试：发送请求,验证响应是否符合需求的过程
##postman/jmeter

#ruquests--发送请求  assert--断言处理
# import unittest    #Python自带的单元测试自动化测试框架
# """  unittest :以下四个
# #unintest.TestCase  ：测试用例--用来做用例管理
# #unintest.TestSuite :测试套件（测试集）--多个测试用例集合在一起
# #unintest.TestLoader ：测试载入--将测试用例加载到测试套件中
# #unintest.TestRunner ：执行封装了检验返回的结果的方法--即是断言"""
#
# class Xuexiao():
#     def ceshi1(self,a):
#         url="http://testsupport-be.haofenshu.com/v1/schools/infos"
#         #a=input("》》")
#         pa={"filterInput":"{}".format(a)}
#         head={"Content-Type":"application/x-www-form-urlencoded",
#               "Accepet-Encoding":"gzip,deflate",
#               "Accpet":"*/*",
#             "cookie":"yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA"}
#         respones= requests.get(url=url,headers=head,params=pa)
#         html=respones.json()  ## 结果字典
#         print(html["msg"])
#         #print(respones.text)
#         assert html["code"]==0    #断言方式
#     def ceshi2(self,a):
#         url = "http://testsupport-be.haofenshu.com/v1/schools/infos"
#         # a=input("》》")
#         pa = {"filterInput": "{}".format(a)}
#         head = {"Content-Type": "application/x-www-form-urlencoded",
#                 "Accepet-Encoding": "gzip,deflate",
#                 "Accpet": "*/*",
#                 "cookie": "yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA"}
#         respones = requests.get(url=url, headers=head, params=pa)
#         html = respones.json()  ## 结果字典
#         print(html["msg"])
#
#

import requests
import unittest



class ceshi(unittest.TestCase):
    def shuju(self):
        shuju2 = []
        f = xlrd.open_workbook("测试.xls")
        sheet = f.sheets()[0]
        num = sheet.nrows
        for i in range(1, num):
            aa = sheet.row_values(i)
            shuju2.append(aa)
        return shuju2
    def ceshi1(self,a):
        url="http://testsupport-be.haofenshu.com/v1/schools/infos"
        #a=input("》》")
        pa={"filterInput":"{}".format(a)}
        head={"Content-Type":"application/x-www-form-urlencoded",
                  "Accepet-Encoding":"gzip,deflate",
                  "Accpet":"*/*",
                "cookie":"yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA"}
        respones= requests.get(url=url,headers=head,params=pa)
        jieguo=respones.json()  ## 结果字典
        return jieguo
            #print(respones.text)

#class Xuexiao2(unittest.TestCase):
    # def setUp(self):  #作用：初始化测试环境 ，每次执行测试用例前执行
    #     print("开始")
    #
    # def tearDown(self):  #作用：清理环境 ，每次用例之后执行
    #     print("结束")

    def test_1(self):  ##测试用例 必须用test开头 以ASCII码的顺序执行
        shuju3=self.shuju()
        html=self.ceshi1(shuju3[0][0])
        self.assertEqual(html["code"],int(shuju3[0][1]))
        self.assertIn(len(html["data"]), range(int(shuju3[0][2])))

    def test_2(self):  ##测试用例 必须用test开头 以ASCII码的顺序执行
        shuju3 = self.shuju()
        html=self.ceshi1(shuju3[1][0])
        self.assertEqual(html["code"], int(shuju3[1][1]))
        self.assertNotEqual(len(html["data"]),int(shuju3[1][2]))

    def test_3(self):
        shuju3 = self.shuju()
        html = self.ceshi1(shuju3[2][0])
        self.assertEqual(html["code"], int(shuju3[2][1]))
        self.assertEqual(len(html["data"]), int(shuju3[2][2]))

    def test_4(self):
        shuju3 = self.shuju()
        html = self.ceshi1(shuju3[3][0])
        self.assertEqual(html["code"], int(shuju3[3][1]))
        self.assertIn(len(html["data"]), range(int(shuju3[3][2])))
        #self.assertIn("msg",html)

#unittest.main()  ##执行用例
if __name__=='__main__':
    #生成测试报告  创建一个测试套件
    suit=unittest.TestSuite()
    #添加测试用例  将测试用例添加到测试套件中
    #suit.addTest（类名（'用例名'）） #每次添加一个
    # suit.addTest(Xuexiao2('test_1'))
    # suit.addTest(Xuexiao2('test_2'))
    # suit.addTest(Xuexiao2('test_3'))
    # suit.addTest(Xuexiao2('test_4'))
    #将类中的所有测试用例添加到测试套件中
    suit.addTest(unittest.makeSuite(ceshi))
    now = time.strftime('%Y %m %d %H-%M-%S',time.localtime(time.time()))
    f=open("abc4.html","wb")
    runner= HTMLTestRunnertest.HTMLTestRunner(tester="郑博",
                                              description='测试结果如下:',
                                              title='好分数测试报告',
                                              stream=f)
    runner.run(suit)
    f.close()



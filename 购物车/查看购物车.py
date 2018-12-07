# usr/bin/env   python
# -*- coding:utf-8 -*-
import unittest
import requests
import  time
from 测试报告 import HTMLTestRunnertest
class gouwuche(unittest.TestCase):
    def qingqiu(self):
        url="http://www.zhaoapi.cn/product/getCarts"
        param={"mobile":"15237888353",
                "password":"123456",
                "uid":22697}
        head={"Content-Type":"application/x-www-form-urlencoded",
                  "Accepet-Encoding":"gzip,deflate",
                  "Accpet":"*/*",
                   'token':"B26C90E2560916C7D6D49CEBAC1694BC"}
        respones=requests.get(url=url,headers=head ,params=param)
        jieguo=respones.json()
        return jieguo
    def test_1(self):
        html=self.qingqiu()
        self.assertEqual(html["code"],"0")
        self.assertEqual(html["msg"],"请求成功")
    def test_2(self):
        html = self.qingqiu()
        self.assertEqual(html["code"], "0")
        self.assertEqual(html["msg"], "请求成功")
if __name__=="__main__":
    suit=unittest.TestSuite()
    suit.addTest(unittest.makeSuite(gouwuche))
    now=time.strftime('%Y %m %d %H-%M-%S',time.localtime(time.time()))
    f=open("aaa.html","wb")
    runner=HTMLTestRunnertest.HTMLTestRunner(tester="郑博",
                                              description="测试结果如下",
                                             title="购物车查询",
                                             stream=f)
    runner.run(suit)
    f.close()


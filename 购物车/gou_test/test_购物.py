# /usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
from 购物车.confing.请求 import 请求2
from 购物车.data.读取 import 表格

class chaxun(unittest.TestCase):
    a=请求2().qingqiu
    c=请求2().qingqiu2
    d=请求2().qingqiu3
    b=表格()
    def test_1(self):
        html=self.a(int(self.b[0][0]))
        #self.assertEqual(html["code"], int(self.b[0][1]))
        self.assertEqual(str(html),self.b[0][2])
    def test_2(self):
        self.c()
        html = self.a(int(self.b[1][0]))
        self.assertEqual(html["code"], int(self.b[1][1]))
        self.assertEqual(html['msg'], self.b[1][2])
        print(html)
        self.d()
    def test_3(self):
        html = self.a(self.b[2][0])
        self.assertNotEqual(html["code"], 0)
        self.assertEqual(html['msg'], self.b[2][2])
if __name__ =='__main__':
    unittest.main()


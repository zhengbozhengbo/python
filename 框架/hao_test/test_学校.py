# /usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
from 框架.config.学校_接口 import 学校_查询
from 框架.data.读取数据 import shuju

class ceshi(unittest.TestCase):

    school=学校_查询().学校_快查
    shuju=shuju()

    def test_1(self):  ##测试用例 必须用test开头 以ASCII码的顺序执行
        html = self.school(self.shuju[0][0])
        self.assertEqual(html["code"], int(self.shuju[0][1]))
        self.assertIn(len(html["data"]), range(int(self.shuju[0][2])))

    def test_2(self):  ##测试用例 必须用test开头 以ASCII码的顺序执行
        html = self.school(self.shuju[1][0])
        self.assertEqual(html["code"], int(self.shuju[1][1]))
        self.assertEqual(len(html["data"]), int(self.shuju[1][2]))

    def test_3(self):
        html = self.school(self.shuju[2][0])
        self.assertEqual(html["code"], int(self.shuju[2][1]))
        self.assertEqual(len(html["data"]), int(self.shuju[2][2]))

    def test_4(self):
        html = self.school(self.shuju[3][0])
        self.assertEqual(html["code"], int(self.shuju[3][1]))
        self.assertIn(len(html["data"]), range(int(self.shuju[3][2])))
        # self.assertIn("msg",html)


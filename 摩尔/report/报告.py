# /usr/bin/env  python
# -*- coding:utf-8 -*-
import unittest
import time
from 摩尔.report import HTMLTestRunnertest


class test_run():
    # def run_duoge(slef,a):
    #     # 生成测试报告  创建一个测试套件
    #     suit = unittest.TestSuite()
    #     #suit.addTest(unittest.makeSuite(a))
    #     #suit.addTest(unittest.makeSuite(ceshi2))  #多个
    #     for i in a:
    #         i = i.strip()
    #         disvover = unittest.defaultTestLoader.discover(r'..\test', pattern='{}.py'.format(i))
    #         suit.addTest(disvover)
    #     now = time.strftime('%Y %m %d %H-%M-%S', time.localtime(time.time()))
    #     f = open(r"E:/python 文件/摩尔/report/aaa.html", "wb")
    #     runner = HTMLTestRunnertest.HTMLTestRunner(tester="郑博",
    #                                                description='测试结果如下:',
    #                                                title='好分数测试报告',
    #                                                stream=f)
    #     runner.run(suit)
    #     f.close()
    def run_all(self):
        suit = unittest.TestSuite()
        disvover=unittest.defaultTestLoader.discover(r'..\test',pattern='ce_test*.py')
        suit.addTest(disvover)
        now = time.strftime('%Y %m %d %H-%M-%S', time.localtime(time.time()))
        f = open(r"E:/python 文件/摩尔/report/bbb23.html", "wb")
        runner = HTMLTestRunnertest.HTMLTestRunner(tester="郑博",
                                                   description='测试结果如下:',
                                                   title='好分数测试报告',
                                                   stream=f)
        runner.run(suit)
        f.close()

# /usr/bin/env python
# -*- coding:utf-8 -*-
# import unittest
# import time
# from 框架.report import HTMLTestRunnertest
#
#
# class test_run():
#     def run_duoge(slef,a):
#         # 生成测试报告  创建一个测试套件
#         suit = unittest.TestSuite()
#         #suit.addTest(unittest.makeSuite(a))
#         #suit.addTest(unittest.makeSuite(ceshi2))  #多个
#         for i in a:
#             i = i.strip()
#             disvover = unittest.defaultTestLoader.discover(r'..\hao_test', pattern='{}.py'.format(i))
#             suit.addTest(disvover)
#         now = time.strftime('%Y %m %d %H-%M-%S', time.localtime(time.time()))
#         f = open(r"E:/python 文件/框架/report/abc.html", "wb")
#         runner = HTMLTestRunnertest.HTMLTestRunner(tester="郑博",
#                                                    description='测试结果如下:',
#                                                    title='好分数测试报告',
#                                                    stream=f)
#         runner.run(suit)
#         f.close()
#     def run_all(self):
#         suit = unittest.TestSuite()
#         disvover=unittest.defaultTestLoader.discover(r'..\hao_test',pattern='test*.py')
#         suit.addTest(disvover)
#         now = time.strftime('%Y %m %d %H-%M-%S', time.localtime(time.time()))
#         f = open("abc4.html", "wb")
#         runner = HTMLTestRunnertest.HTMLTestRunner(tester="郑博",
#                                                    description='测试结果如下:',
#                                                    title='好分数测试报告',
#                                                    stream=f)
#         runner.run(suit)
#         f.close()

from 摩尔.report.报告 import test_run
from 框架.data.读取数据 import shuju3

if __name__=='__main__':
    run=test_run()
    # f = open(r"E:\python 文件\框架\driver\文件1.txt", "r")
    # a = f.readlines()
    if len(shuju3())==1:
        if 'all' in shuju3[0]:
            run.run_all()
    else:
        run.run_duoge(shuju3())




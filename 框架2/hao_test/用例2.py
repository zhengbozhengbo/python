# /usr/bin/env python
#-*- coding:utf-8 -*-
from 框架2.data.数据 import shuju2
from 框架2.confing.test_请求 import 请求1
import  unittest
import time
from 框架.report import HTMLTestRunnertest


class yongli(unittest.TestCase):
    school=请求1().qingqiu
    shuju=shuju2()
    def test_1(self):
        jieguo2=self.school(self.shuju[0][0])
        self.assertEqual(jieguo2["code"], int(self.shuju[0][1]))
        self.assertIn(len(jieguo2["data"]), range(int(self.shuju[0][2])))
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

if __name__=='__main__':

    unittest.main()
    # 生成测试报告  创建一个测试套件
    suit = unittest.TestSuite()
    # 添加测试用例  将测试用例添加到测试套件中
    # suit.addTest（类名（'用例名'）） #每次添加一个
    # suit.addTest(Xuexiao2('test_1'))
    # suit.addTest(Xuexiao2('test_2'))
    # suit.addTest(Xuexiao2('test_3'))
    # suit.addTest(Xuexiao2('test_4'))
    # 将类中的所有测试用例添加到测试套件中
    suit.addTest(unittest.makeSuite(yongli))
    now = time.strftime('%Y %m %d %H-%M-%S', time.localtime(time.time()))
    f = open("abc4.html", "wb")
    runner = HTMLTestRunnertest.HTMLTestRunner(tester="郑博",
                                               description='测试结果如下:',
                                               title='好分数测试报告',
                                               stream=f)
    runner.run(suit)
    f.close()


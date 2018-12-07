#usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
from 摩尔.config.deng import open
from time import sleep
from 摩尔.report.报告 import test_run




open=open()
class ceshi(unittest.TestCase):
    def setUp(self):
        open.open2()
    def tearDown(self):
        print(2222)
    # def test_1(self):
    #     open.dr.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[1]').click()
    #     sleep(1)
    #     m=open.dr.window_handles
    #     sleep(1)
    #     self.assertEqual(len(m), 2)
    # def test_2(self):
    #     open.dr.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[1]').click()
    #     sleep(1)
    #     wd=open.dr.window_handles
    #     open.dr.switch_to_window(wd[-1])
    #     open.dr.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div/li[2]/a/img').click()
    #     a=open.dr.find_element_by_xpath('//*[@id="mini-profile--js"]/li[3]/div[2]/a[2]').text
    #     self.assertEqual(a,'立即加入')
    # def test_3(self):
    #     open.dr.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[2]/a').click()
    #     wd = open.dr.window_handles
    #     open.dr.switch_to_window(wd[-1])
    #     open.dr.find_element_by_xpath('/html/body/div[2]/div/div/div/div[1]/div[1]/div[1]/li[2]').click()
    #     open.dr.find_element_by_xpath('//*[@id="emailInput"]').send_keys('zhengbo19960406@163.com')
    #     open.dr.find_element_by_xpath('//*[@id="passwordInput"]').send_keys('65432122')
    #     open.dr.find_element_by_xpath('//*[@id="userForm"]/input[7]').click()
    #     aa=open.dr.find_element_by_xpath('//*[@id="userForm"]/div[1]/span').text
    #     self.assertEqual(aa, '该邮箱已被注册')
    #
    # def test_4(self):
    #     open.dr.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[2]/a').click()
    #     wd = open.dr.window_handles
    #     open.dr.switch_to_window(wd[-1])
    #     open.dr.find_element_by_xpath('/html/body/div[2]/div/div/div/div[1]/div[1]/div[1]/li[2]').click()
    #     open.dr.find_element_by_xpath('//*[@id="emailInput"]').send_keys(' huimin.du@mooreelite.com')
    #     open.dr.find_element_by_xpath('//*[@id="passwordInput"]').send_keys('65432122')
    #     open.dr.find_element_by_xpath('//*[@id="userForm"]/input[7]').click()
    #     aa=open.dr.find_element_by_xpath('//*[@id="userForm"]/div[1]/span').text
    #     print(aa)
    #     self.assertEqual(aa, '请输入正确的邮箱地址')
    # def test_5(self):
    #     open.dr.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[2]/a').click()
    #     wd = open.dr.window_handles
    #     open.dr.switch_to_window(wd[-1])
    #     open.dr.find_element_by_xpath('/html/body/div[2]/div/div/div/div[1]/div[1]/div[1]/li[2]').click()
    #     open.dr.find_element_by_xpath('//*[@id="emailInput"]').send_keys('zhengbo19960406@163.com')
    #     open.dr.find_element_by_xpath('//*[@id="passwordInput"]').send_keys('11')
    #     open.dr.find_element_by_xpath('//*[@id="userForm"]/input[7]').click()
    #     aa=open.dr.find_element_by_xpath('//*[@id="userForm"]/div[2]/span').text
    #     self.assertEqual(aa, '密码最小长度为6位')
    # def test_6(self):
    #     open.dr.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[2]/a').click()
    #     wd = open.dr.window_handles
    #     open.dr.switch_to_window(wd[-1])
    #     open.dr.find_element_by_xpath('/html/body/div[2]/div/div/div/div[1]/div[1]/div[1]/li[2]').click()
    #     open.dr.find_element_by_xpath('//*[@id="emailInput"]').send_keys('491239317@qq.com')
    #     open.dr.find_element_by_xpath('//*[@id="passwordInput"]').send_keys('123456789')
    #     open.dr.find_element_by_xpath('//*[@id="userForm"]/input[7]').click()
    #     ww=open.dr.find_element_by_xpath('//*[@id="userForm"]/input[7]').text
    #     self.assertNotEquals(ww,'注册')
    #     # aa = open.dr.find_element_by_xpath('//*[@id="userForm"]/div[2]/span').text
    #     # self.assertEqual(aa, '密码最小长度为6位')
    # def test_7(self):
    #     open.dr.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[1]').click()
    #     sleep(1)
    #     wd=open.dr.window_handles
    #     open.dr.switch_to_window(wd[-1])
    #     open.dr.find_element_by_xpath('//*[@id="emailInput"]').send_keys('491239317@qq.com')
    #     sleep(1)
    #     open.dr.find_element_by_xpath('//*[@id="passwordInput"]').send_keys('123456789')
    #     open.dr.find_element_by_xpath('//*[@id="userForm"]/input[1]').click()
    #     sleep(2)
    #     open.dr.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/div[2]/div/p[2]/a').click()
    #     b=open.dr.window_handles
    #     c=open.dr.current_window_handle
    #     self.assertEqual(c,b[-1])
    #     #a = open.dr.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/div[2]/div/ul/li[2]/a').text
    #     #self.assertEqual(a,'换个邮箱')
    def test_8(self):
        open.dr.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[1]').click()
        sleep(1)
        wd=open.dr.window_handles
        open.dr.switch_to.window(wd[-1])
        open.dr.find_element_by_xpath('//*[@id="emailInput"]').send_keys('491239317@qq.com')
        sleep(1)
        open.dr.find_element_by_xpath('//*[@id="passwordInput"]').send_keys('123456789')
        open.dr.find_element_by_xpath('//*[@id="userForm"]/input[1]').click()
        sleep(2)
        a = open.dr.current_window_handle
        open.dr.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/div[2]/div/ul/li[2]/a').click()
        wd2=open.dr.window_handles
        self.assertNotEqual(a,wd2[-1])

    def test_9(self):
        


unittest.main()  ##执行用例










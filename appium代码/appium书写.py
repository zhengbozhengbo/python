# /usr/bin/env  python
#-*- coding:utf-8 -*-

from appium import webdriver
from time import  sleep
import unittest

##启动设备 ，连接设备

class ds(unittest.TestCase):
    def denglu(self):
        desired_caps = {'platformName':'Android',
                        #'platformVersion':'4.4.2',
                        'deviceName':'127.0.0.1:62001',
                        'appPackage':'com.qk.butterfly',
                        'appActivity':'main.LauncherActivity'}
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        sleep(3)

        self.driver.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()
        sleep(3)
        self.driver.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys('15237888353')
        sleep(2)
        self.driver.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys('bo33807358')
        sleep(2)
        self.driver.find_element_by_id('com.qk.butterfly:id/tv_to_login').click()
        sleep(5)
    def test_1(self):
        self.denglu()
        self.driver.find_element_by_id('android.widget.RelativeLayout').click()
        a=self.driver.find_element_by_id('com.qk.butterfly:id/tv_name').text
        self.assertEqual(a,'开心即是一切')


##  driver.quit()
# m=ds()
# m.test_1()
unittest.main()
# /usr/bin/env  python
#-*- coding:utf-8 -*-

from appium import webdriver
from time import  sleep
import unittest

##启动设备 ，连接设备
class wyx(unittest.TestCase):
    def setUp(self):
        desired_caps = {'platformName': 'Android',
                        # 'platformVersion':'4.4.2',
                        'deviceName': '127.0.0.1:62001',
                        'appPackage': 'com.netease.cloudmusic',
                        'appActivity': 'activity.LoadingActivity'}
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        sleep(10)
    def tearDown(self):
        self.driver.quit()
    def denglu(self):
        self.driver.find_element_by_id('com.netease.cloudmusic:id/mw').click()
        sleep(3)
        self.driver.find_element_by_id('com.netease.cloudmusic:id/pt').click()
        sleep(3)
        self.driver.find_element_by_id('com.netease.cloudmusic:id/i4').send_keys('15237888353')
        sleep(3)
        self.driver.find_element_by_id('com.netease.cloudmusic:id/i2').send_keys('bo33807358')
        sleep(3)
        self.driver.find_element_by_id('com.netease.cloudmusic:id/pt').click()
        sleep(3)
        self.driver.find_element_by_id('com.netease.cloudmusic:id/py').click()
        sleep(3)


    def test_1(self):
        self.denglu()
        a=self.driver.find_element_by_id('com.netease.cloudmusic:id/ac2').text
        sleep(3)
        self.assertEqual(a,'开心是所有')

# m=wyx()
if __name__=='__main__':
    unittest.main()

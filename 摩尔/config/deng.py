#usr/bin/env python
# -*- coding:utf-8 -*-

from time import sleep
from selenium import webdriver
class open():
    def open2(self):
        self.dr = webdriver.Chrome()
        self.dr.get('http://www.moore.ren')
        sleep(1)
    def open3(self):
        self.dr = webdriver.Firefox()
        self.dr.get('http://www.moore.ren')
        sleep(1)
# #!/usr/bin/env python
# #-*- coding:utf-8 -*-
# from selenium import webdriver
# from time import sleep
#
# class open():
#
#
#
#
#     def open_Chrom(self):
#         self.dr  = webdriver.Chrome()
#         self.dr.get('http://www.moore.ren')
#         sleep(2)



# from selenium import webdriver
# from time import sleep

# class 注册_摩尔():
#     def 注册(self,a):
#         # dr = webdriver.Chrome()
#         dr=webdriver.Firefox()
#
#         dr.get('http://www.moore.ren/')
#         dr.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[2]/a').click()
#         sleep(2)
#         wd = dr.window_handles
#         dr.switch_to_window(wd[-1])
#         sleep(2)
#         zhanghao=dr.find_element_by_xpath('//*[@id="userForm0"]/div[1]/input').send_keys("{}".format(a))
#         sleep(2)
#         dr.find_element_by_xpath('//*[@id="userForm0"]/div[2]/input').send_keys('123456')
#         sleep(2)
#         dr.find_element_by_xpath('//*[@id="userForm0"]/input[2]').click()
#         wd2 = dr.find_element_by_xpath('//*[@id="userForm0"]/div[1]/span').text
#         return zhanghao,wd2

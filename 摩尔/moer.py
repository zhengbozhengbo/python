    #usr/bin/env python
    # -*- coding:utf-8 -*-

from time import sleep
from selenium import webdriver

class MO():
    def qingqiu(self):

        dr = webdriver.Chrome()
        dr.get('http://www.moore.ren')
        sleep(1)
        dr.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[2]/a').click()
        sleep(1)
        w = dr.window_handles
        dr.switch_to_window(w[-1])
        sleep(1)

        dr.find_element_by_xpath('//*[@id="userForm0"]/div[1]/input').send_keys('15237888353')
        sleep(1)
        dr.find_element_by_xpath('//*[@id="userForm0"]/div[2]/input').send_keys('bo33807358')
        sleep(1)
        dr.find_element_by_xpath('//*[@id="userForm0"]/input[2]').click()
        sleep(2)


m=MO()
m.qingqiu()

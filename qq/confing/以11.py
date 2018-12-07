# /usr/bin/env  python
# -*- coding:utf-8 -*-

from time import sleep
from selenium import webdriver


class 请求():
    def qingqiu(self):
        self.dr = webdriver.Chrome()  # 打开浏览器
        self.dr.get("https://qzone.qq.com/")  ##注意要加 https://
        sleep(1)
        # dr.maximize_window()
        a = self.dr.find_element_by_xpath('//*[@id="login_frame"]')
        self.dr.switch_to_frame(a)
        self.dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
        sleep(1)
        self.dr.find_element_by_xpath('//*[@id="u"]').send_keys('491239317')
        sleep(1)
        self.dr.find_element_by_xpath('//*[@id="p"]').send_keys('bo33807358zh')
        sleep(1)
        self.dr.find_element_by_xpath('//*[@id="login_button"]').click()
        sleep(1)
        b = self.dr.find_element_by_xpath('//*[@id="newVcodeIframe"]/iframe')
        self.dr.switch_to_frame(b)
        self.stat = self.dr.find_element_by_xpath('//*[@id="tcaptcha_drag_thumb"]')
    ## 执行
        sleep(1)
        sleep(10)
请求().qingqiu()




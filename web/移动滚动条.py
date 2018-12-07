# /usr/bin/env  python
# -*- coding:utf-8 -*-

from time import  sleep
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
# dr=webdriver.Firefox()
# dr.get("https://www.zhihu.com/")
# dr.find_element_by_xpath('/html/body/div[1]/div/main/div/div/div/div[2]/div[2]/span').click()

dr=webdriver.Chrome()
dr.get("https://qzone.qq.com/")
sleep(1)

#dr.switch_to_frame('login_frame')   #切换到内嵌框架中，只能根据id/name属性的值 定位到框架


wd=dr.find_element_by_xpath('//*[@id="login_frame"]')  #通过xpath 中iframe
dr.switch_to_frame(wd)     #切换到内框架中
dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
sleep(1)
dr.find_element_by_xpath('//*[@id="u"]').send_keys('231643173')
sleep(1)
dr.find_element_by_xpath('//*[@id="p"]').send_keys('bo3380735zheng.')
sleep(1)
dr.find_element_by_xpath('//*[@id="login_button"]').click()
sleep(2)
wd1=dr.find_element_by_xpath('//*[@id="newVcodeIframe"]/iframe')
dr.switch_to_frame(wd1)
stat=dr.find_element_by_xpath('//*[@id="tcaptcha_drag_thumb"]')
ActionChains(dr).drag_and_drop_by_offset(stat,180,0).perform() ## 执行
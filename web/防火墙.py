# /usr/bin/env  python
# -*- coding:utf-8 -*-

from time import  sleep
from selenium import webdriver
import re

#dr=webdriver.Firefox()
dr=webdriver.Chrome()
dr.get("https://192.168.0.254:8889/")
sleep(1)
dr.find_element_by_name("txt_name").clear()
sleep(1)
dr.find_element_by_class_name("login_input").send_keys("administrator")
sleep(1)
dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[2]/input').send_keys('Bane@7766')
sleep(1)

wd=dr.find_element_by_xpath('//*[@id="checkinfo"]').find_elements_by_tag_name("img")

patt=re.compile(r"/imgs/(.*?).gif",re.S)
a=[]
for i in wd:
    b=i.get_attribute("src")
    c=patt.findall(b)
    a.append(c)
for i in range(len(a)):
    dr.find_element_by_xpath('//*[@id="input1"]').send_keys("{}".format(a[i][0]))
sleep(2)

dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[4]/input[1]').click()
wd=dr.switch_to_alert()    #切换到弹出框
# print(wd.text)   ##获取弹出框的文本
wd.accept()  ##点击确认

wd2=dr.find_element_by_xpath('//*[@id="Content"]/frame[1]')
dr.switch_to_frame(wd2)            ##切换内框架
dr.find_element_by_xpath('//*[@id="04_image"]').click()  #点开关
dr.find_element_by_xpath('//*[@id="041"]').click()   #点策略
sleep(2)
dr.switch_to_default_content()  ##退出到原始的页面
wd4=dr.find_element_by_xpath('//*[@id="Content"]/frameset/frame[1]')
dr.switch_to_frame(wd4)
dr.find_element_by_xpath('//*[@id="nav_0"]').click()  ##安全策略v
sleep(3)
dr.switch_to_default_content()  ##退出到原始的页面
wd3=dr.find_element_by_xpath('//*[@id="main"]')  #新建框架
dr.switch_to_frame(wd3)
dr.find_element_by_xpath('//*[@id="content"]/form[2]/table/tbody/tr/td[2]/div/div/a').click()  #新建
dr.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[2]/td/table/tbody/tr[2]/td[4]/input').clear()
dr.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[2]/td/table/tbody/tr[2]/td[4]/input').send_keys('55')
sleep(3)
dr.find_element_by_xpath('/html/body/form/table[2]/tbody/tr/td/div/div[1]/a').click()  #提交
sleep(2)







# dr.quit()
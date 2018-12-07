# /usr/bin/env  python
# -*- coding:utf-8 -*-


from time import  sleep
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

dr=webdriver.Chrome()
dr.get("http://aaaaaa.alltuu.com/v/work")
sleep(2)
print(dr.title)
print(dr.current_url)

dr.find_element_by_xpath('//*[@id="app"]/div/div/section/div[1]/div/div[2]/ul/li[3]/div/a[1]').click()
w=dr.window_handles
dr.switch_to_window(w[-1]) #切换句柄

dr.find_element_by_id("loginUsername").send_keys("15237888353")
##dr.find_element_by_xpath("/html/body/ul/li[1]").click()
wd2=dr.find_element_by_xpath('/html/body/ul').find_elements_by_tag_name('li')
for i in wd2:
    if '15237888353' == i.text :
        ActionChains(dr).move_to_element(i).perform()
        sleep(2)
        i.click()
    else:
        ActionChains(dr).move_to_element(i).perform()
        sleep(1)
dr.find_element_by_id("loginPassword").send_keys("bo33807358")
sleep(2)

dr.find_element_by_id("login").click()
sleep(2)

dr.find_element_by_class_name("iconfone icon-add").click()
sleep(3)
dr.find_element_by_xpath('//*[@id="app"]/div/div/section/div[3]/div[2]/div[1]/ul/li[1]/div[3]/table/tr/th[1]/a').click()
w=dr.window_handles
dr.switch_to_window(w[-1]) #切换句柄
# dr.get("http://aaaaaa.alltuu.com/v/localUpload?id=1005277404")
# #dr.find_element_by_id("addLocalUpload").send_keys(r"‪C:\Users\zhengbo\Desktop\a.jpg")
wd=dr.switch_to_alert()
wd.find_element_by_id("addLocalUpload").send_keys(r"‪C:\Users\zhengbo\Desktop\a.jpg")
wd.accept()  ##点击确认

#   dr.quit()
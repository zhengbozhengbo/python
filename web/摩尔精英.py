# /usr/bin/env  python
# -*- coding:utf-8 -*-


from time import  sleep
from selenium import webdriver

#dr=webdriver.Firefox()
dr=webdriver.Chrome()
dr.get("http://www.moore.ren")
sleep(2)
print(dr.title)
print(dr.current_url)

#④通过超文本定位 link_test
dr.find_element_by_link_text('登录').click()
w=dr.window_handles
dr.switch_to_window(w[-1]) #切换句柄
sleep(2)
dr.find_element_by_id("emailInput").send_keys("zhengbo19960406@163.com")
dr.find_element_by_id("passwordInput").send_keys("bo33807358")
sleep(3)

dr.find_element_by_xpath("//*[@id='userForm']/input[1]").click()

sleep(10)
dr.quit()


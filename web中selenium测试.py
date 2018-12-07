# /usr/bin/env  python
# -*- coding:utf-8 -*-

#关于selenium模块
# ##检测火狐是否可以
# from time import sleep
# from selenium import webdriver
# dr=webdriver.Firefox()     ##打开浏览器
# dr.get("https://www.baidu.com/")  ##注意要加 https://
# sleep(2)
# dr.quit()  #关闭浏览器

##检测谷歌是否可用

# from time import sleep
# from selenium import webdriver
# dr=webdriver.Chrome()          #打开浏览器
# dr.get("https://www.baidu.com/")  ##注意要加 https://
# sleep(2)

##获取网页的标题
#print(dr.title)  ##通常用来断言
##获取网站的网址
#print(dr.current_url)

##保证所有的测试用例在同一环境下测试（设置大小和位置）
# ##设置浏览器的大小(宽，高)
# dr.set_window_size(400,400)
# ##设置浏览器的位置
# dr.set_window_position(500,500)
#sleep(10)

# dr.maximize_window()   ##浏览器最大化
# sleep(3)
# dr.minimize_window()  ##浏览器最小化
# sleep(5)

# dr.get('https://www.jd.com')
# sleep(3)
# #
# dr.back() #后退
# sleep(3)
# dr.forward()  #前进
# sleep(3)

#webdriver提供了一系列的对象定位方法，常用的有以下几种:
# id/name/class name/link text/partial link text/tag name/xpath/css selector
#定位：保证属性的值的唯一性
##通过id的属性定位  webdriver模拟人的行为

#①通过id的属性定位 定位到id=kw 的位置  (sed_keys  输入)
# dr.find_element_by_id('kw').send_keys('动漫美女')
# sleep(3)
# dr.find_element_by_id('su').click()

    #②通过class的属性定位 定位到class=s_ipt的位置  (sed_keys  输入)
# # dr.find_element_by_class_name('s_ipt').send_keys('动漫美女')
# # sleep(3)
# # dr.find_element_by_id('su').click()
#
# # ③通过name的属性定位 定位到name=wd的位置  (sed_keys  输入)
# # dr.find_element_by_name('wd').send_keys('古风动漫美女')
# # sleep(3)
# # dr.find_element_by_id('su').click()

# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
#
# dr=webdriver.Chrome()          #打开浏览器
# #dr=webdriver.Firefox()
# dr.get("http://www.moore.ren")  ##注意要加 https://
# sleep(3)

#④通过超文本定位 link_test   保证定位元素的唯一性
#dr.find_element_by_link_text('登录').click()

#⑤通过模糊的超文本定位 partial link text
# dr.find_element_by_partial_link_text('登录').click()

#⑥通过标签的名称去定位  通常用于多个元素的定位(了解)
    #dr.find_elements_by_tag_name()

#⑦xpath:路径标记语言（/：绝对路径  //：相对路径）
#       路径===xml:可扩展标记语言
#dr.find_element_by_xpath('/html/body/div[2]/div/div[2]/dl/dd[3]/a').click()  #/html：绝对路径
#dr.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[1]').click()
# dr.find_element_by_xpath('')

#⑧通过css定位
#dr.find_element_by_css_selector('').click()

###定位一组对象
#定位多个class属性的值为 menu-box 的元素  数据类型为列表
# wd=dr.find_elements_by_class_name('menu-box')
# for i in wd:
#     ActionChains(dr).move_to_element(i).perform()
#     sleep(2)

# print(len(wd))

##层级定位
#wd=dr.find_element_by_xpath('//*[@id="J_cate"]/ul').find_elements_by_tag_name('li')

#
# wd=dr.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[1]/a')
#print(wd.get_attribute("target"))   ###获取元素的某一个属性的值

# ##直接获取文本  后加text
# d=dr.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[1]/a').text
# print(d)


##处理web窗口
# dr=webdriver.Chrome()
# dr.get("http://www.moore.ren")
# sleep(2)
#
# dr.find_element_by_link_text('登录').click()
# print(dr.window_handles)       ##获取所有窗口的句柄
#
# print(dr.current_window_handle) ##获取当前窗口的句柄
#
# kk=dr.current_window_handle
# wd=dr.window_handles
# for i in wd:
#     if i != kk:
#         dr.switch_to_window(i)  #根据句柄 切换窗口
###         dr.switch_to.window()  #版本高 时用点

#dr.switch_to_window(wd[-1])  #切换最后一个窗口
#print(dr.current_window_handle)


##框架（ifarme）：是镶嵌在web上的一个窗口
# dr=webdriver.Chrome()
# dr.get("https://qzone.qq.com/")
# sleep(2)
#
# #dr.switch_to_frame('login_frame')   #切换到内嵌框架中，只能根据id/name属性的值 定位到框架
#
#
# wd=dr.find_element_by_xpath('//*[@id="login_frame"]')  #通过xpath 中iframe
# dr.switch_to_frame(wd)     #切换到内框架中
# dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
# sleep(1)
# dr.find_element_by_xpath('//*[@id="u"]').send_keys('2316431731')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="p"]').send_keys('bo33807358zheng.')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="login_button"]').click()

#
#dr.switch_to_default_content()  #退出到原始的页面
#dr.switch_to.parent_frame()   #退出到上一层框架 （注qq空间只有一个框架 退出只能到原始框架）


###弹出框操作
# dr=webdriver.Chrome()
# dr.get("https://192.168.0.254:8889/")
# sleep(2)
#
# dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[4]/input[1]').click()
# sleep(2)
# ##弹出框
# wd=dr.switch_to_alert()    #切换到弹出框（有时间不识别to后的"."只能用下划线）
# print(wd.text)   ##获取弹出框的文本
# wd.accept()  ##点击确认
# wd.dismiss() ##点击取消
# wd.send_keys("内容") ##向弹出框输入内容

##移动滚动条  是属于浏览器的，JavaScript语言
# from selenium.webdriver.common.action_chains import ActionChains
# from time import sleep
# from selenium import webdriver
# dr=webdriver.Chrome()
# dr.get("http://www.alltuu.com/")
# sleep(2)
## ①.根据页面的高度来移动滚动条
#var q=document.documentElement.scrollTop=10000
#控制滚动条的JavaScript代码
# 10000（数字可变） 表示是所有页面的高度
# for i in range(1,10000,500):
#     js='var q=document.documentElement.scrollTop={}'.format(i)
#     dr.execute_script(js)  ##执行JavaScript语句
#     sleep(2)
##②.根据定位到的元素  移动滚动条
#定位一个元素
# wd=dr.find_element_by_xpath('//*[@id="app"]/div/div/section/div[2]/div[3]/div/div[1]/p[1]')
# #JavaScript 代码
# js='arguments[0].scrollIntoView();'
# dr.execute_script(js,wd)

#拖拽
#ActionChains(dr).drag_and_drop_by_offset(stat,180,0).perform() ## 执行


###定位元素是 webdriver  实现的

##  智能等待
# import selenium .webdriver.support.ui as ui
# from time import sleep
# from selenium import webdriver
# dr=webdriver.Chrome()
# dr.get("http://www.moore.ren/")
# dr.maximize_window()
#
# sleep(2)  #强制等待
#
# #智能等待  设置控制器dr等待
# wait = ui.WebDriverWait(dr, 10)
# #判断最大等待时间10s  判断 以下元素是否出现 如10s内没出现 报错（timeout）
# wait.until(lambda dr: dr.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[6]/div/a/img').is_displayed())  ##可判断条件 在if中
#
# ## is_displayed:判断元素是否显示  结果：True  Flase
# ## is_enabled:判断元素是否为灰化状态
#
# dr.quit()

##截图并保存
from time import sleep
from selenium import webdriver
dr=webdriver.Chrome()
dr.get("http://www.moore.ren/")
dr.maximize_window()

dr.get_screenshot_as_file('bbb.png')  # 截图并保存

dr.get_screenshot_as_png()  #截图
dr.save_screenshot('ccc.png')  #保存截图

###click ：点击
#dr.quit()  #关闭浏览器
#dr.close()  #关闭窗口



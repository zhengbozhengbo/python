# # /usr/bin/env python
# # -*- coding:utf-8 -*-
#
# from tkinter import *
# from PIL import Image
# from PIL import ImageTk
# from tkinter import messagebox
#
# def xunhuan():
#     #设置提示信息
#     messagebox.showinfo(title="不许走",message="你关不掉的")
#     return
#
# def kaiqi():
#     #在基础窗口 再开一个窗口
#     b = Toplevel(window)
#     b.geometry("300x100+520+260")
#     b.title("好巧，我也是")
#     tag2=Label(b,text="好巧 我认为不是的",font=("仿宋",20),fg="green")
#     tag2.pack()
#     yes2=Button(b,text="你说的对！", width=10, height=2,command=kaiqi3,fg="red" )
#     yes2.pack()
#     yes2 = Button(b, text="这个不能点", width=11, height=5, command=kaiqi3, fg="red")
#     yes2.pack()
#     b.protocol('WM_DELETE_WINDOW', kaiqi2)
#
#
# def kaiqi2():
#     messagebox.showinfo(title="哈哈哈",message="刚好我也是")
#     return
# def kaiqi3():
#     # 销毁所有窗口
#     window.destroy()
# def guanbi():
#     c=Toplevel(window)
#     c.geometry("300x100+520+260")
#     c.title("再等等啊")
#     tag3= Label(c,text="你是真的自恋啊",font=("仿宋",20),fg="green")
#     tag3.pack()
#     no2=Button(c,text="就是很自信",width=10,height=2,
#                command=c.destroy,fg="red") #销毁所有窗口
#     no2.pack()
#     c.protocol("WM_DELETE_WINDOW",guanbi3)
# def guanbi3():
#     guanbi()
#
# #创建窗口
# window = Tk()
# ###定义窗口标题
# window.title("因为有了因为，所有有了所以")
# ###设置窗口大小
# window.geometry("500x800")
# # 用户关闭窗口触发的时间
# window.protocol('WM_DELETE_WINDOW',xunhuan)
# ###定义一个文本的标签
# tag = Label(window,text="天降一个大美女？",font=("仿宋",20))
# ###将标签放在窗口的哪个位置
# tag.grid(row=0,column=0,sticky=W)
# ###定义一个按钮的标签
# no = Button(window,text="当然了！",width=10,
#             height=2,fg="green",command=guanbi)
# no.grid(row=3,column=1)
# yes = Button(window,text="你说是吗？",width=10,
#             height=2,fg="green",command=kaiqi)
# yes.grid(row=3,column=0)
# ##显示图片
# img = Image.open('1.jpg')  #打开图片
# photo = ImageTk.PhotoImage(img)  #定义图片
# imgphoto = Label(window, image=photo)  #图片写入
# imgphoto.grid(row=2, columnspan=2) #放在位置
# ####显示窗口
# window.mainloop()
#


# import smtplib
# import email.mime.text
# import email.mime.multipart
#
# sender= "2316431731@qq.com"
# recver = "zhengbo19660406@163.com"

# with open("aa.txt","r",encoding="utf-8") as f:
#     a= f.readlines()
#     b=0
#     for i in a:
#         if i =="\n" or i.startswith("#"):
#            continue
#         else:
#             b+=1
#     print(b)


# with open("wenjian ","r",encoding="utf-8" )as f:
#     f.read()
#     f.readline()
#     f.readlines()
#
# import pymysql
# abc=pymysql.connect(host="",user="",port="",password="",charset="")
# aa=abc.cursor()
# aa.execute()
# aa.fetchall()
# aa.fetchmany()
# aa.fetchone()
# abc.commint()

import xlwt
import xlrd
import  xlutils
# aa=xlwt.Workbook(encoding="utf-8")
# sheet = aa.add_sheet("标签页")
# sheet.write()
#
# bb=xlrd.open_workbook("text3.xls")
# print(bb.sheet_names())
# sheet= bb.sheets()[0]
# c=sheet.nrows
# d=sheet.ncols
#
# for i in range(c):
#     e=sheet.row_values(i)
#     print(e)

#import xlutils
# from xlutils.copy import copy
# f=xlrd.open_workbook("text3.xls")
# ff=copy(f)
# print(f.nsheets)
# sheet=ff.get_sheet(0)
# sheet.write(0,4,"你是不是傻")
# ff.save("text3.xls")
#import socket


# class datetext:
    # int
    # y, m, d
    # init()
    # next(x)

# shuju2 = []
# f = open(r"E:\python 文件\框架\driver\文件1.txt","r")
# a=f.readlines()
# print(a)
##压缩完 打印压缩文件
# a=[1,2]
# b=[3,4]
# c=zip(a,b)
# print(c)
# d=[i for i in c]
# print(d)  ##打印压缩数据


# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
#
# dr=webdriver.Chrome()          #打开浏览器
# dr.get("http://www.ctrip.com/")  ##注意要加 https://
# sleep(3)
# #dr.find_element_by_xpath('//*[@id="J_roomCountList"]').click()
# wd=dr.find_element_by_xpath('//*[@id="searchHotelLevelSelect"]').find_elements_by_tag_name('option')
# for i in wd:
#     i.click()
#     sleep(2)

#print(wd.get_attribute("class"))   ###获取元素的某一个属性的值
#wd=dr.find_element_by_xpath('//*[@id="J_cate"]/ul').find_elements_by_tag_name('li')
# for i in wd:
#     ActionChains(dr).move_to_element(i).perform()
#     sleep(1)
#
# print(len(wd))

###随机数1-100之间取20次 前十次升序 后十次倒序
# import random
# c=[]
# d=[]
# for i in range(10):
#     a = random.randrange(1, 100)
#     c.append(a)
# c.sort()
# for j in range(10):
#     a = random.randrange(1, 100)
#     d.append(a)
# d.sort(reverse=True)
# c.extend(d)
# # print(c)
# import turtle as f
# f.speed("fast")
# f.hideturtle()
# f.bgcolor("black")
#
# i=0
# while i<135:
#     f.pencolor("red")
#     f.penup()
#     f.goto(0,0)
#     f.forward(200)
#     f.pendown()
#     f.circle(100)
#     f.left(2)
#     i+=1

# from time import sleep
# from selenium import webdriver
# dr=webdriver.Chrome()
# dr.get('http://www.moore.ren')
# sleep(1)
# dr.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[2]/a').click()
# sleep(1)
# w=dr.window_handles
# dr.switch_to_window(w[-1])
# sleep(1)
#
# dr.find_element_by_xpath('//*[@id="userForm0"]/div[1]/input').send_keys('15237888353')
# sleep(1)
# dr.find_element_by_xpath('//*[@id="userForm0"]/div[2]/input').send_keys('bo33807358')
# sleep(1)
# dr.find_element_by_xpath('//*[@id="userForm0"]/div[5]/div[2]').click()
# dr.find_element_by_xpath('//*[@id="userForm0"]/input[2]').click()


f=open('哈哈2.jpg','rb')

a=f.read()

k=open('999.jpg','wb')
k.write(a)
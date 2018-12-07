#  /usr/bin/env python   #
# -*- coding:utf-8-*-
#import time
#常用的模块的使用：1.pymsql 对MySQL数据库操作

#
# import pymysql   #前提
# #连接数据库
# abc=pymysql.connect(host="192.168.0.182",
#               port=3306,
# aaa.execute("select * from a;")
# print(aaa.fetchmany(2))     #默认读取一条，现在2 读取两条
# print(aaa.fetchall())       #读取(全部) 上一条 未读的全部
# aaa.execute("select * from b;")
# print(aaa.fetchone())   #每次只读取一个结果，本身有迭代功能
# print(aaa.fetchone())
# print(aaa.fetchone())
#               user="root",
#               password="654321",
#               charset="utf8")
#创建游标
# aaa = abc.cursor()

# aaa.execute("show databases;")    #execute(只能写一个语句)执行SQL语句
# print(aaa.fetchall())         #只读取上一句sql语句的结果(元组)
# aaa.execute("use shujuku;")
# aaa.execute("show tables;")

#aaa.execute("create database python1;")
# aaa.execute("use python1;")
# aaa.execute("create table biao1(姓名 char(255),年龄 int,班级 char(255));")
# list1 = ["郑博",1,"软件测试"]
# for i in range(30):
#     aaa.execute('insert into biao1 values("{}","{}","{}");'.format(list1[0],list1[1]+i,list1[2]))
#     abc.commit()  ##提交数据:
#
# aaa.execute("select * from biao1;")
# for i in aaa.fetchall():
#     print(i)
#####数据库到TXT
# aaa.execute("desc biao1")
# biaotou=aaa.fetchall()
# aaa.execute("select * from biao1")
# shuju=aaa.fetchall()
# with open("aa.txt","w",encoding="utf-8") as f:
#     for i in biaotou:
#         if i==len(biaotou)-1:
#             f.write(i[0])
#         else:
#             f.write(i[0]+",")
#     for i in shuju:
#         f.write("\n"+"{},{},{}".format(i[0],i[1],i[2]))

#  os模块：Python自带的模块
#作用：Python与操作系统之间的交互

#import os
# a = os.popen("ping 192.168.0.1")   #执行windows命令
# print(a.read())
# b = os.popen("nslookup www.baidu.com")
# print(b.read())

#获取当前所在的位置
# print(os.getcwd())
# #切换目录
# os.chdir(r"E:/python 文件")  #两个斜杠或前面加r:为了让转义字符不转义
# print(os.getcwd())
# #创建目录
# os.mkdir("aaaa") #如果不加路径就在当前目录下创建
# #创建递归目录
# os.makedirs(r"aaa/bbb/ccc")
# #删除递归目录
# os.removedirs(r"aaa/bbb/ccc")
# #删除空目录
# os.rmdir("aaaa")
# #删除文件
# os.remove("b.txt")

#获取当前目录下的所有文件
# print(os.listdir(r"E:\python 文件"))
#
# #更改文件名
# os.rename("777.jpg","美女.jpg")

#将文件名与路径分割开(注意：分割的是字符串与有无此文件和路径无关)
#print(os.path.split(r"D:\Python\Python36\python\aaa.txt"))

#将文件的后缀名与路径分割开
# print(os.path.splitext(r"D:\Python\Python36\python\aaa.txt"))
#
# os.path.isfile("aaa.txt")  #判断是否为普通文件
# os.path.isdir("aaa.txt")    #判断是否为目录文件
# os.path.islink("aaa.txt")    #判断是否为链接文件

# for i in os.listdir():
#     if os.path.isfile(i):
#         print(i)
# def wenjian(a):
#     m=0
#     k=0
#     os.chdir(a)
#     for i in os.listdir():
#         print(i)
#         if os.path.isfile(i):
#             m+=1
#         elif os.path.isdir(i):
#             k+=1
#     print(m,k)

# a = [i for i in os.listdir() if os.path.isfile(i)]
# b = [k for k in os.listdir() if os.path.isdir(k)]
# print(len(a),len(b))


# ① xlwt 需要下载的模块 作用：给Excel表格写入数据
# ②xlrd 需要下载的模块 作用：读取Excel表格中的数据
# ③xlutils 需要下载的模块 作用：给Excel表格中追加数据

#①写入Excel（xlwt）
# import xlwt
# #打开一个文件
# f=xlwt.Workbook(encoding="utf-8")
# #添加一个标签页，括号写标签页的名称
# sheet=f.add_sheet("python操作Excel表格")
#写入数据
# 第一个数字代表多少行，第一行从0开始
# 第一个数字代表多少列，第一列从0开始
#第三个字符串代表写入的内容
# sheet.write(0,0,"姓名")

#保存文件(文件名)
#f.save("text1.xls")

# a=["姓名","年龄","班级"]
# b=["小明","18","一班"]
# for i in range(3):
#     sheet.write(0,i,a[i])
#     for k in range(30):
#         sheet.write(k+1,i,b[i])
# f.save("text3.xls")

###:TxT转成Excel
# import xlwt
# o=xlwt.Workbook(encoding="utf-8")
# sheet=o.add_sheet("shenmogui")
# f=open("aa.txt","r+",encoding="utf-8")
# b=f.read()
# c=b.split("\n")
# print(c)
# s = 0
# for i in c:
#     p=i.split(",")
#     print(p)
#     d=len(p)
#     print(d)
#     for k in range(d):
#         sheet.write(s,k,p[k])
#     s+=1
# o.save("text10.xls")


#②读取Excel表格（xlrd）

# import xlrd
# #打开一个文件
# f = xlrd.open_workbook("text3.xls")
#两种获取标签页  1.通过索引来获取  2.通过标签页的名称
# sheet = f.nsheets   #获取有多少个标签页
#print(f.nsheets)
#sheet = f.sheets()[0]   #索引获取标签页
# print(f.sheet_names())  #获取所有标签页的名称
# sheet=f.sheet_by_name("python操作Excel表格")  #括号中填写操作的标签页名称

#print(sheet.nrows) #获取文件中有多少行
#print(sheet.row_values(0))  #row_values() #读取第几行的内容，第一行从零 开始
# a = sheet.nrows #获取文件中有多少行
# for i in range(a):
#     print(sheet.row_values(i))  #row_values() #读取第几行的内容，第一行从零 开始

# print(sheet.ncols)   #获取有多少列
# print(sheet.col_values(0))   #读取第几列的内容，第一列从零开始
# b=sheet.ncols
# for i in range(b):
#     print(sheet.col_values(i))

# print(sheet.cell(0,2).value)   #读取某一个单元格的内容

#③Excel表格追加(xlutils)
# import  xlrd
# from xlutils.copy import copy
#
# f= xlrd.open_workbook("text3.xls")
# #复制文件
# new_f = copy(f)
#
# #print(f.nsheets)   #索引的个数
# #操作复制的文件
# sheet = new_f.get_sheet(0)  #通过索引来来获取
#
# sheet.write(5,5,"去你没得")   #写入
# new_f.save("text3.xls")

#paramiko封装ssh协议  作用：远程连接
#import paramiko

#创建一个ssh客户端
# ssh123 = paramiko.SSHClient()
#把将要连接的主机添加到 know_host 文件去
# ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#
# ssh123.connect(hostname="192.168.0.182",
#                port=22,
#                username="root",
#                password="123456")

#执行命令  产生三个结果
#第一个变量：执行命令，输入
#第二个变量：命令的结果，输出
#第三个变量：命令的报错

#输入的命令只能是有结果的命令
# stuin,stuout,stuerr = ssh123.exec_command("ls -al")
# print(stuout.read().decode())   #decode：解码

#ssh123.close()   #断开连接

# #小循环 无限输命令：
# import paramiko
# ssh123 = paramiko.SSHClient()
# ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh123.connect(hostname="192.168.0.182",
#                port=22,
#                username="root",
#                password="123456")
# while True:
#     a=input("输入命令：")
#     if a=="exit":
#         break
#     else:
#         tuin, stuout, stuerr = ssh123.exec_command(a)
#         print(stuout.read().decode())
# ssh123.close()

#
# import paramiko
# #创建一个传输通道  接收的只能是元组
# ssh123 = paramiko.Transport(("192.168.0.182",22))
# ssh123.connect(username="root",password="123456")
# #传输文件使用sftp协议 ， 创建一个sftp的实例
# sftp = paramiko.SFTPClient.from_transport(ssh123)
#
# #get 是从Linux下载文件到本地
# sftp.get("/home/美女.jpg","./哈哈2.jpg")

#put 是从本地向Linux上上传文件
#sftp.put("大美女.jpg","/home/美女.jpg")


# ###### 发送邮件######
#
# import smtplib  #发送邮件的协议
# import email.mime.text  #处理发送的内容
# import email.mime.multipart   # 处理邮件的表头
#
# sender = "zhengbo19960406@163.com"       #发送者
# recver = ["doungln@163.com",
#           "xcz201807@163.com",
#           "m15037109541@163.com",
#           "2316431731@qq.com"]     #接受者
# server = "smtp.163.com"            #服务器地址
# passwd = "bo33807358zheng"               #授权码
# #创建一个空邮件
# zhengbo = email.mime.multipart.MIMEMultipart()
# #发件人
# zhengbo["from"] = sender
# #收件人
# zhengbo["to"] = ','.join(recver)#主题
# zhengbo["subject"] ="小白兔白又白"
# #正文
# text = """
#    煮一壶清月，浅吟流年
# 流年......
# 这便是我所经过的流年
# 不得不说
# 只剩这不经转动的流年"""
# # 处理文本信息
# text = email.mime.text.MIMEText(text)
# # 将处理后的信息添加到邮件里
# zhengbo.attach(text)
#
# #添加附件 ； 处理附件：以二进制的方式读取文件
# att1=email.mime.text.MIMEText(open(r"C:\Users\zhengbo\Desktop\a.jpg","rb").read(),"base64","utf-8")  #添加本地文件
# att1["Content-Type"] = "application/octet-stream"
# att1["Content-Disposition"] = "attachment; filename='a.jpg'"   #图片名称不能是中文
# zhengbo.attach(att1)
#
# #定义服务器和端口
# smtp123 = smtplib.SMTP_SSL(server,465)
#
# #登录服务器
# smtp123.login(sender,passwd)
#
# #发送邮件
# smtp123.sendmail(sender,recver,zhengbo.as_string())
#
# #断开连接
# smtp123.close()


####时间模块

#import time

#时间戳   代表从公元1970年到现在经过的秒数   秒数
#print(time.time())

#本地时间  结果为元组：默认显示当前时间
# 年/月/日/时/分/秒/星期(索引0开始)/是一年中的第几天/是否为夏令时：1代表是，0代表不是
#参数：是填时间戳(秒数)
#print(time.localtime())

#  格式化成现代化时间
#print(time.strftime("%Y-%m-%d %H:%M:%S %A ",time.localtime()))

#将现代化时间格式化为元组
#print(time.strptime("2018 10 20","%Y %m %d")[-2])  # %后要一一对应

#将元组时间转化为时间戳  :九个元素 按前六个算时间戳
# a=(time.strptime("2018 10 20","%Y %m %d"))
# print(time.mktime(a))
# b=(1978,12,12,12,23,33,0,0,0) # :九个元素 按前六个算时间戳
# print(time.mktime(a))
#
# #  休眠
# time.sleep(5)   #休眠5秒后 打印123
# print(123)

#输入：一个现代化的日期，
# 输出：今年是否为闰年，今天星期几，今天是一年中的第几天

#1.输入日期
#2.判断是否为瑞年
#3.将日期格式化元组日期

# import time
# a=input("输入年月日，逗号隔开：")
# b=a.split(",")
# c=time.strptime("{} {} {}".format(b[0],b[1],b[2]),"%Y %m %d")
# print(c)
# d=c[0]
# if d%100==0:
#     if d%400 ==0:
#         print("是瑞年","第{}天".format(c[-2]),"星期{}".format(c[-3]+1))
#     elif d%400!=0:
#         print("平年", "第{}天".format(c[-2]), "星期{}".format(c[-3] + 1))
# else:
#     if d%4==0:
#         print("是瑞年", "第{}天".format(c[-2]), "星期{}".format(c[-3] + 1))
#     elif d%4!=0:
#         print("平年", "第{}天".format(c[-2]), "星期{}".format(c[-3] + 1))
#
# import time
# a=input("输入年月日，逗号隔开：")
# b=a.split(",")
# c=(time.strptime("{} {} {}".format(b[0],b[1],b[2]),"%Y %m %d"))
# print(c)
# d=time.mktime(c)-24*60*60
# print(time.strftime("%Y-%m-%d",time.localtime(d)))

#判断输入年份是否为闰年
# import time
# a=input("输入日期，逗号隔开")
# b=a.split(",")
# c=time.strptime('{} {} {}'.format(b[0],b[1],b[2]),"%Y %m %d")
# print(c)
# if (c[0]%4==0 and c[0]%100!=0) or c[0]%400==0:
#     print("是瑞年", "第{}天".format(c[-2]), "星期{}".format(c[-3] + 1))
# else:
#     print("平年", "第{}天".format(c[-2]), "星期{}".format(c[-3] + 1))

###判断路径下有多少普通文件
# import os
# a=input("输入路径：")
# b=os.listdir(r"{}".format(a))
# c=0
# d=0
# for i in range(len(b)):
#     if os.path.isfile(b[i]):
#         c+=1
#     else:
#         d+=1
# print(c,d)


#########基于tcp的socket 协议
#socket:套接字，提供了网络间通讯的基本功能（向网络发送请求，应答网络请求）
#socketserver:(服务器使用)---协议处理

# #server 服务器端
# import socket
# #创建socket，  封装协议（ipv4协议，tcp协议）
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# #绑定ip和端口号  bind 接收到的参数是元组
# a=("192.168.0.82",3000)   #ip127.0.0.1环回地址 只能自己访问 其他为只要能ping通就能访问 ，端口号1-65536
# s.bind(a)     #元组
# #监听   #参数为数字：指的是最大等待数
# s.listen(3)   #参数为数字：指的是最大等待数
# while True:
#     #接收请求
#     a,b=s.accept()    #接收:产生两个结果 a:是客户端的连接信息 b:客户端的ip地址和端口号
#     #接收数据
#     msg=a.recv(1024)    #1024/512:每次接收的最大字节数
#     print(msg.decode("utf-8"))  #解码
#     #发送响应
#     reg="你是不是傻？"
#     a.send(reg.encode("utf-8"))

# #client 客户端
# import socket
# #创建socket，  封装协议（ipv4协议，tcp协议）
# soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# #连接服务器   #接收到的参数元组
# soc.connect(("192.168.0.26",3000))
# aaa="你个小傻瓜"
# soc.send(aaa.encode("utf-8"))
# #接收响应
# msg=soc.recv(1024)
# print(msg.decode("utf-8"))




#########基于udp的socket 协议
# ###
# #server 服务器端
# import socket
# #创建socket，  封装协议（ipv4协议，tcp协议）
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  #tcp和udp的区别
# #绑定ip和端口号  bind 接收到的参数是元组
# a=("192.168.0.82",3000)   #ip127.0.0.1环回地址 只能自己访问 其他为只要能ping通就能访问 ，端口号1-65536
#                             # 本机ip ,环回地址，默认地址  ，0.0.0.0：所有的ip
# s.bind(a)     #元组
# #udp无监听   #参数为数字：指的是最大等待数
#
# while True:
#     a,b=s.recvfrom(1024) #接收数据 两个变量 a:客户端发送的请求数据 b:客户端的ip地址和端口号
#     print(a.decode("utf-8"))
#     print(b)
#     #发送响应数据
#     msg= "为什么付出的那摸多"
#     s.sendto(msg.encode("utf-8"),b)  #发送数据  发送给b

# # #client 基于udp的客户端
# import socket#创建socket，  封装协议（ipv4协议，tcp协议）
# soc=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# #发送请求数据
# a=("192.168.0.82",3000)
# while True:
#     reg=input("退出exit，输入：")
#     if reg=="exit":
#         break
#     else:
#         #reg="我是谁，我在哪，我还好吗"
#         soc.sendto(reg.encode("utf-8"),a)
#         #接收响应
#         c=soc.recv(1024)
#         print(c.decode("utf-8"))


# ####json模块
# import json
#
# data={"name":"郑","age":20}
# #将字典更改为json字符串数据
# data1=json.dumps(data)
# print(data1)
# #将json数据更改为字典
# data2=json.loads(data1)
# print(type(data2))

#关于selenium模块
# ##检测火狐是否可以
# from time import sleep
# from selenium import webdriver
# dr=webdriver.Firefox()     ##打开浏览器
# dr.get("https://www.baidu.com/")  ##注意要加 https://
# sleep(2)
# dr.quit()  #关闭浏览器

##检测谷歌是否可用

from time import sleep
from selenium import webdriver
dr=webdriver.Chrome()          #打开浏览器
dr.get("https://www.baidu.com/")  ##注意要加 https://
sleep(3)

##获取网页的标题
print(dr.title)  ##通常用来断言
##获取网站的网址
print(dr.current_url)

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
#
# dr.back() #后退
# sleep(3)
# dr.forward()  #前进
# sleep(3)

#webdriver提供了一系列的对象定位方法，常用的有以下几种:
# id/name/class name/link text/partial link text/tag name/xpath/css selector
#定位：保证属性的值的唯一性
##通过id的属性定位  webdriver模拟人的行为

#通过id的属性定位 定位到id=kw 的位置  (sed_keys  输入)
# dr.find_element_by_id('kw').send_keys('动漫美女')
# sleep(3)
# dr.find_element_by_id('su').click()

#通过class的属性定位 定位到class=s_ipt的位置  (sed_keys  输入)
# dr.find_element_by_class_name('s_ipt').send_keys('动漫美女')
# sleep(3)
# dr.find_element_by_id('su').click()

# #通过name的属性定位 定位到name=wd的位置  (sed_keys  输入)
# dr.find_element_by_name('wd').send_keys('古风动漫美女')
# sleep(3)
# dr.find_element_by_id('su').click()

###click ：点击



#dr.quit()  #关闭浏览器
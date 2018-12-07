#! /usr/bin/env   python
#  -*- coding:utf-8 -*-


# #########基于tcp的socket 协议
# ###
# #server 服务器端
# import socket
# #创建socket，  封装协议（ipv4协议，tcp协议）
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# #绑定ip和端口号  bind 接收到的参数是元组
# a=("0.0.0.0",3000)   #ip127.0.0.1环回地址 只能自己访问 其他为只要能ping通就能访问 ，端口号1-65536
#                             # 本机ip ,环回地址，默认地址  ，0.0.0.0：所有的ip
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
#


#########基于udp的socket 协议
###
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
#     #msg= "为什么付出的那摸多"
#     msg=input("shuru:")
#     s.sendto(msg.encode("utf-8"),b)  #发送数据  发送给b

# import socket
# # s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# # a=("192.168.0.68",3000)
# # s.bind(a)
# # #s.listen(2)
# # while True:
# #     # a,b=s.accept()
# #     # msg=a.recv(1024)
# #     # print(msg.decode("utf-8"))
# #     # print(b)
# #     # reg="小垃圾"
# #     # a.send(reg.encode("utf-8"))
# #     a,b=s.recvfrom(1024)
# #     print(a.decode("utf-8"))
# #     reg="号码"
# #     s.sendto(reg.encode("utf-8"),b)


# string="bang"
# a=string*5
# print(a)

# ###输入a 打印菱形
# def s(a):
#     for i in range(a):
#         print(" "*(a-i)+" *"*(i+1))
#     for i in range(a-1):
#         print(" "*(i+2)+ " *"*(a-1-i))
#
# s(2)
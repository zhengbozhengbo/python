#!/usr/bin/env python
# -*- coding:utf-8 -*-

#client 基于tcp的客户端
# import socket#创建socket，  封装协议（ipv4协议，tcp协议）
# soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# #连接服务器   #接收到的参数元组
# soc.connect(("192.168.0.68",3000))
# aaa="你个小傻瓜"
# soc.send(aaa.encode("utf-8"))
# #接收响应
# msg=soc.recv(1024)
# print(msg.decode("utf-8"))

# # #client 基于udp的客户端
# import socket#创建socket，  封装协议（ipv4协议，tcp协议）
# soc=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# #发送请求数据
# a=("192.168.0.68",3000)
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



# import socket
# so=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# #so.connect(("192.168.0.68",3000))
# a=("192.168.0.68",3000)
# aa="你的谁"
# so.sendto(aa.encode("utf-8"),a)
# msg=so.recv(1024)
# print(msg.decode("utf-8"))




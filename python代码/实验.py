#/usr/bin/env  python
#-*- coding:utf-8 -*-


from socket import *
client= socket()
client.connect(("192.168.0.76",18888))
while True:
    send_data= input(">>>")
    client.send(send_data.encode("utf-8"))
    recv_data= client.recv(1024)
    print(">>>%s" % recv_data.decode())
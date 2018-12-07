#  /usr/bin/env python
# -*- coding:utf-8-*-
#import random

#①九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#  #       print("{}*{}={}".format(j,i,i*j),end="\t")
#          print("%d*%d=%d" % (j,i,i*j), end="\t")   #格式化整数
#     print()
# def jiujiu():
#      for i in range(1,10):
#         for j in range(1,i+1):
#      #       print("{}*{}={}".format(j,i,i*j),end="\t")
#              print("%d*%d=%d" % (j,i,i*j), end="\t")   #格式化整数
#         print()
# jiujiu()

#②质数之和
# c=0      #方法一               #方法二
# for i in range(2,101):
#     for k in range(2,i+1):    #for k in range(2,i):
#         b = i % k
#         if b==0:
#             break
    # if i==k:                  #else:
    #     c+=i                   #  a+=i
# print(c)                     print(a)



#阶乘和
# b=int(input("输入:"))
# c=1
# d=0
# for i in range(1,b+1):
#     c=c*i
#     d=d+c
# print(d)

#判断三角形
#a = [3,4,5]     #方法一
#b.sort
# if b[0]+b[1] >b[2]:
#     print("这是个三角形")
#     if b[0]**2+b[1]**2==b[2]**2:
#          print("直角三角形")
#     elif b[0]**2+b[1]**2<b[2]**2:
#         print("钝角")
#     elif b[0]**2+b[1]**2>b[2]**2:
#         print("锐角")
# else:
#     print("不是三角形")
#
#a=input('请输入三个数')   #方法二
#b=a.split(',')
# c=int(b[0])
# d=int(b[1])
# e=int(b[2])
# if c+d>e:
#     if c**2+d**2==e**2:
#         print('直角三角形')
#     elif c**2+d**2<e**2:
#         print('钝角三角形')
#     elif c ** 2 + d ** 2 > e ** 2:
#         print('锐角三角形')
#     else:
#         print('三角形')
# else:
#     print('啥都不是')

#随机产生数字，三次猜数据
# import random
# a= random.randrange(1,10)   #从1-9随机产生一个数
# for i in range(3):         #while True #无线循环
#     b=int(input("///："))
#     if b<a:
#         print("小了")
#         print("还有{}次机会".format(2-i))
#     elif b>a:
#         print("大了")
#         print("还有{}次机会".format(2 - i))
#     elif b==a:
#         print("对了")
#         break
# else:
#     print("真菜")

#水仙花
# for i in range(100,1000):
#     a=i//100
#     b=i//10%10
#     c=i%10
#     d=a**3+b**3+c**3
#     if d==i:
#         print("这个是水仙花{}".format(i))

#去重复 排序
# a=[1,1,1,1,1,1,1,1,1,6,9,9,9,2,2,]
# for i in a:
#     if a.count(i) > 1:
#         for k in range(a.count(i)-1):
#             a.remove(i)
# print(a)
# a.sort()
# print(a)

# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)

#eg:要求：手动输入一组数据 ①打印出平均数 ②低于平均数的数打印 ③一直输，到输入exit退出
# while True:
#     a=input("输入一组数据：")
#     if a=="exit":
#         break
#     b=a.split(",")
#     c=len(b)
#     sum=0
#     for i in b:
#         sum=sum+int(i)
#     d=sum/c
#     print("平均值:{}".format(c))
#     for k in b:
#         if int(k) <= d:
#             print(k)

#冒泡法
# a= input("输入")
# b=a.split(",")
# print(b)
# c=len(b)
# for i in range(c):
#     for j in range(c-1):
#         if  int(b[j]) > int(b[j+1]):
#             d=b[j]
#             b[j]=b[j+1]
#             b[j+1]=d
#   print(b)

#选择排序法
# a= input("输入")
# b=a.split(",")
# print(b)
# c=len(b)
# for i in range(c):
#     for k in range(i+1,c):
#         if int(b[i]) > int(b[k]):
#             d=b[i]
#             b[i]=b[k]
#             b[k]=d
#     print(b)

#不用int将字符串变成整数
#方法一
# a=input("输入：")
# b=a[::-1]
# s=0
# for i,j in enumerate(b):
#     for k in range(10):
#         if str(k)==j:
#             s=k*10**i+s
# print(s)
# print(type(s))
#方法二
# a=input("输入：")
# c=len(a)
# s=0
# for i,j in enumerate(a):
#     for k in range(10):
#         if str(k)==j:
#             s=k*10**(c-i-1)+s
# print(s)

#判断是否回文
# a=input("输入")
# b=len(a)//2
# for i in range(b):
#     if a[i] != a[-i-1]:
#         print("不是")
#         break
# else:
#     print("是回文")

#
#a=input("输入")
# b=a[::-1]
# if a==b:
#     print("是回文")
# else:
#     print("不是回文")

#十进制转化十六进制
# a=int(input("输入："))
# b=["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
# e=''
# while True:
#     c=a%16
#     a=a//16
#     e+=b[c]
#     if a==0:
#         break
# print(e[::-1])

#打印列表中最大的放在最后一位，最小的放在第一位。(不改变列表结构)
#方法一
# a=[55,988,7,7,77,9]
# b=a.index(max(a))
# c=a.index(min(a))
# a[b],a[0]=a[0],a[b]
# a[c],a[-1]=a[-1],a[c]
# print(a)
# 方法二（有问题待解决）

# a=input("输入一组数据")
# a=a.split(",")
# # a=[8,97,97,2,7,40]
# b=a.copy()
# print(b)
# c=a.index(b[0])  #最小
# print(c)
# d=a.index(b[-1])  #最大
# print(d)
# a[d],a[0]=a[0],a[d]  #
# print(a)
# a[c],a[-1]=a[-1],a[c]
# print(a)

#将列表中的元素向左挪一位
# a=[3,5,6,3,89,79,7,1]
# b=len(a)
# for i in range(b-1):
#     a[i],a[i-1]=a[i-1],a[i]
# print(a)

#打印列表中第一大和第二大的数字
#a=[1,1,5,5,5,5,1,1]
# a=input('输入')
# a=a.split(",")
# for i,j in enumerate(a):
#     a[i]=int(j)
# a.sort()
# print(a)
# b=a.count(a[-1])
# c=a.count(a[-b-1])
# for i in range(b):
#     print(a[-1])
# for k in range(c):
#     print(a[-b-1])

#一个数的因数之和等于他本身
# for i in range(1,1000):
#     s=0
#     for k in range(1,i):
#         if i%k==0:
#             s=s+k
#     if i==s:
#         print(i)

#一个有顺序的列表，随机加入一个数，加入的数在正确的位置
# a=[1,2,3,4,5,6,7,9]
# b=int(input("输入数："))
# for i in range(len(a)):
#     if int(a[0])  > b:
#         a.insert(0,b)
#         break
#     elif int(a[-1]) < b:
#         a.append(b)
#         break
#     elif int(a[i]) < b:
#         if int(a[i+1]) >= b:
#             a.insert(i+1,b)
# print(a)

#任意四个数字，组成不同的三位数
# a=input("输入四个数字，逗号隔开：")
# b=a.split(",")
# s=0
# b=[1,2,3,4]
# for i in b:
#     i=int(i)
#     for k in b:
#         k=int(k)
#         for x in b:
#             x=int(x)
#             if i !=k and k!=x and x!=i:
#                 print("%d%d%d"%(i,k,x))  #打印符合要求的三位数
#                 s+=1
# print(s)   #打印共多少个


#查看文件中 除了空行和被注释的行 有多少行
# def wenjian(c):
#     with open("{}".format(c),"r",encoding="utf-8") as f:
#         a= f.readlines()
#         b=0
#         for i in a:
#             if i =="\n" or i.startswith("#"):
#                continue
#             else:
#                 b+=1
#         print(b)
#
# wenjian("aa.txt")

# ####杨辉三角形
# def s(a):
#     for i in range(a):
#         print(" "*i+"* "*(a-i))
# s(3)
#
# ###输入a 打印菱形
# def s(a):
#     for i in range(a):
#         print(" "*(a-i)+" *"*(i+1))
#     for i in range(a-1):
#         print(" "*(i+2)+ " *"*(a-1-i))
#
# s(2)

##男平均75  女平均80.1  总平均76 共380-450人  求男女人数

# for i in range(380,451):
#     for k in range(i):
#         if 76*i==k*75+(i-k)*80.1:
#             print(k)  #男人数
#             print(i-k) #女人数

#压缩完 打印压缩文件
# a=[1,2]
# b=[3,4]
# c=zip(a,b)
# print(c)
# d=[i for i in c]
# print(d)  ##打印压缩数据

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
# print(c)

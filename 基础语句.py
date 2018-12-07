#  /usr/bin/env python
# -*- coding:utf-8-*-
#import random

#基础语句
# 1.判断语句 2.循环语句 3.异常处理语句  4.上下文管理语句

#①判断语句 （1.语句后加冒号 2.严格控制缩进）
#格式
#if 条件:
#    执行语句
#else:
#    执行语句
# a=int(input("输入数字："))
# if a > 50:
#      print("厉害了")
# else:
#     print("垃圾")

#多分支if语句格式
#if 条件1：
#     执行语句
# elif 条件2：
#     执行语句
# elif 条件3：
#     执行语句
# else:
#     执行语句
#判断成绩
# a=int(input("输入数字："))
# if a>90:
#     print("优秀")
# elif a>80:
#     print("良好")
# elif a>70:
#     print("小菜啊")
# elif a>0:
#     print("不及格啊")
# else:
#     print("输入不对")

#嵌套判断
# a=input("输入字符串")
# if a.startswith("a"):
#     if a.endswith("c"):
#       print("hello work")
#     else:
#         prnt(hello)
# elif a.endswith("c"):
#     print("work")
# else:
#     print(123)

#a = [3,4,5]
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
# a=input('请输入三个数')
# b=a.split(',')
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

# 循环语句 for while  1.没有do和done 2.冒号和缩进
# for语句  格式：
# for 变量名 in 范围:   #范围：指的是一组数据的集合
#     执行语句
#     执行语句
#     执行语句
#      .......
#①range()函数：将数字变成一个范围
# (只有一个数字时，默认从零开始，到最后减一）
# （两个数字时第一个数字是起始值，到最后减一)
#（三个数字时，第三个数字是递进，到最后减一)
#②enumerate()函数：将下标号和元素对应(字符串，列表，元组)
#print(sum(range(101)))
# a=0
# for i in range(1,101):
#     a+=i
# print(a)
# for i in range(1,10):  #，不是每次都要用到i(变量名) 主要看语句块
#     print("hlleo")
#
# a ={"name":566,"heheh":"laji","国":"加"}
# for i,j in a.items():    #不止可以写一个变量
#     print(i,j)
#要求：1-2+3-4+5....99
# a=0                 #方法1
# b=0
# for i in range(1,100,2):
#     a+=i
# for j in range(2,99,2):
#     b+=j
# print(a-b)
# b=0                  #方法2
# for i in range(1,10):
#     if i%2==0:
#         b=b-i
#     else:
#         b+=i
# print(b)

# a="7778a"
# for b in enumerate(a):     #将下标位置和元素对应
#     print(b)
# for i,j in a.items():    #不止可以写一个变量
#     print(i,j)

# a=["电脑","计算机","mp3","电视"]
# for i,b in enumerate(a):
#     print(i+1,b)
# c=int(input("输入编码:"))
# print(a[c-1])

# 循环嵌套  循环语句中嵌套其他语句 （判断语句、循环语句）
#循环嵌套判断   for 语句中 if 语句
# for a in range(1,11):
#     if a>5:
#         print(a)

#循环嵌套语句   for ... for ...
# 大循环循环一次 ，小循环循环一轮
# for i in range(3):
#     # print("第i次")
#     for j in range(2):
#         print(555)
#         for k in range(2):
#             print("hello")

#end=""  #不换行   print()：换行
# for i in range(10):
#     print(i,end="")
#     print()

# for i in range(1,10):
#     for j in range(1,i+1):
#  #       print("{}*{}={}".format(j,i,i*j),end="\t")
#          print("%d*%d=%d" % (j,i,i*j), end="\t")   #格式化整数
#     print()

#continue：结束本次循环继续下个循环  break：结束循环
# for i in range(10):
#     if i==5:
#         #continue
#         break
#     else:
#         print(i)

#for ....else....语句 原理：只要循环没有被break，就执行else语句

# a=["skk","qqfffasdasq","pp8"]
# for i in a:
#     print(i)
#     if len(i)==2:
#         break
# else:
#     print("99")
# print(len(a[1]))

#for 循环通常用于循环有序列的数据
#while 循环通常用于根据条件循环（用于无线循环：while True）

#while 循环
# while 格式:                        for语句  格式：
# while 条件:  #符合条件             for 变量名 in 范围:   #范围：指的是一组数据的集合
#     执行语句                              执行语句
#     执行语句                              执行语句
#     ........                              .......

#打印1+..100
# a = 1
# b=0
# while a < 101:   #符合条件执行
#     b+=a
#     a+=1
# print(b)
#while 循环嵌套   嵌套判断语句、循环语句
# while True:
#     while True:
#         for i in range(10):
#             if i==9:
#                 break
#             else:
#                 print(i)
#         break
#     break
# a=1
# while a<10:
#     b=1
#     while b<a+1:
#         print("%d*%d=%d" %(b,a,a*b),end="\t")
#         b+=1
#     print()
#     a += 1
#while ... else ...语句
# 循环只要没有被break掉，就执行else语句
# a=5
# while a<3:
#     print("888")
# else:
#     print(123)

#第三个Python内置函数:sum() 求和
# a=[7,8,7,9587,87]
# print(sum(a))



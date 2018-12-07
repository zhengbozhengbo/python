#  /usr/bin/env python
# -*- coding:utf-8-*-
#import random

#函数 ；具有某种功能，可重复使用的代码块
#定义格式:
# def  函数名():
#     执行语句
#     .......
# 调用函数:函数名()
#函数名的规则和变量名规则一样
# def jiujiu():
#     for i in range(1,10):
#         for k in range(1,i+1):
#             print("{}*{}={}".format(k,i,i*k),end="\t")
#         print()
#
# for t in range(1,4):
#     jiujiu()

#函数的传参：①必须参数 ②默认参数 ③可变长参数
# 1.必须参数:可为多个jiujiu(x,y,z)或jiujiu(y=6,x=5,z=9)
#优先级： 必须参数 > 默认参数 > 可变长参数
# def jiujiu(x):
#     for i in range(1,x+1):
#         for k in range(1,i+1):
#             print("{}*{}={}".format(k,i,i*k),end="\t")
#         print()
#
# jiujiu(6)

#2.默认参数；当传入数值是使用传入的，当没有数值时，使用默认参数

#3.可变长参数：
#def 函数名(*参数名) *默认参数名args  #输入数据类型为元组     #将所有的元素变成1个元组传入
#def 函数名(**参数名) *默认参数名kwargs #输入默认只能是键值对  #接收的参数值只能是键值对

# def  函数名(*参数名): #输入数据类型为元组     # def  函数名(**参数名): #输入默认只能是键值对
#     执行语句                                  #       执行语句
#     .......                                  #       .....

# def xxx(*args):
#     print(args)
#
# xxx({88888,"asdasdas",889,"sahdohaisudgasdu"},["dasuidhasd"])

# def a(x,y=10,*a):

# def quchong():
#     a=input("以逗号隔开,输入：")
#     a=a.split(",")
#     for i in a:
#         if a.count(i) > 1:
#             for k in range(a.count(i)-1):
#                 a.remove(i)
#     print(a)
#
# def quchong2():
#     a = input("以逗号隔开,输入：")
#     a = a.split(",")
#     b=[]
#     for i in a:
#         if i not in b:
#             b.append(i)
#     print(b)
#
# quchong2()

# 变量的作用域
#global   将局部变量变为全局变量
#
# a = 123     #在函数外面的变量属于全局变量
# def aaa():
# #    global a   #将a变成全局变量
#     a=999   #函数中的变量属于局部变量
#     print(a)
#
# aaa()
# print(a)

#return 1.函数的结束语  2.将return后的数据返回给调用者
# def zhishu():
#     c=0
#     for i in range(2,101):
#         for k in range(2,i+1):
#             b = i % k
#             if b==0:
#                 break
#         if i==k:
#             c+=i
#     print(c)
#     return c #将return后c的数据返回给调用者
#
# print(zhishu()+1)

#lambda   匿名函数 用来定义函数的
#格式： 函数名 = lambda:表达式
# aa=lambda:3+4 #简单的表达式
# print(aa())
# aa=lambda x=5,y=10:x*y #可以函数的传参
# print(aa())

# aa = lambda x,y:x+y
# bb = lambda x,y:x-y
# cc = lambda x,y:x*y
# dd = lambda x,y:x//y
# a=input('>>>')
# if '+' in a:
#     a=a.split('+')
#     print(aa(int(a[0]),int(a[1])))
# if '-' in a:
#     a = a.split('-')
#     print(bb(int(a[0]),int(a[1])))
# if '*' in a:
#     a = a.split('*')
#     print(cc(int(a[0]),int(a[1])))
# if '//' in a:
#     a = a.split('//')
#     print(dd(int(a[0]),int(a[1])))


#列表推到式
#将语句放到列表中，产生的结果变成列表的元素
# a=[]
# for i in range(10):
#     if i > 5:
#         a.append(i)
#
# b=[x for x in range(10) if x > 5 and x < 100]
# print(b)
#
# print(a)
# print(b)

###############Python的内置函数
# a=(56,9,7,8,99)
# print(max(a))  #列表中最大的
# min(a)   #列表中最小的

# a=100
# print(hex(a))   #将十进制转换为十六进制0x
# print(oct(a))   #将十进制转换为八进制0o
# print(bin(a))   #将十进制转换为二进制0b
# print(int(0x10))   #将其他进制转换为十进制

# a,b =divmod(100,10)  #整除求余(第一个除以第二个)
# print(a,b)
# print(b)

#对文件的操作   open() 函数
#批量操作
#格式 ：open("文件名","权限","编码方式")
#文件0名：如果不加路径，表示的是当前目录下的文件，如果此目录下有这个文件，那么就操作这个文件，如果没有就创建，写入
#如果加路径的话，要在路径上加一个双斜杠(\\),表示不转义,或者在路径前加r(r"C:\Users\zhengbo\Desktop\文件555.txt",)
#权限：代码对文件的操作权限（r:(read、readlines、readline)读权限，w:(write)写权限，a:(write)追加权限）
#f.read():读取文件中所有内容,结果是字符串
#f.readlines():读取文件中所有内容，结果是列表（\n：换行符）
#f.readline():读取文件中一行（自己能叠加），结果是字符串
# write:写入内容只能是字符串 且具备不换行的功能 a="""内容""":多行    """ """:注释掉
# w,r,a    w+,r+,a+   wb,rb,ab : 以字节码(二进制)的格式读写追加

# f = open("文件.txt","w",encoding="utf-8")   #打开一个空文件
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         f.write("{}*{}={}".format(j, i, i * j))
#          # print("%d*%d=%d" % (j,i,i*j), end="\t")   #格式化整数
#     f.write("\n")
# f.close()     #关闭文件

#上下文管理器  whit 语句 ：原理：_enter_、_exit_
# 对上下文的打开或关闭强制执行的操作
#格式 ：with 打开的文件 as 变量名：
#
#with open("文件.txt","r",encoding='utf-8') as f:
#     cc=f.readlines()
#     #print(len(f.readlines()))
#    # print(f.readlines())
#     #print(cc)
# for i in cc:
#     if i == "\n" or i.startswith("#"):
#         cc.remove(i)
# print(len(cc))
# 添加图片
# with open(r"C:\Users\zhengbo\Desktop\a.jpg","rb") as f:
#     cc=f.read()
#     print(cc)
# f.close()
#
# with open("777.jpg","wb") as e:
#     e.write(cc)
# f.close()

#异常处理语句
#异常：因为代码的逻辑关系，导致的程序中断
#异常处理(捕获)：对将要发生的异常进行预防    try...except...
#格式：

# #(针对某一种异常或多种异常处理)
# try:
#     a="123"#执行语句#(也许会发生异常的语句)
#     print(a+1)
# except NameError as b:#（默认处理name异常）
#     print(b) #执行语句#(上一个执行语句错误，执行此语句)
# except TypeError as c:
#     print(c)
# except Exception:  #默认处理所有异常
#     print("其他错误")
#当你只想处理一种异常错误时，在except语句后面加上异常的类型
#如果要写多个except的话，保证每个后面只能用一个异常

#报错的格式：
#①报错的位置
#②报错的内容
#③报错的类型和描述

#try...except...else  原理：只要try代码没有异常，就执行else
# try :
# #     a=123
# #     print(a+1)
# # except NameError:
# #     peint("123")
# # else:
# #     print("789")

#try...except...finally...  原理：finally 语句一定会执行
# try :
#     a="123"
#     print(a+1)
# except NameError:
#      peint("哈哈错")
# finally:         #(一定会执此语句块)
#      print("789")

#raise    #触发异常（错误开关）：自定义异常
# a = 123
# raise Exception("就是错 没原因")
# print(a)

#下载库
#①pip下载
#pip：是Python自带的一个组件
#作用：用来下载网络上面的Python库
# 安装Python时勾选pip →本机cmd→ python -m pip install --upgrade pip(升级pip)
#用法：在cmd，输入：pip install 库名  (安装)、pip uninstall 库名  (卸载)、pip list (查看)
#连接数据库的库：pymysql
#② pip install 文件名
#③


#格式：import语句（所有的导入语句，写最上面）
#方法一
# import 文件名 #（将文件所有代码导入到本文件中）
# 文件名.zhishu()
# print(函数.zhishu())
# import random
#方法二
#for 文件名 import 函数名

# from 文件名 import zhishu  #从文件中导入zhishu函数
# from 文件名 import *      # 从文件中导入所有函数
# from 草稿 import jiujiu



# if __name__ == '__main__': # _name_:获取的执行文件的文件名 / _main_:文件名
#     print(111)
# print("hello")               ###在本文件里是111和hello都打印 但在其他文件中 import 函数 调用不打印111



####判断是不是英文字母ASCII
# a='a'
# if True in [ (ord(c) > 64 and ord(c) < 91) or (ord(c) > 96 and ord(c) < 123) for c in a ]:
#     print("ok")
# if ord("a")==97:  #英文a在ASCII码中编号97
#     print("ok")
#print(ord('a'))  #显示在ASCII中编号

a,b=divmod(5,2)
print(b)
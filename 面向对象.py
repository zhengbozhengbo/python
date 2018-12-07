#  /usr/bin/env python   #
# -*- coding:utf-8-*-


# 面向对象 （抽象） ：将函数进行分类和封装，使开发更高效（管理代码：面向对象思想）
#面向对象：只关注 输入和输出
#
#不用面向对象（自己做）：做某件事情
#之前写代码:面向过程
#现在的class：面向对象

#在Python上通过“类”来实现某个对象的功能
# 定义类:
# class 类名 ():         #为了跟函数名区分，类名首字母一般为大写
#     def 函数名(self):  #self 是类的实例化
#         执行语句
#     def 函数名(self):
#         执行语句

#调用： 类名.函数名
# 类：属性（每种方法必须具备的条件）、方法（函数在类里面叫方法）
#实例化：①自定义：方便在类的外部调用   ②内置（self）：方便在类的内部调用
# class Shuzi():
#     def jiujiu(self):   #self 是类的实例化 可调用类内部的函数
#         print("hello")
#     def zhishu(self):
#         print(123)

#对象：（a）是类的实例话
# Shuzi().zhishu() # 调用
# a=Shuzi()       #简化调用
# a.zhishu()

# class SHUIZHI():
#     def zhishu(self):
#         b=self.jiecheng()
#         s=0
#         for i in range(2,b+1):
#             for k in range(2,i):
#                 if i%k==0:
#                     break
#             else:
#                 s += i
#         return s
#
#     def jiecheng(self):
#         c=1
#         s=0
#         for i in range(1,6):
#             c*=i
#             s+=c
#         return s

#继承：一个新的类拥有旧的类的所有方法
#多继承：一个新的类拥有多个旧的类的所有方法
#如果继承多个类里面有相同方法，使用最左边的类里面的

#多态  又叫 方法重写

#私有方法：只属于本类的方法（只能在本类内部使用即是self使用）
#定义私有方法：方法前面加两个下划线

#object：一切的基类

# class asd(SHUZI): #继承
#     def aaa(self):
#         print(123)
#     pass           #空语句
#
# asd=asd()
# print(asd.zhishu())
#
# class bbb(SHUIZI,asd): #多继承(以逗号隔开类):有相同的方法时，使用类名在前的方法
#     pass

#多态  又叫 方法重写
# class ccc(asd):       #asd中有aaa,现功能需要 重写
#     def aaa(self):
#         s=0
#         for i in range(101):
#             s+=i
#         print(s)
# c=ccc()
# c.aaa()

# class dd():
#     def __fff(self):
#         s = 0
#         for i in range(101):
#             s += i
#         print(s)
#     def __init__(self,a,b):  #初始化属性
#         self.name=a
#         self.nianling=b
#
# d=dd()
# d.__fff()

#未完成的操作
# class asd(object):
#     def __init__(self,name,xueliang,zhanli):
#         self.name=name
#         self.xueliang=xueliang
#         self.zhanli=zhanli
#
#     def daguai(self):
#         self.xueliang -=500
#
#     def xiulian(self,a=10):
#         self.xueliang +=1000
#         self.xueliang +=a
#
#     def pk(self,a=10):
#         self.xueliang -=1000
#
#     def print_xue(self):
#         print("%s还有%d血量，战力%d"%(self.name,self.xueliang,self.zhanli))
# b=asd()
# b.__init__("赵",500,1)
# b,xiulian()
# b.print_xue

#面向对象：多个某种功能的可重复的

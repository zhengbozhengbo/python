#  /usr/bin/env python   #
# -*- coding:utf-8-*-

# 输出 等同于etho 格式 print()
#print(555,"zheng","中中")

#  输入 从键盘上输入 等同于 read -p 提示 input(提示）
#变量名 = input("请输入成绩：")
#print(变量名)

#a='asdd55dd'
#print (a[-3:])


# # 属于字符串的函数（对字符串的操作）
# #局部变量（只适用于字符串）
#
# #调用函数的方法: 变量名.函数名（）
#
# #abc=" xxxXYYYeeeqq "
#
# #b=abc.upper()   #将字符串中所有的小写变成大写
# ##b=abc.capitalize()# 将首字母变大写
# ###b=abc.swapcase()#将大写变小写，小写变大写
#
# #b=abc.lstrip()#去除字符串左边的空格
# ##b=abc.rstrip()#去除右边的空格
# ###b=abc.strip()#去除两边的空格
#
# #b=abc.replace("q","77") #替换：将前一个字符替换为后一个字符
# ##b=abc.replace("e","88",2)#把"2"个e替换成88
#
# #b=abc.startswith(" x") #判断字符串是否以括号中的元素开头（可当条件使用）
# ##b=abc.endswith("q ")   #判断字符串是否以括号中的元素结尾（可当条件使用）
#
# #print(b)
# #print(abc)
#
# #cc="hello {name},我今年 {age} 岁" # {变量名}占位符
# #d=cc.format(age=55,name="小郑")  #格式化字符串
# #print(d)
# #print(cc)
# ##ee="hello %s,今年 %d 岁"  # %s:格式化字符串 %d:格式化整数
# ##f=ee%("正正",22)  #
# ##print(f)
# ##print(ee)
#
# abc="123"# 加引号数字为字符串
# b="==".join(abc)  # 以字符串为分隔符，将变量中的所有元素合并为一个的新的字符串
# print(b)
# print(type(abc))
#
# abc="1-2-3-4"
# b=abc.split("-") #以指定字符串为分割符，将变量中的元素分割成一个列表
# print(b)

# list（列表）：一组数据的集合（等同于shell中的数组）
#以中括号为标识，以逗号隔开的  [元素1,元素2,元素3]
#作用：用来存储数据的
#特点：1.可变的 2.支持索引：可以通过下标号取值 3.支持切片
#a= [2,88,"asd","rada",99]    #a = [整数,整数,字符串,字符串，整数]
#print(a[:])  #打印数列中所有数据
#print(a[-3]
#print(a[0:3])
#print(a[::2])
#print(a[2][0]) # 多层数据取值，第一层取asd 第二层取第一个字符a

#列表中的内置函数
#a= [2,88,"asd","rada",99,[78,"bb",9,"aaa"]]
# print(a[2].upper()) # a[2]是一个字符串，在upper
#a[5].append([8,7,"mm"])  #是一个过程 动态的 不能赋值给b=a.append(10):错
#print(a)
#将括号中的元素添加到列表中，注意：只能添加一个且在最后添加
#a.insert(2,"abc") # 第一个参数是下标位置，第二个参数是添加的元素

#a[5].remove(78)  #删除某个元素
#a.pop(5)    #删除下标位置所在的元素
#print(a)

# a= [2,88,"asd","rada",99,[78,"bb",9,"aaa"]]
# c=a.index(99)    #获取某个元素的下标值
# #c=a.count(99)      #统计某个元素在列表中的个数
# print(c)
#第一个Python中的内置函数 type()  查看数据类型
#第二个Python中的内置函数 len() 统计某数据类型中有多少个元素  数据类型不能是整数，浮点数
# d=len(a)
# print(d)

# a.reverse()   # 反转列表
# print(a)
#a=[88,22,99,33,666]
#a=["asds","uuu","ZZZ","oo","k","aQpe"]   #根据ASCII编码排序
#a.sort()    #排序 默认是升序（需同一数据类型）
#a.reverse()
#a.sort(reverse=True) # 倒序：先升序在反转  同上两步
#print(a)

#a= [2,88,"asd","rada",99,[78,"bb",9,"aaa"]]
#a.clear()    #清空
# f=a.copy()   #复制列表   浅复制：只能复制第一层的数据
# print(f)

# import copy         #深复制前提条件
# a= [2,88,"asd","rada",99,[78,"bb",9,"aaa"]]
# b=copy.deepcopy(a)  #深复制：完全复制
# print(b)

# a=[88,"uup","haha",33,666]
# b=["asds",666,"ZZZ","rd88","k","aQpe"]
# a.extend(b)  #将b列表中的所有元素更新到a列表中
# print(a)
# print(b)

# list   #按着Ctrl+单击list 进入列数函数


#tuple(元组) 一组数据的集合，都是用来存储数据的
#以小括号为标识，以逗号隔开
# 特点：1.不可变的 2.支持索引 3.支持切片

#a=(88,"ww","pid","zheng",555)  #元组
#a=(256,)  #元组中有一个元素时必须加逗号 否则可能识别不为元组
##b=a.count(555) #统计某元素在元组中的个数
#print(b)
# c=a.index("pid")  #获取某元素的下标位置的值
# print(c)
# print(type(a))


# dict(字典)  存储数据的，数据格式：key=value (字典中键（key)必须是唯一的）
# 以键值对的方式存储数据
# 以大括号为标识，以逗号隔开
# 特点：1.可变的 2.无序的 3.不支持索引：不支持通过下标位置取值，但支持通过key取值
#a={"name":["小明","正","小白"],"age":20,"sex":"男"}
#a["xuexiao"]="开大"  #添加key=value
#a.pop("sex")       #删除key所在的键值对
#a.popitem()       #默认删除最后一个(随机)
#print(a)
# b=a.keys()       #获取所有的key
# print(b)
# c=a.values()     #获取所有的值values
# print(c)
# d=a.items()      #获取所有的键值对key=value
# print(d)
#a={"name":["小明","正","小白"],"age":20,"sex":"男"}
#b={"mingzi":["郑","郑","正"],"nianling":18,"xb":"男"}
# a.update(b)      #将字典b中的所有元素更新到a中
# print(a)
# a["name"]="yyy"  #修改key对应value的值
# print(a)
#print(a["name"][0])  #查看字典中name的 数列中的第一个


#set(集合) 一组数据的集合，存储数据的
#以大括号标识的，以逗号分隔开{1,8,"hhh","rraa",55}
# 特点：1.不重复的 2.无序的 3.不支持索引
#a={55,55,99,"iiasd","ooo",88,565,555}  #重复的覆盖，无序的，不排序的
# a.add("kkk")        #添加一个元素，但是元素不能是列表
# a.pop()         #默认删除最后一个（即随机删除一个）
# a.remove(88)   #删除括号中的元素
# b={55,11,333,"eee","www"}
# a.update(b)     #将集合b中的所有元素更新到a中
# print(a)

# 并集:|(管道符)   交集:&  差集: -
# a={55,55,99,"iiasd","ooo",88,565,555}
# b={55,11,333,"eee","www"}
# print(a|b)


#总结
# a=input("请输入:") #input键盘取值为str类型
# a=int(a)         #改为int类型
# print(type(a))   #查看当前类型

# a = []    #空的列表
# b = ""    #空的字符串
# # 错c = () 没有空的元组
# d = {}   #空的字典
# e = set()  #空的集合：集合可变的，定义一个空集合

# a = a.coun(55)  #当不改变时原值能用"="，b=a.pop() 例外 输出结果为删除的值
# a.apped()  #添加    #当改变时 不能为能用 b"="a.apped

#算数运算符  +（加）、-（减）、*（乘）、/（除）、**（幂）、//（整除）、%（求余）
# 1.不需要命令 2.(//)整除和(/)除法的区别 3.同数据之间的可以做运算
#字符串、列表只能做加法或乘法
# a = 5/3
# a = 5//3
# print(a)
# print

# 比较运算符 >、<、==(等于)、!=（不等于）

#成员运算符 in(在) 和 not in（不在 ）
# a = "acb"
# print( "d" in a)
# a = ["da",8,66]
# print(66 in a)

#逻辑运算符 与（and）、或（or）、非（not）

#赋值运算符  +=、-=、 *=、 /=、 **=、 //=
# a = 3+4
# a = a+5
# a += 5   #等于 a=a+5
# print(a)







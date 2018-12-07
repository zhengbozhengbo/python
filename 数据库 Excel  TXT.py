# ####①数据库到TXT
# import pymysql   #前提
# #连接数据库
# abc=pymysql.connect(host="192.168.0.65",
#               port=3306,
#               user="root",
#               password="654321",
#               charset="utf8")
# #创建游标
# aaa = abc.cursor()
# aaa.execute("use python1;")
# aaa.execute("desc biao1;")
# biaotou=aaa.fetchall()
# aaa.execute("select * from biao1")
# shuju=aaa.fetchall()
# with open("bb.txt","w",encoding="utf-8") as f:
#     for i in biaotou:
#         if i == biaotou[-1]:
#             f.write(i[0]+"\n")
#         else:
#             f.write(i[0]+",")
#     for k in shuju:
#         for j in k:
#             if j == k[-1]:
#                 f.write(str(j))
#             else:
#                 f.write(str(j)+",")
#         f.write("\n")
# f.close()


#####②数据库到Excel
# import pymysql   #前提
# #连接数据库
# abc=pymysql.connect(host="192.168.0.182",
#               port=3306,
#               user="root",
#               password="654321",
#               charset="utf8")
# #创建游标
# aaa = abc.cursor()
# aaa.execute("use python1;")
# aaa.execute("desc biao1")
# biaotou=aaa.fetchall()
# print(biaotou)
# aaa.execute("select * from biao1")
# shuju=aaa.fetchall()
# import xlwt
# f=xlwt.Workbook(encoding="utf-8")
# sheet=f.add_sheet("数据库到Excel")
# for i in range(len(biaotou)):
#     sheet.write(0,i,biaotou[i][0])
# m=1
# for d in shuju:
#     j=len(d)
#     for k in range(j):
#         sheet.write(m, k,d[k])
#     m+=1
# f.save("text11.xls")

# #:③TxT转成Excel
# import xlwt
# o=xlwt.Workbook(encoding="utf-8")
# sheet=o.add_sheet("shenmogui")
# f=open("aa.txt","r+",encoding="utf-8")
# b=f.read()
# print(b)
# c=b.split("\n")
# print(c)
# s = 0
# for i in c:
#     p=i.split(",")
#     #print(p)
#     d=len(p)
#     #print(d)
#     for k in range(d):
#         sheet.write(s,k,p[k])
#     s+=1
# o.save("text10.xls")

#文件小循环判断文件类型
#def wenjian(a):
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



# ####④Excel 转成 txt
# import xlrd  #打开一个文件
#
# f = xlrd.open_workbook("text3.xls")
# b=f.nsheets
# for i in range(b):
#     abc=f.sheets()[i]
#     a=abc.nrows
#     print(a)
#     for k in range(a):
#         g=abc.row_values(k)
#         for j in range(len(g)):
#             ff=open("Excel转TXT4.txt","a+",encoding="utf-8")
#             ff.write(str(g[j]))
#         ff.write("\n")
# ff.close()


# # ###⑤Excel 转 数据库
# import xlrd
# import pymysql
# abc = pymysql.connect(host="192.168.0.182", #连接数据库
#                       port=3306,
#                       user="root",
#                       password="654321",
#                       charset="utf8")
# aaa = abc.cursor()  #游标
# f = xlrd.open_workbook("text3.xls")  #打开一个text
# aaa.execute("create database python4;")   #创建库
# aaa.execute("use python4;")     #  切换库
# bbb=f.sheets()[0]               #标签页
# a=bbb.nrows                    #多少行
# for k in range(a):
#     g = bbb.row_values(k)  # 行内容
#     if k ==0:  #判断第一行 创表
#         aaa.execute("create table excel4({} char(255),{} int,{} char(255));".format(g[0],g[1],g[2]))
#     else:    # 添加表内容
#         aaa.execute("insert into excel4 values('{}','{}','{}');".format(g[0],g[1],g[2]))
# aaa.execute("select * from excel4;")  #查看添加
# print(aaa.fetchall())     #上条命令结果
# aaa.close()   #关闭文件

### ⑥txt转数据库
import pymysql
abc = pymysql.connect(host="192.168.0.182",
                     port=3306,
                     user="root",
                     charset="utf8",
                     password="654321")
bbb=abc.cursor()  #游标

f=open("aa.txt","r+",encoding="utf-8")
a=f.readlines()  # 读全部，结果列表
#bbb.execute("create database python;")   #创建库
bbb.execute("use python4;")     #  切换库
# for k in range(len(a)):
#     g = a[k].strip().split(",")
#     if k ==0:  #判断第一行 创表头
#         bbb.execute("create table txt2({} char(255),{} int,{} char(255));".format(g[0],g[1],g[2]))
#     else:    # 添加表内容
#         bbb.execute("insert into txt1 values('{}','{}','{}');".format(g[0],g[1],g[2]))
# bbb.execute("select * from txt2;")  #查看添加
bbb.execute('select * from txt1;')
print(bbb.fetchall())     #上条命令结果
bbb.close()   #关闭文件


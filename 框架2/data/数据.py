# /usr/bin/env python
# -*- coding:utf-8 -*-

import xlrd

def shuju2():
    shuju3=[]
    f=xlrd.open_workbook(r"E:\python 文件\框架2\data\测试.xls")
    sheet=f.sheets()[0]
    a=sheet.nrows
    for i in range(1,a):
       b= sheet.row_values(i)
       shuju3.append(b)
    return shuju3
def shuju4():
    f=open("导入","r")
    c= f.readlines()
    return c

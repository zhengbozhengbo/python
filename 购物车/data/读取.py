# usr/bin/env   python
# -*- coding:utf-8 -*-
import  xlrd


def 表格():
    g=[]
    f=xlrd.open_workbook(r"E:\python 文件\购物车\data\数据.xls")
    sheet=f.sheets()[0]
    b=sheet.nrows
    for i in range(1,b):
        c=sheet.row_values(i)
        g.append(c)
    return g

def 文档():
    f=open(r"E:\python 文件\购物车\data\数据2.txt","r")
    d=f.readlines()
    return  d


print(表格())


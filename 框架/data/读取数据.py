# /usr/bin/env python
# -*- coding:utf-8 -*-

import xlrd
def shuju():
    shuju2 = []
    f = xlrd.open_workbook(r"E:/python 文件/测试.xls")
    sheet = f.sheets()[0]
    num = sheet.nrows
    for i in range(1, num):
        aa = sheet.row_values(i)
        shuju2.append(aa)
    return shuju2
def shuju3():
    f = open(r"E:\python 文件\框架\driver\文件1.txt", "r")
    a = f.readlines()
    return a
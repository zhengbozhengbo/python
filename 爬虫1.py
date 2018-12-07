#  /usr/bin/env python   #
# -*- coding:utf-8-*-

# requests  第三方下载
#爬虫 ：又叫 网络蜘蛛（spider）
# 模仿浏览器(发送请求的),根据自己制定的规则批量下载网络中的资源
# 正则表达式：匹配文件中内容

#模仿浏览器的模块： urllib、urllib3、requests

#匹配内容的模块：re,bs4(比正则简单),xpath

#爬虫分类： 1.聚焦爬虫：只爬取某个网站的资源  2.搜索爬虫：爬取整个网络中的资源  3.ip被封 :设置公网ip

#面向对象代码：

#爬虫第一步：分析网址的变化，并请求
#'https://www.qiushibaike.com/text/page/{}/'.format(1)

# ②爬虫第二步:分析html文件（找资源上下代码），过滤并下载想要的资源
#导入正则模块  #Python 只能匹配字符串

#贪婪模式：尽可能多的去匹配最后的字符串
#非贪婪模式：尽可能少的去匹配最后的字符串
# 带？的是非贪婪（？最优先），带* 是贪婪
# . 匹配任意一个字符（除了换行符）
# re.S 让点能匹配换行符在内的所有字符/re.I 匹配字符不区分大小写
# import re
#
# a= """qwert23wq
# e456123"""
# #将要匹配的正则编译
# b= re.compile("qwert(.*?)123",re.S)
#有括号 显示括号内容  #re.S 让点能匹配换行符在内的所有字符
#到目的字符串中去查找
# c=b.findall(a)  #结果列表
# print(c)
#
# # #③ 爬虫第三步：保存注意保存的权限和方式（save）
# # abc.save("文件名")
#
# import re
# import requests
# class  Qiushi(object):
#
#     def qingqiu(self,page):
#         url='https://www.qiushibaike.com/text/page/{}/'.format(page)
#         #发送请求 ：1.导入模块(最上方)
#         response = requests.get(url=url)
#         #读取结果的方式(返回html文件)：1.以字符串的方式读取  2.以字节码的方式读取（看源文件的编码方式）
#         #print(response.text)         #1.以字符串的方式读取
#         html=(response.content.decode("utf-8"))   #2.以字节码的方式读取  decode:解码
#         return html
#
#     def guolv(self,bbb):
#         patt=re.compile('<div class="content">(.*?)</div>',re.S)
#         items = patt.findall(bbb)
#         s=0
#         d=[]
#         for i in items:
#             i = i.replace("<span>","")
#             i=i.replace("</span>","")
#             i = i.replace("<br/>","")
#             i = i.replace('<span class="contentForAll">查看全文', "")
#             i = i.strip()
#             d.append(i)
#             s+=1
#         return d
#     def save(self,shuju):
#         with  open("c.txt","w",encoding="utf-8") as f:
#             for i in shuju:
#                 f.write(i+"\n")
# abc=Qiushi()
# jieguo=abc.qingqiu(1)
# shuju=abc.guolv(jieguo)
# abc.save(shuju)
#
# #豆瓣书本的导入
# import os
# import xlwt
# import xlrd
# from xlutils.copy import copy
# import re
# import requests
#
# class  Douban(object):
#
#     def qingqiu(self,page):
#         url='https://book.douban.com/top250?start={}'.format(page*25)
#         response = requests.get(url=url)
#         html = (response.content.decode("utf-8"))
#         return html
#
#     def guolv(self,bbb):
#         aa=re.compile(' title="(.*?)"',re.S)
#         items = aa.findall(bbb)
#         for i in items:
#             if i == '可试读':
#                 items.remove(i)
#         cc = re.compile('<span class="inq">(.*?)</span>', re.S)
#         items2 = cc.findall(bbb)
#         return items,items2
#     def save(self, shuju1,shuju2):
#         if "爬虫2.xls" not in os.listdir():
#             f=xlwt.Workbook(encoding="utf-8")
#             sheet=f.add_sheet("豆瓣图书")
#             sheet.write(0,0,"书名")
#             sheet.write(0,1, "简介")
#             for i in range(len(shuju1)):
#                 sheet.write(i+1,0,shuju1[i])
#             for i in range(len(shuju2)):
#                 sheet.write(i+1,1,shuju2[i])
#             f.save("爬虫2.xls")
#         else:
#             ff=xlrd.open_workbook("爬虫2.xls")
#             sheet=ff.sheets()[0]
#             hh = sheet.nrows
#             fff = copy(ff)
#             sheet1= fff.get_sheet(0)
#             for i in range(len(shuju1)):
#                 sheet1.write(i+hh,0,shuju1[i])
#             for i in range(len(shuju2)):
#                 sheet1.write(i+hh,1,shuju2[i])
#             fff.save("爬虫2.xls")
#
# bb=Douban()
# for i in range(1,5):
#     jieguo=bb.qingqiu(i)
#     shuju=bb.guolv(jieguo)
#     bb.save(shuju[0],shuju[1])

# #面向过程
# import re
# import requests
# url123="http://www.doutula.com/article/list/?page=2"
#
# #反爬：阻止爬虫程序批量下载资源  常见的反爬手段：1.header信息 2.验证码(12306)
# head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
#
# response=requests.get(url=url123,headers=head)
# html = response.content.decode("UTF-8")
#
# patt = re.compile(r'http://www.doutula.com/article/detail/[0-9]{7}')
# items = patt.findall(html)
#
# for i in items:
#     response1 = requests.get(url=i,headers=head)
#     html1 = response1.content.decode("UTF-8")
#     patt1 = re.compile(r'<img src="https://ws(.*?)" alt="')
#     items1 =patt1.findall(html1)
#     ming = re.compile(r'<td align="center" class="wr pl">(.*?)</td>')
#     zi= ming.findall(html1)
#     for j,k in enumerate(items1):
#         k=k.replace('"',"")
#         k="https://ws"+k
#         tupian = requests.get(url=k,headers=head)
#         html2=tupian.content
#         print(html2)
#         if "jpg" in k:
#             with open(r'E:/爬虫图片/{}{}.jpg'.format(zi[j][0:2],j),"wb")as f:
#                 f.write(html2)
#         else:
#             with open(r'E:/爬虫图片/{}{}.gif'.format(zi[j][0:2],j),"wb")as f:
#                 f.write(html2)



#####斗图
# import re
# import requests
#
# class tupian(object):
#     head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
#
#     def qingqiu(self):
#         url="http://www.doutula.com/article/list/?page=2"
#         response = requests.get(url=url, headers=self.head)  # 发送请求
#         html=response.content.decode("UTF-8")      #请求的html文件 以字节码读取
#         patt = re.compile(r'http://www.doutula.com/article/detail/[0-9]{7}')  # 过滤第一次请求文件
#         items = patt.findall(html)  # 过滤得到的结果 十个图片链接
#         return items
#     def guolv(self,items):
#         k=[]
#         l=[]
#         for i in items:
#             response1 = requests.get(url=i,headers=self.head)  #第二次请求图片
#             html1= response1.content.decode("UTF-8") #第二次响应内容
#             patt1=re.compile(r'<img src="https://ws(.*?)" alt=') #过滤第二次请求文件
#             items1=patt1.findall(html1)  #过滤得到的结果 每个图片链接
#             for p in range(len(items1)):
#                 k.append(items1[p])
#             ming = re.compile(r'<td align="center" class="wr pl">(.*?)</td>')  #图片名字过滤
#             zi = ming.findall(html1)  #名字的结果
#             for o in range(len(zi)):
#                 l.append(zi[o])
#         return k,l
#     def baocun(self,items1,zi):
#
#         for j, k in enumerate(items1):
#             k = k.replace('"', "")  # 替换“
#             k = "https://ws" + k  # 还原ip地址(url)
#             tu = requests.get(url=k, headers=self.head)
#             html2 = tu.content  # 以字节码读取
#             if "jpg" in k:
#                 with open(r'E:/爬虫图片/{}{}.jpg'.format(zi[j][0:2], j), "wb")as f:
#                     f.write(html2)
#             else:
#                 with open(r'E:/爬虫图片/{}{}.gif'.format(zi[j][0:2], j), "wb")as f:
#                     f.write(html2)
#
# qq=tupian()
# shuju=qq.qingqiu()
# shuju2=qq.guolv(shuju)
# print(shuju2)
# qq.baocun(shuju2[0],shuju2[1])


######小说
# import re
# import requests
#
# class meizi(object):
#     head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
#
#     def qingqiu(self):
#         url = "http://www.biquge.com.tw/3_3711/"
#         response = requests.get(url=url,headers=self.head)
#         html = response.content.decode("gbk")
#         return html
#     def guolv(self,b):
#         d=[]
#         patt=re.compile('<dd><a href="(.*?)">',re.S)
#         items= patt.findall(b)
#         for i in items:
#             e="http://www.biquge.com.tw"+i
#             response = requests.get(url=e,headers=self.head)
#             html2 = response.content.decode("gbk")
#             patt1=re.compile('&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<')
#             items2=patt1.findall(html2)
#             d.append(items2)
#         return d
#     def save(self,c):
#         r=2
#         for i in range(len(c)):
#             with open("txt999.txt", "a", encoding="utf-8")as f:
#                 for k in range(len(c[i])):
#                     f.write(c[i][k]+"\n")
#                 f.write("第{}章"+"\n".format(r))
#             r+=1
#
#
#
# cc=meizi()
# html=cc.qingqiu()
# dd=cc.guolv(html)
# cc.save(dd)


###图片
# import requests
# import re
#
# class Doutu():
#     head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
#     def qingqiu(self,a):
#         url='https://www.qqtn.com/tp/dmtp_{}.html'.format(a)
#         sponse=requests.get(url=url,headers=self.head)
#         html=sponse.content.decode("gbk")
#         return html
#     def guolv(self,b):
#         patt=re.compile(r'<ul class="g-gxlist-imgbox">(.*?)<div class="page"><div class="tspage">',re.S)
#         items=patt.findall(b)   #结果字符串
#         patt1=re.compile('<a href="(.*?)" target')
#         items1=patt1.findall(items[0]) #结果字符串
#         d=[]
#         for i in items1:
#             i="https://www.qqtn.com"+i
#             d.append(i)
#         return d
#     def save(self,c):
#         r=0
#         for i in range(len(c)):
#             tu = requests.get(url=c[i], headers=self.head)
#             pian= tu.content.decode("gbk")
#             patt2=re.compile(r'<p align="center"><img src="(.*?)"/></p>',re.S)
#             items3 = patt2.findall(pian)
#             print(len(items3))
            # for k in range(len(items3)):
            #     tu2 = "https://pic.qqtn.com/up/" + items3[k]
            #     tu3= requests.get(url=tu2, headers=self.head)
            #     pian3 = tu3.content
                # print(pian3)
                # with open(r'E:/爬虫图片/{}.jpg'.format(r),"wb") as f:
                #     f.write(pian3)
                #     r+=1


# aa=Doutu()
# jieguo=aa.qingqiu(1)
# jieguo2=aa.guolv(jieguo)
# aa.save(jieguo2)


#####智联招聘
# url=https://sou.zhaopin.com/?jl=538&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95&kt=3
# url=https://sou.zhaopin.com/?p=1&jl=538&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95&kt=3
#
# url=https://jobs.zhaopin.com/CC305562912J00133332404.htm
#
# 动态URL=https://fe-api.zhaopin.com/c/i/sou?pageSize=120&cityId=538&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95&kt=3&_v=0.24472720&x-zp-page-request-id=861f1b1fbf2b469f8069d80631f5985c-1541770048790-468736
#https://fe-api.zhaopin.com/c/i/sou?pageSize=60&cityId=653&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95&kt=3&_v=0.58830574&x-zp-page-request-id=27659246a1f445968c93c5a0d96f8c33-1542114175810-535286
##

import requests
import re

class zhilian():
    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

    def qingqiu(self,t):
        #上海
        #url="https://fe-api.zhaopin.com/c/i/sou?pageSize={}&cityId=538&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95&kt=3&_v=0.63219854&x-zp-page-request-id=e9a6ef51d35c4a1db6b25ccf40b69387-1541903097457-547706".format(t)
        #杭州
        #url="https://fe-api.zhaopin.com/c/i/sou?pageSize={}&cityId=653&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95&kt=3&_v=0.58830574&x-zp-page-request-id=27659246a1f445968c93c5a0d96f8c33-1542114175810-535286".format(t)
        #北京
        url="https://fe-api.zhaopin.com/c/i/sou?pageSize={}&cityId=530&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95&kt=3&_v=0.15443199&x-zp-page-request-id=8c57463f62bb4d6499d70ebffe3fef68-1542114884216-994180".format(t)
        rep  =requests.get(url=url,headers=self.head)
        html=rep.content.decode('utf-8')
        items=re.compile('"jobType":(.*?)timeState":',re.S)
        patt=items.findall(html)
        return patt
    def guolv(self,b):
        c=[]
        for i in b:
            items=re.compile('"salary":"(.*?)",',re.S)
            xinzi=items.findall(i)
            c.append(xinzi)
        print(c)
        d=[]
        for i in b:
            items2=re.compile('.htm","name":"(.*?)",',re.S)
            gongsi=items2.findall(i)
            if gongsi==[]:
                d.append(['上海临港地区'])
            else:
                d.append(gongsi)
        print(d)
        e=[]
        for i in b:
            items3 = re.compile('"jobName":"(.*?)",',re.S)
            zhiwei=items3.findall(i)
            e.append(zhiwei)
        print(e)
        f=[]
        for i in b:
            items4 = re.compile('"createDate":"(.*?)",', re.S)
            shijian=items4.findall(i)
            f.append(shijian)
        print(f)
        g=[]
        for i in b:
            items5=re.compile('"workingExp":(.*?)},',re.S)
            jingyan = items5.findall(i)
            items6=re.compile('"name":"(.*?)"',re.S)
            jingyan2=items6.findall(jingyan[0])
            g.append(jingyan2)
        print(g)
        h=[]
        for i in b:
            items7=re.compile('"display":"(.*?)"},',re.S)
            didian= items7.findall(i)
            h.append(didian[1])
        print(h)
        j=[]
        for i in b:
            items8 = re.compile('"positionURL":"(.*?)",', re.S)
            renshu=items8.findall(i)
            j.append(renshu)
        print(j)
        k=[]
        for i in range(len(j)):
            url=j[i][0]
            rep2 = requests.get(url=url, headers=self.head)
            html2=rep2.content.decode("UTF-8")
            patt3=re.compile('span>招(.*?)人</span>',re.S)
            items9=patt3.findall(html2)
            if items9==[]:
                k.append("无")
            else:
                k.append(items9)
        print(k)
        return d,e,c,g,k,h,f

    def save(self,d):
        import xlrd
        from xlutils.copy import copy
        abc = xlrd.open_workbook("北京.xls")
        sheet=abc.sheets()[0]
        hang = sheet.nrows
        abc1=copy(abc)
        sheet=abc1.get_sheet(0)
        # u=["编号","公司","职位","薪资","经验","招人数","地区","发布日期"]
        #         # for i in range(len(u)):
        #         #     sheet.write(0,i,u[i])
        for i in range(len(d[0])):
            sheet.write(hang+i+1,1,d[0][i][0])
            sheet.write(hang+i+1,2,d[1][i][0])
            sheet.write(hang+i+1,3,d[2][i][0])
            sheet.write(hang+i+1,4,d[3][i][0])
            sheet.write(hang+i+1,5,d[4][i][0])
            sheet.write(hang+i+1,6,d[5][i])
            sheet.write(hang+i+1,7,d[6][i][0])
            sheet.write(hang+i+1,0,i+1)
        abc1.save("北京.xls")




a=zhilian()
#jieguo=a.qingqiu()
#jieguo2=a.guolv(jieguo)
# print(jieguo2)
# a.save(jieguo2)
for i in range(0,121,60):
    jieguo = a.qingqiu(60)
    jieguo2 = a.guolv(jieguo)
    a.save(jieguo2)
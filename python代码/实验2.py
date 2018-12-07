# from socket import *
# a=socket()
# a.bind(("192.168.0.76",18888))
# a.listen(3)
#
# c,d=a.accept()
# print("%s已建立连接 "% str(d))
# while True:
#     f= c.recv(1024)
#     print("--%s" % f.decode())
#     msg=input(">>>").encode()
#     c.send(msg)





import re
import requests
import xlwt
class zhilian():
    def qinqiu(self):
        a=['https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=60&cityId=530&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95&kt=3&_v=0.01097835&x-zp-page-request-id=e0f56c50c62c4f84b5bfaec445247355-1541768917339-961731'
                   ,'https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=60&cityId=538&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95&kt=3&_v=0.27393779&x-zp-page-request-id=7161854b4ce84b72a606216d33ca1a46-1541814546568-870708'
                   ,'https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=60&cityId=765&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95&kt=3&_v=0.34573786&x-zp-page-request-id=5ca57d70af1245d688194da90a1acf7f-1541814748861-951786'
                   ,'https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=60&cityId=763&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95&kt=3&_v=0.93934657&x-zp-page-request-id=da763ba5f7124d928d0c5be0471767b9-1541814818979-678695']
        aa=[]
        for i in a:
            for j in range(0,180,60):
                kk=i.format(j)
                aa.append(kk)

        zhiwei1=[]
        xinzi1=[]
        didian1=[]
        time1=[]
        renshu1=[]
        jinyan1=[]
        for dd in aa:
            url=dd
            head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
            response=requests.get(url=url,headers=head)
            html=response.content.decode('utf-8')
            zhiwei=re.compile(r'jobName":"(.*?)","',re.S)
            xinzi=re.compile(r'"salary":"(.*?)","',re.S)
            didian=re.compile(r'city":{"items":(.*?)"},"applyType',re.S)
            time=re.compile(r'updateDate":"(.*?)","',re.S)
            renshu=re.compile(r'size":{"(.*?)"},"type',re.S)
            jinyan=re.compile(r'workingExp":{"(.*?)"},"eduLevel')

            items=zhiwei.findall(html)
            zhiwei1.append(items)
            items1=xinzi.findall(html)
            xinzi1.append(items1)
            items2=time.findall(html)
            time1.append(items2)
            items3=renshu.findall(html)
            renshu1.append(items3)
            items4=didian.findall(html)
            didian1.append(items4)
            items5=jinyan.findall(html)
            jinyan1.append(items5)
        return   zhiwei1,xinzi1,didian1,time1,renshu1,jinyan1

    def baocun(self,a,b,c,d,e,nn):
        dd=1
        f=xlwt.Workbook(encoding='utf-8')
        sheet = f.add_sheet('智联')
        sheet.write(0,0,'职位')
        sheet.write(0,1,'薪资')
        sheet.write(0,2,'公布时间')
        sheet.write(0,3,'公司人数')
        sheet.write(0,4,'公司地址')
        sheet.write(0,5,'工作经验')
        k = 1
        m = 1
        n = 1
        aa = 1
        bb = 1
        cc = 1
        for j in range(12):
            for i in a[j]:
                sheet.write(k, 0, '{}'.format(i))
                k += 1
        for j in range(12):
            for i in b[j]:
                sheet.write(m, 1, '{}'.format(i))
                m += 1
        for j in range(12):
            for i in c[j]:
                sheet.write(n, 2, '{}'.format(i))
                n += 1
        for j in range(12):
            for i in d[j]:
                i = i.split('"')
                sheet.write(aa, 3, '{}'.format(i[-1]))
                aa += 1
        for j in range(12):
            for t in e[j]:
                t = t.split('"')
                sheet.write(bb, 4, '{}'.format(t[-1]))
                bb += 1
        for j in range(12):
            for ff in nn[j]:
                ff = ff.split('"')
                sheet.write(cc, 5, '{}'.format(ff[-1]))
                cc += 1

        f.save('智联招聘.xls')

# aa=zhilian()
# a,b,c,d,e,nn=aa.qinqiu()
# aa.baocun(a,b,c,d,e,nn)
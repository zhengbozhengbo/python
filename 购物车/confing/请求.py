# usr/bin/env   python
# -*- coding:utf-8 -*-
import requests


class 请求2():
    def qingqiu(self,a):

        url = "http://www.zhaoapi.cn/product/getCarts"
        param = {"mobile": "15237888353",
                 "password": "123456",
                 "uid": "{}".format(a)}
        head = {"Content-Type": "application/x-www-form-urlencoded",
                "Accepet-Encoding": "gzip,deflate",
                "Accpet": "*/*",
                'token': "B26C90E2560916C7D6D49CEBAC1694BC"}
        respones = requests.get(url=url, headers=head, params=param)
        jieguo = respones.json()
        return jieguo
    def qingqiu2(self):
        url = "http://www.zhaoapi.cn/product/getCarts"
        data={'mobile':15237888353,
                    'password':123456,
                    'uid':22697,
                        'pid':100}
        head = {"Content-Type": "application/x-www-form-urlencoded",
                "Accepet-Encoding": "gzip,deflate",
                "Accpet": "*/*",
                'token': "B26C90E2560916C7D6D49CEBAC1694BC"}
        respones = requests.post(url=url, headers=head, data=data)
        jieguo2 = respones.json()
        return jieguo2
    def qingqiu3(self):
        url = "http://www.zhaoapi.cn/product/deleteCart"
        param = {'pid':100,
                 "uid":22697}
        head = {"Content-Type": "application/x-www-form-urlencoded",
                "Accepet-Encoding": "gzip,deflate",
                "Accpet": "*/*",
                'token': "B26C90E2560916C7D6D49CEBAC1694BC"}
        respones = requests.get(url=url, headers=head, params=param)
        jieguo3 = respones.json()
        return jieguo3
a=请求2()
print(a.qingqiu3())
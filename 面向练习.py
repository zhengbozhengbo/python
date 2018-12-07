#  /usr/bin/env python
# -*- coding:utf-8-*-

#对象：1.任意范围的质数之和 2.判断字符串是否回文
class quanbu():
    def zhishu(self,a,b):
        s=0
        for i in range(a,b):
            for k in range(2,i):
                if i%k==0:
                    break
            else:
                s+=i
        return s

    def huiwen(self,c):
        d=len(c)//2
        for i in range(d):
            if c[i] != c[-i-1]:
                print("不是回文")
                break
        else:
            print("是回文")

a=quanbu()
a.huiwen("abcba")
print(a.zhishu(50,201))
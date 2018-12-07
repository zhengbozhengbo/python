# /usr/bin/env   python
# -*- coding:utf-8 -*-
a=int(input("总资产："))
goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]
for i,j in enumerate(goods):
    print(i+1,j["name"],j["price"])
u = len(goods)  # 判定商品号是否符合规则
b = []
while True:
    c = input("输入exit退出，商品号购买:")
    if c == "exit":
        break
    elif c == "购买":
        d = b.count("电脑")
        e = b.count("鼠标")
        f = b.count("游艇")
        g = b.count("美女")
        s = d * 1999 + e * 10 + f * 20 + g * 998
        print(s)
        if s > a:
            k=input("余额不足，删除(已选商品)或充值:")
            if k=="充值":
                p = int(input("充值金额"))
                a += p
                print("充值成功，总资产{}".format(a))
            elif k=="删除":
                while True:
                    o = input("退出删除exit,移除商品名：")
                    if o == "exit":
                        break
                    elif o in b:
                        h = b.index(o)
                        b.pop(h + 1)
                        b.remove(o)
                        print(b)
                    else:
                        print("购物车无此商品")
        else:
            print("购买成功，花费{}，余额{}".format(s, a - s))
    elif int(c) <= u:
        b.append(goods[int(c) - 1]["name"], )
        b.append(goods[int(c) - 1]["price"])
        print(b)
    else:
        print("输入错误，没有此商品号：")
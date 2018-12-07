# /usr/bin/env python
# -*- coding:utf-8 -*-

from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import messagebox

def xunhuan():
    #设置提示信息
    messagebox.showinfo(title="不许走",message="你关不掉的")
    return

def kaiqi():
    #在基础窗口 再开一个窗口
    b = Toplevel(window)
    b.geometry("300x100+520+260")
    b.title("好巧，我也是")
    tag2=Label(b,text="好巧 我认为不是的",font=("仿宋",20),fg="green")
    tag2.pack()
    yes2=Button(b,text="你说的对！", width=10, height=2,command=kaiqi3,fg="red" )
    yes2.pack()
    yes2 = Button(b, text="这个不能点", width=11, height=5, command=kaiqi3, fg="red")
    yes2.pack()
    b.protocol('WM_DELETE_WINDOW', kaiqi2)


def kaiqi2():
    messagebox.showinfo(title="哈哈哈",message="刚好我也是")
    return
def kaiqi3():
    # 销毁所有窗口
    window.destroy()
def guanbi():
    c=Toplevel(window)
    c.geometry("300x100+520+260")
    c.title("再等等啊")
    tag3= Label(c,text="你是真的自恋啊",font=("仿宋",20),fg="green")
    tag3.pack()
    no2=Button(c,text="就是很自信",width=10,height=2,
               command=c.destroy,fg="red") #销毁所有窗口
    no2.pack()
    c.protocol("WM_DELETE_WINDOW",guanbi3)
def guanbi3():
    guanbi()

#创建窗口
window = Tk()
###定义窗口标题
window.title("因为有了因为，所有有了所以")
###设置窗口大小
window.geometry("500x800")
# 用户关闭窗口触发的时间
window.protocol('WM_DELETE_WINDOW',xunhuan)
###定义一个文本的标签
tag = Label(window,text="天降一个大美女？",font=("仿宋",20))
###将标签放在窗口的哪个位置
tag.grid(row=0,column=0,sticky=W)
###定义一个按钮的标签
no = Button(window,text="当然了！",width=10,
            height=2,fg="green",command=guanbi)
no.grid(row=3,column=1)
yes = Button(window,text="你说是吗？",width=10,
            height=2,fg="green",command=kaiqi)
yes.grid(row=3,column=0)
##显示图片
img = Image.open('1.jpg')  #打开图片
photo = ImageTk.PhotoImage(img)  #定义图片
imgphoto = Label(window, image=photo)  #图片写入
imgphoto.grid(row=2, columnspan=2) #放在位置
####显示窗口
window.mainloop()


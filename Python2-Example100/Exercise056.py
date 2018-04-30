#!/usr/bin/python
# -*- coding: UTF-8 -*-

#题目：画图，学用circle画圆形。　　　
#程序分析：无。
#Tkinter： Tkinter 模块(Tk 接口)是 Python 的标准 Tk GUI 工具包的接口。
#Canvas画布就是turtle为我们展开用于绘图区域，我们可以设置它的大小和初始位置。# urtle.screensize
# (canvwidth=None,canvheight=None,bg=None)，参数分别为画布的宽(单位像素),高,背景颜色。
#expand置1 使能fill属性
#expand置0 关闭fill属性
#fill=X ：当GUI窗体大小发生变化时，widget在X方向跟随GUI窗体变化
#fill=Y ：当GUI窗体大小发生变化时，widget在Y方向跟随GUI窗体变化
#fill=BOTH：当GUI窗体大小发生变化时，widget在X、Y两方向跟随GUI窗体变化
if __name__ == '__main__':
    from Tkinter import *

    canvas = Canvas(width=800, height=600, bg='yellow')                # 画布宽高，背景颜色       #
    canvas.pack(expand=YES, fill=BOTH)                                 #布置画布的一些属性
    k = 1
    j = 1
    for i in range(0,26):
        canvas.create_oval(310 - k,250 - k,310 + k,250 + k, width=1)    #括号中是圆的一些属性
        k += j
        j += 0.3

    mainloop()                         #无限循环
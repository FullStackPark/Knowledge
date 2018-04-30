#!/usr/bin/python
# -*- coding: UTF-8 -*-

#程序分析：使用 Tkinter。
if __name__ == '__main__':
    from Tkinter import *                     #导入Tkinter
    x = 360
    y = 160
    top = y - 30
    bottom = y - 30

    canvas = Canvas(width = 400,height = 600,bg = 'white')                 #画布属性,canvas画布控件；显示图形元素如线条或文本
    for i in range(20):
        canvas.create_oval(250 - top,250 - bottom,250 + top,250 + bottom)      #画一个圆
        top -= 5
        bottom += 5
    canvas.pack()
    mainloop()                                                                             #消息循环


#!/usr/bin/python
# -*- coding: UTF-8 -*-

#题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，
# 几个数相加由键盘控制。
#程序分析：关键是计算出每一项的值。
#lambda x,y: x*10+y意思是创建一个函数,带两个返回函数计算结果参数x和y,返回x乘以10加y
#reduce() 函数会对参数序列中元素进行累积。返回函数计算结果
func = lambda x,y: x*10+y
func(1,2)
Tn = 0                                            #Tn为每一个数
Sn = []                                           #Sn为数的列表
n = int(raw_input('n = '))
a = int(raw_input('a = '))
for count in range(n):                           #n一共多少个数，a为最初值（后一个数永远是前一个的10倍+a
    Tn = Tn + a                                   #a为第一个值，Tn为每一次的值
    a = a * 10
    Sn.append(Tn)                                 #将Tn放入Sn的尾部
    print Tn

Sn = reduce(lambda x,y : x + y,Sn)                #将Sn中所有的值以x+y方式返回值
print "计算和为：",Sn
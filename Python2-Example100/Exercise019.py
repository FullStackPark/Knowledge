#!/usr/bin/python
# -*- coding: UTF-8 -*-

#题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
#程序分析：请参照程序Python 练习实例14。
from sys import stdout                       #标准输出
for j in range(2,1001):                       #遍历2~1001之间的数
    k = []                                    #k为该数的因子列表
    n = -1                                    #只有当n=-1时，才会出现良好展示的结果；
    s = j
    for i in range(1,j):                      #当该数为j时，遍历1~j找因子
            if j % i == 0:                    #以下情况为i是因子的前提下进行
                n += 1
                s -= i                         #s为剩下因子的和
                k.append(i)                    #将i放入k

    if s == 0:                                # 说明因子找完了，输出该数
        print j
        for i in range(n):
            stdout.write(str(k[i]))            #相当于print，但是没有换行，需要自己输出换行符
            stdout.write(' ')                  #每个因子之间一个空格
        print k[n]                            #若n一开始=0，则k[]不对，可以试验；若n=1,程序不对；只有--1时，k[n]刚好是k
                                                #序列的最后一个，也能完美展示，不出现=0的错误
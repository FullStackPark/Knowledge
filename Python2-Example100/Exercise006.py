#!/usr/bin/python
# -*- coding: UTF-8 -*-

#题目：斐波那契数列。
#程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、
# 8、13、21、34、……。
#在数学上，费波那契数列是以递归的方法来定义：
#F0 = 0     (n=0)
#F1 = 1    (n=1)
#Fn = F[n-1]+ F[n-2](n=>2)
def fib(n):                                             #方法一：不用递归
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a
print fib(10)                                           # 输出了第10个斐波那契数列

def fib(n):                                             #方法二：用递归
    if n==1 or n==2:                                    #实际上当n=0是第一个数，？取n=1or2,因为两个数都为1
        return 1
    return fib(n-1)+fib(n-2)
print fib(10)                                           # 输出了第10个斐波那契数列
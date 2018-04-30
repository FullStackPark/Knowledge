#!/usr/bin/python
# -*- coding: UTF-8 -*-

#题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
#程序分析：对n进行分解质因数，应先找到一个最小的质数k，然后按下述步骤完成：
#(1)如果这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可。
#(2)如果n<>k，但n能被k整除，则应打印出k的值，并用n除以k的商,作为新的正整数你n,重复执行第一步。
#(3)如果n不能被k整除，则用k+1作为k的值,重复执行第一步。
#输出的形式更加多样，可以使用 str.format() 函数来格式化输出值
# isinstance() 方法的语法:isinstance(object, classinfo)，object -实例对象。classinfo -可以是直接或间接类
# 名、基本类型或者有它们组成的元组，对象的类型与参数二的类型（classinfo）相同则返回 True，否则返回 False。
def reduceNum(n):
    print '{} = '.format(n),
    if not isinstance(n, int) or n <= 0 :
        print '请输入一个正确的数字 !'
        exit(0)
    elif n in [1] :                                     #最小质数
        print '{}'.format(n)
    while n not in [1] :                                # 循环保证递归，index是另一个因子
        for index in xrange(2, n + 1) :                 #xrange() 函数用法与 range 完全相同，所不同的是生
                                                         # 成的不是一个数组，而是一个生成器。
            if n % index == 0:
                n /= index                               # n 等于 n/index
                if n == 1:                               # n=1直接输出，否则继续执行循环
                    print index
                else :                                   # index 一定是素数
                    print '{} *'.format(index),
                break
reduceNum(90)
reduceNum(100)
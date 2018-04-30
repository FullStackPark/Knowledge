#!/usr/bin/python
# -*- coding: UTF-8 -*-

#题目：有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。
if __name__ == '__main__':
    nmax = 50
    n = int(raw_input('请输入总人数:'))
    num = []
    for i in range(n):
        num.append(i + 1)               #将i+1放入num

    i = 0                              #i正常序列号
    k = 0                              #k,123
    m = 0                              #m多少个人

    while m < n - 1:
        if num[i] != 0 :
            k += 1
        if k == 3:
            num[i] = 0                        #一旦=3，清除
            k = 0                             #然后从0开始再数一次
            m += 1                            #下一个人
        i += 1
        if i == n : i = 0                     #一圈结束，正常序列号为0

    i = 0
    while num[i] == 0: i += 1
    print num[i]
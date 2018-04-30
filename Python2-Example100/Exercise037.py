#!/usr/bin/python
# -*- coding: UTF-8 -*-

#题目：对10个数进行排序。
#程序分析：可以利用选择法，即从后9个比较过程中，选择一个最小的与第一个元素交换，下次类推，即用第二个元素
# 与后8个进行比较，并进行交换。
if __name__ == "__main__":
    N = 10
    # input data
    print '请输入10个数字:\n'
    l = []
    for i in range(N):                                #range函数返回一个左闭右开（[left,right)）的序列数
        l.append(int(raw_input('输入一个数字:\n')))
    print                                             #输出列表
    for i in range(N):
        print l[i]
    print

    # 排列10个数字
    for i in range(N - 1):
        min = i
        for j in range(i + 1,N):
            if l[min] > l[j]:             #从第二个到第9个依次和第一个比
                min = j                   #第一次内层循环后结果是第一个值或得数列的最小值，第二次内层循环后第二个是剩下几个数中最小的
        l[i],l[min] = l[min],l[i]         #外层循环结束后，序列从小到大排序
    print '排列之后：'
    for i in range(N):
        print l[i]
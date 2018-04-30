#!/usr/bin/python
# -*- coding: UTF-8 -*-

#题目：输入三个整数x,y,z，请把这三个数由小到大输出。
#程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，然后再用x与z
# 进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。
#引用方法：
#l.append,list 的 append() 方法，把新元追加到 list 的末尾,新元素可以是任何形式，区别于extend
#sort()函数是序列的内部函数,L.sort(cmp=None, key=None, reverse=False),key是排序条件，reverse:表示是
# 否反序，默认从小到大，默认为Flase
l = []                                                   #一个空的列表，名字是l
for i in range(3):
    x = int(raw_input('integer:\n'))
    l.append(x)
l.sort()
print l
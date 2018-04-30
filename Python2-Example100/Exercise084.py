#!/usr/bin/python
# -*- coding: UTF-8 -*-

#题目：连接字符串。
#Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。join()方法语法：str.join(sequence)，sequence --
# 要连接的元素序列。返回通过指定字符连接序列中元素后生成的新字符串。
delimiter = ','
mylist = ['Brazil', 'Russia', 'India', 'China']
print delimiter.join(mylist)                       #用“，”连接
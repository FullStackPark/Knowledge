#!/usr/bin/python
# -*- coding: UTF-8 -*-

#题目：按逗号分隔列表。
#程序分析：无。
#join() 函数，将字符串合并为新的字符串，s.join(words) ，words 是一个只含有字符串的 taple 或者 list，join
# 用 s 作为分隔符，将 words 中的字符串连接起来，合并为一个字符串。
L = [1,2,3,4,5]
s1 = ','.join(str(n) for n in L)                 #for n in L,s是在循环L
print s1
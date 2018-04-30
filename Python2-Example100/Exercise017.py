#!/usr/bin/python
# -*- coding: UTF-8 -*-

#题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
#程序分析：利用 while 或 for 语句,条件为输入的字符不为 '\n'。
import string
s = raw_input('请输入一个字符串:\n')
letters = 0
space = 0
digit = 0
others = 0
i=0
while i < len(s):
    c = s[i]
    i += 1
    if c.isalpha():                                #Python isalpha() 方法检测字符串是否只由字母组成。
        letters += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit += 1
    else:
        others += 1
print 'char = %d,space = %d,digit = %d,others = %d' % (letters,space,digit,others)
#!/usr/bin/python
# -*- coding: UTF-8 -*-

 #题目：八进制转换为十进制
 #八进制72变成十进制：2*8**0+7*8**1
if __name__ == '__main__':
    n = 0
    p = raw_input('input a octal number:\n')
    for i in range(len(p)):
        n = n * 8 + ord(p[i]) - ord('0')
    print n
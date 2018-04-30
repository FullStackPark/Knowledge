#!/usr/bin/python
# -*- coding: UTF-8 -*-

#题目：学习使用按位异或 ^ 。
#程序分析：0^0=0; 0^1=1; 1^0=1; 1^1=0
if __name__ == '__main__':
    a = 077
    b = a ^ 3
    print 'The a ^ 3 = %d' % b                    #相同则0，不同则1
    b ^= 7
    print 'The a ^ b = %d' % b
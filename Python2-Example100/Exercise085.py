#!/usr/bin/python
# -*- coding: UTF-8 -*-

#题目：输入一个奇数，然后判断最少几个 9 除于该数的结果为整数。
#程序分析：999999 / 13 = 76923。
if __name__ == '__main__':
    zi = int(raw_input('输入一个数字:\n'))           #zi是除数
    n1 = 1
    c9 = 1                                            #c9指几个9
    m9 = 9
    sum = 9                                           #被除数
    while n1 != 0:
        if sum % zi == 0:
            n1 = 0                                   #0个9
        else:
            m9 *= 10                                   #依次乘10+sum=多一个9后的被除数
            sum += m9
            c9 += 1
    print '%d 个 9 可以被 %d 整除 : %d' % (c9,zi,sum)
    r = sum / zi
    print '%d / %d = %d' % (sum,zi,r)
#!/usr/bin/python
# -*- coding: UTF-8 -*-

#题目：时间函数举例3
#clock()方法语法：time.clock()：该函数有两个功能，在第一次调用的时候，返回的是程序运行的实际时间；以第二次之后的调用，
# 返回的是自第一次调用后,到这次调用的时间间隔;在win32系统下，这个函数返回的是真实时间（wall time），而在Unix/Linux下
# 返回的是CPU时间。
if __name__ == '__main__':
    import time
    start = time.clock()
    for i in range(10000):
        print i
    end = time.clock()
    print 'different is %6.3f' % (end - start)
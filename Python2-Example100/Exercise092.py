#!/usr/bin/python
# -*- coding: UTF-8 -*-

#题目：时间函数举例2
#函数time.time()用于获取当前时间戳

if __name__ == '__main__':
    import time
    start = time.time()
    for i in range(3000):
        print i
    end = time.time()

    print end - start
#!/usr/bin/python
# -*- coding: UTF-8 -*-

#题目：暂停一秒输出。
#程序分析：使用 time 模块的 sleep() 函数。
#sleep()方法语法：time.sleep(t)，t -- 推迟执行的秒数。该函数无返回值
#字典tems()方法语法：dict.items()，返回可遍历的(键, 值) 元组数组
import time
myD = {1: 'a', 2: 'b'}                                         #字典
for key, value in dict.items(myD):
    print key, value                                          #输出键和对应的值
    time.sleep(1)                                              # 暂停 1 秒
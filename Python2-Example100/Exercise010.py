#!/usr/bin/python
# -*- coding: UTF-8 -*-

#题目：暂停一秒输出，并格式化当前时间。
#程序分析：无。
#strftime()方法语法：time.strftime(format[, t])，format - 格式字符串，t -可选的参数t是一个struct_time对象。
#返回以可读字符串表示的当地时间
#localtime()方法语法：time.localtime([ sec ])，sec -转换为time.struct_time类型的对象的秒数，该函数没有任
#  何返回值。
import time
print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
time.sleep(1)                                                                 # 暂停一秒
print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
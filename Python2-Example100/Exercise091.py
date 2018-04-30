#!/usr/bin/python
# -*- coding: UTF-8 -*-

#题目：时间函数举例1。
#time.asctime([tupletime])接受时间元组并返回一个可读的形式为"Tue Dec 11 18:07:14 2008"（2008年12月11日 周二18时07分14秒）
# 的24个字符的字符串。
#	time.ctime([secs])作用相当于asctime(localtime(secs))，未给参数相当于asctime()
#gmtime()方法语法：time.gmtime([ sec ])，sec -- 转换为time.struct_time类型的对象的秒数。
#localtime()方法语法：time.localtime([ sec ])，sec -- 转换为time.struct_time类型的对象的秒数。
if __name__ == '__main__':
    import time
    print time.ctime(time.time())
    print time.asctime(time.localtime(time.time()))
    print time.asctime(time.gmtime(time.time()))
#!/usr/bin/python
# -*- coding: UTF-8 -*-

#题目：输入某年某月某日，判断这一天是这一年的第几天？
#程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份
# 大于2时需考虑多加一天：
year = int(raw_input('year:\n'))
month = int(raw_input('month:\n'))
day = int(raw_input('day:\n'))

months = (0,31,59,90,120,151,181,212,243,273,304,334)            #非闰月每月最后一天是今年的第几天
if 0 < month <= 12:
    sum = months[month - 1]
else:
    print 'data error'
sum += day
leap = 0                                                          #leap在此处作为标志，判断是否后面+1
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)): #能够被4和400整除的是闰年
    leap = 1
if (leap == 1) and (month > 2):
    sum += 1
print 'it is the %dth day.' % sum
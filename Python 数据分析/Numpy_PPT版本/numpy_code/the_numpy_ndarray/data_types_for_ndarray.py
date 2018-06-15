# -*- coding: utf-8 -*-

import numpy as np

print '生成数组时指定数据类型'
arr = np.array([1, 2, 3], dtype = np.float64)
print arr.dtype
arr = np.array([1, 2, 3], dtype = np.int32)
print arr.dtype
print

print '使用astype复制数组并转换数据类型'
int_arr = np.array([1, 2, 3, 4, 5])
float_arr = int_arr.astype(np.float)
print int_arr.dtype
print float_arr.dtype
print

print '使用astype将float转换为int时小数部分被舍弃'
float_arr = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])
int_arr = float_arr.astype(dtype = np.int)
print int_arr
print

print '使用astype把字符串转换为数组，如果失败抛出异常。'
str_arr = np.array(['1.25', '-9.6', '42'], dtype = np.string_)
float_arr = str_arr.astype(dtype = np.float)
print float_arr
print

print 'astype使用其它数组的数据类型作为参数'
int_arr = np.arange(10)
float_arr = np.array([.23, 0.270, .357, 0.44, 0.5], dtype = np.float64)
print int_arr.astype(float_arr.dtype)
print int_arr[0], int_arr[1]  # astype做了复制，数组本身不变。
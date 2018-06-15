# -*- coding: utf-8 -*-

import numpy as np
import numpy.random as np_random


print '连接两个二维数组'
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[7, 8, 9], [10, 11, 12]])
print np.concatenate([arr1, arr2], axis = 0)  # 按行连接
print np.concatenate([arr1, arr2], axis = 1)  # 按列连接
print

# 所谓堆叠，参考叠盘子。。。连接的另一种表述
print '垂直stack与水平stack'
print np.vstack((arr1, arr2)) # 垂直堆叠
print np.hstack((arr1, arr2)) # 水平堆叠
print

print '拆分数组'
arr = np_random.randn(5, 5)
print arr
print '水平拆分'
first, second, third = np.split(arr, [1, 3], axis = 0)
print 'first'
print first
print 'second'
print second
print 'third'
print third
print '垂直拆分'
first, second, third = np.split(arr, [1, 3], axis = 1)
print 'first'
print first
print 'second'
print second
print 'third'
print third
print

# 堆叠辅助类
arr = np.arange(6)
arr1 = arr.reshape((3, 2))
arr2 = np_random.randn(3, 2)
print 'r_用于按行堆叠'
print np.r_[arr1, arr2]
print 'c_用于按列堆叠'
print np.c_[np.r_[arr1, arr2], arr]
print '切片直接转为数组'
print np.c_[1:6, -10:-5]

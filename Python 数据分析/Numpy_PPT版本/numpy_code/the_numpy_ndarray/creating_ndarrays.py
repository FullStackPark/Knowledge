# -*- coding: utf-8 -*-

import numpy as np

print '使用普通一维数组生成NumPy一维数组'
data = [6, 7.5, 8, 0, 1]
arr = np.array(data)
print arr
print '打印元素类型'
print arr.dtype
print 

print '使用普通二维数组生成NumPy二维数组'
data = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr = np.array(data)
print arr
print '打印数组维度'
print arr.shape
print

print '使用zeros/empty'
print np.zeros(10) # 生成包含10个0的一维数组
print np.zeros((3, 6)) # 生成3*6的二维数组
print np.empty((2, 3, 2)) # 生成2*3*2的三维数组，所有元素未初始化。
print

print '使用arrange生成连续元素'
print np.arange(15)  # [0, 1, 2, ..., 14]
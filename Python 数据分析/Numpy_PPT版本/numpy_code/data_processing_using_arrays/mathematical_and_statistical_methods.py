# -*- coding: utf-8 -*-

import numpy as np
import numpy.random as np_random

print '求和，求平均'
arr = np.random.randn(5, 4)
print arr
print arr.mean()
print arr.sum()
print arr.mean(axis = 1)  # 对每一行的元素求平均
print arr.sum(0)  # 对每一列元素求和，axis可以省略。
print

'''
cumsum:
- 按列操作：a[i][j] += a[i - 1][j]
- 按行操作：a[i][j] *= a[i][j - 1]
cumprod:
- 按列操作：a[i][j] += a[i - 1][j]
- 按行操作：a[i][j] *= a[i][j - 1]
'''
print 'cunsum和cumprod函数演示'
arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
print arr.cumsum(0)
print arr.cumprod(1)
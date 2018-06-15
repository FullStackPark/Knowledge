# -*- coding: utf-8 -*-

import numpy as np
import numpy.random as np_random

print '转置矩阵'
arr = np.arange(15).reshape((3, 5))
print arr
print arr.T
print

print '转置矩阵做点积'
arr = np_random.randn(6, 3)
print np.dot(arr.T, arr)
print

print '高维矩阵转换'
arr = np.arange(16).reshape((2, 2, 4))
print arr
'''
详细解释：
arr数组的内容为
- a[0][0] = [0, 1, 2, 3]
- a[0][1] = [4, 5, 6, 7]
- a[1][0] = [8, 9, 10, 11]
- a[1][1] = [12, 13, 14, 15]
transpose的参数为坐标，正常顺序为(0, 1, 2, ... , n - 1)，
现在传入的为(1, 0, 2)代表a[x][y][z] = a[y][x][z]，第0个和第1个坐标互换。
- a'[0][0] = a[0][0] = [0, 1, 2, 3]
- a'[0][1] = a[1][0] = [8, 9, 10, 11]
- a'[1][0] = a[0][1] = [4, 5, 6, 7]
- a'[1][1] = a[1][1] = [12, 13, 14, 15]
'''
print arr.transpose((1, 0, 2))
print arr.swapaxes(1, 2)  # 直接交换第1和第2个坐标
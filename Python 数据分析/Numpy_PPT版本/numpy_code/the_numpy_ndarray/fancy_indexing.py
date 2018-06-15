# -*- coding: utf-8 -*-

import numpy as np

print 'Fancy Indexing: 使用整数数组作为索引'
arr = np.empty((8, 4))
for i in range(8):
    arr[i] = i
print arr
print arr[[4, 3, 0, 6]] # 打印arr[4]、arr[3]、arr[0]和arr[6]。
print arr[[-3, -5, -7]] # 打印arr[3]、arr[5]和arr[-7]行
arr = np.arange(32).reshape((8, 4))  # 通过reshape变换成二维数组
print arr[[1, 5, 7, 2], [0, 3, 1, 2]] # 打印arr[1, 0]、arr[5, 3]，arr[7, 1]和arr[2, 2]
print arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]]  # 1572行的0312列
print arr[np.ix_([1, 5, 7, 2], [0, 3, 1, 2])] # 可读性更好的写法
# -*- coding: utf-8 -*-

import numpy as np
import numpy.random as np_random

print 'Fancy Indexing例子代码'
arr = np.arange(10) * 100
inds = [7, 1, 2, 6]
print arr[inds]
print

print '使用take'
print arr.take(inds)
print

print '使用put更新内容'
arr.put(inds, 50)
print arr
arr.put(inds, [70, 10, 20, 60])
print arr
print

print 'take，指定轴'
arr = np_random.randn(2, 4)
inds = [2, 0, 2, 1]
print arr
print arr.take(inds, axis = 1)  # 按列take

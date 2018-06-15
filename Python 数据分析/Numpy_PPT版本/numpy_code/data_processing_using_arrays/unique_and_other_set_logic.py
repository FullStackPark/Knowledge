# -*- coding: utf-8 -*-

import numpy as np
import numpy.random as np_random

print '用unique函数去重'
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
print sorted(set(names))  # 传统Python做法
print np.unique(names)
ints = np.array([3, 3, 3, 2, 2, 1, 1, 4, 4])
print np.unique(ints)
print

print '查找数组元素是否在另一数组'
values = np.array([6, 0, 0, 3, 2, 5, 6])
print np.in1d(values, [2, 3, 6])
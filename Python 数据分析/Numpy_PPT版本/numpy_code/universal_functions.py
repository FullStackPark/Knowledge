# -*- coding: utf-8 -*-

import numpy as np
import numpy.random as np_random

print '求平方根'
arr = np.arange(10)
print np.sqrt(arr)
print

print '数组比较'
x = np_random.randn(8)
y = np_random.randn(8)
print x
print y
print np.maximum(x, y)
print

print '使用modf函数把浮点数分解成整数和小数部分'
arr = np_random.randn(7) * 5  # 统一乘5
print np.modf(arr)
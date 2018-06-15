# -*- coding: utf-8 -*-

import numpy as np

# 数组乘法／减法，对应元素相乘／相减。
arr = np.array([[1.0, 2.0, 3.0], [4., 5., 6.]])
print arr * arr
print arr - arr
print

# 标量操作作用在数组的每个元素上
arr = np.array([[1.0, 2.0, 3.0], [4., 5., 6.]])
print 1 / arr
print arr ** 0.5  # 开根号
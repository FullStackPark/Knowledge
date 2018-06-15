# -*- coding: utf-8 -*-

import numpy as np
import numpy.random as np_random
from numpy.linalg import inv, qr

print '矩阵乘法'
x = np.array([[1., 2., 3.], [4., 5., 6.]])
y = np.array([[6., 23.], [-1, 7], [8, 9]])
print x.dot(y)
print np.dot(x, np.ones(3))
x = np_random.randn(5, 5)
print

print '矩阵求逆'
mat = x.T.dot(x)
print inv(mat)  # 矩阵求逆
print mat.dot(inv(mat)) # 与逆矩阵相乘，得到单位矩阵。
print

print '矩阵消元'
print mat
q, r = qr(mat)
print q
print r
# TODO: http://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.qr.html q代表什么矩阵？
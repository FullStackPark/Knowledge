# -*- coding: utf-8 -*-

import numpy as np

print '数组文件读写'
arr = np.arange(10)
np.save('some_array', arr)
print np.load('some_array.npy')
print

print '多个数组压缩存储'
np.savez('array_archive.npz', a = arr, b = arr)
arch = np.load('array_archive.npz')
print arch['b']
# -*- coding: utf-8 -*-

import numpy as np

# 通过索引访问二维数组某一行或某个元素
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print arr[2]
print arr[0][2]
print arr[0, 2] # 普通Python数组不能用。
print

# 对更高维数组的访问和操作
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print arr[0]  # 结果是个2维数组
print arr[1, 0] # 结果是个2维数组
old_values = arr[0].copy()  # 复制arr[0]的值
arr[0] = 42 # 把arr[0]所有的元素都设置为同一个值
print arr
arr[0] = old_values # 把原来的数组写回去
print arr
print

print '使用切片访问和操作数组'
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print arr[1:6]  # 打印元素arr[1]到arr[5]
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print arr[:2] # 打印第1、2行
print arr[:2, 1:] # 打印第1、2行，第2、3列
print arr[:, :1]  # 打印第一列的所有元素
arr[:2, 1:] = 0 # 第1、2行，第2、3列的元素设置为0
print arr
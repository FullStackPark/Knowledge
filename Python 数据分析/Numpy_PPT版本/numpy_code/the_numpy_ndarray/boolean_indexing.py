# -*- coding: utf-8 -*-

import numpy as np
import numpy.random as np_random

print '使用布尔数组作为索引'
name_arr = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
rnd_arr = np_random.randn(7, 4) # 随机7*4数组
print rnd_arr
print name_arr == 'Bob' # 返回布尔数组，元素等于'Bob'为True，否则False。
print rnd_arr[name_arr == 'Bob']  # 利用布尔数组选择行
print rnd_arr[name_arr == 'Bob', :2]  # 增加限制打印列的范围
print rnd_arr[-(name_arr == 'Bob')] # 对布尔数组的内容取反
mask_arr = (name_arr == 'Bob') | (name_arr == 'Will') # 逻辑运算混合结果
print rnd_arr[mask_arr]
rnd_arr[name_arr != 'Joe'] = 7  # 先布尔数组选择行，然后把每行的元素设置为7。
print rnd_arr
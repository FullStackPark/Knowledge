# -*- coding: utf-8 -*- 

import numpy as np
from pandas import Series, DataFrame

print 'Series的索引，默认数字索引可以工作。'
obj = Series(np.arange(4.), index = ['a', 'b', 'c', 'd'])
print obj['b']
print obj[3]
print obj[[1, 3]]
print obj[obj < 2]
print

print 'Series的数组切片'
print obj['b':'c']  # 闭区间
obj['b':'c'] = 5
print obj
print

print 'DataFrame的索引'
data = DataFrame(np.arange(16).reshape((4, 4)),
                  index = ['Ohio', 'Colorado', 'Utah', 'New York'],
                  columns = ['one', 'two', 'three', 'four'])
print data
print data['two'] # 打印列
print data[['three', 'one']]
print data[:2]
print data.ix['Colorado', ['two', 'three']] # 指定索引和列
print data.ix[['Colorado', 'Utah'], [3, 0, 1]]
print data.ix[2]  # 打印第2行（从0开始）
print data.ix[:'Utah', 'two'] # 从开始到Utah，第2列。
print

print '根据条件选择'
print data[data.three > 5]
print data < 5  # 打印True或者False
data[data < 5] = 0
print data

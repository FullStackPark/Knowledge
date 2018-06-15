# -*- coding: utf-8 -*- 

import numpy as np
from pandas import Series, DataFrame

print '求和'
df = DataFrame([[1.4, np.nan], [7.1, -4.5], [np.nan, np.nan], [0.75, -1.3]],
              index = ['a', 'b', 'c', 'd'],
              columns = ['one', 'two'])
print df
print df.sum()  # 按列求和
print df.sum(axis = 1)  # 按行求和
print

print '平均数'
print df.mean(axis = 1, skipna = False)
print df.mean(axis = 1)
print

print '其它'
print df.idxmax()
print df.cumsum()
print df.describe()
obj = Series(['a', 'a', 'b', 'c'] * 4)
print obj.describe()

# -*- coding: utf-8 -*- 

import numpy as np
from numpy import nan as NA
from pandas import Series, DataFrame

print '丢弃NA'
data = Series([1, NA, 3.5, NA, 7])
print data.dropna()
print data[data.notnull()]
print

print 'DataFrame对丢弃NA的处理'
data = DataFrame([[1., 6.5, 3.], [1., NA, NA],
                  [NA, NA, NA], [NA, 6.5, 3.]])
print data.dropna() # 默认只要某行有NA就全部删除
print data.dropna(how = 'all')  # 全部为NA才删除
data[4] = NA  # 新增一列
print data.dropna(axis = 1, how = 'all')
data = DataFrame(np.random.randn(7, 3))
data.ix[:4, 1] = NA
data.ix[:2, 2] = NA
print data
print data.dropna(thresh = 2) # 每行至少要有2个非NA元素

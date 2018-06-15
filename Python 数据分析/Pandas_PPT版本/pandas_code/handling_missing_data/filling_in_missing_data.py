# -*- coding: utf-8 -*- 

import numpy as np
from numpy import nan as NA
import pandas as pd
from pandas import Series, DataFrame, Index

print '填充0'
df = DataFrame(np.random.randn(7, 3))
df.ix[:4, 1] = NA
df.ix[:2, 2] = NA
print df.fillna(0)
df.fillna(0, inplace = True)
print df
print

print '不同行列填充不同的值'
print df.fillna({1:0.5, 3:-1})  # 第3列不存在
print

print '不同的填充方式'
df = DataFrame(np.random.randn(6, 3))
df.ix[2:, 1] = NA
df.ix[4:, 2] = NA
print df
print df.fillna(method = 'ffill')
print df.fillna(method = 'ffill', limit = 2)
print

print '用统计数据填充'
data = Series([1., NA, 3.5, NA, 7])
print data.fillna(data.mean())

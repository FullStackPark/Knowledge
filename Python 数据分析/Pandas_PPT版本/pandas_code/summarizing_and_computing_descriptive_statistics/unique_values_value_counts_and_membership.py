# -*- coding: utf-8 -*- 

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

print '去重'
obj = Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])
print obj.unique()
print obj.value_counts()
print

print '判断元素存在'
mask = obj.isin(['b', 'c'])
print mask
print obj[mask] #只打印元素b和c
data = DataFrame({'Qu1':[1, 3, 4, 3, 4],
                  'Qu2':[2, 3, 1, 2, 3],
                  'Qu3':[1, 5, 2, 4, 4]})
print data
print data.apply(pd.value_counts).fillna(0)
print data.apply(pd.value_counts, axis = 1).fillna(0)

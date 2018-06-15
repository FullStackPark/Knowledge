# -*- coding: utf-8 -*- 

import numpy as np
from pandas import Series, DataFrame

print 'Series根据索引删除元素'
obj = Series(np.arange(5.), index = ['a', 'b', 'c', 'd', 'e'])
new_obj = obj.drop('c')
print new_obj
print obj.drop(['d', 'c'])
print

print 'DataFrame删除元素，可指定索引或列。'
data = DataFrame(np.arange(16).reshape((4, 4)),
                  index = ['Ohio', 'Colorado', 'Utah', 'New York'],
                  columns = ['one', 'two', 'three', 'four'])
print data
print data.drop(['Colorado', 'Ohio'])
print data.drop('two', axis = 1)
print data.drop(['two', 'four'], axis = 1)

# -*- coding: utf-8 -*- 

import numpy as np
from pandas import Series, DataFrame

print '用字典生成DataFrame，key为列的名字。'
data = {'state':['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year':[2000, 2001, 2002, 2001, 2002],
        'pop':[1.5, 1.7, 3.6, 2.4, 2.9]}
print DataFrame(data)
print DataFrame(data, columns = ['year', 'state', 'pop']) # 指定列顺序
print

print '指定索引，在列中指定不存在的列，默认数据用NaN。'
frame2 = DataFrame(data,
                    columns = ['year', 'state', 'pop', 'debt'],
                    index = ['one', 'two', 'three', 'four', 'five'])
print frame2
print frame2['state']
print frame2.year
print frame2.ix['three']
frame2['debt'] = 16.5 # 修改一整列
print frame2
frame2.debt = np.arange(5)  # 用numpy数组修改元素
print frame2
print

print '用Series指定要修改的索引及其对应的值，没有指定的默认数据用NaN。'
val = Series([-1.2, -1.5, -1.7], index = ['two', 'four', 'five'])
frame2['debt'] = val
print frame2
print

print '赋值给新列'
frame2['eastern'] = (frame2.state == 'Ohio')  # 如果state等于Ohio为True
print frame2
print frame2.columns
print

print 'DataFrame转置'
pop = {'Nevada':{2001:2.4, 2002:2.9},
        'Ohio':{2000:1.5, 2001:1.7, 2002:3.6}}
frame3 = DataFrame(pop)
print frame3
print frame3.T
print

print '指定索引顺序，以及使用切片初始化数据。'
print DataFrame(pop, index = [2001, 2002, 2003])
pdata = {'Ohio':frame3['Ohio'][:-1], 'Nevada':frame3['Nevada'][:2]}
print DataFrame(pdata)
print

print '指定索引和列的名称'
frame3.index.name = 'year'
frame3.columns.name = 'state'
print frame3
print frame3.values
print frame2.values

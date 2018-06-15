# -*- coding: utf-8 -*- 

from pandas import Series

print '用数组生成Series'
obj = Series([4, 7, -5, 3])
print obj
print obj.values
print obj.index
print

print '指定Series的index'
obj2 = Series([4, 7, -5, 3], index = ['d', 'b', 'a', 'c'])
print obj2
print obj2.index
print obj2['a']
obj2['d'] = 6
print obj2[['c', 'a', 'd']]
print obj2[obj2 > 0]  # 找出大于0的元素
print 'b' in obj2 # 判断索引是否存在
print 'e' in obj2
print

print '使用字典生成Series'
sdata = {'Ohio':45000, 'Texas':71000, 'Oregon':16000, 'Utah':5000}
obj3 = Series(sdata)
print obj3
print

print '使用字典生成Series，并额外指定index，不匹配部分为NaN。'
states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = Series(sdata, index = states)
print obj4
print

print 'Series相加，相同索引部分相加。'
print obj3 + obj4
print

print '指定Series及其索引的名字'
obj4.name = 'population'
obj4.index.name = 'state'
print obj4
print

print '替换index'
obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
print obj

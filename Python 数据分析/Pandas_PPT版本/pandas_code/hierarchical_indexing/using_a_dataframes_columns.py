# -*- coding: utf-8 -*- 

import numpy as np
from pandas import DataFrame

print '使用列生成层次索引'
frame = DataFrame({'a':range(7),
                   'b':range(7, 0, -1),
                   'c':['one', 'one', 'one', 'two', 'two', 'two', 'two'],
                   'd':[0, 1, 2, 0, 1, 2, 3]})
print frame
print frame.set_index(['c', 'd'])  # 把c/d列变成索引
print frame.set_index(['c', 'd'], drop = False) # 列依然保留
frame2 = frame.set_index(['c', 'd'])
print frame2.reset_index()


# -*- coding: utf-8 -*- 

import numpy as np
from pandas import DataFrame

print '根据指定的key计算统计信息'
frame = DataFrame(np.arange(12).reshape((4, 3)),
                  index = [['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                  columns = [['Ohio', 'Ohio', 'Colorado'], ['Green', 'Red', 'Green']])
frame.index.names = ['key1', 'key2']
print frame
print frame.sum(level = 'key2')

# -*- coding: utf-8 -*- 

import numpy as np
from pandas import Series

print '作为null处理的值'
string_data = Series(['aardvark', 'artichoke', np.nan, 'avocado'])
print string_data
print string_data.isnull()
string_data[0] = None
print string_data.isnull()

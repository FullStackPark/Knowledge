# -*- coding: utf-8 -*-

import numpy as np
import numpy.random as np_random
from random import normalvariate

print '正态分布随机数'
samples = np.random.normal(size=(4, 4))
print samples

print '批量按正态分布生成0到1的随机数'
N = 10
print [normalvariate(0, 1) for _ in xrange(N)]
print np.random.normal(size = N)  # 与上面代码等价
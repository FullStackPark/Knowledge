# -*- coding: utf-8 -*- 

import numpy as np
import pandas as pd
import pandas.io.data as web
from pandas import Series, DataFrame, Index, Panel

pdata = Panel(dict((stk, web.get_data_yahoo(stk, '1/1/2016', '1/15/2016')) for stk in ['AAPL', 'GOOG', 'BIDU', 'MSFT']))
print pdata
pdata = pdata.swapaxes('items', 'minor')
print pdata
print

print "访问顺序：# Item -> Major -> Minor"
print pdata['Adj Close']
print pdata[:, '1/5/2016', :]
print pdata['Adj Close', '1/6/2016', :]
print

print 'Panel与DataFrame相互转换'
stacked = pdata.ix[:, '1/7/2016':, :].to_frame()
print stacked
print stacked.to_panel()

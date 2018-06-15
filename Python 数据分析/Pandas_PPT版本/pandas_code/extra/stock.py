# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

names = ['date',
         'time',
         'opening_price',
         'ceiling_price',
         'floor_price',
         'closing_price',
         'volume',
         'amount']
raw = pd.read_csv('SH600690.csv', names = names, header = None, index_col='date', parse_dates=True)
print raw.head()
print

'''
# 根据涨跌幅判断数据是否有效
def _valid_price(prices):
    return (((prices.max() - prices.min()) / prices.min()) < 0.223).all()

# 按日期分组
days = raw.groupby(level = 0).agg(
        {'opening_price':lambda prices: _valid_price(prices) and prices[0] or 0,
         'ceiling_price':lambda prices: _valid_price(prices) and np.max(prices) or 0,
         'floor_price':lambda prices: _valid_price(prices) and np.min(prices) or 0,
         'closing_price':lambda prices: _valid_price(prices) and prices[-1] or 0,
         'volume':'sum',
         'amount':'sum'})
print days.head()
print


# 缺少数据处理，因为周末没有交易。
start = days.iloc[0:1].index.tolist()[0]
end = days.iloc[-2:-1].index.tolist()[0]
new_idx = pd.date_range(start = start, end = end)
print new_idx
data = days.reindex(new_idx)    # 重新索引
zero_values = data.loc[~(data.volume > 0)].loc[:, ['volume', 'amount']]
data.update(zero_values.fillna(0))  # 交易量和金额填0
data.fillna(method = 'ffill', inplace = True)   # 价格用前一天的填充
print data.head()
print

# 计算30各自然日里的股票平均波动周率
def gen_item_group_index(total, group_len):
    group_count = total / group_len
    group_index = np.arange(total)
    for i in xrange(group_count):
        group_index[i * group_len: (i+ 1) * group_len] = i
    group_index[(i + 1) * group_len:] = i +1
    return group_index.tolist()

period = 30
group_index = gen_item_group_index(len(data), period)
data['group_index'] = group_index
print data.head().append(data.tail())

# 为负表示先出现最高价再出现最低价，即下跌波动。
def _ceiling_price(prices):
    return prices.idxmin() < prices.idxmax() and np.max(prices) or (-np.max(prices))

group = data.groupby('group_index').agg(
            {'volume': 'sum',
             'floor_price': 'min',
             'ceiling_price': _ceiling_price})
print group.head()
date_col = pd.DataFrame({'group_index': group_index, 'date': new_idx})
print date_col
group['date'] = date_col.groupby('group_index').agg('first')    # 为每个索引添加开始日期
print group.head()
group['ripples_ratio'] = group.ceiling_price / group.floor_price    # 计算并添加波动率
print group.head()
print

# 波动率排序
ripples = group.sort_values('ripples_ratio', ascending = False)
print ripples
print ripples.head(10).ripples_ratio.mean()
print ripples.tail(10).ripples_ratio.mean()
print

# 计算涨跌幅
rise = data.closing_price.diff()
data['rise'] = rise
print data.head()
'''

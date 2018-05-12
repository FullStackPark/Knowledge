**有这样一个列表：**

```language-python
list = [{'channel_id': -3, 'name': u'\u7ea2\u5fc3\u5146\u8d6b'}, {u'seq_id': 0, u'name_en': u'Personal Radio', u'channel_id': 0, u'abbr_en': u'My', u'name': u'\u79c1\u4eba\u5146\u8d6b'}]
```

- 1

**其中name值是中文，如何讲其显示为中文？**

```language-python
s = str(self.channel_list).replace('u\'','\'')
print s.decode("unicode-escape")
```

- 1
- 2

**成功显示：**

```language-python
[{'channel_id': -3, 'name': '红心兆赫'}, {'seq_id': 0, 'name_en': 'Personal Radio', 'channel_id': 0, 'abbr_en': 'My', 'name': '私人兆赫'}, ]
```

- 1

**但此时类型为unicode**

```language-python
>>> type(s)
<type 'unicode'>
```

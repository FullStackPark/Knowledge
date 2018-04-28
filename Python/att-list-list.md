Python List list()方法
====================

 [![Python 列表](../images/up.gif)
 Python 列表](python-lists.html)


  描述
--

 list() 方法用于将元组转换为列表。

 **注：**元组与列表是非常类似的，区别在于元组的元素值不能修改，元组是放在括号中，列表是放于方括号中。

 语法
--

 list()方法语法：

 
```

list( tup )

```

 参数
--

  * tup -- 要转换为列表的元组。
  返回值
---

 返回列表。

 实例
--

 以下实例展示了 list()函数的使用方法：

  <pre>

#!/usr/bin/python
# -*- coding: UTF-8 -*-
aTuple = (123, 'xyz', 'zara', 'abc');
aList = list(aTuple)
print "列表元素 : ", aList
</pre>

 以上实例输出结果如下：

 
```

列表元素 :  [123, 'xyz', 'zara', 'abc']

```

[![Python 列表](../images/up.gif)
 Python 列表](python-lists.html)
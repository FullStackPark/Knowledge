Python List cmp()方法
===================

 [![Python 列表](../images/up.gif)
 Python 列表](python-lists.html)


  描述
--

 cmp() 方法用于比较两个列表的元素。

 语法
--

 cmp()方法语法：

 
```

cmp(list1, list2)

```

 参数
--

  * list1 -- 比较的列表。
 * list2 -- 比较的列表。
  返回值
---

 如果比较的元素是同类型的,则比较其值,返回结果。

 如果两个元素不是同一种类型,则检查它们是否是数字。

  * 如果是数字,执行必要的数字强制类型转换,然后比较。 
 * 如果有一方的元素是数字,则另一方的元素"大"(数字是"最小的") 
 * 否则,通过类型名字的字母顺序进行比较。
  如果有一个列表首先到达末尾,则另一个长一点的列表"大"。

 如果我们用尽了两个列表的元素而且所 有元素都是相等的,那么结果就是个平局,就是说返回一个 0。

 实例
--

 以下实例展示了 cmp()函数的使用方法：

 
```

#!/usr/bin/python

list1, list2 = [123, 'xyz'], [456, 'abc']

print cmp(list1, list2);
print cmp(list2, list1);
list3 = list2 + [786];
print cmp(list2, list3)

```

 以上实例输出结果如下：

 
```

-1
1
-1

```

 [![Python 列表](../images/up.gif)
 Python 列表](python-lists.html)
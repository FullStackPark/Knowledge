Python List count()方法
=====================

 [![Python 列表](../images/up.gif)
 Python 列表](python-lists.html)


  描述
--

 count() 方法用于统计某个元素在列表中出现的次数。

 语法
--

 count()方法语法：

 
```

list.count(obj)

```

 参数
--

  * obj -- 列表中统计的对象。
  返回值
---

 返回元素在列表中出现的次数。

 实例
--

 以下实例展示了 count()函数的使用方法：

 
```

#!/usr/bin/python

aList = [123, 'xyz', 'zara', 'abc', 123];

print "Count for 123 : ", aList.count(123);
print "Count for zara : ", aList.count('zara');

```

 以上实例输出结果如下：

 
```

Count for 123 :  2
Count for zara :  1

```

[![Python 列表](../images/up.gif)
 Python 列表](python-lists.html)
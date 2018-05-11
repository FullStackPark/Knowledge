Python List index()方法
=====================

 [![Python 列表](../images/up.gif)
 Python 列表](python-lists.html)


  描述
--

 index() 函数用于从列表中找出某个值第一个匹配项的索引位置。

 语法
--

 index()方法语法：

 
```

list.index(obj)

```

 参数
--

  * obj -- 查找的对象。
  返回值
---

 该方法返回查找对象的索引位置，如果没有找到对象则抛出异常。

 实例
--

 以下实例展示了 index()函数的使用方法：

 
```

#!/usr/bin/python

aList = [123, 'xyz', 'zara', 'abc'];

print "Index for xyz : ", aList.index( 'xyz' ) ;
print "Index for zara : ", aList.index( 'zara' ) ;

```

 以上实例输出结果如下：

 
```

Index for xyz :  1
Index for zara :  2

```

[![Python 列表](../images/up.gif)
 Python 列表](python-lists.html)
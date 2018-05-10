Python time mktime()方法
======================

  描述
--

 Python time mktime() 函数执行与gmtime(), localtime()相反的操作，它接收struct\_time对象作为参数，返回用秒数来表示时间的浮点数。 

 如果输入的值不是一个合法的时间，将触发 OverflowError 或 ValueError。

 语法
--

 mktime()方法语法：

 
```

time.mktime(t)

```

 参数
--

  * t -- 结构化的时间或者完整的9位元组元素。
  返回值
---

 返回用秒数来表示时间的浮点数。

 实例
--

 以下实例展示了 mktime() 函数的使用方法：

 
```

#!/usr/bin/python
import time

t = (2009, 2, 17, 17, 3, 38, 1, 48, 0)
secs = time.mktime( t )
print "time.mktime(t) : %f" %  secs
print "asctime(localtime(secs)): %s" % time.asctime(time.localtime(secs))

```

 以上实例输出结果为：

 
```

time.mktime(t) : 1234915418.000000
asctime(localtime(secs)): Tue Feb 17 17:03:38 2009

```
Python lstrip()方法
=================

 [![Python 字符串](../images/up.gif)
 Python 字符串](python-strings.html)


  描述
--

 Python lstrip() 方法用于截掉字符串左边的空格或指定字符。

 语法
--

 lstrip()方法语法：

 
```

str.lstrip([chars])

```

 参数
--

  * chars --指定截取的字符。
  返回值
---

 返回截掉字符串左边的空格或指定字符后生成的新字符串。

 实例
--

 以下实例展示了lstrip()的使用方法：

 
```

#!/usr/bin/python

str = "     this is string example....wow!!!     ";
print str.lstrip();
str = "88888888this is string example....wow!!!8888888";
print str.lstrip('8');

```

 以上实例输出结果如下：

 
```

this is string example....wow!!!
this is string example....wow!!!8888888

```

  [![Python 字符串](../images/up.gif)
 Python 字符串](python-strings.html)
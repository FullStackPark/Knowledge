Python index()方法
================

 [![Python 字符串](../images/up.gif)
 Python 字符串](python-strings.html)


  描述
--

 Python index() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，该方法与 python find()方法一样，只不过如果str不在 string中会报一个异常。

 语法
--

 index()方法语法：

 
```

str.index(str, beg=0, end=len(string))

```

 参数
--

  * str -- 指定检索的字符串
 * beg -- 开始索引，默认为0。
 * end -- 结束索引，默认为字符串的长度。
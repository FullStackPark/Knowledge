Python  exec 内置语句
=================

 [![Python 内置函数](../images/up.gif)
 Python 内置函数](python-built-in-functions.html)


  描述
--

 exec 执行储存在字符串或文件中的Python语句，相比于 eval，exec可以执行更复杂的 Python 代码。

 
>  需要说明的是在 Python2 中exec不是函数，而是一个内置语句(statement)，但是Python 2中有一个 execfile() 函数。可以理解为 Python 3 把 exec 这个 statement 和 execfile() 函数的功能够整合到一个新的 exec() 函数中去了。
> 
>
Python 练习实例88
=============

 [![Python 100例](../images/up.gif)
 Python 100例](python-100-examples.html)


 **题目：** 读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的＊。

 **程序分析：** 无。

  实例
--

 <pre>

#!/usr/bin/python
# -*- coding: UTF-8 -*-
if __name__ == '__main__':
    n = 1
while n <= 7:
        a = int(raw_input('input a number:\n'))
while a < 1 or a > 50:
            a = int(raw_input('input a number:\n'))
print a * '*'
n += 1
</pre>

 以上实例输出结果为：


```

input a number:
9
*********
input a number:
5
*****
input a number:
6
******
input a number:

```

 [![Python 100例](../images/up.gif)
 Python 100例](python-100-examples.html)

Python 练习实例3
============

[![Python 100例](../images/up.gif)
 Python 100例](python-100-examples.html)


 **题目：** 一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？

 **程序分析：**

 假设该数为 x。

 1、则：x + 100 = n2, x + 100 + 168 = m2

 2、计算等式：m2 - n2 = (m + n)(m - n) = 168

 3、设置： m + n = i，m - n = j，i * j =168，i 和 j 至少一个是偶数

 4、可得： m = (i + j) / 2， n = (i - j) / 2，i 和 j 要么都是偶数，要么都是奇数。

 5、从 3 和 4 推导可知道，i 与 j 均是大于等于 2 的偶数。

 6、由于 i * j = 168， j>=2，则 **1 < i < 168 / 2 + 1**。

 7、接下来将 i 的所有数字循环计算即可。

 程序源代码：

  实例(Python 2.0+)
---------------

 <pre>

#!/usr/bin/python
# -*- coding: UTF-8 -*-
for i in range(1,85):
    if 168 % i == 0:
        j = 168 / i;
        if i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0 :
            m = (i + j) / 2
n = (i - j) / 2
x = n * n - 100
print(x)
</pre>

  以上实例输出结果为：


```

-99
21
261
1581

```

[![Python 100例](../images/up.gif)
 Python 100例](python-100-examples.html)

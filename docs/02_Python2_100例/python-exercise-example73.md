Python 练习实例73
=============

 [Python 100例](python-100-examples.md)


 **题目：** 反向输出一个链表。

 **程序分析：** 无。

  实例(Python 2.0+)
---------------

 <pre>

#!/usr/bin/python
# -*- coding: UTF-8 -*-
if __name__ == '__main__':
    ptr = []
for i in range(5):
        num = int(raw_input('please input a number:\n'))
ptr.append(num)
print ptr
ptr.reverse()
print ptr
</pre>

 以上实例输出结果为：


```

please input a number:
6
please input a number:
5
please input a number:
3
please input a number:
4
please input a number:
8
[6, 5, 3, 4, 8]
[8, 4, 3, 5, 6]

```

 [Python 100例](python-100-examples.md)

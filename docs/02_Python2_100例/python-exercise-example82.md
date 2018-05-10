Python 练习实例82
=============

 [Python 100例](python-100-examples.md)


 **题目：** 八进制转换为十进制

 **程序分析：** 无。

  实例(Python 2.0+)
---------------

 <pre>

#!/usr/bin/python
# -*- coding: UTF-8 -*-
if __name__ == '__main__':
    n = 0
p = raw_input('input a octal number:\n')
for i in range(len(p)):
        n = n * 8 + ord(p[i]) - ord('0')
print n
</pre>

 以上实例输出结果为：


```

input a octal number:
122
82

```

 [Python 100例](python-100-examples.md)

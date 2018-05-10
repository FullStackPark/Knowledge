Python 练习实例92
=============

 [Python 100例](python-100-examples.md)


 **题目：** 时间函数举例2。

 **程序分析：** 无。

**实例(Python 2.0+)**


 <pre>

#!/usr/bin/python
# -*- coding: UTF-8 -*-
if __name__ == '__main__':
    import time
start = time.time()
for i in range(3000):
        print i
end = time.time()
print end - start
</pre>

  以上实例输出结果为：


```

0
1
2
3
4
……

```

 [Python 100例](python-100-examples.md)

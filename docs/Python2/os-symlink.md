Python os.symlink() 方法
======================

 [![Python File(文件) 方法](../images/up.gif)
 Python OS 文件/目录方法](os-file-methods.html)


  ### 概述

 os.symlink() 方法用于创建一个软链接。

 ### 语法

 **symlink()** 方法语法格式如下：


```

os.symlink(src, dst)

```

 ### 参数

  * **src** -- 源地址。


 * **dst** -- 目标地址。


  ### 返回值

 该方法没有返回值。

 ### 实例

 以下实例演示了 symlink() 方法的使用：


```

#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

src = '/usr/bin/python'
", u"dst = '/tmp/python'

# 创建软链接
os.symlink(src, dst)

print "软链接创建成功"

```

 执行以上程序输出结果为：


```
软链接创建成功

```

 [![Python File(文件) 方法](../images/up.gif)
 Python OS 文件/目录方法](os-file-methods.html)

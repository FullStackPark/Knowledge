Python os.lstat() 方法
====================

 [![Python File(文件) 方法](../images/up.gif)
 Python OS 文件/目录方法](os-file-methods.html)


  ### 概述

 os.lstat() 方法用于类似 stat() 返回文件的信息,但是没有符号链接。在某些平台上，这是fstat的别名，例如 Windows。

 ### 语法

 **lstat()** 方法语法格式如下：


```

os.lstat(path)

```

 ### 参数

  * **path** -- 要返回信息的文件。


  ### 返回值

 返回文件信息。

 ### 实例

 以下实例演示了 lstat() 方法的使用：


```

#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, sys

# 打开文件
path = "/var/www/html/foo.txt"
fd = os.open( path, os.O_RDWR|os.O_CREAT )

# 关闭打开的文件
os.close( fd )

# 获取元组
info = os.lstat(path)

print "文件信息 :", info

# 获取文件 uid
print "文件 UID  :%d" % info.st_uid

# 获取文件 gid
print "文件 GID :%d" % info.st_gid

```

 执行以上程序输出结果为：


```

文件信息 : (33261, 3450178L, 103L, 1, 500, 500, 0L,
             1238866944, 1238866944, 1238948312)
文件 UID :500
文件 GID :500

```

 [![Python File(文件) 方法](../images/up.gif)
 Python OS 文件/目录方法](os-file-methods.html)

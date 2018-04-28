Python os.getcwd() 方法
=====================

 [![Python File(文件) 方法](../images/up.gif)
 Python OS 文件/目录方法](os-file-methods.html)


  ### 概述

 os.getcwd() 方法用于返回当前工作目录。

 ### 语法

 **getcwd()**方法语法格式如下：

 
```

os.getcwd()

```

 ### 参数

  * 无
  ### 返回值

 返回当前进程的工作目录。

 ### 实例

 以下实例演示了 getcwd() 方法的使用：

 
```

#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, sys

# 切换到 "/var/www/html" 目录
os.chdir("/var/www/html" )

# 打印当前目录
print "当前工作目录 : %s" % os.getcwd()

# 打开 "/tmp"
fd = os.open( "/tmp", os.O_RDONLY )

# 使用 os.fchdir() 方法修改目录
os.fchdir(fd)

# 打印当前目录
print "当前工作目录 : %s" % os.getcwd()

# 关闭文件
os.close( fd )

```

 执行以上程序输出结果为：

 
```

当前工作目录 : /var/www/html
当前工作目录 : /tmp

```

 [![Python File(文件) 方法](../images/up.gif)
 Python OS 文件/目录方法](os-file-methods.html)
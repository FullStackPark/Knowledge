Python os.makedev() 方法
======================

 [![Python File(文件) 方法](../images/up.gif)
 Python OS 文件/目录方法](os-file-methods.html)


  ### 概述

 os.makedev() 方法用于以major和minor设备号组成一个原始设备号。

 ### 语法

 **makedev()** 方法语法格式如下：


```

os.makedev(major, minor)

```

 ### 参数

  * **major** -- Major 设备号。


 * **minor** -- inor 设备号。


  ### 返回值

 返回设备号。

 ### 实例

 以下实例演示了 makedev() 方法的使用：


```

#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, sys

path = "/var/www/html/foo.txt"

# 获取元组
info = os.lstat(path)

# 获取 major 和 minor 设备号
major_dnum = os.major(info.st_dev)
minor_dnum = os.minor(info.st_dev)

print "Major 设备号 :", major_dnum
print "Minor 设备号 :", minor_dnum

# 生成设备号
dev_num = os.makedev(major_dnum, minor_dnum)
print "设备号 :", dev_num

```

 执行以上程序输出结果为：


```

Major 设备号 : 0
Minor 设备号 : 103
设备号 : 103

```

 [![Python File(文件) 方法](../images/up.gif)
 Python OS 文件/目录方法](os-file-methods.html)

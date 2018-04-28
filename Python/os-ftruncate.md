Python os.ftruncate() 方法
========================

 [![Python File(文件) 方法](../images/up.gif)
 Python OS 文件/目录方法](os-file-methods.html)


  ### 概述

 os.ftruncate() 裁剪文件描述符fd对应的文件, 它最大不能超过文件大小。

 Unix, Windows上可用。

 ### 语法

 **ftruncate()**方法语法格式如下：

 
```

os.ftruncate(fd, length)

```

 ### 参数

  * **fd** -- 文件的描述符。


 * **length** -- 要裁剪文件大小。


  ### 返回值

 该方法没有返回值。

 ### 实例

 以下实例演示了 ftruncate() 方法的使用：

 
```

#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, sys

# 打开文件
fd = os.open( "foo.txt", os.O_RDWR|os.O_CREAT )

# 写入字符串
os.write(fd, "This is test - This is test")

# 使用 ftruncate() 方法
os.ftruncate(fd, 10)

# 读取内容
os.lseek(fd, 0, 0)
str = os.read(fd, 100)
print "读取的字符串是 : ", str

# 关闭文件
os.close( fd)

print "关闭文件成功!!"

```

 执行以上程序输出结果为：

 
```

读取的字符串是 :  This is te
关闭文件成功!!

```

 [![Python File(文件) 方法](../images/up.gif)
 Python OS 文件/目录方法](os-file-methods.html)
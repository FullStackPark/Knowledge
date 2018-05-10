Python os.fpathconf() 方法
========================

 [![Python File(文件) 方法](../images/up.gif)
 Python OS 文件/目录方法](os-file-methods.html)


  ### 概述

 os.fpathconf() 方法用于返回一个打开的文件的系统配置信息。

 Unix上可用。

 ### 语法

 **fpathconf()** 方法语法格式如下：


```

os.fpathconf(fd, name)

```

 ### 参数

  * **fd** -- 打开的文件的描述符。


 * **name** -- 可选，和buffersize参数和Python内建的open函数一样，mode参数可以指定『r,w,a,r+,w+,a+,b』等，表示文件的是只读的还是可以读写的，以及打开文件是以二进制还是文本形式打开。这些参数和C语言中的<stdio.h>中fopen函数中指定的mode参数类似。


 * **bufsize** -- 检索的系统配置的值，它也许是一个定义系统值的字符串，这些名字在很多标准中指定（POSIX.1, Unix 95, Unix 98, 和其它）。一些平台也定义了一些额外的名字。这些名字在主操作系统上pathconf\_names的字典中。对于不在pathconf\_names中的配置变量，传递一个数字作为名字，也是可以接受的。


  ### 返回值

 返回一个打开的文件的系统配置信息。

 ### 实例

 以下实例演示了 fpathconf() 方法的使用：


```

#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, sys

# 打开文件
fd = os.open( "foo.txt", os.O_RDWR|os.O_CREAT )

print "%s" % os.pathconf_names

# 获取最大文件连接数
no = os.fpathconf(fd, 'PC_LINK_MAX')
print "文件最大连接数为 :%d" % no

# 获取文件名最大长度
no = os.fpathconf(fd, 'PC_NAME_MAX')
print "文件名最大长度为 :%d" % no

# 关闭文件
os.close( fd )

print "关闭文件成功!!"

```

 执行以上程序输出结果为：


```

{'PC_MAX_INPUT': 2, 'PC_VDISABLE': 8, 'PC_SYNC_IO': 9,
", u"'PC_SOCK_MAXBUF': 12, 'PC_NAME_MAX': 3, 'PC_MAX_CANON': 1,
", u"'PC_PRIO_IO': 11, 'PC_CHOWN_RESTRICTED': 6, 'PC_ASYNC_IO': 10,
", u"'PC_NO_TRUNC': 7, 'PC_FILESIZEBITS': 13, 'PC_LINK_MAX': 0,
", u"'PC_PIPE_BUF': 5, 'PC_PATH_MAX': 4}

文件最大连接数为 :127
文件名最大长度为 :255
Closed the file successfully!!

```

 [![Python File(文件) 方法](../images/up.gif)
 Python OS 文件/目录方法](os-file-methods.html)

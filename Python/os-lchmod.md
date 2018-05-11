Python os.lchmod() 方法
=====================

 [![Python File(文件) 方法](../images/up.gif)
 Python OS 文件/目录方法](os-file-methods.html)


  ### 概述

 os.lchmod() 方法用于修改连接文件权限。

 只支持在 Unix 下使用。

 ### 语法

 **lchmod()** 方法语法格式如下：


```

os.lchmod(path, mode)

```

 ### 参数

  * **path** -- 设置标记的文件路径


 * **mode** -- 可以是以下一个或多个组成，多个使用 "|" 隔开：


	 + **stat.S\_ISUID:**设置 UID 位


	 + **stat.S\_ISGID:** 设置组 ID 位


	 + **stat.S\_ENFMT:** 系统文件锁定的执法行动


	 + **stat.S\_ISVTX:** 在执行之后保存文字和图片


	 + **stat.S\_IREAD:** 对于拥有者读的权限


	 + **stat.S\_IWRITE:** 对于拥有者写的权限


	 + **stat.S\_IEXEC:** 对于拥有者执行的权限


	 + **stat.S\_IRWXU:**对于拥有者读、写、执行的权限


	 + **stat.S\_IRUSR:** 对于拥有者读的权限


	 + **stat.S\_IWUSR:** 对于拥有者写的权限


	 + **stat.S\_IXUSR:** 对于拥有者执行的权限


	 + **stat.S\_IRWXG:** 对于同组的人读写执行的权限


	 + **stat.S\_IRGRP:** 对于同组读的权限


	 + **stat.S\_IWGRP:**对于同组写的权限


	 + **stat.S\_IXGRP:** 对于同组执行的权限


	 + **stat.S\_IRWXO:** 对于其他组读写执行的权限


	 + **stat.S\_IROTH:** 对于其他组读的权限


	 + **stat.S\_IWOTH:** 对于其他组写的权限


	 + **stat.S\_IXOTH:**对于其他组执行的权限



  ### 返回值

 该方法没有返回值。

 ### 实例

 以下实例演示了 lchmod() 方法的使用：


```

#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, sys

# 打开文件
path = "/var/www/html/foo.txt"
fd = os.open( path, os.O_RDWR|os.O_CREAT )

# 关闭文件
os.close( fd )

# 修改文件权限
# 设置文件可以通过组执行
os.lchmod( path, stat.S_IXGRP)

# 设置文件可以被其他用户写入
os.lchmod("/tmp/foo.txt", stat.S_IWOTH)

print "修改权限成功!!"

```

 执行以上程序输出结果为：


```

修改权限成功!!

```

 [![Python File(文件) 方法](../images/up.gif)
 Python OS 文件/目录方法](os-file-methods.html)

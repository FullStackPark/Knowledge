Python os.chmod() 方法
====================

 [![Python File(文件) 方法](../images/up.gif)
 Python OS 文件/目录方法](os-file-methods.html)


  ### 概述

 os.chmod() 方法用于更改文件或目录的权限。

 ### 语法

 **chmod()**方法语法格式如下：

 
```

os.chmod(path, mode)

```

 ### 参数

  * **path** -- 文件名路径或目录路径。 


 * **flags** -- 可用以下选项按位或操作生成， 目录的读权限表示可以获取目录里文件名列表， ，执行权限表示可以把工作目录切换到此目录 ，删除添加目录里的文件必须同时有写和执行权限 ，文件权限以用户id->组id->其它顺序检验,最先匹配的允许或禁止权限被应用。 

 
	 + **stat.S\_IXOTH:** 其他用户有执行权0o001
	
 * **stat.S\_IWOTH:** 其他用户有写权限0o002
 * **stat.S\_IROTH:** 其他用户有读权限0o004
 * **stat.S\_IRWXO:** 其他用户有全部权限(权限掩码)0o007
 * **stat.S\_IXGRP:** 组用户有执行权限0o010
 * **stat.S\_IWGRP:** 组用户有写权限0o020
 * **stat.S\_IRGRP:** 组用户有读权限0o040
 * **stat.S\_IRWXG:** 组用户有全部权限(权限掩码)0o070
 * **stat.S\_IXUSR:** 拥有者具有执行权限0o100
 * **stat.S\_IWUSR:** 拥有者具有写权限0o200
 * **stat.S\_IRUSR:** 拥有者具有读权限0o400
 * **stat.S\_IRWXU:** 拥有者有全部权限(权限掩码)0o700
 * **stat.S\_ISVTX:** 目录里文件目录只有拥有者才可删除更改0o1000
 * **stat.S\_ISGID:** 执行此文件其进程有效组为文件所在组0o2000
 * **stat.S\_ISUID:** 执行此文件其进程有效用户为文件所有者0o4000
 * **stat.S\_IREAD:** windows下设为只读
 * **stat.S\_IWRITE:** windows下取消只读
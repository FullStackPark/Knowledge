Python os.walk() 方法
===================

 [![Python File(文件) 方法](../images/up.gif)
 Python OS 文件/目录方法](os-file-methods.html)


  ### 概述

 os.walk() 方法用于通过在目录树中游走输出在目录中的文件名，向上或者向下。

 os.walk() 方法是一个简单易用的文件、目录遍历器，可以帮助我们高效的处理文件、目录方面的事情。

 在Unix，Windows中有效。

 ### 语法

 **walk()** 方法语法格式如下：


```

os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])

```

 ### 参数

 *  **top** -- 是你所要便利的目录的地址, 返回的是一个三元组(root,dirs,files)。


	 + root 所指的是当前正在遍历的这个文件夹的本身的地址
	 + dirs 是一个 list ，内容是该文件夹中所有的目录的名字(不包括子目录)
	 + files 同样是 list , 内容是该文件夹中所有的文件(不包括子目录)

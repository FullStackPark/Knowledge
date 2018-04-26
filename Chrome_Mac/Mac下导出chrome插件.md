chrome最强大的功能之一就是插件，有时候需要给小伙伴们共享一些插件，所以需要将自己chrome中的插件打包，在mac下打包插件还是挺费劲的，在此记录。

* 打开chrome的扩展程序，找到要导出的插件，拷贝下插件的ID。

![这里写图片描述](https://img-blog.csdn.net/20160329175425100)

* 进入~/Library/Application   

    Support/Google/Chrome/Default/Extensions/{ID值}下，执行：

```hljs
cd ~/Library/Application\ Support/Google/Chrome/Default/Extensions/egkcjgapmgioadbkhaciondahbjggnhj
```

* 1

该目录下可以看到插件的文件夹，是以版本号命名的，   
![这里写图片描述](https://img-blog.csdn.net/20160329175952055)

* 注意可能会有很多版本，cd进入到自己想打包的文件夹，执行：

```hljs
cd 1.0.2_0
```

* 1

* 执行pwd，复制当前的整个路径，一会需要填写到chrome打包扩展程序中。

![这里写图片描述](https://img-blog.csdn.net/20160329180438026)

* 在chrome的扩展程序中点击打包扩展程序，把刚刚复制的全路径拷贝到扩展程序根目录中。

![这里写图片描述](https://img-blog.csdn.net/20160329180631464)

* 点击打包扩展程序，把弹出的打包结果中的扩展程序路径复制下来，也就是.crx结尾的那段。

![这里写图片描述](https://img-blog.csdn.net/20160329180837209)

* 接下来就可以到打包的路径下找到插件，发送给小伙伴了。

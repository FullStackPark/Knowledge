Python CGI编程
============

  什么是CGI
------

 CGI 目前由NCSA维护，NCSA定义CGI如下：

 CGI(Common Gateway Interface),通用网关接口,它是一段程序,运行在服务器上如：HTTP服务器，提供同客户端HTML页面的接口。

 网页浏览
----

 为了更好的了解CGI是如何工作的，我们可以从在网页上点击一个链接或URL的流程：

  *  1、使用你的浏览器访问URL并连接到HTTP web 服务器。
*  2、Web服务器接收到请求信息后会解析URL，并查找访问的文件在服务器上是否存在，如果存在返回文件的内容，否则返回错误信息。
*  3、浏览器从服务器上接收信息，并显示接收的文件或者错误信息。
 CGI程序可以是Python脚本，PERL脚本，SHELL脚本，C或者C++程序等。

   CGI架构图
-------

 ![cgiarch](http://www.runoob.com/wp-content/uploads/2013/11/Cgi01.png)


  Web服务器支持及配置
-----------

 在你进行CGI编程前，确保您的Web服务器支持CGI及已经配置了CGI的处理程序。

 Apache 支持CGI 配置：

 设置好CGI目录：

 
```

ScriptAlias /cgi-bin/ /var/www/cgi-bin/

```

  所有的HTTP服务器执行CGI程序都保存在一个预先配置的目录。这个目录被称为CGI目录，并按照惯例，它被命名为/var/www/cgi-bin目录。

 CGI文件的扩展名为.cgi，python也可以使用.py扩展名。

 默认情况下，Linux服务器配置运行的cgi-bin目录中为/var/www。

 如果你想指定其他运行 CGI 脚本的目录，可以修改 httpd.conf 配置文件，如下所示：

 
```
<Directory "/var/www/cgi-bin">
   AllowOverride None
   Options +ExecCGI
   Order allow,deny
   Allow from all
</Directory>
```
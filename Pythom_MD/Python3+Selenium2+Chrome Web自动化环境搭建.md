当一件事情要做两次以上，那么你就需要为它写个自动化脚本，本系列文章讲的就是如何执行Web自动化。一般Web自动化测试环境主要有三部分组成：Python、Selenium和浏览器。

* Pycharm是一个用于python语言编程的开发环境，分为普通版和专业版两款。正常学习只需要下载免费的普通版，但是要用Django制作网页只能选择安装专业版本。

* Selenium是一款关于Web的自动化测试工具，分为selenium 1、

    selenium 2和selenium 3三个版本。这里我们使用selenium2作为我们的安装版本。selenium 2是selenium 1与WebDiver的集合，比selenium 3更加稳定。

* Chrome是Google开发的网页浏览器，它的功能十分强大，有各种各样的小插件。当然这里的浏览器可以选择自己喜欢的，chrome只是一个举例。

![Python3+Selenium2+Chrome Web自动化环境搭建](http://p3.pstatp.com/large/4e620001e985adb5d699)

环境的版本信息：

Windows 10、Python 3.6.3、Pycharm professional、selenium-3.8.0、Chrome 62.0.3202.75、chromedriver 2.33

安装步骤：

1.python版本安装：

点击链接：https://www.python.org/downloads/

选择Python 3以上的版本下载，下载完成后直接安装并配置环境信息

![Python3+Selenium2+Chrome Web自动化环境搭建](http://p1.pstatp.com/large/4e5f0003c3b369053cba)

2.Pycharrm安装：

点击链接：https://www.jetbrains.com/pycharm/download/#section=windows

选择普通版（免费）或者专业版（付费）两者中的任意一种下载，点击安装

![Python3+Selenium2+Chrome Web自动化环境搭建](http://p1.pstatp.com/large/4e5f0003c3b1ce2f4264)

3.Selenium安装：

3.1 直接使用pip安装

在cmd中执行pip install selenium

3.2 直接下载安装包安装

点击链接：https://pypi.python.org/pypi/selenium#downloads

选择file中的selenium-3.8.0.tar.gz文件，解压缩后cmd进入该目录，

执行python setup.py install命令

![Python3+Selenium2+Chrome Web自动化环境搭建](http://p1.pstatp.com/large/4e5d0003d2fb4addcf30)

4.Chrome安装：

点击链接：https://www.google.com/chrome/browser/desktop/index.html

直接在google官网直接下载安装浏览器

5.ChromeWebdiver安装：

点击链接：https://chromedriver.storage.googleapis.com/index.html?path=2.33/

选择与chrome匹配的chromediver（这里是2.33版本），下载后解压缩，

chromedriver将占用9515 端口，需要把它放到chrome的安装目录下...GoogleChromeApplication,然后设置path环境变量或者将chromedriver.exe放在python的安装目录

![Python3+Selenium2+Chrome Web自动化环境搭建](http://p3.pstatp.com/large/4e5e0003c32cf20e6767)

6.调试web

执行以下命令，能够直接打开百度界面，如若失败，则可能安装错误，请再次排查。

<pre>
fromseleniumimportwebdriverbrowser=webdriver.Chrome()browser.get(http://www.baidu.com)
</pre>

成功样板：

![Python3+Selenium2+Chrome Web自动化环境搭建](http://p3.pstatp.com/large/4e5f0003c3b216c37bbb)

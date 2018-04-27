Mac OSX本身系统自带Python2.7，但 **不建议直接使用、删除和更改** ，因为可能有些程序是需要依赖系统自带的python 2.\*，盲目修改后可能会导致系统产生未知错误。

所以建议在 **不修改系统的python条件下** 搭建Python双版本环境。在给大家分享之前呢，小编推荐一下一个挺不错的交流宝地，里面都是一群热爱并在学习Python的小伙伴们，大几千了吧，各种各样的人群都有，特别喜欢看到这种大家一起交流解决难题的氛围，群资料也上传了好多，各种大牛解决小白的问题，这个Python群：330637182 欢迎大家进来一起交流讨论，一起进步，尽早掌握这门Python语言。

![神级程序员把Python2和3当中最常见的问题都收集了！很全面的总结](http://p9.pstatp.com/large/432f000466e52aaae3e5)

Mac OSX在系统自带的python之外，可以 **安装Python2.7和Python3.5/3.6版本** ，并且双版本兼容。

本文下方，防止原文链接失效】

在参考的安装流程中，我发现了一些问题并进行了解决，列出问题及解决方法如下：

1.Python2.7安装后，按原文博主的安装方法无法修改系统默认的Python命令为自己安装Python路径和版本：

解决方法：

打开系统配置文件：

<pre>
vi ~/.bash_profile
</pre>

添加入自己的安装的Python2.7的路径地址：

<pre>
PATH="/usr/local/Cellar/python/2.7.14/bin:${PATH}"
</pre>

让PATH变量生效：

<pre>
source ~/.bash_profile
</pre>

我们看到，命令行输入 `which python2.7` 时，路径地址改变，不再是系统默认地址：

![神级程序员把Python2和3当中最常见的问题都收集了！很全面的总结](http://p3.pstatp.com/large/43340001754ecbcb0ccc)

python2.7

我们前往路径地址修改添加 `python`

文件：（复制一个python2.7然后重命名为python即可）

![神级程序员把Python2和3当中最常见的问题都收集了！很全面的总结](http://p3.pstatp.com/large/433200018bfd3d77073b)

前往路径地址修改添加`python`文件

这样默认的python即修改为我们所安装的python2.7版本，而非系统自带的python路径，命令行输入 `which python`

查看：

![神级程序员把Python2和3当中最常见的问题都收集了！很全面的总结](http://p1.pstatp.com/large/4331000195d723111a1b)

查看所安装的python2.7版本

这样，我们就将系统的默认python命令链接到了我们所安装的python目录下，而非系统自带的python路径。

2.Python2.7和Python3.6安装后，pip2和pip3下载的包仍在Mac OSX系统自带的Python2.7的包目录下，而非Python2.7和Python3.6的安装目录：

问题图示如下：

pip的version都是系统自带python的包下载路径：

![神级程序员把Python2和3当中最常见的问题都收集了！很全面的总结](http://p3.pstatp.com/large/43340001754d315bff43)

pip的version都是系统自带python的路径

pip的路径都是系统自带python的路径，而非我们的安装路径：

![神级程序员把Python2和3当中最常见的问题都收集了！很全面的总结](http://p1.pstatp.com/large/433500016b946106fab5)

python的路径

解决方法：

打开系统配置文件：

<pre>
vi ~/.bash_profile
</pre>

添加入自己的安装的Python2.7和Python3.6的路径地址：

![神级程序员把Python2和3当中最常见的问题都收集了！很全面的总结](http://p1.pstatp.com/large/432f0004674c32a76545)

让PATH变量生效：

<pre>
source ~/.bash_profile
</pre>

我们看到，命令行输入 `which pip` 和 `pip --version` 时，pip的路径地址改变，pip下载的包的地址也改变，不再是系统默认地址：

![神级程序员把Python2和3当中最常见的问题都收集了！很全面的总结](http://p1.pstatp.com/large/43310001966024fccb6d)

pip版本显示

这样，即可保证使用pip下载的包路径正确，且和我们所安装的两个版本python分别对应。

3.Pip总是不能正常下载包，安装模块包ConnectTimeoutError错误：

解决方法：

我们在使用pip无法正常下载包的时候可以使用国内镜像服务，如用豆瓣的源下载安装 `selenium` 包：

<pre>
pip install selenium -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
</pre>

如果是要给python3下载依赖，注意pip和python版本对应，同理：

<pre>
pip3 install selenium -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
</pre>

这样，即可正常的使用pip来下载安装包了。

安装流程

主要就这几个步骤而已，不会太困难的（或许有些你本来就装好了）

Step 2 安装套件管理工具Homebrew

Step 4 设定路径$PATH（不跟系统Python 打架）

Step 5 完成啰！确认安装结果～

Step 1 安装Xcode

可以到App Store搜寻Xcode并安装安装好了之后就把Xcode打开～第一次开启的时候会需要同意他的License Agreement之类的东西。然后到terminal输入来安装Xcode command line tool：

![神级程序员把Python2和3当中最常见的问题都收集了！很全面的总结](http://p3.pstatp.com/large/43300003d5ebc2731650)

<pre>
xcode-select--install
</pre>

安装Xcode 就到此结束啰，要进入下一个步骤了！

Step 2安装套件管理工具： Homebrew

可以到官网或是在terminal 里贴上：

![神级程序员把Python2和3当中最常见的问题都收集了！很全面的总结](http://p1.pstatp.com/large/43330001837c4a8b6eb6)

<pre>
ruby-e"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
</pre>

安装好后可以跑一下

<pre>
brew doctor
</pre>

如果出现

<pre>
Your system is ready to brew.
</pre>

代表万事OK，那如果有Warning的话，也不用太担心，可以按照里面的步骤去修正就好啰！

如果有出现Warning的话，虽然会在上面看到一句

<pre>
If everything you use Homebrew for is working fine: please don't worry and just ignore them.
</pre>

不过还是建议大家把东西装好，才不会到时候忘记自己到底什么东西还没设定好。

Step 3 安装Python

接下来要正式进入安装Python的步骤了！

首先，输入

<pre>
python --version
</pre>

天哪！都还没开始装Python，电脑里面怎么已经有了？

这是Mac系统要使用的Python，所以平常没适不要去乱动比较好唷！

所以现在我们要用homebrew来安装平常可以（乱搞？）使用的Python。

利用homebrew 搜寻Python

<pre>
brew search python
</pre>

这时候，会看到python和python3。

因为我已经装了，所以旁边会写(installed)。要安装Python啰！

<pre>
brew install python
</pre>

这样就开始安装了。

装完之后在输入

<pre>
brew install python3
</pre>

在安装的时候，Python 会被安装在

![神级程序员把Python2和3当中最常见的问题都收集了！很全面的总结](http://p9.pstatp.com/large/433200018c78b247476a)

<pre>
/usr/local/Cellar
</pre>

那就来看看这个资料夹吧

<pre>
open /usr/local/Cellar/
</pre>

![神级程序员把Python2和3当中最常见的问题都收集了！很全面的总结](http://p3.pstatp.com/large/4334000175b5a7504a78)

就可以看到你正在安装的Python出现了！

除了Python之外，也有可能会装一些其他的东西，例如sqlite。

总之，不用太担心，homebrew会自己搞定。

（因为我装了很多哩哩抠抠，所以你的资料夹里可能不会有这么多东西）

Step 4 设定路径$PATH（不跟系统Python 打架）

什么是路径$PATH 呢？

还记得我们在装Python的时候，输入了brew，

系统就自动会知道要开始跑homebrew。

系统到底怎么知道我们的brew在哪里？

这就是$PATH的用途了！

<pre>
echo $PATH
</pre>

接下来就会看到一串类似这样的东西

<pre>
/usr/bin**:**/bin**:**/usr/sbin**:**/sbin**:**/usr/local/bin
</pre>

分号(:)是 **分隔** 的意思

所以当你在terminal里面输入brew时

系统就会开始从/usr/bin找起

如果在/usr/bin里面找不到的话

就会往下一个/bin去搜寻，以此类推

现在，我们回到资料夹去看

brew其实就在/usr/local/bin里面！

![神级程序员把Python2和3当中最常见的问题都收集了！很全面的总结](http://p3.pstatp.com/large/433500016c16edd2cb9e)

所以现在的问题就是，系统在/usr/bin里面也有一份Python

现在我们在/usr/local/Cellar里面也装了Python

这样在terminal打上python指令时，谁会被开启呢？

因为路径有 **顺序** ，所以它会先找到系统的Python

现在就要来解决这个问题

<pre>
sudo emacs/etc/paths
</pre>

sudo让我们取得管理员权限

用emacs这个程式编辑路径档案

terminal会要求输入密码

（就是平常装东西也需要输入的密码）现在要把/usr/local/bin移到上面去control + k：把一行字剪下来control + y：把字贴上control + x + s：存档control + x + c：关掉emacs

![神级程序员把Python2和3当中最常见的问题都收集了！很全面的总结](http://p1.pstatp.com/large/43300003d5ec26daa73b)

![神级程序员把Python2和3当中最常见的问题都收集了！很全面的总结](http://p1.pstatp.com/large/43330001837efb21896e)

这时，再打一次

<pre>
echo $PATH
</pre>

为什么没有变！？

因为要 **开一个新的terminal** 才会更新唷！

开新式窗后再输入一次就会看到我们刚刚修改的结果了。

Step 5 完成啰！确认安装结果～

这样就完成啰！

其实python3本身比较不会跟其他人打架

因为他就是独立的python3

所以我们主要是要确认是不是读到我们用brew装的python

<pre>
which python
</pre>

这时候看到

<pre>
/usr/local/bin/python
</pre>

再来看看python3 吧

<pre>
which python3
</pre>

应该会是

<pre>
/usr/local/bin/python3
</pre>

就代表读到刚刚装好的python啰！

当然如果你要跑系统本身的python

（应该是用不到啦～）

就输入

<pre>
/usr/bin/python
</pre>

总之就是…大功告成啰！

谢谢阅读！原文链接：

![神级程序员把Python2和3当中最常见的问题都收集了！很全面的总结](http://p3.pstatp.com/large/433200018cb7b7d3bf4e)

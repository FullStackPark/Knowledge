# Python 数据分析

> 本教程主要是针对使用Python对数据进行处理的一门课程。

比较好的课程介绍，[基于卷积神经网络的视觉识别](http://cs231n.github.io/) [斯坦福大学网站](http://vision.stanford.edu/teaching/cs231n/)

> 前置条件：

> [Python3](http://www.runoob.com/python/python-tutorial.html) 

> [MongoDB](http://www.runoob.com/mongodb/mongodb-tutorial.html)

> [MySQL](http://www.runoob.com/mysql/mysql-tutorial.html)

> [Navicat 12 Windows 版本安装和简单使用](https://www.jianshu.com/p/5f693b4c9468)

> [Navicat 12 Mac 版本 xclient.info](http://xclient.info/s/navicat-for-mysql.html?t=607f34623d47ed1b8125fc5bd7515a28c1cd4f41#versions)
> 
>> 讲在前面
>> 
>> 找偏门的包到，lfd的网址，里面有很多python的资源和库与工具
http://www.lfd.uci.edu/~gohlke/pythonlibs/
在上面的网址中找到python_igraph去下载具体的python对应版本和是32位还是64位的，我这里下载的的python27 win64的
python_igraph-0.7.1.post6-cp27-none-win_amd64.whl
利用pip 安装whl文件
命令格式就是：pip install 文件名.whl
但是避免出错的前提是，打开cmd以后，要cd进入你存放的该whl文件的解压后的目录下在用pip进行安装。 
*感谢叶作霖的贡献*

- [PyCharm 安装和使用](http://yezuolin.com/2018/05/Pycharm/)
- [MongoDB 安装和使用](http://yezuolin.com/2018/05/MongoDB/)
- [爬虫的相关的视频- 密码: 3axh](https://pan.baidu.com/s/1UdOfqGgTIhR9fGAE_58AoA)


## 第一章 Python 入门

> “数据分析是Python的杀手锏"

### 1.1 课前准备

[Python基础教程](http://www.runoob.com/python/python-tutorial.html)

[Python Numpy Tutorial](http://cs231n.github.io/python-numpy-tutorial/)

[CS228 Python Tutorial](https://github.com/kuleshov/cs228-material/blob/master/tutorials/python/cs228-python-tutorial.ipynb)

[Navicat 12 Windows 版本安装和简单使用](https://www.jianshu.com/p/5f693b4c9468)

[Navicat 12 Mac 版本 xclient.info](http://xclient.info/s/navicat-for-mysql.html?t=607f34623d47ed1b8125fc5bd7515a28c1cd4f41#versions)

[Jupyter使用](https://zhuanlan.zhihu.com/p/33105153)


### 1.2 主要内容

* 安装Python与环境配置
* Anaconda安装和使用
* 常用数据分析库Numpy、Scipy、Pandas和matplotlib 安装和简介
* 常用高级数据分析库nltk、igraph和scikit-learn介绍
* Python2和Python3区别简介


### 1.3 安装Python与环境配置

* 安装Python 2.7.12

    * https://www.python.org/downloads/
    * Mac OS X：自带python 2.7或者brew install  python

* 环境变量配置

    * Windows
    (cmd输入)path=%path%;C:\Python 或 右键计算机->属性->高级系统设置->系统属性->环境 变量->双击path ->添加“; C:\Python”安装路径

    * Linux：export PATH="$PATH:/usr/local/bin/python”

### 1.4 安装pip

* [Pip](https://pip.pypa.io/en/stable/installing/) 已经在Python 2 >=2.7.9或Python 3 >=3.4中自带，但需要更新。

    * Linux或者OS X：

        pip install -U pip

    * Windows（cmd输入）：

        python -m pip install -U pip

    * 安装大部分python库：

        pip install “some software”

        pip uninstall ”some software“



### 1.5 Anaconda安装和使用

![Anacoda](https://ws1.sinaimg.cn/large/006tKfTcly1fsasniu1sxj30f306hdh1.jpg)

* Anaconda安装

    - 下载：https://www.continuum.io/downloads
    - 命令行创建和启动环境：


        ```
        conda create --name py27 python=2.7

        activate py27

        ```

    - 列出安装packages：

        conda list

    - 安装package：

        ```conda install numpy（conda install 会安装或更新库所依赖的各种库，pip install不会更新）```

* Anaconda使用

    - Jupyter QtConsole or IPython（命令行式）

    ```

    conda update ipython 或 如需本地安装pip install  ipython

    ```

    - Jupyter Notebook（Web）：

    如需本地安装：```pip install jupyter```

    - spyder（IDE，如需本地安装推荐Pycharm）


### 1.6 常用数据分析库Numpy、Scipy、Pandas和matplotlib安装和简介

#### 安装数据分析库

    - pip install numpy
    - pip install scipy
    - pip install pandas
    - pip install matplotlib

#### [Numpy](http://www.numpy.org/)

    - [中文资料](Python之numpy的基本使用.md)
    - 提供常用的数值数组、矩阵等函数
    
    - 优点：
    是基于向量化的运算
    进行数值运算时Numpy数组比list效率高

    ![](https://ws4.sinaimg.cn/large/006tKfTcly1fsau9a3yc5j30cc056jrn.jpg)

#### [Scipy](https://www.scipy.org/)

    ![](https://ws2.sinaimg.cn/large/006tNc79ly1fsb4tlhldvj30fc09uq5d.jpg)
    
    - [简易教程](Python之SciPy快速入门教程.md)
    - [SciPyLectureNotes 中文版](https://wizardforcel.gitbooks.io/scipy-lecture-notes/content/0.html)
    - 是一种使用NumPy来做高等数学、信号处理、 优化、统计的扩展包
    - Linear Algebra (scipy.linalg) 线性代数
    - Statistics (scipy.stats) 统计
    - Spatial data structures and algorithms (scipy.spatial) 空间数据结构和算法

#### [Pandas](https://pandas.pydata.org/)

    [10分钟入门系列](http://codingpy.com/article/a-quick-intro-to-pandas/)

    ![](https://ws1.sinaimg.cn/large/006tNc79ly1fsb4wmazxej30y20getap.jpg)
    ![](https://ws1.sinaimg.cn/large/006tNc79ly1fsb4yl7eu0j30sa0b0wgn.jpg)
    ![](https://ws2.sinaimg.cn/large/006tNc79ly1fsb4yv0ybbj30gw0byq4q.jpg)

    * 是一种构建于Numpy的高级数据结构和精巧 工具，快速简单的处理数据。
        * 支持自动或明确的数据对齐的带有标签轴的数据结构。
        * 整合的时间序列功能。
        * 以相同的数据结构来处理时间序列和非时间序列。
        * 支持传递元数据（坐标轴标签）的算术运算和缩减。
        * 灵活处理丢失数据。
        * 在常用的基于数据的数据库（例如基于SQL）中的合并 和其它关系操作。
    * 数据结构：Series和DataFrame

#### [matplotlib Python绘图库](https://matplotlib.org/)

![](https://ws2.sinaimg.cn/large/006tNc79ly1fsb50fk4sij30ji0g63zh.jpg)
![](https://ws3.sinaimg.cn/large/006tNc79ly1fsb50m8yhvj30jw0got9s.jpg)

### 1.7 常用高级数据分析库nltk、igraph和scikit-learn介绍

#### [nltk](https://www.nltk.org/)

[中文入门资料](http://hao.jobbole.com/nltk/)

NLTK是一个高效的Python构建的平台，用来处理人类自然语言数据。它提供了易于使用的接口，通过这些接口可以访问[超过50个语料库和词汇资源](http://nltk.org/nltk_data/)（如WordNet），还有一套用于分类、标记化、词干标记、解析和语义推理的文本处理库，以及工业级NLP库的封装器和一个活跃的[讨论论坛](http://groups.google.com/group/nltk-users)。

统计语言学话题方面的手动编程指南加上全面的API文档，使得NLTK非常适用于语言学家、工程师、学生、教育家、研究人员以及行业用户等人群。NLTK可以在Windows、Mac OS X以及Linux系统上使用。最好的一点是，NLTK是一个免费、开源的社区驱动的项目。

NLTK被称为“一个使用Python开发的用于统计语言学的教学和研究的有利工具”和“一个自然语言处理的高效库”。

[Python自然语言处理](http://www.nltk.org/book/)提供了一个自然语言处理的实例介绍。这个介绍是由NLTK的创建者所写的，它引导读者通过编写Python程序，使用语料库，分类文本，分析语言结构等基本过程来理解NLTK的使用。 这本书正在为Python3版本和NLTK3版本更新内容。（Python2版本仍然可以在http://nltk.org/book_1ed获得。）


    - 自然语言处理工具包（Natural Language Toolkit）
        * 安装：pip install -U nltk
        * 引入：import nltk
        * 下载预料库：nltk.download()
    - 应用：
        * 文本提取
        * 词汇切分
        * 词频分析
        * 词袋模型
        * 情感分析


#### [igraph](http://igraph.org/python/)

![](https://ws1.sinaimg.cn/large/006tNc79ly1fsb59cpyf6j30ts0b6q48.jpg)
![](https://ws4.sinaimg.cn/large/006tNc79ly1fsb59jhk66j309i09qjs6.jpg)

igraph是免费的复杂网络（graphs）处理包，可以处理百万级节点的网络（取决于机器内存）。igraph提供了R和C语言程序包，以及Python和Ruby语言扩展，它包括的功能包括：
    - 网络可视化
    - 传统图论算法：最小生成树，网络流等
    - 复杂网络处理算法：随机网络模型，网络处理（k-cores, PageRank, betweenness,    - motifs），社区发现算法等
    - 图计算和社交网络分析

    - 安装

      * pip install -U python-igraph
      * conda install -c marufr python-igraph=0.7.1.post6  

#### [Scikit-learn](http://scikit-learn.org/stable/index.html)

[中文资料](http://sklearn.apachecn.org/cn/0.19.0/)

![](https://ws1.sinaimg.cn/large/006tNc79ly1fsb5axmhw1j30ks0cyac6.jpg)

 * Scikit-learn是建立在Scipy之上的一个用于机器 学习的Python模块。

 * 安装：pip install -U scikit-learn / conda install scikit-learn

### 1.8 Python2和Python3区别简介

- print()函数
- 整除：3/2=1.5(python3);3/2=1(python2)
- 支持Unicode (utf-8) 字符串
- xrange()函数被集成在range()函数中
- raising exceptions：raise IOError("file error")
- Handling exceptions：except NameError as e
- 取消.next()
- For 循环变量和全局命名空间泄漏: [... for var in (item1, item2, ...)]
- 比较不可排序内容抛出错误
- 通过input()解析用户输入：把用户的输入存储为一个 str 对象
- 返回可迭代对象，而不是列表
- 使用  future  模块支持python3：division、print_function


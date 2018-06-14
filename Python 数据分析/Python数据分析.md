# Python 数据分析

> 本教程主要是针对使用Python对数据进行处理的一门课程。


## 第一章 Python 入门 

> “数据分析是Python的杀手锏"

### 1.1 课前准备

[Python基础教程](http://www.runoob.com/python/python-tutorial.html)

### 1.2 主要内容

* 安装Python与环境配置
* Anaconda安装和使用
* 常用数据分析库Numpy、Scipy、Pandas和
* matplotlib安装和简介
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

* Anaconda安装

    - 下载：https://www.continuum.io/downloads
    - 命令行创建和启动环境：

        
        ```
        conda create --name py27 python=2.7

        activate py27
        ```

    - 列出安装packages：conda list
    - 安装package：conda install numpy（conda install 会安装或更新库所依赖的各种库，pip install不会更新）

* Anaconda使用

    - Jupyter QtConsole or IPython（命令行式）
    
    ```
    conda update ipython 或 如需本地安装pip install  ipython
    ```

    - Jupyter Notebook（Web）：
    
    如需本地安装：pip install jupyter
    
    - spyder（IDE，如需本地安装推荐Pycharm）


### 常用数据分析库Numpy、Scipy、Pandas和
### matplotlib安装和简介
### 常用高级数据分析库nltk、igraph和scikit-learn介绍
### Python2和Python3区别简介


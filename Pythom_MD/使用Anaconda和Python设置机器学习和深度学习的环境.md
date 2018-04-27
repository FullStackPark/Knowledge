# 前言

在某些平台上安装Python机器学习环境可能很困难。

Python本身必须先安装，然后安装很多软件包，这对初学者来说可能会造成混淆。

在本教程中，您将了解如何使用Anaconda设置Python机器学习开发环境。

完成本教程后，您将拥有一个可用的Python环境，以开始学习，练习和开发机器学习和深度学习软件。

本教程适用于Windows，Mac OS X和Linux平台。 我将在OS X上演示它们，以便您可以看到一些mac对话框和文件扩展名。

# 概要

在本教程中，我们将介绍以下步骤：

* 下载Anaconda

* 安装Anaconda

* 启动并更新Anaconda

* 更新scikit-learn库

* 安装深度学习库

# 下载Anaconda

在这一步中，我们将为您的平台下载Anaconda Python软件包。

Anaconda是一个免费且易于使用的科学Python环境。

* 访问Anaconda主页https://www.anaconda.com/。

* 从菜单中点击“Anaconda”，然后点击“下载”进入下载页面。

* 选择适合您的平台的下载（Windows，OSX或Linux）：

选择Python 3.6

选择图形安装程序

![使用Anaconda和Python设置机器学习和深度学习的环境](http://p3.pstatp.com/large/66bf000239a4e21e091c)

为您的平台选择Anaconda下载

这会将Anaconda Python软件包下载到您的工作站。

我在OS X上，所以我选择了OS X版本。 该文件大约是595 MB。

你应该有一个名字如下的文件：

Anaconda3-5.1.0-MacOSX-x86_64.pkg

# 安装Anaconda

在这一步中，我们将在您的系统上安装Anaconda Python软件。

此步骤假定您有足够的管理权限在系统上安装软件。

* 双击下载的文件。

* 按照安装向导。

安装快速而流畅，应该没有棘手的问题或困难点。

![使用Anaconda和Python设置机器学习和深度学习的环境](http://p3.pstatp.com/large/66c10001383f53f3bc78)

安装应该少于10分钟，并占用硬盘驱动器上超过1 GB的空间。

# 启动并更新Anaconda

在这一步中，我们将确认您的Anaconda Python环境是最新的。

Anaconda附带一套叫做Anaconda Navigator的图形工具。 您可以通过从应用程序启动器中打开Anaconda Navigator来启动它。

![使用Anaconda和Python设置机器学习和深度学习的环境](http://p3.pstatp.com/large/66bd0002b0d983595733)

您可以在这里了解有关Anaconda Navigator的所有信息。

稍后您可以使用Anaconda Navigator和图形开发环境; 现在，我推荐从名为conda的Anaconda命令行环境开始。

Conda速度快，操作简单，很难隐藏错误信息，您可以快速确认您的环境已安装并正常工作。

1.  打开一个终端（命令行窗口）。

2.  通过输入以下内容确认conda安装正确：

    **>conda -V**

    **conda 4.3.34**

3.  **通过输入以下内容确认Python安装正确：**

    **>python -V**

    **Python 3.6.4 :: Anaconda custom (64-bit)**

4.  确认您的conda环境是最新的，请输入：

    conda update conda

    conda update anaconda

    您可能需要安装一些软件包并确认更新。  

5.  确认您的SciPy环境。

    下面的脚本将打印您机器学习开发所需的关键SciPy库的版本号，具体为：SciPy，NumPy，Matplotlib，Pandas，Statsmodels和Scikit-learn。

    你可以输入“python”并直接键入命令。 另外，我建议打开一个文本编辑器并将脚本复制粘贴到您的编辑器中。

6.  下面的脚本将打印您机器学习开发所需的关键SciPy库的版本号，具体为：SciPy，NumPy，Matplotlib，Pandas，Statsmodels和Scikit-learn。

    你可以输入“python”并直接键入命令。 另外，我建议打开一个文本编辑器并将脚本复制粘贴到您的编辑器中。

    下面的脚本将打印您机器学习开发所需的关键SciPy库的版本号，具体为：SciPy，NumPy，Matplotlib，Pandas，Statsmodels和Scikit-learn。

    你可以输入“python”并直接键入命令。 另外，我建议打开一个文本编辑器并将脚本复制粘贴到您的编辑器中

\# scipy

import scipy

print('scipy: %s' % scipy.__version__)

\# numpy

import numpy

print('numpy: %s' % numpy.__version__)

\# matplotlib

import matplotlib

print('matplotlib: %s' % matplotlib.__version__)

\# pandas

import pandas

print('pandas: %s' % pandas.__version__)

\# statsmodels

import statsmodels

print('statsmodels: %s' % statsmodels.__version__)

\# scikit-learn

import sklearn

print('sklearn: %s' % sklearn.__version__)

将该脚本另存为名为versions.py的文件。

在命令行上，将您的目录更改为保存脚本的位置并键入：

**> python version.py**

**你应该看到如下的输出：**

**scipy: 1.0.0**

**numpy: 1.14.0**

**matplotlib: 2.1.2**

**pandas: 0.22.0**

**statsmodels: 0.8.0**

**sklearn: 0.19.1**

你得到了什么版本？

将输出粘贴到下面的注释中。

# 更新scikit-learn库

在这一步中，我们将更新Python中用于机器学习的主库，称为scikit-learn。

1.将scikit-learn更新为最新版本。

在撰写本文时，Anaconda附带的scikit-learn版本已过时。 您可以使用conda命令更新特定的库; 以下是将scikit-learn更新为最新版本的示例。

在终端输入：

```
 conda update scikit-learn
```

# 安装深度学习库

在这一步中，我们将安装用于深度学习的Python库，特别是：Theano，TensorFlow和Keras。

注意：我建议使用Keras进行深入学习，而Keras只需要安装Theano或TensorFlow中的一个。 你不需要两个！ 在某些Windows机器上安装TensorFlow可能有问题。

1.  通过输入以下内容安装Theano深度学习库：

    conda install theano  

2.  通过输入以下内容安装TensorFlow深度学习库（除Windows以外的所有内容）：

    conda install -c conda-forge tensorflow  

3.  键入以下内容以安装Keras：

    pip install keras  

4.  确认您的深度学习环境已安装并正常工作。

    创建一个脚本来打印每个库的版本号，就像我们以前为SciPy环境所做的那样。

    \# theano

    import theano

    print('theano: %s' % theano.__version__)

    \# tensorflow

    import tensorflow

    print('tensorflow: %s' % tensorflow.__version__)

    \# keras

    import keras

    print('keras: %s' % keras.__version__

    将脚本保存到文件deep_versions.py。 输入以下命令来运行脚本：

  \> python deep_versions.py

    theano: 1.0.1

    tensorflow: 1.5.0

    Using TensorFlow backend.

    keras: 2.1.4

# 总结

恭喜，您现在有了一个可用于机器学习和深度学习的Python开发环境。

您现在可以在工作站上学习和练习机器学习和深度学习。

你做的怎么样？

请在下面的评论中告诉我

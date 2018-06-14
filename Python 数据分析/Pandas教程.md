
# Pandas教程

Pandas是一款开放源码的BSD许可的Python库，为Python编程语言提供了高性能，易于使用的数据结构和数据分析工具。Pandas用于广泛的领域，包括金融，经济，统计，分析等学术和商业领域。在本教程中，我们将学习Python Pandas的各种功能以及如何在实践中使用它们。
 Pandas的官方网站是： http://pandas.pydata.org/ ，打开后如下所示 - 

![Python Pandas教程](http://www.yiibai.com/uploads/images/201710/3010/120141023_72190.png)

## Pandas库的介绍

Pandas是一个开放源码的Python库，它使用强大的数据结构提供高性能的数据操作和分析工具。它的名字：_Pandas_是从_Panel Data_ - 多维数据的计量经济学(_an Econometrics from Multidimensional data_)。

2008年，为满足需要高性能，灵活的数据分析工具，开发商Wes McKinney开始开发_Pandas_。

在_Pandas_之前，Python主要用于数据迁移和准备。它对数据分析的贡献更小。 _Pandas_解决了这个问题。 使用_Pandas_可以完成数据处理和分析的五个典型步骤，而不管数据的来源 - 加载，准备，操作，模型和分析。
 _Pandas_用于广泛的领域，包括金融，经济，统计，分析等学术和商业领域。

**Pandas的主要特点**

* 快速高效的DataFrame对象，具有默认和自定义的索引。
* 将数据从不同文件格式加载到内存中的数据对象的工具。
* 丢失数据的数据对齐和综合处理。
* 重组和摆动日期集。
* 基于标签的切片，索引和大数据集的子集。
* 可以删除或插入来自数据结构的列。
* 按数据分组进行聚合和转换。
* 高性能合并和数据加入。
* 时间序列功能。

## 读者

本教程为准备学习Pandas基础知识和各种功能的人员而做准备的。它对数据清理和分析的人员特别有用。 完成本教程之后，将发现自己处于适度的专业知识水平，可以从中获得更高水平的专业知识。

## 先决条件

要求对计算机编程术语有一个基本的了解。 对任何编程语言的基本了解是一个加分。Pandas库使用NumPy的大部分功能。建议在继续本教程之前，先阅读NumPy的教程

# Pandas环境安装配置

标准的Python发行版并没有将Pandas模块捆绑在一起发布。安装Pandas模块的一个轻量级的替代方法是使用流行的Python包安装程序，`pip`来安装`NumPy`。

```
pip install pandas
```



大多数用户安装_pandas_最简单的方法是将其作为_Anaconda_发行版的一部分进行安装，这是一个用于数据分析和科学计算的跨平台分发。这是大多数用户推荐的安装方法。

还提供了从源代码，PyPI，各种Linux发行版或开发版本进行安装的说明。

**Python版本支持**

* 官方的`Python 2.7`,`Python 3.5`和`Python 3.6`版本。

如果想通过安装Anaconda Python包，Pandas将默认安装如下 -

## Windows环境安装

* **Anaconda**(来自 http://www.continuum.io )是SciPy堆栈的免费Python发行版。它也适用于Linux和Mac。
* **Canopy**( http://www.enthought.com/products/canopy/ )可免费使用，并提供完整的SciPy堆栈，适用于Windows，Linux和Mac。
* **Python(x，y)**是一个免费的Python发行版，具有SciPy堆栈和适用于Windows操作系统的Spyder IDE。(可从 http://python-xy.github.io/ 下载)

这里仅以 _Anaconda_ 安装作为示例演示，有关_Anaconda_ 安装的过程请参考: http://docs.anaconda.com/anaconda/install/windows

## Linux环境安装

各个Linux发行版的软件包管理器用于在SciPy堆栈中安装一个或多个软件包。

**对于Ubuntu系统**

```
sudo apt-get install python-numpy python-scipy python-matplotlibipythonipythonnotebook
python-pandas python-sympy python-nose
```



**对于Fedora用户**

```
sudo yum install numpyscipy python-matplotlibipython python-pandas sympy
python-nose atlas-devel
```



## 在Window 10上安装Anaconda

这里简单地介绍如何在Window 10(64位)上安装Anaconda，请参考以下步骤：

第一步：下载Anaconda，下载网址： http://anaconda.com/downloads.html ，文件大约是500Mb，请耐心等待下载完成。

![](http://www.yiibai.com/uploads/images/201710/3010/707201044_39151.png)

第二步：双击安装程序(**)启动。

> 注意：如果在安装过程中遇到任何问题，请在安装期间临时禁用防病毒软件，然后在安装结束后重新启用它。 如果您已安装所有用户，请卸载_Anaconda_，然后重新安装，仅供用户使用，然后重试。

![](http://www.yiibai.com/uploads/images/201710/3010/627201045_53662.png)

第三步：阅读许可条款，然后点击“我同意”。

![](http://www.yiibai.com/uploads/images/201710/3010/105201045_96717.png)

第四步：选择安装类型(Just Me)

![](http://www.yiibai.com/uploads/images/201710/3010/375201047_44879.png)

第五步：选择安装位置(_D:\software\Anaconda3\_)，如下图所示 -

![](http://www.yiibai.com/uploads/images/201710/3010/174201050_74911.png)

第六步：高级安装选项(默认就可以了)

![](http://www.yiibai.com/uploads/images/201710/3010/930201052_45841.png)

安装过程，如下图所示 - 

![](http://www.yiibai.com/uploads/images/201710/3010/400201056_16610.png)

第七步：安装完成

![](http://www.yiibai.com/uploads/images/201710/3010/352211002_78992.png)

# Pandas数据结构

_Pandas_处理以下三个数据结构 - 

* 系列(`Series`)
* 数据帧(`DataFrame`)
* 面板(`Panel`)

这些数据结构构建在_Numpy_数组之上，这意味着它们很快。

## 维数和描述

考虑这些数据结构的最好方法是，较高维数据结构是其较低维数据结构的容器。 例如，`DataFrame`是`Series`的容器，`Panel`是`DataFrame`的容器。

| 数据结构 | 维数 | 描述                           |
| ---- | -- | ---------------------------- |
| 系列   | 1  | `1`D标记均匀数组，大小不变。             |
| 数据帧  | 2  | 一般`2`D标记，大小可变的表结构与潜在的异质类型的列。 |
| 面板   | 3  | 一般`3`D标记，大小可变数组。             |

构建和处理两个或更多个维数组是一项繁琐的任务，用户在编写函数时要考虑数据集的方向。 但是使用_Pandas_数据结构，减少了用户的思考。

例如，使用表格数据(`DataFrame`)，在语义上更有用于考虑索引(行)和列，而不是轴`0`和轴`1`。

**可变性**

所有_Pandas_数据结构是值可变的(可以更改)，除了系列都是大小可变的。系列是大小不变的。

> 注 - `DataFrame`被广泛使用，是最重要的数据结构之一。面板使用少得多。

## 系列

系列是具有均匀数据的一维数组结构。例如，以下系列是整数：`10`,`23`,`56`，`...`的集合。

![](http://www.yiibai.com/uploads/images/201710/3110/493141059_40874.png)

**关键点**

* 均匀数据
* 尺寸大小不变
* 数据的值可变

## 数据帧

<ins class="adsbygoogle" style="display:inline-block;width:728px;height:90px" data-ad-client="ca-pub-1090193214637198" data-ad-slot="6494738921"></ins>

数据帧(_DataFrame_)是一个具有异构数据的二维数组。 例如，

| 姓名    | 年龄 | 性别 | 等级   |
| ----- | -- | -- | ---- |
| Maxsu | 25 | 男  | 4.45 |
| Katie | 34 | 女  | 2.78 |
| Vina  | 46 | 女  | 3.9  |
| Lia   | 女  | x女 | 4.6  |

上表表示具有整体绩效评级组织的销售团队的数据。数据以行和列表示。每列表示一个属性，每行代表一个人。

**列的数据类型**

上面数据帧中四列的数据类型如下：

| 列  | 类型  |
| -- | --- |
| 姓名 | 字符串 |
| 年龄 | 整数  |
| 性别 | 字符串 |
| 等级 | 浮点型 |

**关键点**

* 异构数据
* 大小可变
* 数据可变

## 面板

面板是具有异构数据的三维数据结构。在图形表示中很难表示面板。但是一个面板可以说明为`DataFrame`的容器。

**关键点**

* 异构数据
* 大小可变
* 数据可变

# Pandas快速入门

这是一个_Pandas_快速入门教程，主要面向新用户。这里主要是为那些喜欢“短平快”的读者准备的，有兴趣的读者可通过其它教程文章来一步一步地更复杂的应用知识。

首先，假设您安装好了_Anaconda_，现在启动_Anaconda_开始学始本教程中的示例。工作界面如下所示 - 

![](http://www.yiibai.com/uploads/images/201710/3110/853151046_43371.png)

测试工作环境是否有安装好了_Pandas_，导入相关包如下：

```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
print("Hello, Pandas")
```


然后执行一下，看有没有问题，如果正常应该会在终端输出区看到以下结果 - 

![](http://www.yiibai.com/uploads/images/201710/3110/833151050_42278.png)

## 对象创建

通过传递值列表来创建一个系列，让_Pandas_创建一个默认的整数索引：

```
import pandas as pd
import numpy as np

s = pd.Series([1,3,5,np.nan,6,8])

print(s)
```


执行后输出结果如下 - 

```
runfile('C:/Users/Administrator/.spyder-py3/temp.py', wdir='C:/Users/Administrator/.spyder-py3')
0    1.0
1    3.0
2    5.0
3    NaN
4    6.0
5    8.0
dtype: float64
```



通过传递`numpy`数组，使用`datetime`索引和标记列来创建`DataFrame`：

```
import pandas as pd
import numpy as np

dates = pd.date_range('20170101', periods=7)
print(dates)

print("--"*16)
df = pd.DataFrame(np.random.randn(7,4), index=dates, columns=list('ABCD'))
print(df)
```


执行后输出结果如下 - 

```
runfile('C:/Users/Administrator/.spyder-py3/temp.py', wdir='C:/Users/Administrator/.spyder-py3')
DatetimeIndex(['2017-01-01', '2017-01-02', '2017-01-03', '2017-01-04',
               '2017-01-05', '2017-01-06', '2017-01-07'],
              dtype='datetime64[ns]', freq='D')
--------------------------------
                   A         B         C         D
2017-01-01 -0.732038  0.329773 -0.156383  0.270800
2017-01-02  0.750144  0.722037 -0.849848 -1.105319
2017-01-03 -0.786664 -0.204211  1.246395  0.292975
2017-01-04 -1.108991  2.228375  0.079700 -1.738507
2017-01-05  0.348526 -0.960212  0.190978 -2.223966
2017-01-06 -0.579689 -1.355910  0.095982  1.233833
2017-01-07  1.086872  0.664982  0.377787  1.012772
```



通过传递可以转换为类似系列的对象的字典来创建DataFrame。参考以下示例代码 - 

```
import pandas as pd
import numpy as np

df2 = pd.DataFrame({ 'A' : 1.,
                     'B' : pd.Timestamp('20170102'),
                     'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                     'D' : np.array([3] * 4,dtype='int32'),
                     'E' : pd.Categorical(["test","train","test","train"]),
                     'F' : 'foo' })

print(df2)
```


执行上面示例代码后，输出结果如下 - 

```
runfile('C:/Users/Administrator/.spyder-py3/temp.py', wdir='C:/Users/Administrator/.spyder-py3')
     A          B    C  D      E    F
0  1.0 2017-01-02  1.0  3   test  foo
1  1.0 2017-01-02  1.0  3  train  foo
2  1.0 2017-01-02  1.0  3   test  foo
3  1.0 2017-01-02  1.0  3  train  foo
```



有指定`dtypes`，参考以下示例代码 - 

```
runfile('C:/Users/Administrator/.spyder-py3/temp.py', wdir='C:/Users/Administrator/.spyder-py3')
A           float64
B    datetime64[ns]
C           float32
D             int32
E          category
F            object
dtype: object
```


执行上面示例代码后，输出结果如下 - 

```
runfile('C:/Users/Administrator/.spyder-py3/temp.py', wdir='C:/Users/Administrator/.spyder-py3')
A           float64
B    datetime64[ns]
C           float32
D             int32
E          category
F            object
dtype: object
```



如果使用IPython，则会自动启用列名(以及公共属性)的选项完成。 以下是将要完成的属性的一个子集：

```
In [13]: df2.<TAB>
df2.A                  df2.bool
df2.abs                df2.boxplot
df2.add                df2.C
df2.add_prefix         df2.clip
df2.add_suffix         df2.clip_lower
df2.align              df2.clip_upper
df2.all                df2.columns
df2.any                df2.combine
df2.append             df2.combine_first
df2.apply              df2.compound
df2.applymap           df2.consolidate
df2.D
```


可以看到，列`A`，`B`，`C`和`D`自动标签完成。`E`也在一样。其余的属性为了简洁而被截短。

## 查看数据

查看框架的顶部和底部的数据行。参考以下示例代码 - 

```
import pandas as pd
import numpy as np

dates = pd.date_range('20170101', periods=7)
df = pd.DataFrame(np.random.randn(7,4), index=dates, columns=list('ABCD'))
print(df.head())
print("--------------" * 10)
print(df.tail(3))
```


执行上面示例代码后，输出结果如下 - 

```
runfile('C:/Users/Administrator/.spyder-py3/temp.py', wdir='C:/Users/Administrator/.spyder-py3')
                   A         B         C         D
2017-01-01 -0.520856 -0.555019 -2.286424  1.745681
2017-01-02  1.114030  0.861933  0.795958  0.420670
2017-01-03 -0.343605 -0.937356  0.052693 -0.540735
2017-01-04  1.587684 -0.743756  0.021738 -0.702190
2017-01-05  1.243403  0.930299  0.234343  1.604182
------------------------------------------------------------
                   A         B         C         D
2017-01-05  1.243403  0.930299  0.234343  1.604182
2017-01-06 -0.087004 -0.368055  1.434022  0.464193
2017-01-07 -1.248981  0.973724 -0.288384 -0.577388
```



显示索引，列和底层numpy数据，参考以下代码 - 

```
import pandas as pd
import numpy as np

dates = pd.date_range('20170101', periods=7)
df = pd.DataFrame(np.random.randn(7,4), index=dates, columns=list('ABCD'))
print("index is :" )
print(df.index)
print("columns is :" )
print(df.columns)
print("values is :" )
print(df.values)
```


执行上面示例代码后，输出结果如下 - 

```
runfile('C:/Users/Administrator/.spyder-py3/temp.py', wdir='C:/Users/Administrator/.spyder-py3')
index is :
DatetimeIndex(['2017-01-01', '2017-01-02', '2017-01-03', '2017-01-04',
               '2017-01-05', '2017-01-06', '2017-01-07'],
              dtype='datetime64[ns]', freq='D')
columns is :
Index(['A', 'B', 'C', 'D'], dtype='object')
values is :
[[ 2.23820398  0.18440123  0.08039084 -0.27751926]
 [-0.12335513  0.36641304 -0.28617579  0.34383109]
 [-0.85403491  0.63876989  1.26032173 -1.27382333]
 [-0.07262661 -0.01788962  0.28748668  1.12715561]
 [-1.14293392 -0.88263364  0.72250762 -1.64051326]
 [ 0.41864083  0.40545953 -0.14591541 -0.57168728]
 [ 1.01383531 -0.22793823 -0.44045634  1.04799829]]
```



描述显示数据的快速统计摘要，参考以下示例代码 - 

```
import pandas as pd
import numpy as np

dates = pd.date_range('20170101', periods=7)
df = pd.DataFrame(np.random.randn(7,4), index=dates, columns=list('ABCD'))
print(df.describe())
```


执行上面示例代码后，输出结果如下 - 

```
runfile('C:/Users/Administrator/.spyder-py3/temp.py', wdir='C:/Users/Administrator/.spyder-py3')
              A         B         C         D
count  7.000000  7.000000  7.000000  7.000000
mean  -0.675425 -0.257835  0.144049  0.275621
std    1.697957  0.793953  1.301520  1.412291
min   -2.595040 -1.200401 -1.230538 -0.976166
25%   -1.992393 -0.723464 -0.897041 -0.800919
50%   -1.050666 -0.445612  0.004719 -0.705840
75%    0.592677  0.068574  0.874195  1.398337
max    1.717166  1.150948  2.279856  2.416514
```



调换数据，参考以下示例代码 - 

```
import pandas as pd
import numpy as np

dates = pd.date_range('20170101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print(df.T)
```


执行上面示例代码后，输出结果如下 - 

```
runfile('C:/Users/Administrator/.spyder-py3/temp.py', wdir='C:/Users/Administrator/.spyder-py3')
   2017-01-01  2017-01-02  2017-01-03  2017-01-04  2017-01-05  2017-01-06
A    0.932454   -2.148503    1.398975    1.565676   -0.167527   -0.242041
B    0.584585    1.373330   -0.069801   -0.102857    1.286432   -0.703491
C   -0.345119   -0.680955    1.686750    1.184996    0.016170   -0.663963
D    0.431751    0.444830   -1.524739    0.040007    0.220172    1.423627
```



通过轴排序，参考以下示例程序 - 

```
import pandas as pd
import numpy as np

dates = pd.date_range('20170101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print(df.sort_index(axis=1, ascending=False))
`
```


执行上面示例代码后，输出结果如下 - 

```
runfile('C:/Users/Administrator/.spyder-py3/temp.py', wdir='C:/Users/Administrator/.spyder-py3')
                   D         C         B         A
2017-01-01  0.426359  2.542352 -0.324047  0.418973
2017-01-02 -0.834625 -1.356709  0.150744 -1.690500
2017-01-03 -0.018274  0.900801  1.072851  0.149830
2017-01-04 -1.075027 -0.889379 -0.663223 -1.404002
2017-01-05 -1.273966 -1.335761 -1.356561 -1.135199
2017-01-06 -1.590793  0.693430 -0.504164  0.143386
```



按值排序，参考以下示例程序 - 

```
import pandas as pd
import numpy as np

dates = pd.date_range('20170101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print(df.sort_values(by='B'))
`
```


执行上面示例代码后，输出结果如下 - 

```
A         B         C         D
2017-01-06  0.764517 -1.526019  0.400456 -0.182082
2017-01-05 -0.177845 -1.269836 -0.534676  0.796666
2017-01-04 -0.981485 -0.082572 -1.272123  0.508929
2017-01-02 -0.290117  0.053005 -0.295628 -0.346965
2017-01-03  0.941131  0.799280  2.054011 -0.684088
2017-01-01  0.597788  0.892008  0.903053 -0.821024
```



## 选择区块

> 注意虽然用于选择和设置的标准Python/Numpy表达式是直观的，可用于交互式工作，但对于生产代码，但建议使用优化的_Pandas_数据访问方法`.at`，`.iat`，`.loc`，`.iloc`和`.ix`。

### 获取

选择一列，产生一个系列，相当于`df.A`，参考以下示例程序 - 

```
import pandas as pd
import numpy as np

dates = pd.date_range('20170101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df['A'])
`
```


执行上面示例代码后，输出结果如下 - 

```
runfile('C:/Users/Administrator/.spyder-py3/temp.py', wdir='C:/Users/Administrator/.spyder-py3')
2017-01-01    0.317460
2017-01-02   -0.933726
2017-01-03    0.167860
2017-01-04    0.816184
2017-01-05   -0.745503
2017-01-06    0.505319
Freq: D, Name: A, dtype: float64
```



选择通过`[]`操作符，选择切片行。参考以下示例程序 - 

```
import pandas as pd
import numpy as np

dates = pd.date_range('20170101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df[0:3])

print("========= 指定选择日期 ========")

print(df['20170102':'20170103'])
`
```


执行上面示例代码后，输出结果如下 - 

```
runfile('C:/Users/Administrator/.spyder-py3/temp.py', wdir='C:/Users/Administrator/.spyder-py3')
                   A         B         C         D
2017-01-01  1.103449  0.926571 -1.649978 -0.309270
2017-01-02  0.516404 -0.734076 -0.081163 -0.528497
2017-01-03  0.240356  0.231224 -1.463315 -1.157256
========= 指定选择日期 ========
                   A         B         C         D
2017-01-02  0.516404 -0.734076 -0.081163 -0.528497
2017-01-03  0.240356  0.231224 -1.463315 -1.157256
```



### 按标签选择

使用标签获取横截面，参考以下示例程序 - 

```
import pandas as pd
import numpy as np

dates = pd.date_range('20170101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df.loc[dates[0]])
`
```


执行上面示例代码后，输出结果如下 - 

```
runfile('C:/Users/Administrator/.spyder-py3/temp.py', wdir='C:/Users/Administrator/.spyder-py3')
A   -0.483292
B   -0.536987
C   -0.889947
D    1.250857
Name: 2017-01-01 00:00:00, dtype: float64
```



通过标签选择多轴，参考以下示例程序 - 

<ins class="adsbygoogle" style="display:inline-block;width:728px;height:90px" data-ad-client="ca-pub-1090193214637198" data-ad-slot="6494738921"></ins>

```
import pandas as pd
import numpy as np

dates = pd.date_range('20170101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df.loc[:,['A','B']])
`
```


执行上面示例代码后，输出结果如下 - 

```
A         B
2017-01-01  0.479048 -0.105106
2017-01-02  0.172920  0.086570
2017-01-03 -1.302485 -0.593550
2017-01-04 -0.595438  1.304054
2017-01-05  0.154267  1.336219
2017-01-06 -0.341204  0.781300
```



显示标签切片，包括两个端点，参考以下示例程序 - 

```
import pandas as pd
import numpy as np

dates = pd.date_range('20170101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df.loc['20170102':'20170104',['A','B']])
`
```


执行上面示例代码后，输出结果如下 - 

```
A         B
2017-01-02  1.062995 -0.108277
2017-01-03  1.962106 -0.294664
2017-01-04 -0.128576  0.717738
```



减少返回对象的尺寸(大小)，参考以下示例程序 - 

```
import pandas as pd
import numpy as np

dates = pd.date_range('20170101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df.loc['20170102',['A','B']])
`
```


执行上面示例代码后，输出结果如下 - 

```
A    0.252749
B    0.119747
Name: 2017-01-02 00:00:00, dtype: float64
```



获得标量值，参考以下示例程序 - 

```
import pandas as pd
import numpy as np

dates = pd.date_range('20170101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df.loc[dates[0],'A'])
`
```


执行上面示例代码后，输出结果如下 - 

```
-0.0839903627822
```



快速访问标量(等同于先前的方法)，参考以下示例程序 - 

```
import pandas as pd
import numpy as np

dates = pd.date_range('20170101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df.at[dates[0],'A'])
`
```


执行上面示例代码后，输出结果如下 - 

```
-0.0839903627822
```



## 通过位置选择

通过传递的整数的位置选择，参考以下示例程序 - 

```
import pandas as pd
import numpy as np

dates = pd.date_range('20170101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df.iloc[3])
`
```


执行上面示例代码后，输出结果如下 - 

```
A    0.944506
B    1.035781
C    0.421373
D    0.017660
Name: 2017-01-04 00:00:00, dtype: float64
```



通过整数切片，类似于_numpy/python_，参考以下示例程序 - 

```
import pandas as pd
import numpy as np

dates = pd.date_range('20170101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df.iloc[3:5,0:2])
`
```


执行上面示例代码后，输出结果如下 - 

```
A         B
2017-01-04 -1.617068  0.548090
2017-01-05 -0.864247  0.419743
```



通过整数位置的列表，类似于_numpy/python_样式，参考以下示例程序 - 

```
import pandas as pd
import numpy as np

dates = pd.date_range('20170101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df.iloc[[1,2,4],[0,2]])
`
```


执行上面示例代码后，输出结果如下 - 

```
A         C
2017-01-02  0.085091  0.568128
2017-01-03  0.729076 -0.451151
2017-01-05 -1.281975 -0.190119
```



明确切片行，参考以下示例程序 - 

```
import pandas as pd
import numpy as np

dates = pd.date_range('20170101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df.iloc[1:3,:])
`
```


执行上面示例代码后，输出结果如下 - 

```
A         B         C         D
2017-01-02 -1.123970 -0.010969 -1.076657 -0.538908
2017-01-03 -0.314408  0.004415 -0.356924  0.337539
```



明确切片列，参考以下示例程序 - 

```
import pandas as pd
import numpy as np

dates = pd.date_range('20170101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df.iloc[:,1:3])
`
```


执行上面示例代码后，输出结果如下 - 

```
B         C
2017-01-01  0.323663  1.027599
2017-01-02 -0.176624 -0.959683
2017-01-03  0.689698  0.622540
2017-01-04  1.864511  1.023157
2017-01-05  0.964123  2.062503
2017-01-06 -0.375143  0.231328
```



要明确获取值，参考以下示例程序 - 

```
import pandas as pd
import numpy as np

dates = pd.date_range('20170101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df.iloc[1,1])
`
```


执行上面示例代码后，输出结果如下 - 

```
0.829950900219
```



要快速访问标量(等同于先前的方法)，参考以下示例程序 - 

```
import pandas as pd
import numpy as np

dates = pd.date_range('20170101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df.iat[1,1])
`
```


执行上面示例代码后，输出结果如下 - 

```
-0.170996002652
```



### 布尔索引

使用单列的值来选择数据，参考以下示例程序 - 

```
import pandas as pd
import numpy as np

dates = pd.date_range('20170101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df[df.A > 0])
`
```


执行上面示例代码后，输出结果如下 - 

```
A         B         C         D
2017-01-03  0.276486 -1.003779  0.721863 -0.558061
2017-01-04  1.177206 -0.464778 -0.116442 -0.385712
2017-01-06  0.846665 -1.398207 -0.145356  0.924342
```



从满足布尔条件的DataFrame中选择值。，参考以下示例程序 - 

```
import pandas as pd
import numpy as np

dates = pd.date_range('20170101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df[df > 0])
`
```


执行上面示例代码后，输出结果如下 - 

```
A         B         C         D
2017-01-01       NaN  1.963213  0.643244  0.945643
2017-01-02  0.364237  0.917368       NaN       NaN
2017-01-03  0.702624       NaN  0.088565       NaN
2017-01-04  1.274313       NaN  2.313910       NaN
2017-01-05  2.586315  0.588273       NaN  1.482597
2017-01-06       NaN  0.405928  0.309201       NaN
```



使用`isin()`方法进行过滤，参考以下示例程序 - 

```
import pandas as pd
import numpy as np

dates = pd.date_range('20170101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

df2 = df.copy()
df2['E'] = ['one', 'one','two','three','four','three']

print(df2)

print("============= start to filter =============== ")

print(df2[df2['E'].isin(['two','four'])])

`
```


执行上面示例代码后，输出结果如下 - 

```
A         B         C         D      E
2017-01-01  0.723399 -0.369247  0.863941 -1.910875    one
2017-01-02 -0.047573 -0.609780  2.130650 -0.019281    one
2017-01-03 -0.566122 -0.850374 -0.031516  0.362023    two
2017-01-04  0.903819 -0.513673  0.118850 -0.351811  three
2017-01-05 -0.485232 -0.864457  1.396835 -1.696083   four
2017-01-06  0.272145 -0.644449 -1.319063 -0.201354  three
============= start to filter =============== 
                   A         B         C         D     E
2017-01-03 -0.566122 -0.850374 -0.031516  0.362023   two
2017-01-05 -0.485232 -0.864457  1.396835 -1.696083  four
```

# Pandas系列

系列(`Series`)是能够保存任何类型的数据(整数，字符串，浮点数，Python对象等)的一维标记数组。轴标签统称为索引。

## pandas.Series

_Pandas_系列可以使用以下构造函数创建 -

```
pandas.Series( data, index, dtype, copy)。
```


构造函数的参数如下 -

| 编号 | 参数      | 描述                                                 |
| -- | ------- | -------------------------------------------------- |
| 1  | `data`  | 数据采取各种形式，如：`ndarray`，`list`，`constants`            |
| 2  | `index` | 索引值必须是唯一的和散列的，与数据的长度相同。 默认`np.arange(n)`如果没有索引被传递。 |
| 3  | `dtype` | `dtype`用于数据类型。如果没有，将推断数据类型                         |
| 4  | `copy`  | 复制数据，默认为`false`。                                   |

可以使用各种输入创建一个系列，如 -

* 数组
* 字典
* 标量值或常数

## 创建一个空的系列

创建一个基本系列是一个空系列。

**示例**

```
#import the pandas library and aliasing as pd
import pandas as pd
s = pd.Series()
print s
```


执行上面示例代码，输出结果如下 - 

```
Series([], dtype: float64)
```



## 从ndarray创建一个系列

如果数据是`ndarray`，则传递的索引必须具有相同的长度。 如果没有传递索引值，那么默认的索引将是范围(`n`)，其中`n`是数组长度，即`[0,1,2,3…. range(len(array))-1] - 1]`。

**示例1**

```
#import the pandas library and aliasing as pd
import pandas as pd
import numpy as np
data = np.array(['a','b','c','d'])
s = pd.Series(data)
print s
```


执行上面示例代码，输出结果如下 - 

```
0   a
1   b
2   c
3   d
dtype: object
```



这里没有传递任何索引，因此默认情况下，它分配了从`0`到`len(data)-1`的索引，即：`0`到`3`。

**示例2**

```
#import the pandas library and aliasing as pd
import pandas as pd
import numpy as np
data = np.array(['a','b','c','d'])
s = pd.Series(data,index=[100,101,102,103])
print s
```


执行上面示例代码，输出结果如下 - 

```
100  a
101  b
102  c
103  d
dtype: object
```


在这里传递了索引值。现在可以在输出中看到自定义的索引值。

## 从字典创建一个系列

字典(`dict`)可以作为输入传递，如果没有指定索引，则按排序顺序取得字典键以构造索引。 如果传递了索引，索引中与标签对应的数据中的值将被拉出。

**示例2**

```
#import the pandas library and aliasing as pd
import pandas as pd
import numpy as np
data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data)
print s
```


执行上面示例代码，输出结果如下 - 

```
a 0.0
b 1.0
c 2.0
dtype: float64
```


> 注意 - 字典键用于构建索引。

**示例**

```
#import the pandas library and aliasing as pd
import pandas as pd
import numpy as np
data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data,index=['b','c','d','a'])
print s
```


执行上面示例代码，输出结果如下 - 

```
b 1.0
c 2.0
d NaN
a 0.0
dtype: float64
```


> 注意观察 - 索引顺序保持不变，缺少的元素使用NaN(不是数字)填充。

## 从标量创建一个系列

如果数据是标量值，则必须提供索引。将重复该值以匹配索引的长度。

```
#import the pandas library and aliasing as pd
import pandas as pd
import numpy as np
s = pd.Series(5, index=[0, 1, 2, 3])
print s
```


执行上面示例代码，得到以下结果 - 

<ins class="adsbygoogle" style="display:inline-block;width:728px;height:90px" data-ad-client="ca-pub-1090193214637198" data-ad-slot="6494738921"></ins>

```
0  5
1  5
2  5
3  5
dtype: int64
```



## 从具有位置的系列中访问数据

系列中的数据可以使用类似于访问`ndarray`中的数据来访问。

**示例-1**

检索第一个元素。比如已经知道数组从零开始计数，第一个元素存储在零位置等等。

```
import pandas as pd
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])

#retrieve the first element
print s[0]
```


执行上面示例，得到以下结果 - 

```
1
```



**示例-2**

检索系列中的前三个元素。 如果`a:`被插入到其前面，则将从该索引向前的所有项目被提取。 如果使用两个参数(使用它们之间)，两个索引之间的项目(不包括停止索引)。

```
import pandas as pd
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])

#retrieve the first three element
print s[:3]
```


执行上面示例，得到以下结果 - 

```
a  1
b  2
c  3
dtype: int64
```



**示例-3**

检索最后三个元素，参考以下示例代码 - 

```
import pandas as pd
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])

#retrieve the last three element
print s[-3:]
```


执行上面示例代码，得到以下结果 - 

```
c  3
d  4
e  5
dtype: int64
```



## 使用标签检索数据(索引)

一个系列就像一个固定大小的字典，可以通过索引标签获取和设置值。

**示例1**

使用索引标签值检索单个元素。

```
import pandas as pd
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])

#retrieve a single element
print s['a']
```


执行上面示例代码，得到以下结果 - 

```
1
```



**示例2**

使用索引标签值列表检索多个元素。

```
import pandas as pd
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])

#retrieve multiple elements
print s[['a','c','d']]
```


执行上面示例代码，得到以下结果 - 

```
a  1
c  3
d  4
dtype: int64
```



**示例3**

如果不包含标签，则会出现异常。

```
import pandas as pd
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])

#retrieve multiple elements
print s['f']
```


执行上面示例代码，得到以下结果 - 

```
…
KeyError: 'f'
```

# Pandas数据帧（DataFrame）

数据帧(DataFrame)是二维数据结构，即数据以行和列的表格方式排列。

数据帧(DataFrame)的功能特点：

* 潜在的列是不同的类型
* 大小可变
* 标记轴(行和列)
* 可以对行和列执行算术运算

**结构体**

假设要创建一个包含学生数据的数据帧。参考以下图示 - 

![](http://www.yiibai.com/uploads/images/201710/3110/113091148_50780.jpg)

可以将上图表视为SQL表或电子表格数据表示。

## pandas.DataFrame

_pandas_中的`DataFrame`可以使用以下构造函数创建 -

```
pandas.DataFrame( data, index, columns, dtype, copy)
```


构造函数的参数如下 -  

| 编号 | 参数        | 描述                                                                            |
| -- | --------- | ----------------------------------------------------------------------------- |
| 1  | `data`    | 数据采取各种形式，如:`ndarray`，`series`，`map`，`lists`，`dict`，`constant`和另一个`DataFrame`。 |
| 2  | `index`   | 对于行标签，要用于结果帧的索引是可选缺省值`np.arrange(n)`，如果没有传递索引值。                               |
| 3  | `columns` | 对于列标签，可选的默认语法是 - `np.arange(n)`。 这只有在没有索引传递的情况下才是这样。                          |
| 4  | `dtype`   | 每列的数据类型。                                                                      |
| 5  | `copy`    | 如果默认值为`False`，则此命令(或任何它)用于复制数据。                                               |

## 创建DataFrame

Pandas数据帧(_DataFrame_)可以使用各种输入创建，如 - 

* 列表
* 字典
* 系列
* Numpy ndarrays
* 另一个数据帧(_DataFrame_)

在本章的后续章节中，我们将看到如何使用这些输入创建数据帧(_DataFrame_)。

## 创建一个空的DataFrame

创建基本数据帧是空数据帧。  
**示例**

```
#import the pandas library and aliasing as pd
import pandas as pd
df = pd.DataFrame()
print df
```


执行上面示例代码，得到以下结果 - 

```
Empty DataFrame
Columns: []
Index: []
```



## 从列表创建DataFrame

可以使用单个列表或列表列表创建数据帧(_DataFrame_)。

**实例-1**

```
import pandas as pd
data = [1,2,3,4,5]
df = pd.DataFrame(data)
print df
```


执行上面示例代码，得到以下结果 - 

```
0
0    1
1    2
2    3
3    4
4    5
```



**实例-2**

```
import pandas as pd
data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'])
print df
```


执行上面示例代码，得到以下结果 - 

```
Name      Age
0     Alex      10
1     Bob       12
2     Clarke    13
```



**实例-3**

```
import pandas as pd
data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'],dtype=float)
print df
```


执行上面示例代码，得到以下结果 - 

```
Name     Age
0     Alex     10.0
1     Bob      12.0
2     Clarke   13.0
```



> 注意 - 可以观察到，`dtype`参数将`Age`列的类型更改为浮点。

## 从ndarrays/Lists的字典来创建DataFrame

所有的`ndarrays`必须具有相同的长度。如果传递了索引(`index`)，则索引的长度应等于数组的长度。

如果没有传递索引，则默认情况下，索引将为`range(n)`，其中`n`为数组长度。

**实例-1**

```
import pandas as pd
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data)
print df
```


执行上面示例代码，得到以下结果 - 

```
Age      Name
0     28        Tom
1     34       Jack
2     29      Steve
3     42      Ricky
```



> 注 - 观察值`0`,`1`,`2`,`3`。它们是分配给每个使用函数`range(n)`的默认索引。

**示例-2**

使用数组创建一个索引的数据帧(_DataFrame_)。

```
import pandas as pd
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
print df
```


执行上面示例代码，得到以下结果 - 

```
Age    Name
rank1    28      Tom
rank2    34     Jack
rank3    29    Steve
rank4    42    Ricky
```



> 注意 - `index`参数为每行分配一个索引。

## 从列表创建数据帧DataFrame

字典列表可作为输入数据传递以用来创建数据帧(_DataFrame_)，字典键默认为列名。

**实例-1**

以下示例显示如何通过传递字典列表来创建数据帧(_DataFrame_)。

```
import pandas as pd
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print df
```


执行上面示例代码，得到以下结果 - 

```
a    b      c
0   1   2     NaN
1   5   10   20.0
```



> 注意 - 观察到，NaN(不是数字)被附加在缺失的区域。

**示例-2**

以下示例显示如何通过传递字典列表和行索引来创建数据帧(_DataFrame_)。

```
import pandas as pd
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data, index=['first', 'second'])
print df
```


执行上面示例代码，得到以下结果 - 

```
a   b       c
first   1   2     NaN
second  5   10   20.0
```



**实例-3**

以下示例显示如何使用字典，行索引和列索引列表创建数据帧(_DataFrame_)。

```
import pandas as pd
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]

#With two column indices, values same as dictionary keys
df1 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b'])

#With two column indices with one index with other name
df2 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b1'])
print df1
print df2
```


执行上面示例代码，得到以下结果 - 

```
#df1 output
         a  b
first    1  2
second   5  10

#df2 output
         a  b1
first    1  NaN
second   5  NaN
```



> 注意 - 观察，`df2`使用字典键以外的列索引创建`DataFrame`; 因此，附加了NaN到位置上。 而`df1`是使用列索引创建的，与字典键相同，所以也附加了NaN。

## 从系列的字典来创建DataFrame

字典的系列可以传递以形成一个DataFrame。 所得到的索引是通过的所有系列索引的并集。

**示例**

```
import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
      'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print df
`
```


执行上面示例代码，得到以下结果 - 

```
one    two
a     1.0    1
b     2.0    2
c     3.0    3
d     NaN    4
```



> 注意 - 对于第一个系列，观察到没有传递标签`'d'`，但在结果中，对于`d`标签，附加了NaN。

现在通过实例来了解列选择，添加和删除。

### 列选择

下面将通过从数据帧(DataFrame)中选择一列。

示例

```
import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
      'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print df ['one']
```


执行上面示例代码，得到以下结果 - 

<ins class="adsbygoogle" style="display:inline-block;width:728px;height:90px" data-ad-client="ca-pub-1090193214637198" data-ad-slot="6494738921"></ins>

```
a     1.0
b     2.0
c     3.0
d     NaN
Name: one, dtype: float64
```



### 列添加

下面将通过向现有数据框添加一个新列来理解这一点。

**示例**

```
import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
      'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)

# Adding a new column to an existing DataFrame object with column label by passing new series

print ("Adding a new column by passing as Series:")
df['three']=pd.Series([10,20,30],index=['a','b','c'])
print df

print ("Adding a new column using the existing columns in DataFrame:")
df['four']=df['one']+df['three']

print df
```


执行上面示例代码，得到以下结果 - 

```
Adding a new column by passing as Series:
     one   two   three
a    1.0    1    10.0
b    2.0    2    20.0
c    3.0    3    30.0
d    NaN    4    NaN

Adding a new column using the existing columns in DataFrame:
      one   two   three    four
a     1.0    1    10.0     11.0
b     2.0    2    20.0     22.0
c     3.0    3    30.0     33.0
d     NaN    4     NaN     NaN
```



### 列删除

列可以删除或弹出; 看看下面的例子来了解一下。

**例子**

```
# Using the previous DataFrame, we will delete a column
# using del function
import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 
     'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']), 
     'three' : pd.Series([10,20,30], index=['a','b','c'])}

df = pd.DataFrame(d)
print ("Our dataframe is:")
print df

# using del function
print ("Deleting the first column using DEL function:")
del df['one']
print df

# using pop function
print ("Deleting another column using POP function:")
df.pop('two')
print df
```


执行上面示例代码，得到以下结果 - 

```
Our dataframe is:
      one   three  two
a     1.0    10.0   1
b     2.0    20.0   2
c     3.0    30.0   3
d     NaN     NaN   4

Deleting the first column using DEL function:
      three    two
a     10.0     1
b     20.0     2
c     30.0     3
d     NaN      4

Deleting another column using POP function:
   three
a  10.0
b  20.0
c  30.0
d  NaN
```



## 行选择，添加和删除

现在将通过下面实例来了解行选择，添加和删除。我们从选择的概念开始。

**标签选择**

可以通过将行标签传递给`loc()`函数来选择行。参考以下示例代码 - 

```
import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 
     'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print df.loc['b']
```


执行上面示例代码，得到以下结果 - 

```
one 2.0
two 2.0
Name: b, dtype: float64
```



结果是一系列标签作为`DataFrame`的列名称。 而且，系列的名称是检索的标签。

**按整数位置选择**

可以通过将整数位置传递给`iloc()`函数来选择行。参考以下示例代码 - 

```
import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print df.iloc[2]
```


执行上面示例代码，得到以下结果 - 

```
one   3.0
two   3.0
Name: c, dtype: float64
```



## 行切片

可以使用`:`运算符选择多行。参考以下示例代码 - 

```
import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 
    'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print df[2:4]
```


执行上面示例代码，得到以下结果 - 

```
one    two
c     3.0     3
d     NaN     4
```



**附加行**

使用`append()`函数将新行添加到DataFrame。 此功能将附加行结束。

```
import pandas as pd

df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])

df = df.append(df2)
print df
```


执行上面示例代码，得到以下结果 - 

```
a  b
0  1  2
1  3  4
0  5  6
1  7  8
```



**删除行**

使用索引标签从DataFrame中删除或删除行。 如果标签重复，则会删除多行。

如果有注意，在上述示例中，有标签是重复的。这里再多放一个标签，看看有多少行被删除。

```
import pandas as pd

df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])

df = df.append(df2)

# Drop rows with label 0
df = df.drop(0)

print df
```


执行上面示例代码，得到以下结果 - 

```
a b
1 3 4
1 7 8
```



在上面的例子中，一共有两行被删除，因为这两行包含相同的标签`0`。

# Pandas面板（Panel）

面板(Panel)是3D容器的数据。面板数据一词来源于计量经济学，部分源于名称：`Pandas` - `pan(el)-da(ta)-s`。

`3`轴(`axis`)这个名称旨在给出描述涉及面板数据的操作的一些语义。它们是 -

* _items_ - `axis 0`，每个项目对应于内部包含的数据帧(DataFrame)。
* _major_axis_ - `axis 1`，它是每个数据帧(DataFrame)的索引(行)。
* _minor_axis_ - `axis 2`，它是每个数据帧(DataFrame)的列。

## 1. pandas.Panel()

可以使用以下构造函数创建面板 -

```
pandas.Panel(data, items, major_axis, minor_axis, dtype, copy)
```


构造函数的参数如下 -

| 参数           | 描述                                                                                |
| ------------ | --------------------------------------------------------------------------------- |
| `data`       | 数据采取各种形式，如：`ndarray`，`series`，`map`，`lists`，`dict`，`constant`和另一个数据帧(`DataFrame`) |
| `items`      | `axis=0`                                                                          |
| `major_axis` | `axis=1`                                                                          |
| `minor_axis` | `axis=2`                                                                          |
| `dtype`      | 每列的数据类型                                                                           |
| `copy`       | 复制数据，默认 - `false`                                                                 |

## 2. 创建面板

可以使用多种方式创建面板 - 

* 从ndarrays创建
* 从DataFrames的dict创建

### 2.1 从3D ndarray创建

```
# creating an empty panel
import pandas as pd
import numpy as np

data = np.random.rand(2,4,5)
p = pd.Panel(data)
print p
```


执行上面示例代码，得到以下结果 - 

```
<class 'pandas.core.panel.Panel'>
Dimensions: 2 (items) x 4 (major_axis) x 5 (minor_axis)
Items axis: 0 to 1
Major_axis axis: 0 to 3
Minor_axis axis: 0 to 4
```



> 注意 - 观察空面板和上面板的尺寸大小，所有对象都不同。

### 2.2 从DataFrame对象的dict创建面板

```
#creating an empty panel
import pandas as pd
import numpy as np

data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)), 
        'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
print p
```


执行上面示例代码，得到以下结果 - 

```
<class 'pandas.core.panel.Panel'>
Dimensions: 2 (items) x 4 (major_axis) x 5 (minor_axis)
Items axis: 0 to 1
Major_axis axis: 0 to 3
Minor_axis axis: 0 to 4
```



### 2.3 创建一个空面板

可以使用`Panel`的构造函数创建一个空面板，如下所示：

```
#creating an empty panel
import pandas as pd
p = pd.Panel()
print p
```


执行上面示例代码，得到以下结果 - 

```
<class 'pandas.core.panel.Panel'>
Dimensions: 0 (items) x 0 (major_axis) x 0 (minor_axis)
Items axis: None
Major_axis axis: None
Minor_axis axis: None
```



## 3. 从面板中选择数据

要从面板中选择数据，可以使用以下方式 -

* Items
* Major_axis
* Minor_axis

**使用Items**

<ins class="adsbygoogle" style="display:inline-block;width:728px;height:90px" data-ad-client="ca-pub-1090193214637198" data-ad-slot="6494738921"></ins>

```
# creating an empty panel
import pandas as pd
import numpy as np
data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)), 
        'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
print p['Item1']
```


执行上面示例代码，得到以下结果 - 

```
0          1          2
0    0.488224  -0.128637   0.930817
1    0.417497   0.896681   0.576657
2   -2.775266   0.571668   0.290082
3   -0.400538  -0.144234   1.110535
```



上面示例有两个数据项，这里只检索`item1`。结果是具有`4`行和`3`列的数据帧(`DataFrame`)，它们是`Major_axis`和`Minor_axis`维。

**使用major_axis**

可以使用`panel.major_axis(index)`方法访问数据。参考以下示例代码 - 

```
# creating an empty panel
import pandas as pd
import numpy as np
data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)), 
        'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
print p.major_xs(1)
```


执行上面示例代码，得到以下结果 - 

```
Item1       Item2
0   0.417497    0.748412
1   0.896681   -0.557322
2   0.576657       NaN
```



**使用minor_axis**

可以使用`panel.minor_axis(index)`方法访问数据。参考以下示例代码 - 

```
# creating an empty panel
import pandas as pd
import numpy as np
data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)), 
        'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
print p.minor_xs(1)
```


执行上面示例代码，得到以下结果 - 

```
Item1       Item2
0   -0.128637   -1.047032
1    0.896681   -0.557322
2    0.571668    0.431953
3   -0.144234    1.302466
```



> 注意 - 观察尺寸大不的变化。

# Pandas基本功能

到目前为止，我们了解了三种_Pandas_数据结构以及如何创建它们。接下来将主要关注数据帧(DataFrame)对象，因为它在实时数据处理中非常重要，并且还讨论其他数据结构。

## 系列基本功能

| 编号 | 属性或方法    | 描述                  |
| -- | -------- | ------------------- |
| 1  | `axes`   | 返回行轴标签列表。           |
| 2  | `dtype`  | 返回对象的数据类型(`dtype`)。 |
| 3  | `empty`  | 如果系列为空，则返回`True`。   |
| 4  | `ndim`   | 返回底层数据的维数，默认定义：`1`。 |
| 5  | `size`   | 返回基础数据中的元素数。        |
| 6  | `values` | 将系列作为`ndarray`返回。   |
| 7  | `head()` | 返回前`n`行。            |
| 8  | `tail()` | 返回最后`n`行。           |

现在创建一个系列并演示如何使用上面所有列出的属性操作。

**示例**

```
import pandas as pd
import numpy as np

#Create a series with 100 random numbers
s = pd.Series(np.random.randn(4))
print s
```


执行上面示例代码，得到以下输出结果 - 

```
0   0.967853
1  -0.148368
2  -1.395906
3  -1.758394
dtype: float64
```


**axes示例**

返回系列的标签列表。参考以下示例代码 - 

```
import pandas as pd
import numpy as np

#Create a series with 100 random numbers
s = pd.Series(np.random.randn(4))
print ("The axes are:")
print s.axes
```


执行上面示例代码，得到以下输出结果 - 

```
The axes are:
[RangeIndex(start=0, stop=4, step=1)]
```


上述结果是从`0`到`5`的值列表的紧凑格式，即：`[0,1,2,3,4]`。

**empty示例**

返回布尔值，表示对象是否为空。返回`True`则表示对象为空。

```
import pandas as pd
import numpy as np

#Create a series with 100 random numbers
s = pd.Series(np.random.randn(4))
print ("Is the Object empty?")
print s.empty
```


执行上面示例代码，得到以下输出结果 - 

```
Is the Object empty?
False
```


**ndim示例**

返回对象的维数。根据定义，一个系列是一个`1D`数据结构，参考以下示例代码 - 

```
import pandas as pd
import numpy as np

#Create a series with 4 random numbers
s = pd.Series(np.random.randn(4))
print s

print ("The dimensions of the object:")
print s.ndim
```


执行上面示例代码，得到以下结果 - 

```
0   0.175898
1   0.166197
2  -0.609712
3  -1.377000
dtype: float64

The dimensions of the object:
1
```



**size示例**

返回系列的大小(长度)。参考以下示例代码 - 

```
import pandas as pd
import numpy as np

#Create a series with 4 random numbers
s = pd.Series(np.random.randn(2))
print s
print ("The size of the object:")
print s.size
```


执行上面示例代码，得到以下结果 - 

```
0   3.078058
1  -1.207803
dtype: float64

The size of the object:
2
```



**values示例**

以数组形式返回系列中的实际数据值。

```
import pandas as pd
import numpy as np

#Create a series with 4 random numbers
s = pd.Series(np.random.randn(4))
print s

print ("The actual data series is:")
print s.values
```


执行上面示例代码，得到以下结果 - 

```
0   1.787373
1  -0.605159
2   0.180477
3  -0.140922
dtype: float64

The actual data series is:
[ 1.78737302 -0.60515881 0.18047664 -0.1409218 ]
```



**head()和tail()方法示例**

要查看Series或DataFrame对象的小样本，请使用`head()`和`tail()`方法。

`head()`返回前`n`行(观察索引值)。要显示的元素的默认数量为`5`，但可以传递自定义这个数字值。

```
import pandas as pd
import numpy as np

#Create a series with 4 random numbers
s = pd.Series(np.random.randn(4))
print ("The original series is:")
print s

print ("The first two rows of the data series:")
print s.head(2)
```


执行上面示例代码，得到以下结果 - 

```
The original series is:
0   0.720876
1  -0.765898
2   0.479221
3  -0.139547
dtype: float64

The first two rows of the data series:
0   0.720876
1  -0.765898
dtype: float64
```



`tail()`返回最后`n`行(观察索引值)。 要显示的元素的默认数量为`5`，但可以传递自定义数字值。参考以下示例代码 - 

```
import pandas as pd
import numpy as np

#Create a series with 4 random numbers
s = pd.Series(np.random.randn(4))
print ("The original series is:")
print s

print ("The last two rows of the data series:")
print s.tail(2)
```


执行上面示例代码，得到以下结果 - 

```
The original series is:
0 -0.655091
1 -0.881407
2 -0.608592
3 -2.341413
dtype: float64

The last two rows of the data series:
2 -0.608592
3 -2.341413
dtype: float64
```



## DataFrame基本功能

下面来看看数据帧(DataFrame)的基本功能有哪些？下表列出了DataFrame基本功能的重要属性或方法。

| 编号 | 属性或方法    | 描述                                             |
| -- | -------- | ---------------------------------------------- |
| 1  | `T`      | 转置行和列。                                         |
| 2  | `axes`   | 返回一个列，行轴标签和列轴标签作为唯一的成员。                        |
| 3  | `dtypes` | 返回此对象中的数据类型(`dtypes`)。                         |
| 4  | `empty`  | 如果`NDFrame`完全为空[无项目]，则返回为`True`; 如果任何轴的长度为`0`。 |
| 5  | `ndim`   | 轴/数组维度大小。                                      |
| 6  | `shape`  | 返回表示`DataFrame`的维度的元组。                         |
| 7  | `size`   | `NDFrame`中的元素数。                                |
| 8  | `values` | NDFrame的Numpy表示。                               |
| 9  | `head()` | 返回开头前`n`行。                                     |
| 10 | `tail()` | 返回最后`n`行。                                      |

下面来看看如何创建一个DataFrame并使用上述属性和方法。

**示例**

```
import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}

#Create a DataFrame
df = pd.DataFrame(d)
print ("Our data series is:")
print df
```


执行上面示例代码，得到以下结果 - 

```
Our data series is:
    Age   Name    Rating
0   25    Tom     4.23
1   26    James   3.24
2   25    Ricky   3.98
3   23    Vin     2.56
4   30    Steve   3.20
5   29    Minsu   4.60
6   23    Jack    3.80
```



**T(转置)示例**

返回`DataFrame`的转置。行和列将交换。参考以下示例代码 - 

```
import pandas as pd
import numpy as np

# Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}

# Create a DataFrame
df = pd.DataFrame(d)
print ("The transpose of the data series is:")
print df.T
```


执行上面示例代码，得到以下结果 - 

```
The transpose of the data series is:
         0     1       2      3      4      5       6
Age      25    26      25     23     30     29      23
Name     Tom   James   Ricky  Vin    Steve  Minsu   Jack
Rating   4.23  3.24    3.98   2.56   3.2    4.6     3.8
```



**axes示例**

返回行轴标签和列轴标签列表。参考以下示例代码 - 

```
import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}

#Create a DataFrame
df = pd.DataFrame(d)
print ("Row axis labels and column axis labels are:")
print df.axes
```


执行上面示例代码，得到以下结果 - 

```
Row axis labels and column axis labels are:

[RangeIndex(start=0, stop=7, step=1), Index([u'Age', u'Name', u'Rating'],
dtype='object')]
```



**dtypes示例**

返回每列的数据类型。参考以下示例代码 - 

```
import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}

#Create a DataFrame
df = pd.DataFrame(d)
print ("The data types of each column are:")
print df.dtypes
```


执行上面示例代码，得到以下结果 - 

```
The data types of each column are:
Age     int64
Name    object
Rating  float64
dtype: object
```



**empty示例**

返回布尔值，表示对象是否为空; 返回`True`表示对象为空。

<ins class="adsbygoogle" style="display:inline-block;width:728px;height:90px" data-ad-client="ca-pub-1090193214637198" data-ad-slot="6494738921"></ins>

```
import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}

#Create a DataFrame
df = pd.DataFrame(d)
print ("Is the object empty?")
print df.empty
```


执行上面示例代码，得到以下结果 - 

```
Is the object empty?
False
```



**ndim示例**

返回对象的维数。根据定义，DataFrame是一个`2D`对象。参考以下示例代码 - 

```
import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}

#Create a DataFrame
df = pd.DataFrame(d)
print ("Our object is:")
print df
print ("The dimension of the object is:")
print df.ndim
```


执行上面示例代码，得到以下结果 - 

```
Our object is:
      Age    Name     Rating
0     25     Tom      4.23
1     26     James    3.24
2     25     Ricky    3.98
3     23     Vin      2.56
4     30     Steve    3.20
5     29     Minsu    4.60
6     23     Jack     3.80

The dimension of the object is:
2
```



**shape示例**

返回表示`DataFrame`的维度的元组。 元组`(a，b)`，其中`a`表示行数，`b`表示列数。

```
import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}

#Create a DataFrame
df = pd.DataFrame(d)
print ("Our object is:")
print df
print ("The shape of the object is:")
print df.shape
```


执行上面示例代码，得到以下结果 - 

```
Our object is:
   Age   Name    Rating
0  25    Tom     4.23
1  26    James   3.24
2  25    Ricky   3.98
3  23    Vin     2.56
4  30    Steve   3.20
5  29    Minsu   4.60
6  23    Jack    3.80

The shape of the object is:
(7, 3)
```



**size示例**

返回DataFrame中的元素数。参考以下示例代码 - 

```
import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}

#Create a DataFrame
df = pd.DataFrame(d)
print ("Our object is:")
print df
print ("The total number of elements in our object is:")
print df.size
```


执行上面示例代码，得到以下结果 - 

```
Our object is:
    Age   Name    Rating
0   25    Tom     4.23
1   26    James   3.24
2   25    Ricky   3.98
3   23    Vin     2.56
4   30    Steve   3.20
5   29    Minsu   4.60
6   23    Jack    3.80

The total number of elements in our object is:
21
```



**values示例**

将`DataFrame`中的实际数据作为`NDarray`返回。参考以下示例代码 - 

```
import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}

#Create a DataFrame
df = pd.DataFrame(d)
print ("Our object is:")
print df
print ("The actual data in our data frame is:")
print df.values
```


执行上面示例代码，得到以下结果 - 

```
Our object is:
    Age   Name    Rating
0   25    Tom     4.23
1   26    James   3.24
2   25    Ricky   3.98
3   23    Vin     2.56
4   30    Steve   3.20
5   29    Minsu   4.60
6   23    Jack    3.80
The actual data in our data frame is:
[[25 'Tom' 4.23]
[26 'James' 3.24]
[25 'Ricky' 3.98]
[23 'Vin' 2.56]
[30 'Steve' 3.2]
[29 'Minsu' 4.6]
[23 'Jack' 3.8]]
```



**head()和tail()示例**

要查看DataFrame对象的小样本，可使用`head()`和`tail()`方法。`head()`返回前`n`行(观察索引值)。显示元素的默认数量为`5`，但可以传递自定义数字值。参考以下示例代码 - 

```
import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}

#Create a DataFrame
df = pd.DataFrame(d)
print ("Our data frame is:")
print df
print ("The first two rows of the data frame is:")
print df.head(2)
```


执行上面示例代码，得到以下结果 - 

```
Our data frame is:
    Age   Name    Rating
0   25    Tom     4.23
1   26    James   3.24
2   25    Ricky   3.98
3   23    Vin     2.56
4   30    Steve   3.20
5   29    Minsu   4.60
6   23    Jack    3.80

The first two rows of the data frame is:
   Age   Name   Rating
0  25    Tom    4.23
1  26    James  3.24
```



`tail()`返回最后`n`行(观察索引值)。显示元素的默认数量为`5`，但可以传递自定义数字值。

```
import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]), 
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}

#Create a DataFrame
df = pd.DataFrame(d)
print ("Our data frame is:")
print df
print ("The last two rows of the data frame is:")
print df.tail(2)
```


执行上面示例代码，得到以下结果 - 

```
Our data frame is:
    Age   Name    Rating
0   25    Tom     4.23
1   26    James   3.24
2   25    Ricky   3.98
3   23    Vin     2.56
4   30    Steve   3.20
5   29    Minsu   4.60
6   23    Jack    3.80

The last two rows of the data frame is:
    Age   Name    Rating
5   29    Minsu    4.6
6   23    Jack     3.8
```

# Pandas描述性统计

有很多方法用来集体计算`DataFrame`的描述性统计信息和其他相关操作。 其中大多数是`sum()`，`mean()`等聚合函数，但其中一些，如`sumsum()`，产生一个相同大小的对象。 一般来说，这些方法采用轴参数，就像`ndarray.{sum，std，...}`，但轴可以通过名称或整数来指定：

* _数据帧(DataFrame)_ - “index”(axis=0，默认)，columns(axis=1)

下面创建一个数据帧(DataFrame)，并使用此对象进行演示本章中所有操作。

**示例**

```
import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}

#Create a DataFrame
df = pd.DataFrame(d)
print df
```


执行上面示例代码，得到以下结果 - 

```
Age  Name   Rating
0   25   Tom     4.23
1   26   James   3.24
2   25   Ricky   3.98
3   23   Vin     2.56
4   30   Steve   3.20
5   29   Minsu   4.60
6   23   Jack    3.80
7   34   Lee     3.78
8   40   David   2.98
9   30   Gasper  4.80
10  51   Betina  4.10
11  46   Andres  3.65
```



**sum()方法**

返回所请求轴的值的总和。 默认情况下，轴为索引(`axis=0`)。

```
import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}

#Create a DataFrame
df = pd.DataFrame(d)
print df.sum()
```


执行上面示例代码，得到以下结果 - 

```
Age                                                    382
Name     TomJamesRickyVinSteveMinsuJackLeeDavidGasperBe...
Rating                                               44.92
dtype: object
```



每个单独的列单独添加(附加字符串)。

**axis=1示例**

此语法将给出如下所示的输出，参考以下示例代码 - 

```
import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}

#Create a DataFrame
df = pd.DataFrame(d)
print df.sum(1)
```


执行上面示例代码，得到以下结果 - 

```
0    29.23
1    29.24
2    28.98
3    25.56
4    33.20
5    33.60
6    26.80
7    37.78
8    42.98
9    34.80
10   55.10
11   49.65
dtype: float64
```



**mean()示例**  
返回平均值，参考以下示例代码 - 

```
import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}

#Create a DataFrame
df = pd.DataFrame(d)
print df.mean()
```


执行上面示例代码，得到以下结果 - 

```
Age       31.833333
Rating     3.743333
dtype: float64
```



**std()示例**

返回数字列的Bressel标准偏差。

```
import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}

#Create a DataFrame
df = pd.DataFrame(d)
print df.std()
```


执行上面示例代码，得到以下结果 - 

```
Age       9.232682
Rating    0.661628
dtype: float64
```



## 函数和说明

下面来了解Python Pandas中描述性统计信息的函数，下表列出了重要函数 -

| 编号 | 函数          | 描述       |
| -- | ----------- | -------- |
| 1  | `count()`   | 非空观测数量   |
| 2  | `sum()`     | 所有值之和    |
| 3  | `mean()`    | 所有值的平均值  |
| 4  | `median()`  | 所有值的中位数  |
| 5  | `mode()`    | 值的模值     |
| 6  | `std()`     | 值的标准偏差   |
| 7  | `min()`     | 所有值中的最小值 |
| 8  | `max()`     | 所有值中的最大值 |
| 9  | `abs()`     | 绝对值      |
| 10 | `prod()`    | 数组元素的乘积  |
| 11 | `cumsum()`  | 累计总和     |
| 12 | `cumprod()` | 累计乘积     |

> 注 - 由于DataFrame是异构数据结构。通用操作不适用于所有函数。

* 类似于：`sum()`，`cumsum()`函数能与数字和字符(或)字符串数据元素一起工作，不会产生任何错误。字符聚合从来都比较少被使用，虽然这些函数不会引发任何异常。
* 由于这样的操作无法执行，因此，当DataFrame包含字符或字符串数据时，像`abs()`，`cumprod()`这样的函数会抛出异常。

## 汇总数据

`describe()`函数是用来计算有关DataFrame列的统计信息的摘要。

<ins class="adsbygoogle" style="display:inline-block;width:728px;height:90px" data-ad-client="ca-pub-1090193214637198" data-ad-slot="6494738921"></ins>

```
import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}

#Create a DataFrame
df = pd.DataFrame(d)
print df.describe()
```


执行上面示例代码，得到以下结果 - 

```
Age         Rating
count    12.000000      12.000000
mean     31.833333       3.743333
std       9.232682       0.661628
min      23.000000       2.560000
25%      25.000000       3.230000
50%      29.500000       3.790000
75%      35.500000       4.132500
max      51.000000       4.800000
```



该函数给出了平均值，标准差和IQR值。 而且，函数排除字符列，并给出关于数字列的摘要。 `include`是用于传递关于什么列需要考虑用于总结的必要信息的参数。获取值列表; 默认情况下是”数字值”。

* `object` - 汇总字符串列
* `number` - 汇总数字列
* `all` - 将所有列汇总在一起(不应将其作为列表值传递)

现在，在程序中使用以下语句并检查输出 -

```
import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}

#Create a DataFrame
df = pd.DataFrame(d)
print df.describe(include=['object'])
```


执行上面示例代码，得到以下结果 - 

```
Name
count       12
unique      12
top      Ricky
freq         1
```



现在，使用以下语句并查看输出 -

```
import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}

#Create a DataFrame
df = pd.DataFrame(d)
print df. describe(include='all')
```



执行上面示例代码，得到以下结果 - 

```
Age          Name       Rating
count   12.000000        12    12.000000
unique        NaN        12          NaN
top           NaN     Ricky          NaN
freq          NaN         1          NaN
mean    31.833333       NaN     3.743333
std      9.232682       NaN     0.661628
min     23.000000       NaN     2.560000
25%     25.000000       NaN     3.230000
50%     29.500000       NaN     3.790000
75%     35.500000       NaN     4.132500
max     51.000000       NaN     4.800000
```

# Pandas函数应用

要将自己或其他库的函数应用于_Pandas_对象，应该了解三种重要的方法。以下讨论了这些方法。 使用适当的方法取决于函数是否期望在整个`DataFrame`，行或列或元素上进行操作。

* 表明智函数应用：`pipe()`
* 行或列函数应用：`apply()`
* 元素函数应用：`applymap()`

## 表格函数应用

可以通过将函数和适当数量的参数作为管道参数来执行自定义操作。 因此，对整个DataFrame执行操作。

例如，为DataFrame中的所有元素相加一个值`2`。 然后，

**加法器函数**

加法器函数将两个数值作为参数添加并返回总和。

```
def adder(ele1,ele2):
return ele1+ele2
```


现在将使用自定义函数对DataFrame进行操作。

```
df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df.pipe(adder,2)
```


下面来看看完整的程序 -

```
import pandas as pd
import numpy as np

def adder(ele1,ele2):
   return ele1+ele2

df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df.pipe(adder,2)
print df
```


执行上面示例代码，得到以下结果 - 

```
col1       col2       col3
0   2.176704   2.219691   1.509360
1   2.222378   2.422167   3.953921
2   2.241096   1.135424   2.696432
3   2.355763   0.376672   1.182570
4   2.308743   2.714767   2.130288
```



## 行或列智能函数应用

可以使用`apply()`方法沿`DataFrame`或`Panel`的轴应用任意函数，它与描述性统计方法一样，采用可选的轴参数。 默认情况下，操作按列执行，将每列列为数组。

**示例**

```
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df.apply(np.mean)
print df
```


执行上面示例代码，得到以下结果 - 

```
col1       col2        col3                                                      
0   0.343569  -1.013287    1.131245 

1   0.508922  -0.949778   -1.600569 

2  -1.182331  -0.420703   -1.725400

3   0.860265   2.069038   -0.537648

4   0.876758  -0.238051    0.473992
```



通过传递`axis`参数，可以在行上执行操作。

**示例-2**

```
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df.apply(np.mean,axis=1)
print df
```


执行上面示例代码，得到以下结果 - 

```
col1         col2         col3

0  0.543255    -1.613418    -0.500731   

1  0.976543    -1.135835    -0.719153   

2  0.184282    -0.721153    -2.876206    

3  0.447738     0.268062    -1.937888

4 -0.677673     0.177455     1.397360
```



**示例-3**

<ins class="adsbygoogle" style="display:inline-block;width:728px;height:90px" data-ad-client="ca-pub-1090193214637198" data-ad-slot="6494738921"></ins>

```
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df.apply(lambda x: x.max() - x.min())
print df
```


执行上面示例代码，得到以下结果 - 

```
col1        col2      col3

0   -0.585206   -0.104938   1.424115 

1   -0.326036   -1.444798   0.196849 

2   -2.033478    1.682253   1.223152  

3   -0.107015    0.499846   0.084127

4   -1.046964   -1.935617  -0.009919
```



## 元素智能函数应用

并不是所有的函数都可以向量化(也不是返回另一个数组的NumPy数组，也不是任何值)，在DataFrame上的方法`applymap()`和类似地在Series上的`map()`接受任何Python函数，并且返回单个值。

**示例-1**

```
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])

# My custom function
df['col1'].map(lambda x:x*100)
print df
```


执行上面示例代码，得到以下结果 - 

```
col1      col2       col3    

0    0.629348  0.088467  -1.790702 

1   -0.592595  0.184113  -1.524998

2   -0.419298  0.262369  -0.178849

3   -1.036930  1.103169   0.941882 

4   -0.573333 -0.031056   0.315590
```



**示例-2**

```
import pandas as pd
import numpy as np

# My custom function
df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df.applymap(lambda x:x*100)
print df
```


执行上面示例代码，得到以下结果 -

```
output is as follows:
         col1         col2         col3
0   17.670426    21.969052    -49.064031
1   22.237846    42.216693     195.392124
2   24.109576   -86.457646     69.643171
3   35.576312   -162.332803   -81.743023
4   30.874333    71.476717     13.028751
```

# Pandas重建索引

重新索引会更改DataFrame的行标签和列标签。重新索引意味着符合数据以匹配特定轴上的一组给定的标签。

可以通过索引来实现多个操作 -

* 重新排序现有数据以匹配一组新的标签。
* 在没有标签数据的标签位置插入缺失值(NA)标记。

**示例**

```
import pandas as pd
import numpy as np

N=20

df = pd.DataFrame({
   'A': pd.date_range(start='2016-01-01',periods=N,freq='D'),
   'x': np.linspace(0,stop=N-1,num=N),
   'y': np.random.rand(N),
   'C': np.random.choice(['Low','Medium','High'],N).tolist(),
   'D': np.random.normal(100, 10, size=(N)).tolist()
})

#reindex the DataFrame
df_reindexed = df.reindex(index=[0,2,5], columns=['A', 'C', 'B'])

print (df_reindexed)
```


执行上面示例代码，得到以下结果 - 

```
A    C     B
0  2016-01-01  Low   NaN
2  2016-01-03  High  NaN
5  2016-01-06  Low   NaN
```



## 重建索引与其他对象对齐

有时可能希望采取一个对象和重新索引，其轴被标记为与另一个对象相同。 考虑下面的例子来理解这一点。

**示例**

```
import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.random.randn(10,3),columns=['col1','col2','col3'])
df2 = pd.DataFrame(np.random.randn(7,3),columns=['col1','col2','col3'])

df1 = df1.reindex_like(df2)
print df1
```


执行上面示例代码，得到以下结果 - 

```
col1         col2         col3
0    -2.467652    -1.211687    -0.391761
1    -0.287396     0.522350     0.562512
2    -0.255409    -0.483250     1.866258
3    -1.150467    -0.646493    -0.222462
4     0.152768    -2.056643     1.877233
5    -1.155997     1.528719    -1.343719
6    -1.015606    -1.245936    -0.295275
```



> 注意 - 在这里，`df1`数据帧(_DataFrame_)被更改并重新编号，如`df2`。 列名称应该匹配，否则将为整个列标签添加`NAN`。

## 填充时重新加注

`reindex()`采用可选参数方法，它是一个填充方法，其值如下：

* `pad/ffill` - 向前填充值
* `bfill/backfill` - 向后填充值
* `nearest`  - 从最近的索引值填充

**示例**

```
import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
df2 = pd.DataFrame(np.random.randn(2,3),columns=['col1','col2','col3'])

# Padding NAN's
print df2.reindex_like(df1)

# Now Fill the NAN's with preceding Values
print ("Data Frame with Forward Fill:")
print df2.reindex_like(df1,method='ffill')
```


执行上面示例代码时，得到以下结果 - 

```
col1        col2       col3
0    1.311620   -0.707176   0.599863
1   -0.423455   -0.700265   1.133371
2         NaN         NaN        NaN
3         NaN         NaN        NaN
4         NaN         NaN        NaN
5         NaN         NaN        NaN

Data Frame with Forward Fill:
         col1        col2        col3
0    1.311620   -0.707176    0.599863
1   -0.423455   -0.700265    1.133371
2   -0.423455   -0.700265    1.133371
3   -0.423455   -0.700265    1.133371
4   -0.423455   -0.700265    1.133371
5   -0.423455   -0.700265    1.133371
```



> 注 - 最后四行被填充了。

## 重建索引时的填充限制

限制参数在重建索引时提供对填充的额外控制。限制指定连续匹配的最大计数。考虑下面的例子来理解这个概念 -

**示例**

<ins class="adsbygoogle" style="display:inline-block;width:728px;height:90px" data-ad-client="ca-pub-1090193214637198" data-ad-slot="6494738921"></ins>

```
import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
df2 = pd.DataFrame(np.random.randn(2,3),columns=['col1','col2','col3'])

# Padding NAN's
print df2.reindex_like(df1)

# Now Fill the NAN's with preceding Values
print ("Data Frame with Forward Fill limiting to 1:")
print df2.reindex_like(df1,method='ffill',limit=1)
```


在执行上面示例代码时，得到以下结果 - 

```
col1        col2        col3
0    0.247784    2.128727    0.702576
1   -0.055713   -0.021732   -0.174577
2         NaN         NaN         NaN
3         NaN         NaN         NaN
4         NaN         NaN         NaN
5         NaN         NaN         NaN

Data Frame with Forward Fill limiting to 1:
         col1        col2        col3
0    0.247784    2.128727    0.702576
1   -0.055713   -0.021732   -0.174577
2   -0.055713   -0.021732   -0.174577
3         NaN         NaN         NaN
4         NaN         NaN         NaN
5         NaN         NaN         NaN
```



> 注意 - 只有第`7`行由前`6`行填充。 然后，其它行按原样保留。

## 重命名

`rename()`方法允许基于一些映射(字典或者系列)或任意函数来重新标记一个轴。  
看看下面的例子来理解这一概念。

**示例**

```
import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
print df1

print ("After renaming the rows and columns:")
print df1.rename(columns={'col1' : 'c1', 'col2' : 'c2'},
index = {0 : 'apple', 1 : 'banana', 2 : 'durian'})
```


执行上面示例代码，得到以下结果 - 

```
col1        col2        col3
0    0.486791    0.105759    1.540122
1   -0.990237    1.007885   -0.217896
2   -0.483855   -1.645027   -1.194113
3   -0.122316    0.566277   -0.366028
4   -0.231524   -0.721172   -0.112007
5    0.438810    0.000225    0.435479

After renaming the rows and columns:
                c1          c2        col3
apple     0.486791    0.105759    1.540122
banana   -0.990237    1.007885   -0.217896
durian   -0.483855   -1.645027   -1.194113
3        -0.122316    0.566277   -0.366028
4        -0.231524   -0.721172   -0.112007
5         0.438810    0.000225    0.435479
```



`rename()`方法提供了一个`inplace`命名参数，默认为`False`并复制底层数据。 指定传递`inplace = True`则表示将数据重命名。

# Pandas迭代


`Pandas`对象之间的基本迭代的行为取决于类型。当迭代一个系列时，它被视为数组式，基本迭代产生这些值。其他数据结构，如：`DataFrame`和`Panel`，遵循类似惯例迭代对象的键。

简而言之，基本迭代(对于`i`在对象中)产生 -

* _Series_ - 值
* _DataFrame_ - 列标签
* _Pannel_ - 项目标签

## 迭代DataFrame

迭代`DataFrame`提供列名。现在来看看下面的例子来理解这个概念。

```
import pandas as pd
import numpy as np

N=20

df = pd.DataFrame({
    'A': pd.date_range(start='2016-01-01',periods=N,freq='D'),
    'x': np.linspace(0,stop=N-1,num=N),
    'y': np.random.rand(N),
    'C': np.random.choice(['Low','Medium','High'],N).tolist(),
    'D': np.random.normal(100, 10, size=(N)).tolist()
    })

for col in df:
   print (col)
```


执行上面示例代码，得到以下结果 - 

```
A
C
D
x
y
```



要遍历数据帧(DataFrame)中的行，可以使用以下函数 -

* `iteritems()` - 迭代`(key，value)`对
* `iterrows()` - 将行迭代为(索引，系列)对
* `itertuples()` - 以`namedtuples`的形式迭代行

**iteritems()示例**

将每个列作为键，将值与值作为键和列值迭代为Series对象。

```
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(4,3),columns=['col1','col2','col3'])
for key,value in df.iteritems():
   print (key,value)
```


执行上面示例代码，得到以下结果 - 

```
col1 0    0.802390
1    0.324060
2    0.256811
3    0.839186
Name: col1, dtype: float64

col2 0    1.624313
1   -1.033582
2    1.796663
3    1.856277
Name: col2, dtype: float64

col3 0   -0.022142
1   -0.230820
2    1.160691
3   -0.830279
Name: col3, dtype: float64
```



观察一下，单独迭代每个列作为系列中的键值对。

**iterrows()示例**

`iterrows()`返回迭代器，产生每个索引值以及包含每行数据的序列。

```
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(4,3),columns = ['col1','col2','col3'])
for row_index,row in df.iterrows():
   print (row_index,row)
```


执行上面示例代码，得到以下结果 - 

```
0  col1    1.529759
   col2    0.762811
   col3   -0.634691
Name: 0, dtype: float64

1  col1   -0.944087
   col2    1.420919
   col3   -0.507895
Name: 1, dtype: float64

2  col1   -0.077287
   col2   -0.858556
   col3   -0.663385
Name: 2, dtype: float64
3  col1    -1.638578
   col2     0.059866
   col3     0.493482
Name: 3, dtype: float64
```



> 注意 - 由于`iterrows()`遍历行，因此不会跨该行保留数据类型。`0`,`1`,`2`是行索引，`col1`，`col2`，`col3`是列索引。

**itertuples()示例**

`itertuples()`方法将为`DataFrame`中的每一行返回一个产生一个命名元组的迭代器。元组的第一个元素将是行的相应索引值，而剩余的值是行值。

**示例**

<ins class="adsbygoogle" style="display:inline-block;width:728px;height:90px" data-ad-client="ca-pub-1090193214637198" data-ad-slot="6494738921"></ins>

```
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(4,3),columns = ['col1','col2','col3'])
for row in df.itertuples():
    print (row)
```


执行上面示例代码，得到以下结果 - 

```
Pandas(Index=0, col1=1.5297586201375899, col2=0.76281127433814944, col3=-
0.6346908238310438)

Pandas(Index=1, col1=-0.94408735763808649, col2=1.4209186418359423, col3=-
0.50789517967096232)

Pandas(Index=2, col1=-0.07728664756791935, col2=-0.85855574139699076, col3=-
0.6633852507207626)

Pandas(Index=3, col1=0.65734942534106289, col2=-0.95057710432604969,
col3=0.80344487462316527)
```



> 注意 - 不要尝试在迭代时修改任何对象。迭代是用于读取，迭代器返回原始对象(视图)的副本，因此更改将不会反映在原始对象上。

**示例代码**

```
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(4,3),columns = ['col1','col2','col3'])

for index, row in df.iterrows():
   row['a'] = 10
print (df)
```


执行上面示例代码，得到以下结果 - 

```
      col1       col2       col3
0  -1.739815   0.735595  -0.295589
1   0.635485   0.106803   1.527922
2  -0.939064   0.547095   0.038585
3  -1.016509  -0.116580  -0.523158
```



注意观察结果，修改变化并未反映出来。


# Pandas排序

_Pandas_有两种排序方式，它们分别是 - 

* 按标签
* 按实际值

下面来看看一个输出的例子。

```
import pandas as pd
import numpy as np

unsorted_df=pd.DataFrame(np.random.randn(10,2),index=[1,4,6,2,3,5,9,8,0,7],colu
mns=['col2','col1'])
print (unsorted_df)
```


执行上面示例代码，得到以下结果 - 

```
    col2      col1
1  1.069838  0.096230
4 -0.542406 -0.219829
6 -0.071661  0.392091
2  1.399976 -0.472169
3  0.428372 -0.624630
5  0.471875  0.966560
9 -0.131851 -1.254495
8  1.180651  0.199548
0  0.906202  0.418524
7  0.124800  2.011962
```



在`unsorted_df`数据值中，标签和值未排序。下面来看看如何按标签来排序。

## 按标签排序

使用`sort_index()`方法，通过传递`axis`参数和排序顺序，可以对`DataFrame`进行排序。 默认情况下，按照升序对行标签进行排序。

```
import pandas as pd
import numpy as np

unsorted_df = pd.DataFrame(np.random.randn(10,2),index=[1,4,6,2,3,5,9,8,0,7],columns = ['col2','col1'])

sorted_df=unsorted_df.sort_index()
print (sorted_df)
```


执行上面示例代码，得到以下结果 - 

```
    col2      col1
0  0.431384 -0.401538
1  0.111887 -0.222582
2 -0.166893 -0.237506
3  0.476472  0.508397
4  0.670838  0.406476
5  2.065969 -0.324510
6 -0.441630  1.060425
7  0.735145  0.972447
8 -0.051904 -1.112292
9  0.134108  0.759698
```



## 排序顺序

通过将布尔值传递给升序参数，可以控制排序顺序。 来看看下面的例子来理解一下。

```
import pandas as pd
import numpy as np

unsorted_df = pd.DataFrame(np.random.randn(10,2),index=[1,4,6,2,3,5,9,8,0,7],columns = ['col2','col1'])

sorted_df = unsorted_df.sort_index(ascending=False)
print (sorted_df)
```


执行上面示例代码，得到以下结果 - 

```
    col2      col1
9  0.750452  1.754815
8  0.945238  2.079394
7  0.345238 -0.162737
6 -0.512060  0.887094
5  1.163144  0.595402
4 -0.063584 -0.185536
3 -0.275438 -2.286831
2 -1.504792 -1.222394
1  1.031234 -1.848174
0 -0.615083  0.784086
```



## 按列排列

通过传递`axis`参数值为`0`或`1`，可以对列标签进行排序。 默认情况下，`axis = 0`，逐行排列。来看看下面的例子来理解这个概念。

```
import pandas as pd
import numpy as np

unsorted_df = pd.DataFrame(np.random.randn(10,2),index=[1,4,6,2,3,5,9,8,0,7],columns = ['col2','col1'])

sorted_df=unsorted_df.sort_index(axis=1)

print (sorted_df)
```


执行上面示例代码，得到以下结果 - 

```
    col1      col2
1 -0.997962  0.736707
4  1.196464  0.703710
6 -0.387800  1.207803
2  1.614043  0.356389
3 -0.057181 -0.551742
5  1.034451 -0.731490
9 -0.564355  0.892203
8 -0.763526  0.684207
0 -1.213615  1.268649
7  0.316543 -1.450784
```



## 按值排序

像索引排序一样，`sort_values()`是按值排序的方法。它接受一个`by`参数，它将使用要与其排序值的`DataFrame`的列名称。

<ins class="adsbygoogle" style="display:inline-block;width:728px;height:90px" data-ad-client="ca-pub-1090193214637198" data-ad-slot="6494738921"></ins>

```
import pandas as pd
import numpy as np

unsorted_df = pd.DataFrame({'col1':[2,1,1,1],'col2':[1,3,2,4]})
sorted_df = unsorted_df.sort_values(by='col1')

print (sorted_df)
```


执行上面示例代码，得到以下结果 - 

```
     col1  col2
1     1     3
2     1     2
3     1     4
0     2     1
```



> 注意： 观察上面的输出结果，`col1`值被排序，相应的`col2`值和行索引将随`col1`一起改变。因此，它们看起来没有排序。

通过`by`参数指定需要列值，参考以下示例代码 - 

```
import pandas as pd
import numpy as np

unsorted_df = pd.DataFrame({'col1':[2,1,1,1],'col2':[1,3,2,4]})
sorted_df = unsorted_df.sort_values(by=['col1','col2'])

print (sorted_df)
```


执行上面示例代码，得到以下结果 - 

```
    col1  col2
2     1     2
1     1     3
3     1     4
0     2     1
```



## 排序算法

`sort_values()`提供了从`mergeesort`，`heapsort`和`quicksort`中选择算法的一个配置。`Mergesort`是唯一稳定的算法。参考以下示例代码 - 

```
import pandas as pd
import numpy as np

unsorted_df = pd.DataFrame({'col1':[2,1,1,1],'col2':[1,3,2,4]})
sorted_df = unsorted_df.sort_values(by='col1' ,kind='mergesort')

print (sorted_df)
```


执行上面示例代码，得到以下结果 - 

```
     col1  col2
1     1     3
2     1     2
3     1     4
0     2     1
```

# Pandas字符串和文本数据

在本章中，我们将使用基本系列/索引来讨论字符串操作。在随后的章节中，将学习如何将这些字符串函数应用于数据帧(_DataFrame_)。

_Pandas_提供了一组字符串函数，可以方便地对字符串数据进行操作。 最重要的是，这些函数忽略(或排除)丢失/NaN值。

几乎这些方法都使用Python字符串函数(请参阅： http://docs.python.org/3/library/stdtypes.html#string-methods )。 因此，将Series对象转换为String对象，然后执行该操作。

下面来看看每个操作的执行和说明。

| 编号 | 函数                    | 描述                                        |
| -- | --------------------- | ----------------------------------------- |
| 1  | `lower()`             | 将`Series/Index`中的字符串转换为小写。                |
| 2  | `upper()`             | 将`Series/Index`中的字符串转换为大写。                |
| 3  | `len()`               | 计算字符串长度。                                  |
| 4  | `strip()`             | 帮助从两侧的系列/索引中的每个字符串中删除空格(包括换行符)。           |
| 5  | `split(' ')`          | 用给定的模式拆分每个字符串。                            |
| 6  | `cat(sep=' ')`        | 使用给定的分隔符连接系列/索引元素。                        |
| 7  | `get_dummies()`       | 返回具有单热编码值的数据帧(DataFrame)。                 |
| 8  | `contains(pattern)`   | 如果元素中包含子字符串，则返回每个元素的布尔值`True`，否则为`False`。 |
| 9  | `replace(a,b)`        | 将值`a`替换为值`b`。                             |
| 10 | `repeat(value)`       | 重复每个元素指定的次数。                              |
| 11 | `count(pattern)`      | 返回模式中每个元素的出现总数。                           |
| 12 | `startswith(pattern)` | 如果系列/索引中的元素以模式开始，则返回`true`。               |
| 13 | `endswith(pattern)`   | 如果系列/索引中的元素以模式结束，则返回`true`。               |
| 14 | `find(pattern)`       | 返回模式第一次出现的位置。                             |
| 15 | `findall(pattern)`    | 返回模式的所有出现的列表。                             |
| 16 | `swapcase`            | 变换字母大小写。                                  |
| 17 | `islower()`           | 检查系列/索引中每个字符串中的所有字符是否小写，返回布尔值             |
| 18 | `isupper()`           | 检查系列/索引中每个字符串中的所有字符是否大写，返回布尔值             |
| 19 | `isnumeric()`         | 检查系列/索引中每个字符串中的所有字符是否为数字，返回布尔值。           |

现在创建一个系列，看看上述所有函数是如何工作的。

```
import pandas as pd
import numpy as np

s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t', np.nan, '1234','SteveMinsu'])

print (s)
```


执行上面示例代码，得到以下结果 - 

```
0             Tom
1    William Rick
2            John
3         Alber@t
4             NaN
5            1234
6      SteveMinsu
dtype: object
```



**1. lower()函数示例**

```
import pandas as pd
import numpy as np

s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t', np.nan, '1234','SteveMinsu'])

print (s.str.lower())
```


执行上面示例代码，得到以下结果 - 

```
0             tom
1    william rick
2            john
3         alber@t
4             NaN
5            1234
6      steveminsu
dtype: object
```



**2. upper()函数示例**

```
import pandas as pd
import numpy as np

s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t', np.nan, '1234','SteveMinsu'])

print (s.str.upper())
```


执行上面示例代码，得到以下结果 - 

```
0             TOM
1    WILLIAM RICK
2            JOHN
3         ALBER@T
4             NaN
5            1234
6      STEVESMITH
dtype: object
```



**3. len()函数示例**

```
import pandas as pd
import numpy as np

s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t', np.nan, '1234','SteveMinsu'])
print (s.str.len())
```


执行上面示例代码，得到以下结果 - 

```
0     3.0
1    12.0
2     4.0
3     7.0
4     NaN
5     4.0
6    10.0
dtype: float64
```



**4. strip()函数示例**

```
import pandas as pd
import numpy as np
s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print (s)
print ("=========== After Stripping ================")
print (s.str.strip())
```


执行上面示例代码，得到以下结果 - 

```
0             Tom 
1     William Rick
2             John
3          Alber@t
dtype: object
=========== After Stripping ================
0             Tom
1    William Rick
2            John
3         Alber@t
dtype: object
```



**5. split(pattern)函数示例**

```
import pandas as pd
import numpy as np
s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print (s)
print ("================= Split Pattern: ==================")
print (s.str.split(' '))
```


执行上面示例代码，得到以下结果 - 

```
0             Tom 
1     William Rick
2             John
3          Alber@t
dtype: object
================= Split Pattern: ==================
0              [Tom, ]
1    [, William, Rick]
2               [John]
3            [Alber@t]
dtype: object
```



**6. cat(sep=pattern)函数示例**

```
import pandas as pd
import numpy as np

s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])

print (s.str.cat(sep=' <=> '))
```


执行上面示例代码，得到以下结果 - 

```
Tom  <=>  William Rick <=> John <=> Alber@t
```



**7. get_dummies()函数示例**

```
import pandas as pd
import numpy as np

s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])

print (s.str.get_dummies())
```


执行上面示例代码，得到以下结果 - 

```
William Rick  Alber@t  John  Tom 
0              0        0     0     1
1              1        0     0     0
2              0        0     1     0
3              0        1     0     0
```



**8. contains()函数示例**

```
import pandas as pd
s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print (s.str.contains(' '))
```


执行上面示例代码，得到以下结果 - 

```
0     True
1     True
2    False
3    False
dtype: bool
```



**9. replace(a,b)函数示例**

<ins class="adsbygoogle" style="display:inline-block;width:728px;height:90px" data-ad-client="ca-pub-1090193214637198" data-ad-slot="6494738921"></ins>

```
import pandas as pd
s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print (s)
print ("After replacing @ with $: ============== ")
print (s.str.replace('@','$'))
```


执行上面示例代码，得到以下结果 - 

```
0             Tom 
1     William Rick
2             John
3          Alber@t
dtype: object
After replacing @ with $: ============== 
0             Tom 
1     William Rick
2             John
3          Alber$t
dtype: object
```



**10. repeat(value)函数示例**

```
import pandas as pd

s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])

print (s.str.repeat(2))
```


执行上面示例代码，得到以下结果 - 

```
0                      Tom Tom 
1     William Rick William Rick
2                      JohnJohn
3                Alber@tAlber@t
dtype: object
```



**11. count(pattern)函数示例**

```
import pandas as pd

s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])

print ("The number of 'm's in each string:")
print (s.str.count('m'))
```


执行上面示例代码，得到以下结果 - 

```
The number of 'm's in each string:
0    1
1    1
2    0
3    0
dtype: int64
```



**12. startswith(pattern)函数示例**

```
import pandas as pd

s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])

print ("Strings that start with 'T':")
print (s.str. startswith ('T'))
```


执行上面示例代码，得到以下结果 - 

```
Strings that start with 'T':
0     True
1    False
2    False
3    False
dtype: bool
```



**13. endswith(pattern)函数示例**

```
import pandas as pd
s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print ("Strings that end with 't':")
print (s.str.endswith('t'))
```


执行上面示例代码，得到以下结果 - 

```
Strings that end with 't':
0    False
1    False
2    False
3     True
dtype: bool
```



**14. find(pattern)函数示例**

```
import pandas as pd
s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print (s.str.find('e'))
```


执行上面示例代码，得到以下结果 - 

```
0   -1
1   -1
2   -1
3    3
dtype: int64
```



> 注意：`-1`表示元素中没有这样的模式可用。

**15. findall(pattern)函数示例**

```
import pandas as pd

s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print (s.str.findall('e'))
```


执行上面示例代码，得到以下结果 - 

```
0     []
1     []
2     []
3    [e]
dtype: object
```



> 空列表(`[]`)表示元素中没有这样的模式可用。

**16. swapcase()函数示例**

```
import pandas as pd

s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t'])
print (s.str.swapcase())
```


执行上面示例代码，得到以下结果 - 

```
0             tOM
1    wILLIAM rICK
2            jOHN
3         aLBER@T
dtype: object
```



**17. islower()函数示例**

```
import pandas as pd

s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t'])
print (s.str.islower())
```


执行上面示例代码，得到以下结果 - 

```
0    False
1    False
2    False
3    False
dtype: bool
```



**18. isupper()函数示例**

```
import pandas as pd

s = pd.Series(['TOM', 'William Rick', 'John', 'Alber@t'])

print (s.str.isupper())
```


执行上面示例代码，得到以下结果 - 

```
0    True
1    False
2    False
3    False
dtype: bool
```



**19. isnumeric()函数示例**

```
import pandas as pd
s = pd.Series(['Tom', '1199','William Rick', 'John', 'Alber@t'])
print (s.str.isnumeric())
```


执行上面示例代码，得到以下结果 - 

```
0    False
1     True
2    False
3    False
4    False
dtype: bool
```

# Pandas选项和自定义

Pandas提供API来自定义其行为的某些方面，大多使用来显示。

API由五个相关函数组成。它们分别是 -

* _get_option()_
* _set_option()_
* _reset_option()_
* _describe_option()_
* _option_context()_

现在来了解函数是如何工作的。

## get_option(param)

`get_option(param)`需要一个参数，并返回下面输出中给出的值 -

`get_option`需要一个参数，并返回下面输出中给出的值 -

**display.max_rows**

显示默认值。解释器读取此值并显示此值作为显示上限的行。

```
import pandas as pd
print ("display.max_rows = ", pd.get_option("display.max_rows"))
```


执行上面示例代码，得到以下结果 - 

```
display.max_rows =  60
```



**display.max_columns**

显示默认值，解释器读取此值并显示此值作为显示上限的行。

```
import pandas as pd
print ("display.max_columns = ", pd.get_option("display.max_columns"))
```


执行上面示例代码，得到以下结果 - 

```
display.max_columns =  20
```



这里，`60`和`20`是默认配置参数值。

## set_option(param,value)

`set_option`需要两个参数，并将该值设置为指定的参数值，如下所示：

**display.max_rows**

使用`set_option()`，可以更改要显示的默认行数。

```
import pandas as pd

print ("before set display.max_rows = ", pd.get_option("display.max_rows")) 

pd.set_option("display.max_rows",80)
print ("after set display.max_rows = ", pd.get_option("display.max_rows"))
```


执行上面示例代码，得到以下结果 - 

```
before set display.max_rows =  60
after set display.max_rows =  80
```



**display.max_columns**

使用`set_option()`，可以更改要显示的默认行数。

```
import pandas as pd

print ("before set display.max_columns = ", pd.get_option("display.max_columns")) 

pd.set_option("display.max_columns",32)
print ("after set display.max_columns = ", pd.get_option("display.max_columns"))
```


执行上面示例代码，得到以下结果 - 

```
before set display.max_columns =  20
after set display.max_columns =  32
```



## reset_option(param)

`reset_option`接受一个参数，并将该值设置为默认值。

**display.max_rows**

使用`reset_option()`，可以将该值更改回显示的默认行数。

```
import pandas as pd

pd.set_option("display.max_rows",32)
print ("after set display.max_rows = ", pd.get_option("display.max_rows")) 

pd.reset_option("display.max_rows")
print ("reset display.max_rows = ", pd.get_option("display.max_rows"))
```


执行上面示例代码，得到以下结果 - 

```
after set display.max_rows =  32
reset display.max_rows =  60
```



## describe_option(param)

`describe_option`打印参数的描述。

**display.max_rows**

使用`reset_option()`，可以将该值更改回显示的默认行数。

<ins class="adsbygoogle" style="display:inline-block;width:728px;height:90px" data-ad-client="ca-pub-1090193214637198" data-ad-slot="6494738921"></ins>

```
import pandas as pd

pd.describe_option("display.max_rows")
```


执行上面示例代码，得到以下结果 - 

```
display.max_rows : int
    If max_rows is exceeded, switch to truncate view. Depending on
    `large_repr`, objects are either centrally truncated or printed as
    a summary view. 'None' value means unlimited.

    In case python/IPython is running in a terminal and `large_repr`
    equals 'truncate' this can be set to 0 and pandas will auto-detect
    the height of the terminal and print a truncated object which fits
    the screen height. The IPython notebook, IPython qtconsole, or
    IDLE do not run in a terminal and hence it is not possible to do
    correct auto-detection.
    [default: 60] [currently: 60]
```



## option_context()

`option_context`上下文管理器用于临时设置语句中的选项。当退出使用块时，选项值将自动恢复 -

**display.max_rows**  
使用`option_context()`，可以临时设置该值。

```
import pandas as pd
with pd.option_context("display.max_rows",10):
   print(pd.get_option("display.max_rows"))
   print(pd.get_option("display.max_rows"))
```


执行上面示例代码，得到以下结果 - 

```
10
10
```



请参阅第一和第二个打印语句之间的区别。第一个语句打印由`option_context()`设置的值，该值在上下文中是临时的。在使用上下文之后，第二个打印语句打印配置的值。

常用参数，请参考下表 - 

| 编号 | 参数                          | 描述         |
| -- | --------------------------- | ---------- |
| 1  | `display.max_rows`          | 要显示的最大行数   |
| 2  | `display.max_columns`       | 要显示的最大列数   |
| 3  | `display.expand_frame_repr` | 显示数据帧以拉伸页面 |
| 4  | `display.max_colwidth`      | 显示最大列宽     |
| 5  | `display.precision`         | 显示十进制数的精度  |

# Pandas索引和选择数据

在本章中，我们将讨论如何切割和丢弃日期，并获取_Pandas_中大对象的子集。
和NumPy索引运算符`"[]"`和属性运算符`"."`。 可以在广泛的用例中快速轻松地访问_Pandas_数据结构。然而，由于要访问的数据类型不是预先知道的，所以直接使用标准运算符具有一些优化限制。对于生产环境的代码，我们建议利用本章介绍的优化_Pandas_数据访问方法。

_Pandas_现在支持三种类型的多轴索引; 这三种类型在下表中提到 -

| 编号 | 索引        | 描述      |
| -- | --------- | ------- |
| 1  | `.loc()`  | 基于标签    |
| 2  | `.iloc()` | 基于整数    |
| 3  | `.ix()`   | 基于标签和整数 |

## .loc()

_Pandas_提供了各种方法来完成基于标签的索引。 切片时，也包括起始边界。整数是有效的标签，但它们是指标签而不是位置。

`.loc()`具有多种访问方式，如 -

* 单个标量标签
* 标签列表
* 切片对象
* 一个布尔数组

`loc`需要两个单/列表/范围运算符，用`","`分隔。第一个表示行，第二个表示列。

**示例1**

```
#import the pandas library and aliasing as pd
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4),
index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])

#select all rows for a specific column
print (df.loc[:,'A'])
```


执行上面示例代码，得到以下结果 - 

```
a    0.015860
b   -0.014135
c    0.446061
d    1.801269
e   -1.404779
f   -0.044016
g    0.996651
h    0.764672
Name: A, dtype: float64
```



**示例2**

```
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4),
index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])

# Select all rows for multiple columns, say list[]
print (df.loc[:,['A','C']])
```


执行上面示例代码，得到以下结果 - 

```
A         C
a -0.529735 -1.067299
b -2.230089 -1.798575
c  0.685852  0.333387
d  1.061853  0.131853
e  0.990459  0.189966
f  0.057314 -0.370055
g  0.453960 -0.624419
h  0.666668 -0.433971
```



**示例3**

```
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4),
index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])

# Select few rows for multiple columns, say list[]
print (df.loc[['a','b','f','h'],['A','C']])
# Select all rows for multiple columns, say list[]
print (df.loc[:,['A','C']])
```


执行上面示例代码，得到以下结果 - 

```
A         C
a -1.959731  0.720956
b  1.318976  0.199987
f -1.117735 -0.181116
h -0.147029  0.027369
          A         C
a -1.959731  0.720956
b  1.318976  0.199987
c  0.839221 -1.611226
d  0.722810  1.649130
e -0.524845 -0.037824
f -1.117735 -0.181116
g -0.642907  0.443261
h -0.147029  0.027369
```



**示例4**

```
# import the pandas library and aliasing as pd
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4),
index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])

# Select range of rows for all columns
print (df.loc['a':'h'])
```


执行上面示例代码，得到以下结果 - 

```
A         B         C         D
a  1.556186  1.765712  1.060657  0.810279
b  1.377965 -0.183283 -0.224379  0.963105
c -0.530016  0.167183 -0.066459  0.074198
d -1.515189 -1.453529 -1.559400  1.072148
e -0.487399  0.436143 -1.045622 -0.029507
f  0.552548  0.410745  0.570222 -0.628133
g  0.865293 -0.638388  0.388827 -0.469282
h -0.690596  1.765139 -0.492070 -0.176074
```



**示例5**

```
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4),
index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])

# for getting values with a boolean array
print (df.loc['a']>0)
```


执行上面示例代码，得到以下结果 - 

```
A    False
B     True
C    False
D     True
Name: a, dtype: bool
```



## .iloc()

_Pandas_提供了各种方法，以获得纯整数索引。像python和numpy一样，第一个位置是基于`0`的索引。

各种访问方式如下 -

* 整数
* 整数列表
* 系列值

**示例1**

```
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])

# select all rows for a specific column
print (df.iloc[:4])
```


执行上面示例代码，得到以下结果 - 

```
A         B         C         D
0  0.277146  0.274234  0.860555 -1.312323
1 -1.064776  2.082030  0.695930  2.409340
2  0.033953 -1.155217  0.113045 -0.028330
3  0.241075 -2.156415  0.939586 -1.670171
```



**示例2**

```
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])

# Integer slicing
print (df.iloc[:4])
print (df.iloc[1:5, 2:4])
```


执行上面示例代码，得到以下结果 - 

```
A         B         C         D
0  1.346210  0.251839  0.975964  0.319049
1  0.459074  0.038155  0.893615  0.659946
2 -1.097043  0.017080  0.869331 -1.443731
3  1.008033 -0.189436 -0.483688 -1.167312
          C         D
1  0.893615  0.659946
2  0.869331 -1.443731
3 -0.483688 -1.167312
4  1.566395 -1.292206
```



**示例3**

```
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])

# Slicing through list of values
print (df.iloc[[1, 3, 5], [1, 3]])
print (df.iloc[1:3, :])
print (df.iloc[:,1:3])
```


执行上面示例代码，得到以下结果 - 

<ins class="adsbygoogle" style="display:inline-block;width:728px;height:90px" data-ad-client="ca-pub-1090193214637198" data-ad-slot="6494738921"></ins>

```
B         D
1  0.081257  0.009109
3  1.037680 -1.467327
5  1.106721  0.320468
          A         B         C         D
1 -0.133711  0.081257 -0.031869  0.009109
2  0.895576 -0.513450 -0.048573  0.698965
          B         C
0  0.442735 -0.949859
1  0.081257 -0.031869
2 -0.513450 -0.048573
3  1.037680 -0.801157
4 -0.547456 -0.255016
5  1.106721  0.688142
6 -0.466452  0.219914
7  1.583112  0.982030
```



## .ix()

除了基于纯标签和整数之外，_Pandas_还提供了一种使用`.ix()`运算符进行选择和子集化对象的混合方法。

**示例1**

```
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])

# Integer slicing
print (df.ix[:4])
```


执行上面示例代码，得到以下结果 - 

```
A         B         C         D
0 -1.449975 -0.002573  1.349962  0.539765
1 -1.249462 -0.800467  0.483950  0.187853
2  1.361273 -1.893519  0.307613 -0.119003
3 -0.103433 -1.058175 -0.587307 -0.114262
4 -0.612298  0.873136 -0.607457  1.047772
```



**示例2**

```
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])
# Index slicing
print (df.ix[:,'A'])
```


执行上面示例代码，得到以下结果 - 

```
0    1.539915
1    1.359477
2    0.239694
3    0.563254
4    2.123950
5    0.341554
6   -0.075717
7   -0.606742
Name: A, dtype: float64
```



## 使用符号

使用多轴索引从Pandas对象获取值可使用以下符号 -

| 对象        | 索引                                           | 描述                                         |
| --------- | -------------------------------------------- | ------------------------------------------ |
| Series    | `s.loc[indexer]`                             | 标量值                                        |
| DataFrame | `df.loc[row_index,col_index]`                | 标量对象                                       |
| Panel     | `p.loc[item_index,major_index, minor_index]` | p.loc[item_index,major_index, minor_index] |

> 注意 - `.iloc()`和`.ix()`应用相同的索引选项和返回值。

现在来看看如何在DataFrame对象上执行每个操作。这里使用基本索引运算符`[]` -

**示例1**

```
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])
print (df['A'])
```


执行上面示例代码，得到以下结果 - 

```
0    0.028277
1   -1.037595
2   -0.563495
3   -1.196961
4   -0.805250
5   -0.911648
6   -0.355171
7   -0.232612
Name: A, dtype: float64
```



**示例2**

```
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])

print (df[['A','B']])
```


执行上面示例代码，得到以下结果 - 

```
A         B
0 -0.767339 -0.729411
1 -0.563540 -0.639142
2  0.873589 -2.166382
3  0.900330  0.253875
4 -0.520105  0.064438
5 -1.452176 -0.440864
6 -0.291556 -0.861924
7 -1.464235  0.313168
```



**示例3**

```
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])
print (df[2:2])
```


执行上面示例代码，得到以下结果 - 

```
Empty DataFrame
Columns: [A, B, C, D]
Index: []
```



## 属性访问

可以使用属性运算符`.`来选择列。

**示例**

```
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])

print (df.A)
```


执行上面示例代码，得到以下结果 - 

```
0    0.104820
1   -1.206600
2    0.469083
3   -0.821226
4   -1.238865
5    1.083185
6   -0.827833
7   -0.199558
Name: A, dtype: float64
```

# Pandas统计函数

统计方法有助于理解和分析数据的行为。现在我们将学习一些统计函数，可以将这些函数应用到_Pandas_的对象上。

## pct_change()函数

系列，DatFrames和Panel都有`pct_change()`函数。此函数将每个元素与其前一个元素进行比较，并计算变化百分比。

```
import pandas as pd
import numpy as np
s = pd.Series([1,2,3,4,5,4])
print (s.pct_change())

df = pd.DataFrame(np.random.randn(5, 2))
print (df.pct_change())
```


执行上面示例代码，得到以下结果 - 

```
0        NaN
1   1.000000
2   0.500000
3   0.333333
4   0.250000
5  -0.200000
dtype: float64

            0          1
0         NaN        NaN
1  -15.151902   0.174730
2  -0.746374   -1.449088
3  -3.582229   -3.165836
4   15.601150  -1.860434
```



默认情况下，`pct_change()`对列进行操作; 如果想应用到行上，那么可使用`axis = 1`参数。

## 协方差

协方差适用于系列数据。Series对象有一个方法`cov`用来计算序列对象之间的协方差。`NA`将被自动排除。

**Cov系列示例**

```
import pandas as pd
import numpy as np
s1 = pd.Series(np.random.randn(10))
s2 = pd.Series(np.random.randn(10))
print (s1.cov(s2))
```


执行上面示例代码，得到以下结果 - 

```
0.0667296739178
```


当应用于`DataFrame`时，协方差方法计算所有列之间的协方差(`cov`)值。

```
import pandas as pd
import numpy as np
frame = pd.DataFrame(np.random.randn(10, 5), columns=['a', 'b', 'c', 'd', 'e'])
print (frame['a'].cov(frame['b']))
print (frame.cov())
```


执行上面示例代码，得到以下结果 - 

```
-0.406796939839
          a         b         c         d         e
a  0.784886 -0.406797  0.181312  0.513549 -0.597385
b -0.406797  0.987106 -0.662898 -0.492781  0.388693
c  0.181312 -0.662898  1.450012  0.484724 -0.476961
d  0.513549 -0.492781  0.484724  1.571194 -0.365274
e -0.597385  0.388693 -0.476961 -0.365274  0.785044
```



> 注 - 观察第一个语句中`a`和`b`列之间的`cov`结果值，与由DataFrame上的`cov`返回的值相同。

## 相关性

相关性显示了任何两个数值(系列)之间的线性关系。有多种方法来计算`pearson`(默认)，`spearman`和`kendall`之间的相关性。

<ins class="adsbygoogle" style="display:inline-block;width:728px;height:90px" data-ad-client="ca-pub-1090193214637198" data-ad-slot="6494738921"></ins>

```
import pandas as pd
import numpy as np
frame = pd.DataFrame(np.random.randn(10, 5), columns=['a', 'b', 'c', 'd', 'e'])

print (frame['a'].corr(frame['b']))
print (frame.corr())
```


执行上面示例代码，得到以下结果 - 

```
-0.613999376618
          a         b         c         d         e
a  1.000000 -0.613999 -0.040741 -0.227761 -0.192171
b -0.613999  1.000000  0.012303  0.273584  0.591826
c -0.040741  0.012303  1.000000 -0.391736 -0.470765
d -0.227761  0.273584 -0.391736  1.000000  0.364946
e -0.192171  0.591826 -0.470765  0.364946  1.000000
```



如果DataFrame中存在任何非数字列，则会自动排除。

## 数据排名

数据排名为元素数组中的每个元素生成排名。在关系的情况下，分配平均等级。

```
import pandas as pd
import numpy as np
s = pd.Series(np.random.np.random.randn(5), index=list('abcde'))

s['d'] = s['b'] # so there's a tie

print (s.rank())
```


执行上面示例代码，得到以下结果 - 

```
a    4.0
b    1.5
c    3.0
d    1.5
e    5.0
dtype: float64
```



`Rank`可选地使用一个默认为`true`的升序参数; 当错误时，数据被反向排序，也就是较大的值被分配较小的排序。

`Rank`支持不同的`tie-breaking`方法，用方法参数指定 -

* `average` - 并列组平均排序等级
* `min` - 组中最低的排序等级
* `max` - 组中最高的排序等级
* `first` - 按照它们出现在数组中的顺序分配队列

# Pandas窗口函数 

为了处理数字数据，Pandas提供了几个变体，如滚动，展开和指数移动窗口统计的权重。 其中包括总和，均值，中位数，方差，协方差，相关性等。

下来学习如何在DataFrame对象上应用上提及的每种方法。

## .rolling()函数

这个函数可以应用于一系列数据。指定`window=n`参数并在其上应用适当的统计函数。

```
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4),
index = pd.date_range('1/1/2020', periods=10),
columns = ['A', 'B', 'C', 'D'])

print (df.rolling(window=3).mean())
```


执行上面示例代码，得到以下结果 - 

```
                   A         B         C         D
2020-01-01       NaN       NaN       NaN       NaN
2020-01-02       NaN       NaN       NaN       NaN
2020-01-03 -0.306293  0.214001 -0.076004 -0.200793
2020-01-04  0.236632 -0.437033  0.046111 -0.252062
2020-01-05  0.761818 -0.181635 -0.546929 -0.738482
2020-01-06  1.306498 -0.411834 -0.680948 -0.070285
2020-01-07  0.956877 -0.749315 -0.503484  0.160620
2020-01-08  0.354319 -1.067165 -1.238036  1.051048
2020-01-09  0.262081 -0.898373 -1.059351  0.342291
2020-01-10  0.326801 -0.350519 -1.064437  0.749869
```



> 注 - 由于窗口大小为`3`(`window`)，前两个元素有空值，第三个元素的值将是`n`，`n-1`和`n-2`元素的平均值。这样也可以应用上面提到的各种函数了。

## .expanding()函数

这个函数可以应用于一系列数据。 指定`min_periods = n`参数并在其上应用适当的统计函数。

```
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4),
      index = pd.date_range('1/1/2018', periods=10),
      columns = ['A', 'B', 'C', 'D'])
print (df.expanding(min_periods=3).mean())
```


执行上面示例代码得到以下结果 - 

```
                   A         B         C         D
2018-01-01       NaN       NaN       NaN       NaN
2018-01-02       NaN       NaN       NaN       NaN
2018-01-03 -0.425085 -0.124270 -0.324134 -0.234001
2018-01-04 -0.293824 -0.038188 -0.172855  0.447226
2018-01-05 -0.516146 -0.013441 -0.384935  0.379267
2018-01-06 -0.614905  0.290308 -0.594635  0.414396
2018-01-07 -0.606090  0.121265 -0.604148  0.246296
2018-01-08 -0.597291  0.075374 -0.425182  0.092831
2018-01-09 -0.380505  0.074956 -0.253081  0.146426
2018-01-10 -0.235030  0.018936 -0.259566  0.315200
```



## .ewm()函数

`ewm()`可应用于系列数据。指定`com`，`span`，`halflife`参数，并在其上应用适当的统计函数。它以指数形式分配权重。

<ins class="adsbygoogle" style="display:inline-block;width:728px;height:90px" data-ad-client="ca-pub-1090193214637198" data-ad-slot="6494738921"></ins>

```
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4),
   index = pd.date_range('1/1/2019', periods=10),
   columns = ['A', 'B', 'C', 'D'])
print (df.ewm(com=0.5).mean())
```


执行上面示例函数，得到以下结果 - 

```
                   A         B         C         D
2019-01-01  1.047165  0.777385 -1.286948 -0.080564
2019-01-02  0.484093 -0.630998 -0.975172 -0.117832
2019-01-03  0.056189  0.830492  0.116325  1.005547
2019-01-04 -0.363824  1.222173  0.497901 -0.235209
2019-01-05 -0.260685  1.066029  0.391480  1.196190
2019-01-06  0.389649  1.458152 -0.231936 -0.481003
2019-01-07  1.071035 -0.016003  0.387420 -0.170811
2019-01-08 -0.573686  1.052081  1.218439  0.829366
2019-01-09  0.222927  0.556430  0.811838 -0.562096
2019-01-10  0.224624 -1.225446  0.204961 -0.800444
```



窗口函数主要用于通过平滑曲线来以图形方式查找数据内的趋势。如果日常数据中有很多变化，并且有很多数据点可用，那么采样和绘图就是一种方法，应用窗口计算并在结果上绘制图形是另一种方法。 通过这些方法，可以平滑曲线或趋势。

# Pandas聚合

当有了滚动，扩展和`ewm`对象创建了以后，就有几种方法可以对数据执行聚合。

## DataFrame应用聚合

让我们创建一个DataFrame并在其上应用聚合。

```
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4),
      index = pd.date_range('1/1/2019', periods=10),
      columns = ['A', 'B', 'C', 'D'])

print (df)
print("=======================================")
r = df.rolling(window=3,min_periods=1)
print (r)
```


执行上面示例代码，得到以下结果 - 

```
A         B         C         D
2019-01-01 -0.901602 -1.778484  0.728295 -0.758108
2019-01-02 -0.826162  0.994140  0.976164 -0.918249
2019-01-03  0.260841  0.905993  1.505967 -0.124883
2019-01-04 -0.112230 -0.111885  0.702712 -0.871768
2019-01-05 -0.239969  1.435918 -0.160140 -0.547702
2019-01-06 -0.126897 -2.628206 -0.280658  0.167422
2019-01-07  0.367903  0.994337 -0.529830  0.195990
2019-01-08 -0.530872 -0.384915 -0.397150 -0.024074
2019-01-09 -0.418925  0.049046 -0.816616  0.308107
2019-01-10 -0.176857  2.573145  0.010211 -1.427078
=======================================
Rolling [window=3,min_periods=1,center=False,axis=0]
```



可以通过向整个DataFrame传递一个函数来进行聚合，或者通过标准的获取项目方法来选择一个列。

## 在整个数据框上应用聚合

```
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4),
      index = pd.date_range('1/1/2000', periods=10),
      columns = ['A', 'B', 'C', 'D'])
print df

r = df.rolling(window=3,min_periods=1)
print r.aggregate(np.sum)
```


执行示例代码，得到以下结果 - 

```
A         B         C         D
2020-01-01  1.069090 -0.802365 -0.323818 -1.994676
2020-01-02  0.190584  0.328272 -0.550378  0.559738
2020-01-03  0.044865  0.478342 -0.976129  0.106530
2020-01-04 -1.349188 -0.391635 -0.292740  1.412755
2020-01-05  0.057659 -1.331901 -0.297858 -0.500705
2020-01-06  2.651680 -1.459706 -0.726023  0.294283
2020-01-07  0.666481  0.679205 -1.511743  2.093833
2020-01-08 -0.284316 -1.079759  1.433632  0.534043
2020-01-09  1.115246 -0.268812  0.190440 -0.712032
2020-01-10 -0.121008  0.136952  1.279354  0.275773
============================================
                   A         B         C         D
2020-01-01  1.069090 -0.802365 -0.323818 -1.994676
2020-01-02  1.259674 -0.474093 -0.874197 -1.434938
2020-01-03  1.304539  0.004249 -1.850326 -1.328409
2020-01-04 -1.113739  0.414979 -1.819248  2.079023
2020-01-05 -1.246664 -1.245194 -1.566728  1.018580
2020-01-06  1.360151 -3.183242 -1.316621  1.206333
2020-01-07  3.375821 -2.112402 -2.535624  1.887411
2020-01-08  3.033846 -1.860260 -0.804134  2.922160
2020-01-09  1.497411 -0.669366  0.112329  1.915845
2020-01-10  0.709922 -1.211619  2.903427  0.097785
```



**在数据框的单个列上应用聚合**

示例代码

```
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4),
      index = pd.date_range('1/1/2000', periods=10),
      columns = ['A', 'B', 'C', 'D'])
print (df)
print("====================================")
r = df.rolling(window=3,min_periods=1)
print (r['A'].aggregate(np.sum))
```


执行上面示例代码，得到以下结果 -

```
A         B         C         D
2000-01-01 -1.095530 -0.415257 -0.446871 -1.267795
2000-01-02 -0.405793 -0.002723  0.040241 -0.131678
2000-01-03 -0.136526  0.742393 -0.692582 -0.271176
2000-01-04  0.318300 -0.592146 -0.754830  0.239841
2000-01-05 -0.125770  0.849980  0.685083  0.752720
2000-01-06  1.410294  0.054780  0.297992 -0.034028
2000-01-07  0.463223 -1.239204 -0.056420  0.440893
2000-01-08 -2.244446 -0.516937 -2.039601 -0.680606
2000-01-09  0.991139  0.026987 -2.391856  0.585565
2000-01-10  0.112228 -0.701284 -1.139827  1.484032
====================================
2000-01-01   -1.095530
2000-01-02   -1.501323
2000-01-03   -1.637848
2000-01-04   -0.224018
2000-01-05    0.056004
2000-01-06    1.602824
2000-01-07    1.747747
2000-01-08   -0.370928
2000-01-09   -0.790084
2000-01-10   -1.141079
Freq: D, Name: A, dtype: float64
```



**在DataFrame的多列上应用聚合**

```
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4),
      index = pd.date_range('1/1/2018', periods=10),
      columns = ['A', 'B', 'C', 'D'])
print (df)
print ("==========================================")
r = df.rolling(window=3,min_periods=1)
print (r[['A','B']].aggregate(np.sum))
```


执行上面示例代码，得到以下结果 - 

```
A         B         C         D
2018-01-01  0.518897  0.988917  0.435691 -1.005703
2018-01-02  1.793400  0.130314  2.313787  0.870057
2018-01-03 -0.297601  0.504137 -0.951311 -0.146720
2018-01-04  0.282177  0.142360 -0.059013  0.633174
2018-01-05  2.095398 -0.153359  0.431514 -1.185657
2018-01-06  0.134847  0.188138  0.828329 -1.035120
2018-01-07  0.780541  0.138942 -1.001229  0.714896
2018-01-08  0.579742 -0.642858  0.835013 -1.504110
2018-01-09 -1.692986 -0.861327 -1.125359  0.006687
2018-01-10 -0.263689  1.182349 -0.916569  0.617476
==========================================
                   A         B
2018-01-01  0.518897  0.988917
2018-01-02  2.312297  1.119232
2018-01-03  2.014697  1.623369
2018-01-04  1.777976  0.776811
2018-01-05  2.079975  0.493138
2018-01-06  2.512422  0.177140
2018-01-07  3.010786  0.173722
2018-01-08  1.495130 -0.315777
2018-01-09 -0.332703 -1.365242
2018-01-10 -1.376932 -0.321836
```



**在DataFrame的单个列上应用多个函数**

<ins class="adsbygoogle" style="display:inline-block;width:728px;height:90px" data-ad-client="ca-pub-1090193214637198" data-ad-slot="6494738921"></ins>

```
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4),
      index = pd.date_range('2019/01/01', periods=10),
      columns = ['A', 'B', 'C', 'D'])
print (df)

print("==========================================")

r = df.rolling(window=3,min_periods=1)
print (r['A'].aggregate([np.sum,np.mean]))
```


执行上面示例代码，得到以下结果 - 

```
A         B         C         D
2019-01-01  1.022641 -1.431910  0.780941 -0.029811
2019-01-02 -0.302858  0.009886 -0.359331 -0.417708
2019-01-03 -1.396564  0.944374 -0.238989 -1.873611
2019-01-04  0.396995 -1.152009 -0.560552 -0.144212
2019-01-05 -2.513289 -1.085277 -1.016419 -1.586994
2019-01-06 -0.513179  0.823411  0.670734  1.196546
2019-01-07 -0.363239 -0.991799  0.587564 -1.100096
2019-01-08  1.474317  1.265496 -0.216486 -0.224218
2019-01-09  2.235798 -1.381457 -0.950745 -0.209564
2019-01-10 -0.061891 -0.025342  0.494245 -0.081681
==========================================
                 sum      mean
2019-01-01  1.022641  1.022641
2019-01-02  0.719784  0.359892
2019-01-03 -0.676780 -0.225593
2019-01-04 -1.302427 -0.434142
2019-01-05 -3.512859 -1.170953
2019-01-06 -2.629473 -0.876491
2019-01-07 -3.389707 -1.129902
2019-01-08  0.597899  0.199300
2019-01-09  3.346876  1.115625
2019-01-10  3.648224  1.216075
```



**在DataFrame的多列上应用多个函数**

```
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4),
      index = pd.date_range('2020/01/01', periods=10),
      columns = ['A', 'B', 'C', 'D'])

print (df)
print("==========================================")
r = df.rolling(window=3,min_periods=1)
print (r[['A','B']].aggregate([np.sum,np.mean]))
```


执行上面示例代码，得到以下结果 - 

```
A         B         C         D
2020-01-01  1.053702  0.355985  0.746638 -0.233968
2020-01-02  0.578520 -1.171843 -1.764249 -0.709913
2020-01-03 -0.491185  0.975212  0.200139 -3.372621
2020-01-04 -1.331328  0.776316  0.216623  0.202313
2020-01-05 -1.023147 -0.913686  1.457512  0.999232
2020-01-06  0.995328 -0.979826 -1.063695  0.057925
2020-01-07  0.576668  1.065767 -0.270744 -0.513707
2020-01-08  0.520258  0.969043 -0.119177 -0.125620
2020-01-09 -0.316480  0.549085  1.862249  1.091265
2020-01-10  0.461321 -0.368662 -0.988323  0.543011
==========================================
                   A                   B          
                 sum      mean       sum      mean
2020-01-01  1.053702  1.053702  0.355985  0.355985
2020-01-02  1.632221  0.816111 -0.815858 -0.407929
2020-01-03  1.141037  0.380346  0.159354  0.053118
2020-01-04 -1.243993 -0.414664  0.579686  0.193229
2020-01-05 -2.845659 -0.948553  0.837843  0.279281
2020-01-06 -1.359146 -0.453049 -1.117195 -0.372398
2020-01-07  0.548849  0.182950 -0.827744 -0.275915
2020-01-08  2.092254  0.697418  1.054985  0.351662
2020-01-09  0.780445  0.260148  2.583896  0.861299
2020-01-10  0.665099  0.221700  1.149466  0.383155
```



**将不同的函数应用于DataFrame的不同列**

```
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(3, 4),
      index = pd.date_range('2020/01/01', periods=3),
      columns = ['A', 'B', 'C', 'D'])
print (df)
print("==========================================")
r = df.rolling(window=3,min_periods=1)
print (r.aggregate({'A' : np.sum,'B' : np.mean}))
```


执行上面示例代码，得到以下结果 - 

```
A         B         C         D
2020-01-01 -0.246302 -0.057202  0.923807 -1.019698
2020-01-02  0.285287  1.467206 -0.368735 -0.397260
2020-01-03 -0.163219 -0.401368  1.254569  0.580188
==========================================
                   A         B
2020-01-01 -0.246302 -0.057202
2020-01-02  0.038985  0.705002
2020-01-03 -0.124234  0.336212
```

# Pandas缺失数据

数据丢失(缺失)在现实生活中总是一个问题。 机器学习和数据挖掘等领域由于数据缺失导致的数据质量差，在模型预测的准确性上面临着严重的问题。 在这些领域，缺失值处理是使模型更加准确和有效的重点。

## 何时以及为什么数据丢失？

想象一下有一个产品的在线调查。很多时候，人们不会分享与他们有关的所有信息。 很少有人分享他们的经验，但不是他们使用产品多久; 很少有人分享使用产品的时间，经验，但不是他们的个人联系信息。 因此，以某种方式或其他方式，总会有一部分数据总是会丢失，这是非常常见的现象。

现在来看看如何处理使用_Pandas_的缺失值(如`NA`或`NaN`)。

```
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f',
'h'],columns=['one', 'two', 'three'])

df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

print (df)
```


执行上面示例代码，得到以下结果 - 

```
one       two     three
a  0.691764 -0.118095 -0.950871
b       NaN       NaN       NaN
c -0.886898  0.053705 -1.269253
d       NaN       NaN       NaN
e -0.344967 -0.837128  0.730831
f -1.193740  1.767796  0.888104
g       NaN       NaN       NaN
h -0.755934 -1.331638  0.272248
```



使用重构索引(reindexing)，创建了一个缺少值的DataFrame。 在输出中，`NaN`表示不是数字的值。

## 检查缺失值

为了更容易地检测缺失值(以及跨越不同的数组`dtype`)，Pandas提供了`isnull()`和`notnull()`函数，它们也是Series和DataFrame对象的方法 -

**示例1**

```
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f',
'h'],columns=['one', 'two', 'three'])

df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

print (df['one'].isnull())
```


执行上面示例代码，得到以下结果 - 

```
a    False
b     True
c    False
d     True
e    False
f    False
g     True
h    False
Name: one, dtype: bool
```



**示例2**

```
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f',
'h'],columns=['one', 'two', 'three'])

df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

print (df['one'].notnull())
```


执行上面示例代码，得到以下结果 - 

```
a     True
b    False
c     True
d    False
e     True
f     True
g    False
h     True
Name: one, dtype: bool
```



#### 缺少数据的计算

* 在求和数据时，`NA`将被视为`0`
* 如果数据全部是`NA`，那么结果将是`NA`

**实例1**

```
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f',
'h'],columns=['one', 'two', 'three'])

df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

print (df['one'].sum())
```


执行上面示例代码，得到以下结果 - 

```
-2.6163354325445014
```



**示例2**

```
import pandas as pd
import numpy as np

df = pd.DataFrame(index=[0,1,2,3,4,5],columns=['one','two'])
print (df['one'].sum())
```


执行上面示例代码，得到以下结果 - 

```
nan
```



## 清理/填充缺少数据

_Pandas_提供了各种方法来清除缺失的值。`fillna()`函数可以通过几种方法用非空数据“填充”`NA`值，在下面的章节中将学习和使用。

## 用标量值替换NaN

以下程序显示如何用`0`替换`NaN`。

```
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(3, 3), index=['a', 'c', 'e'],columns=['one',
'two', 'three'])
df = df.reindex(['a', 'b', 'c'])
print (df)
print ("NaN replaced with '0':")
print (df.fillna(0))
```


执行上面示例代码，得到以下结果 - 

```
one       two     three
a -0.479425 -1.711840 -1.453384
b       NaN       NaN       NaN
c -0.733606 -0.813315  0.476788
NaN replaced with '0':
        one       two     three
a -0.479425 -1.711840 -1.453384
b  0.000000  0.000000  0.000000
c -0.733606 -0.813315  0.476788
```



在这里填充零值; 当然，也可以填写任何其他的值。

## 填写NA前进和后退

使用重构索引章节讨论的填充概念，来填补缺失的值。

| 方法               | 动作     |
| ---------------- | ------ |
| `pad/fill`       | 填充方法向前 |
| `bfill/backfill` | 填充方法向后 |

**示例1**

```
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f',
'h'],columns=['one', 'two', 'three'])
df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

print (df.fillna(method='pad'))
```


执行上面示例代码，得到以下结果 - 

<ins class="adsbygoogle" style="display:inline-block;width:728px;height:90px" data-ad-client="ca-pub-1090193214637198" data-ad-slot="6494738921"></ins>

```
one       two     three
a  0.614938 -0.452498 -2.113057
b  0.614938 -0.452498 -2.113057
c -0.118390  1.333962 -0.037907
d -0.118390  1.333962 -0.037907
e  0.699733  0.502142 -0.243700
f  0.544225 -0.923116 -1.123218
g  0.544225 -0.923116 -1.123218
h -0.669783  1.187865  1.112835
```



**示例2**

```
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f',
'h'],columns=['one', 'two', 'three'])

df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print (df.fillna(method='backfill'))
```


执行上面示例代码，得到以下结果 - 

```
one       two     three
a  2.278454  1.550483 -2.103731
b -0.779530  0.408493  1.247796
c -0.779530  0.408493  1.247796
d  0.262713 -1.073215  0.129808
e  0.262713 -1.073215  0.129808
f -0.600729  1.310515 -0.877586
g  0.395212  0.219146 -0.175024
h  0.395212  0.219146 -0.175024
```



## 丢失缺少的值

如果只想排除缺少的值，则使用`dropna`函数和`axis`参数。 默认情况下，`axis = 0`，即在行上应用，这意味着如果行内的任何值是`NA`，那么整个行被排除。

**实例1**

```
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f',
'h'],columns=['one', 'two', 'three'])

df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print (df.dropna())
```


执行上面示例代码，得到以下结果 - 

```
one       two     three
a -0.719623  0.028103 -1.093178
c  0.040312  1.729596  0.451805
e -1.029418  1.920933  1.289485
f  1.217967  1.368064  0.527406
h  0.667855  0.147989 -1.035978
```



**示例2**

```
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f',
'h'],columns=['one', 'two', 'three'])

df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print (df.dropna(axis=1))
```


执行上面示例代码，得到以下结果 - 

```
Empty DataFrame
Columns: []
Index: [a, b, c, d, e, f, g, h]
```



## 替换丢失(或)通用值

很多时候，必须用一些具体的值取代一个通用的值。可以通过应用替换方法来实现这一点。

用标量值替换`NA`是`fillna()`函数的等效行为。

**示例1**

```
import pandas as pd
import numpy as np
df = pd.DataFrame({'one':[10,20,30,40,50,2000],
'two':[1000,0,30,40,50,60]})
print (df.replace({1000:10,2000:60}))
```


执行上面示例，得到以下结果 - 

```
one  two
0   10   10
1   20    0
2   30   30
3   40   40
4   50   50
5   60   60
```



**示例2**

```
import pandas as pd
import numpy as np
df = pd.DataFrame({'one':[10,20,30,40,50,2000],
'two':[1000,0,30,40,50,60]})
print (df.replace({1000:10,2000:60}))
```


执行上面示例代码，得到以下结果 - 

```
one  two
0   10   10
1   20    0
2   30   30
3   40   40
4   50   50
5   60   60
```

# Pandas分组（GroupBy）

任何分组(_groupby_)操作都涉及原始对象的以下操作之一。它们是 - 

* 分割对象
* 应用一个函数
* 结合的结果

在许多情况下，我们将数据分成多个集合，并在每个子集上应用一些函数。在应用函数中，可以执行以下操作 -

* _聚合_ - 计算汇总统计
* _转换_ - 执行一些特定于组的操作
* _过滤_ - 在某些情况下丢弃数据

下面来看看创建一个DataFrame对象并对其执行所有操作 -

```
import pandas as pd

ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
         'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
         'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
         'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
         'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)

print (df)
```


执行上面示例代码，得到以下结果 - 

```
Points  Rank    Team  Year
0      876     1  Riders  2014
1      789     2  Riders  2015
2      863     2  Devils  2014
3      673     3  Devils  2015
4      741     3   Kings  2014
5      812     4   kings  2015
6      756     1   Kings  2016
7      788     1   Kings  2017
8      694     2  Riders  2016
9      701     4  Royals  2014
10     804     1  Royals  2015
11     690     2  Riders  2017
```



## 将数据拆分成组

Pandas对象可以分成任何对象。有多种方式来拆分对象，如 -

* _obj.groupby(‘key’)_
* _obj.groupby([‘key1’,’key2’])_
* _obj.groupby(key,axis=1)_

现在来看看如何将分组对象应用于DataFrame对象

**示例**

```
import pandas as pd

ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
         'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
         'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
         'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
         'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)

print (df.groupby('Team'))
```


执行上面示例代码，得到以下结果 - 

```
<pandas.core.groupby.DataFrameGroupBy object at 0x00000245D60AD518>
```



## 查看分组

```
import pandas as pd
ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
         'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
         'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
         'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],           'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)

print (df.groupby('Team').groups)
```


执行上面示例代码，得到以下结果 -

```
{
'Devils': Int64Index([2, 3], dtype='int64'), 
'Kings': Int64Index([4, 6, 7], dtype='int64'), 
'Riders': Int64Index([0, 1, 8, 11], dtype='int64'), 
'Royals': Int64Index([9, 10], dtype='int64'), 
'kings': Int64Index([5], dtype='int64')
}
```



**示例**

按多列分组 -

```
import pandas as pd
ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
         'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
         'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
         'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
         'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)
print (df.groupby(['Team','Year']).groups)
```


执行上面示例代码，得到以下结果 -

```
{
('Devils', 2014): Int64Index([2], dtype='int64'), 
('Devils', 2015): Int64Index([3], dtype='int64'), 
('Kings', 2014): Int64Index([4], dtype='int64'),
('Kings', 2016): Int64Index([6], dtype='int64'),
('Kings', 2017): Int64Index([7], dtype='int64'), 
('Riders', 2014): Int64Index([0], dtype='int64'), 
('Riders', 2015): Int64Index([1], dtype='int64'), 
('Riders', 2016): Int64Index([8], dtype='int64'), 
('Riders', 2017): Int64Index([11], dtype='int64'),
('Royals', 2014): Int64Index([9], dtype='int64'), 
('Royals', 2015): Int64Index([10], dtype='int64'), 
('kings', 2015): Int64Index([5], dtype='int64')
}
```



## 迭代遍历分组

使用`groupby`对象，可以遍历类似`itertools.obj`的对象。

```
import pandas as pd

ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
         'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
         'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
         'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
         'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)

grouped = df.groupby('Year')

for name,group in grouped:
    print (name)
    print (group)
```


执行上面示例代码，得到以下结果 - 

```
2014
   Points  Rank    Team  Year
0     876     1  Riders  2014
2     863     2  Devils  2014
4     741     3   Kings  2014
9     701     4  Royals  2014
2015
    Points  Rank    Team  Year
1      789     2  Riders  2015
3      673     3  Devils  2015
5      812     4   kings  2015
10     804     1  Royals  2015
2016
   Points  Rank    Team  Year
6     756     1   Kings  2016
8     694     2  Riders  2016
2017
    Points  Rank    Team  Year
7      788     1   Kings  2017
11     690     2  Riders  2017
```



默认情况下，`groupby`对象具有与分组名相同的标签名称。

## 选择一个分组

使用`get_group()`方法，可以选择一个组。参考以下示例代码 - 

```
import pandas as pd

ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
         'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
         'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
         'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
         'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)

grouped = df.groupby('Year')
print (grouped.get_group(2014))
```


执行上面示例代码，得到以下结果 - 

```
Points  Rank    Team  Year
0     876     1  Riders  2014
2     863     2  Devils  2014
4     741     3   Kings  2014
9     701     4  Royals  2014
```



## 聚合

聚合函数为每个组返回单个聚合值。当创建了分组(_group by_)对象，就可以对分组数据执行多个聚合操作。

一个比较常用的是通过聚合或等效的`agg`方法聚合 -

```
import pandas as pd
import numpy as np

ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
         'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
         'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
         'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
         'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)

grouped = df.groupby('Year')
print (grouped['Points'].agg(np.mean))
```


执行上面示例代码，得到以下结果 - 

<ins class="adsbygoogle" style="display:inline-block;width:728px;height:90px" data-ad-client="ca-pub-1090193214637198" data-ad-slot="6494738921"></ins>

```
Year
2014    795.25
2015    769.50
2016    725.00
2017    739.00
Name: Points, dtype: float64
```



另一种查看每个分组的大小的方法是应用`size()`函数 -

```
import pandas as pd
import numpy as np

ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
         'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
         'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
         'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
         'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)
grouped = df.groupby('Team')
print (grouped.agg(np.size))
```


执行上面示例代码，得到以下结果 - 

```
Team                      
Devils       2     2     2
Kings        3     3     3
Riders       4     4     4
Royals       2     2     2
kings        1     1     1
```



## 一次应用多个聚合函数

通过分组系列，还可以传递函数的列表或字典来进行聚合，并生成`DataFrame`作为输出 -

```
import pandas as pd
import numpy as np

ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
         'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
         'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
         'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
         'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)

grouped = df.groupby('Team')
agg = grouped['Points'].agg([np.sum, np.mean, np.std])
print (agg)
```


执行上面示例代码，得到以下结果 - 

```
        sum        mean         std
Team                                
Devils  1536  768.000000  134.350288
Kings   2285  761.666667   24.006943
Riders  3049  762.250000   88.567771
Royals  1505  752.500000   72.831998
kings    812  812.000000         NaN
```



## 转换

分组或列上的转换返回索引大小与被分组的索引相同的对象。因此，转换应该返回与组块大小相同的结果。

```
import pandas as pd
import numpy as np

ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
         'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
         'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
         'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
         'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)

grouped = df.groupby('Team')
score = lambda x: (x - x.mean()) / x.std()*10
print (grouped.transform(score))
```


执行上面示例代码，得到以下结果 - 

```
      Points       Rank       Year
0   12.843272 -15.000000 -11.618950
1    3.020286   5.000000  -3.872983
2    7.071068  -7.071068  -7.071068
3   -7.071068   7.071068   7.071068
4   -8.608621  11.547005 -10.910895
5         NaN        NaN        NaN
6   -2.360428  -5.773503   2.182179
7   10.969049  -5.773503   8.728716
8   -7.705963   5.000000   3.872983
9   -7.071068   7.071068  -7.071068
10   7.071068  -7.071068   7.071068
11  -8.157595   5.000000  11.618950
```



## 过滤

过滤根据定义的标准过滤数据并返回数据的子集。`filter()`函数用于过滤数据。

```
import pandas as pd
import numpy as np
ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
         'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
         'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
         'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
         'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)
filter = df.groupby('Team').filter(lambda x: len(x) >= 3)

print (filter)
```


执行上面示例代码，得到以下结果 - 

```
      Points  Rank    Team  Year
0      876     1  Riders  2014
1      789     2  Riders  2015
4      741     3   Kings  2014
6      756     1   Kings  2016
7      788     1   Kings  2017
8      694     2  Riders  2016
11     690     2  Riders  2017
```



在上述过滤条件下，要求返回三次以上参加IPL的队伍。

# Pandas合并/连接

Pandas具有功能全面的高性能内存中连接操作，与SQL等关系数据库非常相似。  
Pandas提供了一个单独的`merge()`函数，作为DataFrame对象之间所有标准数据库连接操作的入口 -

```
pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None,
left_index=False, right_index=False, sort=True)
```


在这里，有以下几个参数可以使用 -

* _left_ - 一个DataFrame对象。
* _right_ - 另一个DataFrame对象。
* _on_ - 列(名称)连接，必须在左和右DataFrame对象中存在(找到)。
* _left_on_ - 左侧DataFrame中的列用作键，可以是列名或长度等于DataFrame长度的数组。
* _right_on_ - 来自右的DataFrame的列作为键，可以是列名或长度等于DataFrame长度的数组。
* _left_index_ - 如果为`True`，则使用左侧DataFrame中的索引(行标签)作为其连接键。 在具有MultiIndex(分层)的DataFrame的情况下，级别的数量必须与来自右DataFrame的连接键的数量相匹配。
* _right_index_ - 与右DataFrame的_left_index_具有相同的用法。
* _how_ - 它是_left_, _right_, _outer_以及_inner_之中的一个，默认为内_inner_。 下面将介绍每种方法的用法。
* _sort_ - 按照字典顺序通过连接键对结果DataFrame进行排序。默认为`True`，设置为`False`时，在很多情况下大大提高性能。

现在创建两个不同的DataFrame并对其执行合并操作。

```
import pandas as pd
left = pd.DataFrame({
         'id':[1,2,3,4,5],
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5']})
right = pd.DataFrame(
         {'id':[1,2,3,4,5],
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5']})
print (left)
print("========================================")
print (right)
```


执行上面示例代码，得到以下结果 -

```
Name  id subject_id
0    Alex   1       sub1
1     Amy   2       sub2
2   Allen   3       sub4
3   Alice   4       sub6
4  Ayoung   5       sub5
========================================
    Name  id subject_id
0  Billy   1       sub2
1  Brian   2       sub4
2   Bran   3       sub3
3  Bryce   4       sub6
4  Betty   5       sub5
```



**在一个键上合并两个数据帧**

```
import pandas as pd
left = pd.DataFrame({
         'id':[1,2,3,4,5],
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5']})
right = pd.DataFrame(
         {'id':[1,2,3,4,5],
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5']})
rs = pd.merge(left,right,on='id')
print(rs)
```


执行上面示例代码，得到以下结果 - 

```
Name_x  id subject_id_x Name_y subject_id_y
0    Alex   1         sub1  Billy         sub2
1     Amy   2         sub2  Brian         sub4
2   Allen   3         sub4   Bran         sub3
3   Alice   4         sub6  Bryce         sub6
4  Ayoung   5         sub5  Betty         sub5
```



**合并多个键上的两个数据框**

```
import pandas as pd
left = pd.DataFrame({
         'id':[1,2,3,4,5],
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5']})
right = pd.DataFrame(
         {'id':[1,2,3,4,5],
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5']})
rs = pd.merge(left,right,on=['id','subject_id'])
print(rs)
```


执行上面示例代码，得到以下结果 - 

```
Name_x  id subject_id Name_y
0   Alice   4       sub6  Bryce
1  Ayoung   5       sub5  Betty
```



## 合并使用“how”的参数

如何合并参数指定如何确定哪些键将被包含在结果表中。如果组合键没有出现在左侧或右侧表中，则连接表中的值将为`NA`。

这里是`how`选项和SQL等效名称的总结 -

| 合并方法    | SQL等效              | 描述       |
| ------- | ------------------ | -------- |
| `left`  | `LEFT OUTER JOIN`  | 使用左侧对象的键 |
| `right` | `RIGHT OUTER JOIN` | 使用右侧对象的键 |
| `outer` | `FULL OUTER JOIN`  | 使用键的联合   |
| `inner` | `INNER JOIN`       | 使用键的交集   |

**Left Join示例**

```
import pandas as pd
left = pd.DataFrame({
         'id':[1,2,3,4,5],
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5']})
right = pd.DataFrame(
         {'id':[1,2,3,4,5],
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5']})
rs = pd.merge(left, right, on='subject_id', how='left')
print (rs)
```


执行上面示例代码，得到以下结果 - 

<ins class="adsbygoogle" style="display:inline-block;width:728px;height:90px" data-ad-client="ca-pub-1090193214637198" data-ad-slot="6494738921"></ins>

```
Name_x  id_x subject_id Name_y  id_y
0    Alex     1       sub1    NaN   NaN
1     Amy     2       sub2  Billy   1.0
2   Allen     3       sub4  Brian   2.0
3   Alice     4       sub6  Bryce   4.0
4  Ayoung     5       sub5  Betty   5.0
```



**Right Join示例**

```
import pandas as pd
left = pd.DataFrame({
         'id':[1,2,3,4,5],
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5']})
right = pd.DataFrame(
         {'id':[1,2,3,4,5],
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5']})
rs = pd.merge(left, right, on='subject_id', how='right')
print (rs)
```


执行上面示例代码，得到以下结果 - 

```
Name_x  id_x subject_id Name_y  id_y
0     Amy   2.0       sub2  Billy     1
1   Allen   3.0       sub4  Brian     2
2   Alice   4.0       sub6  Bryce     4
3  Ayoung   5.0       sub5  Betty     5
4     NaN   NaN       sub3   Bran     3
```



**Outer Join示例**

```
import pandas as pd
left = pd.DataFrame({
         'id':[1,2,3,4,5],
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5']})
right = pd.DataFrame(
         {'id':[1,2,3,4,5],
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5']})
rs = pd.merge(left, right, how='outer', on='subject_id')
print (rs)
```


执行上面示例代码，得到以下结果 - 

```
Name_x  id_x subject_id Name_y  id_y
0    Alex   1.0       sub1    NaN   NaN
1     Amy   2.0       sub2  Billy   1.0
2   Allen   3.0       sub4  Brian   2.0
3   Alice   4.0       sub6  Bryce   4.0
4  Ayoung   5.0       sub5  Betty   5.0
5     NaN   NaN       sub3   Bran   3.0
```



**Inner Join示例**

连接将在索引上进行。连接(`Join`)操作将授予它所调用的对象。所以，`a.join(b)`不等于`b.join(a)`。

```
import pandas as pd
left = pd.DataFrame({
         'id':[1,2,3,4,5],
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5']})
right = pd.DataFrame(
         {'id':[1,2,3,4,5],
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5']})
rs = pd.merge(left, right, on='subject_id', how='inner')
print (rs)
```


执行上面示例代码，得到以下结果 - 

```
Name_x  id_x subject_id Name_y  id_y
0     Amy     2       sub2  Billy     1
1   Allen     3       sub4  Brian     2
2   Alice     4       sub6  Bryce     4
3  Ayoung     5       sub5  Betty     5
```

# Pandas级联

**Pandas**提供了各种工具(功能)，可以轻松地将`Series`，`DataFrame`和`Panel`对象组合在一起。

```
pd.concat(objs,axis=0,join='outer',join_axes=None,
ignore_index=False)
```


其中，

* _objs_ - 这是Series，DataFrame或Panel对象的序列或映射。
* _axis_ - `{0，1，...}`，默认为`0`，这是连接的轴。
* _join_ - `{'inner', 'outer'}`，默认`inner`。如何处理其他轴上的索引。联合的外部和交叉的内部。
* _ignore_index_ − 布尔值，默认为`False`。如果指定为`True`，则不要使用连接轴上的索引值。结果轴将被标记为：`0，...，n-1`。
* _join_axes_ - 这是Index对象的列表。用于其他`(n-1)`轴的特定索引，而不是执行内部/外部集逻辑。

## 连接对象

`concat()`函数完成了沿轴执行级联操作的所有重要工作。下面代码中，创建不同的对象并进行连接。

```
import pandas as pd
one = pd.DataFrame({
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5'],
         'Marks_scored':[98,90,87,69,78]},
         index=[1,2,3,4,5])
two = pd.DataFrame({
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5'],
         'Marks_scored':[89,80,79,97,88]},
         index=[1,2,3,4,5])
rs = pd.concat([one,two])
print(rs)
```


执行上面示例代码，得到以下结果 - 

```
Marks_scored    Name subject_id
1            98    Alex       sub1
2            90     Amy       sub2
3            87   Allen       sub4
4            69   Alice       sub6
5            78  Ayoung       sub5
1            89   Billy       sub2
2            80   Brian       sub4
3            79    Bran       sub3
4            97   Bryce       sub6
5            88   Betty       sub5
```



假设想把特定的键与每个碎片的DataFrame关联起来。可以通过使用键参数来实现这一点 -

```
import pandas as pd
one = pd.DataFrame({
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5'],
         'Marks_scored':[98,90,87,69,78]},
         index=[1,2,3,4,5])
two = pd.DataFrame({
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5'],
         'Marks_scored':[89,80,79,97,88]},
         index=[1,2,3,4,5])
rs = pd.concat([one,two],keys=['x','y'])
print(rs)
```


执行上面示例代码，得到以下结果 - 

```
Marks_scored    Name subject_id
x 1            98    Alex       sub1
  2            90     Amy       sub2
  3            87   Allen       sub4
  4            69   Alice       sub6
  5            78  Ayoung       sub5
y 1            89   Billy       sub2
  2            80   Brian       sub4
  3            79    Bran       sub3
  4            97   Bryce       sub6
  5            88   Betty       sub5
```



结果的索引是重复的; 每个索引重复。如果想要生成的对象必须遵循自己的索引，请将`ignore_index`设置为`True`。参考以下示例代码 - 

```
import pandas as pd
one = pd.DataFrame({
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5'],
         'Marks_scored':[98,90,87,69,78]},
         index=[1,2,3,4,5])
two = pd.DataFrame({
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5'],
         'Marks_scored':[89,80,79,97,88]},
         index=[1,2,3,4,5])
rs = pd.concat([one,two],keys=['x','y'],ignore_index=True)

print(rs)
```


执行上面示例代码，得到以下结果 - 

```
Marks_scored    Name subject_id
0            98    Alex       sub1
1            90     Amy       sub2
2            87   Allen       sub4
3            69   Alice       sub6
4            78  Ayoung       sub5
5            89   Billy       sub2
6            80   Brian       sub4
7            79    Bran       sub3
8            97   Bryce       sub6
9            88   Betty       sub5
```



观察，索引完全改变，键也被覆盖。如果需要沿`axis=1`添加两个对象，则会添加新列。

```
import pandas as pd
one = pd.DataFrame({
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5'],
         'Marks_scored':[98,90,87,69,78]},
         index=[1,2,3,4,5])
two = pd.DataFrame({
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5'],
         'Marks_scored':[89,80,79,97,88]},
         index=[1,2,3,4,5])
rs = pd.concat([one,two],axis=1)
print(rs)
```


执行上面示例代码，得到以下结果 - 

```
Marks_scored    Name subject_id  Marks_scored   Name subject_id
1            98    Alex       sub1            89  Billy       sub2
2            90     Amy       sub2            80  Brian       sub4
3            87   Allen       sub4            79   Bran       sub3
4            69   Alice       sub6            97  Bryce       sub6
5            78  Ayoung       sub5            88  Betty       sub5
```



#### 使用附加连接

连接的一个有用的快捷方式是在Series和DataFrame实例的`append`方法。这些方法实际上早于`concat()`方法。 它们沿`axis=0`连接，即索引 -

```
import pandas as pd
one = pd.DataFrame({
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5'],
         'Marks_scored':[98,90,87,69,78]},
         index=[1,2,3,4,5])
two = pd.DataFrame({
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5'],
         'Marks_scored':[89,80,79,97,88]},
         index=[1,2,3,4,5])
rs = one.append(two)
print(rs)
```


执行上面示例代码，得到以下结果 - 

```
Marks_scored    Name subject_id
1            98    Alex       sub1
2            90     Amy       sub2
3            87   Allen       sub4
4            69   Alice       sub6
5            78  Ayoung       sub5
1            89   Billy       sub2
2            80   Brian       sub4
3            79    Bran       sub3
4            97   Bryce       sub6
5            88   Betty       sub5
```



`append()`函数也可以带多个对象 -

```
import pandas as pd

one = pd.DataFrame({
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5'],
         'Marks_scored':[98,90,87,69,78]},
         index=[1,2,3,4,5])

two = pd.DataFrame({
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5'],
         'Marks_scored':[89,80,79,97,88]},
         index=[1,2,3,4,5])
rs = one.append([two,one,two])
print(rs)
```


执行上面示例代码，得到以下结果 - 

<ins class="adsbygoogle" style="display:inline-block;width:728px;height:90px" data-ad-client="ca-pub-1090193214637198" data-ad-slot="6494738921"></ins>

```
Marks_scored    Name subject_id
1            98    Alex       sub1
2            90     Amy       sub2
3            87   Allen       sub4
4            69   Alice       sub6
5            78  Ayoung       sub5
1            89   Billy       sub2
2            80   Brian       sub4
3            79    Bran       sub3
4            97   Bryce       sub6
5            88   Betty       sub5
1            98    Alex       sub1
2            90     Amy       sub2
3            87   Allen       sub4
4            69   Alice       sub6
5            78  Ayoung       sub5
1            89   Billy       sub2
2            80   Brian       sub4
3            79    Bran       sub3
4            97   Bryce       sub6
5            88   Betty       sub5
```



## 时间序列

_Pandas_为时间序列数据的工作时间提供了一个强大的工具，尤其是在金融领域。在处理时间序列数据时，我们经常遇到以下情况 -

* 生成时间序列
* 将时间序列转换为不同的频率

_Pandas_提供了一个相对紧凑和自包含的工具来执行上述任务。

### 获取当前时间

`datetime.now()`用于获取当前的日期和时间。

```
import pandas as pd
print pd.datetime.now()
```


上述代码执行结果如下 - 

```
2017-11-03 02:17:45.997992
```



#### 创建一个时间戳

时间戳数据是时间序列数据的最基本类型，它将数值与时间点相关联。 对于_Pandas_对象来说，意味着使用时间点。举个例子 -

```
import pandas as pd
time = pd.Timestamp('2018-11-01')
print(time)
```


执行上面示例代码，得到以下结果 - 

```
2018-11-01 00:00:00
```



也可以转换整数或浮动时期。这些的默认单位是纳秒(因为这些是如何存储时间戳的)。 然而，时代往往存储在另一个可以指定的单元中。 再举一个例子 - 

```
import pandas as pd
time = pd.Timestamp(1588686880,unit='s')
print(time)
```


执行上面示例代码，得到以下结果 - 

```
2020-05-05 13:54:40
```



#### 创建一个时间范围

```
import pandas as pd

time = pd.date_range("12:00", "23:59", freq="30min").time
print(time)
```


执行上面示例代码，得到以下结果 - 

```
[datetime.time(12, 0) datetime.time(12, 30) datetime.time(13, 0)
 datetime.time(13, 30) datetime.time(14, 0) datetime.time(14, 30)
 datetime.time(15, 0) datetime.time(15, 30) datetime.time(16, 0)
 datetime.time(16, 30) datetime.time(17, 0) datetime.time(17, 30)
 datetime.time(18, 0) datetime.time(18, 30) datetime.time(19, 0)
 datetime.time(19, 30) datetime.time(20, 0) datetime.time(20, 30)
 datetime.time(21, 0) datetime.time(21, 30) datetime.time(22, 0)
 datetime.time(22, 30) datetime.time(23, 0) datetime.time(23, 30)]
```



#### 改变时间的频率

```
import pandas as pd

time = pd.date_range("12:00", "23:59", freq="H").time
print(time)
```


执行上面示例代码，得到以下结果 - 

```
[datetime.time(12, 0) datetime.time(13, 0) datetime.time(14, 0)
 datetime.time(15, 0) datetime.time(16, 0) datetime.time(17, 0)
 datetime.time(18, 0) datetime.time(19, 0) datetime.time(20, 0)
 datetime.time(21, 0) datetime.time(22, 0) datetime.time(23, 0)]
```



#### 转换为时间戳

要转换类似日期的对象(例如字符串，时代或混合)的序列或类似列表的对象，可以使用`to_datetime`函数。当传递时将返回一个Series(具有相同的索引)，而类似列表被转换为`DatetimeIndex`。 看看下面的例子 -

```
import pandas as pd

time = pd.to_datetime(pd.Series(['Jul 31, 2009','2019-10-10', None]))
print(time)
```


执行上面示例代码，得到以下结果 - 

```
0   2009-07-31
1   2019-10-10
2          NaT
dtype: datetime64[ns]
```



`NaT`表示不是一个时间的值(相当于`NaN`)

举一个例子，

```
import pandas as pd
import pandas as pd
time = pd.to_datetime(['2009/11/23', '2019.12.31', None])
print(time)
```


执行上面示例代码，得到以下结果 - 

```
DatetimeIndex(['2009-11-23', '2019-12-31', 'NaT'], dtype='datetime64[ns]', freq=None)
```

# Pandas日期功能

日期功能扩展了时间序列，在财务数据分析中起主要作用。在处理日期数据的同时，我们经常会遇到以下情况 -

* 生成日期序列
* 将日期序列转换为不同的频率

## 创建一个日期范围

通过指定周期和频率，使用`date.range()`函数就可以创建日期序列。 默认情况下，范围的频率是天。参考以下示例代码 - 

```
import pandas as pd
datelist = pd.date_range('2020/11/21', periods=5)
print(datelist)
```


执行上面示例代码，得到以下结果 - 

```
DatetimeIndex(['2020-11-21', '2020-11-22', '2020-11-23', '2020-11-24',
               '2020-11-25'],
              dtype='datetime64[ns]', freq='D')
```



#### 更改日期频率

```
import pandas as pd
datelist = pd.date_range('2020/11/21', periods=5,freq='M')
print(datelist)
```


执行上面示例代码，得到以下结果 - 

```
DatetimeIndex(['2020-11-30', '2020-12-31', '2021-01-31', '2021-02-28',
               '2021-03-31'],
              dtype='datetime64[ns]', freq='M')
```



## bdate_range()函数

`bdate_range()`用来表示商业日期范围，不同于`date_range()`，它不包括星期六和星期天。

```
import pandas as pd
datelist = pd.date_range('2011/11/03', periods=5)
print(datelist)
```


执行上面示例代码，得到以下结果 - 

```
DatetimeIndex(['2017-11-03', '2017-11-06', '2017-11-07', '2017-11-08',
               '2017-11-09'],
              dtype='datetime64[ns]', freq='B')
```



观察到11月3日以后，日期跳至11月6日，不包括4日和5日(因为它们是周六和周日)。

像`date_range`和`bdate_range`这样的便利函数利用了各种频率别名。`date_range`的默认频率是日历中的自然日，而`bdate_range`的默认频率是工作日。参考以下示例代码 - 

```
import pandas as pd
start = pd.datetime(2017, 11, 1)
end = pd.datetime(2017, 11, 5)
dates = pd.date_range(start, end)
print(dates)
```


执行上面示例代码，得到以下结果 - 

```
DatetimeIndex(['2017-11-01', '2017-11-02', '2017-11-03', '2017-11-04',
               '2017-11-05'],
              dtype='datetime64[ns]', freq='D')
```



## 偏移别名

大量的字符串别名被赋予常用的时间序列频率。我们把这些别名称为偏移别名。

| 别名       | 描述说明      |
| -------- | --------- |
| `B`      | 工作日频率     |
| `BQS`    | 商务季度开始频率  |
| `D`      | 日历/自然日频率  |
| `A`      | 年度(年)结束频率 |
| `W`      | 每周频率      |
| `BA`     | 商务年底结束    |
| `M`      | 月结束频率     |
| `BAS`    | 商务年度开始频率  |
| `SM`     | 半月结束频率    |
| `BH`     | 商务时间频率    |
| `SM`     | 半月结束频率    |
| `BH`     | 商务时间频率    |
| `BM`     | 商务月结束频率   |
| `H`      | 小时频率      |
| `MS`     | 月起始频率     |
| `T, min` | 分钟的频率     |
| `SMS`    | SMS半开始频率  |
| `S`      | 秒频率       |
| `BMS`    | 商务月开始频率   |
| `L, ms`  | 毫秒        |
| `Q`      | 季度结束频率    |
| `U, us`  | 微秒        |
| `BQ`     | 商务季度结束频率  |
| `N`      | 纳秒        |
| `BQ`     | 商务季度结束频率  |
| `QS`     | 季度开始频率    |


# Pandas时间差（Timedelta）

时间差(Timedelta)是时间上的差异，以不同的单位来表示。例如：日，小时，分钟，秒。它们可以是正值，也可以是负值。  
可以使用各种参数创建`Timedelta`对象，如下所示 -

## 字符串

通过传递字符串，可以创建一个`timedelta`对象。参考以下示例代码 - 

```
import pandas as pd

timediff = pd.Timedelta('2 days 2 hours 15 minutes 30 seconds')
print(timediff)
```


执行上面救命代码，得到以下结果 - 

```
2 days 02:15:30
```



## 整数

通过传递一个整数值与指定单位，这样的一个参数也可以用来创建`Timedelta`对象。

```
import pandas as pd

timediff = pd.Timedelta(6,unit='h')
print(timediff)
```


执行上面救命代码，得到以下结果 - 

```
0 days 06:00:00
```



## 数据偏移

例如 - 周，天，小时，分钟，秒，毫秒，微秒，纳秒的数据偏移也可用于构建。

```
import pandas as pd

timediff = pd.Timedelta(days=2)
print(timediff)
```


执行上面救命代码，得到以下结果 - 

```
2 days 00:00:00
```



## 运算操作

可以在Series/DataFrames上执行运算操作，并通过在`datetime64 [ns]`系列或在时间戳上减法操作来构造`timedelta64 [ns]`系列。参考以下示例代码 - 

```
import pandas as pd

s = pd.Series(pd.date_range('2012-1-1', periods=3, freq='D'))
td = pd.Series([ pd.Timedelta(days=i) for i in range(3) ])
df = pd.DataFrame(dict(A = s, B = td))
print(df)
```


执行上面示例代码，得到以下结果 - 

<ins class="adsbygoogle" style="display:inline-block;width:728px;height:90px" data-ad-client="ca-pub-1090193214637198" data-ad-slot="6494738921"></ins>

```
      A      B
0 2012-01-01 0 days
1 2012-01-02 1 days
2 2012-01-03 2 days
```



#### 相加操作

```
import pandas as pd

s = pd.Series(pd.date_range('2018-1-1', periods=3, freq='D'))
td = pd.Series([ pd.Timedelta(days=i) for i in range(3) ])
df = pd.DataFrame(dict(A = s, B = td))
df['C']=df['A']+df['B']
print(df)
```


执行上面示例代码，得到以下结果 - 

```
           A      B          C
0 2018-01-01 0 days 2018-01-01
1 2018-01-02 1 days 2018-01-03
2 2018-01-03 2 days 2018-01-05
```



#### 相减操作

```
import pandas as pd

s = pd.Series(pd.date_range('2012-1-1', periods=3, freq='D'))
td = pd.Series([ pd.Timedelta(days=i) for i in range(3) ])
df = pd.DataFrame(dict(A = s, B = td))
df['C']=df['A']+df['B']
df['D']=df['C']-df['B']
print(df)
```


执行上面示例代码，得到以下结果 - 

```
           A      B          C          D
0 2018-01-01 0 days 2018-01-01 2018-01-01
1 2018-01-02 1 days 2018-01-03 2018-01-02
2 2018-01-03 2 days 2018-01-05 2018-01-03
```

# Pandas分类数据

通常实时的数据包括重复的文本列。例如：性别，国家和代码等特征总是重复的。这些是分类数据的例子。

分类变量只能采用有限的数量，而且通常是固定的数量。除了固定长度，分类数据可能有顺序，但不能执行数字操作。 分类是_Pandas_数据类型。

分类数据类型在以下情况下非常有用 -

* 一个字符串变量，只包含几个不同的值。将这样的字符串变量转换为分类变量将会节省一些内存。
* 变量的词汇顺序与逻辑顺序(`"one"`，`"two"`，`"three"`)不同。 通过转换为分类并指定类别上的顺序，排序和最小/最大将使用逻辑顺序，而不是词法顺序。
* 作为其他python库的一个信号，这个列应该被当作一个分类变量(例如，使用合适的统计方法或`plot`类型)。

## 对象创建

分类对象可以通过多种方式创建。下面介绍了不同的方法 -

**类别/分类**

通过在`pandas`对象创建中将`dtype`指定为`“category”`。

```
import pandas as pd
s = pd.Series(["a","b","c","a"], dtype="category")
print (s)
```


执行上面示例代码，得到以下结果 - 

```
0    a
1    b
2    c
3    a
dtype: category
Categories (3, object): [a, b, c]
```



传递给系列对象的元素数量是四个，但类别只有三个。观察相同的输出类别。

**pd.Categorical**

使用标准_Pandas_分类构造函数，我们可以创建一个类别对象。语法如下 - 

```
pandas.Categorical(values, categories, ordered)
```


举个例子 -

```
import pandas as pd
cat = pd.Categorical(['a', 'b', 'c', 'a', 'b', 'c'])
print (cat)
```


执行上面示例代码，得到以下结果 - 

```
[a, b, c, a, b, c]
Categories (3, object): [a, b, c]
```



再举一个例子 -

```
import pandas as pd
cat = cat=pd.Categorical(['a','b','c','a','b','c','d'], ['c', 'b', 'a'])
print (cat)
```


执行上面示例代码，得到以下结果 - 

```
[a, b, c, a, b, c, NaN]
Categories (3, object): [c, b, a]
```



这里，第二个参数表示类别。因此，在类别中不存在的任何值将被视为`NaN`。

现在，看看下面的例子 -

```
import pandas as pd
cat = cat=pd.Categorical(['a','b','c','a','b','c','d'], ['c', 'b', 'a'],ordered=True)
print (cat)
```


执行上面示例代码，得到以结果 - 

```
[a, b, c, a, b, c, NaN]
Categories (3, object): [c < b < a]
```



从逻辑上讲，排序(_ordered_)意味着，`a`大于`b`，`b`大于`c`。

**描述**

使用分类数据上的`.describe()`命令，可以得到与类型字符串的Series或DataFrame类似的输出。

```
import pandas as pd
import numpy as np

cat = pd.Categorical(["a", "c", "c", np.nan], categories=["b", "a", "c"])
df = pd.DataFrame({"cat":cat, "s":["a", "c", "c", np.nan]})
print (df.describe())
print ("=============================")
print (df["cat"].describe())
```


执行上面示例代码，得到以下结果 - 

```
cat  s
count    3  3
unique   2  2
top      c  c
freq     2  2
=============================
count     3
unique    2
top       c
freq      2
Name: cat, dtype: object
```



**获取类别的属性**

`obj.cat.categories`命令用于获取对象的类别。

```
import pandas as pd
import numpy as np

s = pd.Categorical(["a", "c", "c", np.nan], categories=["b", "a", "c"])
print (s.categories)
```


执行上面示例代码，得到以下结果 - 

```
Index(['b', 'a', 'c'], dtype='object')
```



**obj.ordered**命令用于获取对象的顺序。

```
import pandas as pd
import numpy as np

cat = pd.Categorical(["a", "c", "c", np.nan], categories=["b", "a", "c"])
print (cat.ordered)
```


执行上面示例代码，得到以下结果 - 

<ins class="adsbygoogle" style="display:inline-block;width:728px;height:90px" data-ad-client="ca-pub-1090193214637198" data-ad-slot="6494738921"></ins>

```
False
```



该函数返回结果为：_False_，因为这里没有指定任何顺序。

**重命名类别**

重命名类别是通过将新值分配给`series.cat.categories`属性来完成的。参考以下示例代码 -

```
import pandas as pd

s = pd.Series(["a","b","c","a"], dtype="category")
s.cat.categories = ["Group %s" % g for g in s.cat.categories]

print (s.cat.categories)
```


执行上面示例代码，得到以下结果 - 

```
Index(['Group a', 'Group b', 'Group c'], dtype='object')
```



初始类别`[a，b，c]`由对象的`s.cat.categories`属性更新。

**附加新类别**  
使用`Categorical.add.categories()`方法，可以追加新的类别。

```
import pandas as pd

s = pd.Series(["a","b","c","a"], dtype="category")
s = s.cat.add_categories([4])
print (s.cat.categories)
```


执行上面示例代码，得到以下结果 - 

```
Index(['a', 'b', 'c', 4], dtype='object')
```



**删除类别**  
使用`Categorical.remove_categories()`方法，可以删除不需要的类别。

```
import pandas as pd

s = pd.Series(["a","b","c","a"], dtype="category")
print ("Original object:")
print (s)
print("=====================================")
print ("After removal:")
print (s.cat.remove_categories("a"))
```


执行上面示例代码，得到以下结果 - 

```
Original object:
0    a
1    b
2    c
3    a
dtype: category
Categories (3, object): [a, b, c]
=====================================
After removal:
0    NaN
1      b
2      c
3    NaN
dtype: category
Categories (2, object): [b, c]
```



**分类数据的比较**

在三种情况下可以将分类数据与其他对象进行比较 -

* 将等号(`==`和`!=`)与类别数据相同长度的类似列表的对象(列表，系列，数组…)进行比较。
* 当`ordered==True`和类别是相同时，所有比较(`==`，`!=`，`>`，`>=`，`<`，和`<=`)分类数据到另一个分类系列。
* 将分类数据与标量进行比较。

看看下面的例子 -

```
import pandas as pd

cat = pd.Series([1,2,3]).astype("category", categories=[1,2,3], ordered=True)
cat1 = pd.Series([2,2,2]).astype("category", categories=[1,2,3], ordered=True)

print (cat>cat1)
```


执行上面示例代码，得到以下结果 - 

```
0    False
1    False
2     True
dtype: bool
```

# Pandas可视化

**基本绘图：绘图**

Series和DataFrame上的这个功能只是使用`matplotlib`库的`plot()`方法的简单包装实现。参考以下示例代码 - 

```
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10,4),index=pd.date_range('2018/12/18',
   periods=10), columns=list('ABCD'))

df.plot()
```


执行上面示例代码，得到以下结果 - 

![](http://www.yiibai.com/uploads/images/201711/0511/385181122_97686.png)

如果索引由日期组成，则调用`gct().autofmt_xdate()`来格式化`x`轴，如上图所示。

我们可以使用`x`和`y`关键字绘制一列与另一列。

绘图方法允许除默认线图之外的少数绘图样式。 这些方法可以作为`plot()`的`kind`关键字参数提供。这些包括 -

* `bar`或`barh`为条形
* `hist`为直方图
* `boxplot`为盒型图
* `area`为“面积”
* `scatter`为散点图

## 条形图

现在通过创建一个条形图来看看条形图是什么。条形图可以通过以下方式来创建 -

```
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.rand(10,4),columns=['a','b','c','d'])
df.plot.bar()
```


执行上面示例代码，得到以下结果 - 

![](http://www.yiibai.com/uploads/images/201711/0511/220181133_35165.png)

要生成一个堆积条形图，通过指定：_pass stacked=True_ -

```
import pandas as pd
df = pd.DataFrame(np.random.rand(10,4),columns=['a','b','c','d'])
df.plot.bar(stacked=True)
```


执行上面示例代码，得到以下结果 - 

![](http://www.yiibai.com/uploads/images/201711/0511/726181135_51813.png)

要获得水平条形图，使用`barh()`方法 -

```
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.rand(10,4),columns=['a','b','c','d'])

df.plot.barh(stacked=True)
```


执行上面示例代码，得到以下结果 - 

![](http://www.yiibai.com/uploads/images/201711/0511/596181136_49400.png)

## 直方图

可以使用`plot.hist()`方法绘制直方图。我们可以指定`bins`的数量值。

```
import pandas as pd
import numpy as np

df = pd.DataFrame({'a':np.random.randn(1000)+1,'b':np.random.randn(1000),'c':
np.random.randn(1000) - 1}, columns=['a', 'b', 'c'])

df.plot.hist(bins=20)
```


执行上面示例代码，得到以下结果 - 

![](http://www.yiibai.com/uploads/images/201711/0511/354181140_72017.png)

要为每列绘制不同的直方图，请使用以下代码 -

```
import pandas as pd
import numpy as np

df=pd.DataFrame({'a':np.random.randn(1000)+1,'b':np.random.randn(1000),'c':
np.random.randn(1000) - 1}, columns=['a', 'b', 'c'])

df.hist(bins=20)
```


执行上面示例代码，得到以下结果 - 

![](http://www.yiibai.com/uploads/images/201711/0511/532181142_60937.png)

## 箱形图

Boxplot可以绘制调用`Series.box.plot()`和`DataFrame.box.plot()`或`DataFrame.boxplot()`来可视化每列中值的分布。

例如，这里是一个箱形图，表示对`[0,1)`上的统一随机变量的`10`次观察的五次试验。

<ins class="adsbygoogle" style="display:inline-block;width:728px;height:90px" data-ad-client="ca-pub-1090193214637198" data-ad-slot="6494738921"></ins>

```
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.rand(10, 5), columns=['A', 'B', 'C', 'D', 'E'])
df.plot.box()
```


执行上面示例代码，得到以下结果 - 

![](http://www.yiibai.com/uploads/images/201711/0511/693191128_29628.png)

## 区域块图形

可以使用`Series.plot.area()`或`DataFrame.plot.area()`方法创建区域图形。

```
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
df.plot.area()
```


执行上面示例代码，得到以下结果 - 

![](http://www.yiibai.com/uploads/images/201711/0511/936191130_18945.png)

## 散点图形

可以使用`DataFrame.plot.scatter()`方法创建散点图。

```
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.rand(50, 4), columns=['a', 'b', 'c', 'd'])
df.plot.scatter(x='a', y='b')
```


执行上面示例代码，得到以下结果 - 

![](http://www.yiibai.com/uploads/images/201711/0511/605191131_96919.png)

## 饼状图

饼状图可以使用`DataFrame.plot.pie()`方法创建。

```
import pandas as pd
import numpy as np

df = pd.DataFrame(3 * np.random.rand(4), index=['a', 'b', 'c', 'd'], columns=['x'])
df.plot.pie(subplots=True)
```


执行上面示例代码，得到以下结果 - 

![](http://www.yiibai.com/uploads/images/201711/0511/571191132_24324.png)

# Pandas IO工具

Pandas I/O API是一套像`pd.read_csv()`一样返回`Pandas`对象的顶级读取器函数。

读取文本文件(或平面文件)的两个主要功能是`read_csv()`和`read_table()`。它们都使用相同的解析代码来智能地将表格数据转换为`DataFrame`对象 -

```
pandas.read_csv(filepath_or_buffer, sep=',', delimiter=None, header='infer',
names=None, index_col=None, usecols=None)
```


形式2-

```
pandas.read_csv(filepath_or_buffer, sep='\t', delimiter=None, header='infer',
names=None, index_col=None, usecols=None)
```


以下是csv文件数据的内容 -

```
S.No,Name,Age,City,Salary
1,Tom,28,Toronto,20000
2,Lee,32,HongKong,3000
3,Steven,43,Bay Area,8300
4,Ram,38,Hyderabad,3900
```

Csv

将这些数据保存为`temp.csv`并对其进行操作。

```
S.No,Name,Age,City,Salary
1,Tom,28,Toronto,20000
2,Lee,32,HongKong,3000
3,Steven,43,Bay Area,8300
4,Ram,38,Hyderabad,3900
```

## read.csv

`read.csv`从csv文件中读取数据并创建一个`DataFrame`对象。

```
import pandas as pd
df=pd.read_csv("temp.csv")
print (df)
```


执行上面示例代码，得到以下结果 - 

```
S.No    Name  Age       City  Salary
0     1     Tom   28    Toronto   20000
1     2     Lee   32   HongKong    3000
2     3  Steven   43   Bay Area    8300
3     4     Ram   38  Hyderabad    3900
```



**自定义索引**

可以指定csv文件中的一列来使用`index_col`定制索引。

```
import pandas as pd

df=pd.read_csv("temp.csv",index_col=['S.No'])
print (df)
```


执行上面示例代码，得到以下结果 - 

```
         Name  Age       City  Salary
S.No                                
1        Tom   28    Toronto   20000
2        Lee   32   HongKong    3000
3     Steven   43   Bay Area    8300
4        Ram   38  Hyderabad    3900
```



**转换器**  
`dtype`的列可以作为字典传递。

```
import pandas as pd
import numpy as np
df = pd.read_csv("temp.csv", dtype={'Salary': np.float64})
print (df.dtypes)
```


执行上面示例代码，得到以下结果 - 

```
S.No        int64
Name       object
Age         int64
City       object
Salary    float64
dtype: object
```



默认情况下，Salary列的`dtype`是`int`，但结果显示为`float`，因为我们明确地转换了类型。

因此，数据看起来像浮点数 -

```
   S.No   Name   Age      City    Salary
0   1     Tom   28    Toronto   20000.0
1   2     Lee   32   HongKong    3000.0
2   3  Steven   43   Bay Area    8300.0
3   4     Ram   38  Hyderabad    3900.0
```

**header_names**  
使用`names`参数指定标题的名称。

<ins class="adsbygoogle" style="display:inline-block;width:728px;height:90px" data-ad-client="ca-pub-1090193214637198" data-ad-slot="6494738921"></ins>

```
import pandas as pd
import numpy as np

df=pd.read_csv("temp.csv", names=['a', 'b', 'c','d','e'])
print (df)
```


执行上面示例代码，得到以下结果 - 

```
      a       b    c          d       e
0  S.No    Name  Age       City  Salary
1     1     Tom   28    Toronto   20000
2     2     Lee   32   HongKong    3000
3     3  Steven   43   Bay Area    8300
4     4     Ram   38  Hyderabad    3900
```



观察可以看到，标题名称附加了自定义名称，但文件中的标题还没有被消除。 现在，使用`header`参数来删除它。

如果标题不是第一行，则将行号传递给标题。这将跳过前面的行。

```
import pandas as pd
import numpy as np

df=pd.read_csv("temp.csv",names=['a','b','c','d','e'],header=0)
print (df)
```


执行上面示例代码，得到以下结果 - 

```
   a       b   c          d      e
0  1     Tom  28    Toronto  20000
1  2     Lee  32   HongKong   3000
2  3  Steven  43   Bay Area   8300
3  4     Ram  38  Hyderabad   3900
```



**skiprows**

`skiprows`跳过指定的行数。参考以下示例代码 - 

```
import pandas as pd
import numpy as np

df=pd.read_csv("temp.csv", skiprows=2)
print (df)
```


执行上面示例代码，得到以下结果 -

```
   2     Lee  32   HongKong  3000
0  3  Steven  43   Bay Area  8300
1  4     Ram  38  Hyderabad  3900
```

# Pandas稀疏数据

当任何匹配特定值的数据(NaN/缺失值，尽管可以选择任何值)被省略时，稀疏对象被“压缩”。 一个特殊的SparseIndex对象跟踪数据被“稀疏”的地方。 这将在一个例子中更有意义。 所有的标准Pandas数据结构都应用了`to_sparse`方法 -

```
import pandas as pd
import numpy as np

ts = pd.Series(np.random.randn(10))
ts[2:-2] = np.nan
sts = ts.to_sparse()
print (sts)
```


执行上面示例代码，得到以下结果 - 

```
0   -0.391926
1   -1.774880
2         NaN
3         NaN
4         NaN
5         NaN
6         NaN
7         NaN
8    0.642988
9   -0.373698
dtype: float64
BlockIndex
Block locations: array([0, 8])
Block lengths: array([2, 2])
```



为了内存效率的原因，所以需要稀疏对象的存在。

现在假设有一个大的NA DataFrame并执行下面的代码 -

```
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10000, 4))
df.ix[:9998] = np.nan
sdf = df.to_sparse()

print (sdf.density)
```


执行上面示例代码，得到以下结果 - 

```
0.0001
```



通过调用`to_dense`可以将任何稀疏对象转换回标准密集形式 -

```
import pandas as pd
import numpy as np
ts = pd.Series(np.random.randn(10))
ts[2:-2] = np.nan
sts = ts.to_sparse()
print (sts.to_dense())
```


执行上面示例代码，得到以下结果 - 

```
0   -0.275846
1    1.172722
2         NaN
3         NaN
4         NaN
5         NaN
6         NaN
7         NaN
8   -0.612009
9   -1.413996
dtype: float64
```



## 稀疏Dtypes

稀疏数据应该具有与其密集表示相同的dtype。 目前，支持`float64`，`int64`和`booldtypes`。 取决于原始的`dtype`，`fill_value`默认值的更改 -

* `float64` − `np.nan`
* `int64` − `0`
* `bool` − `False`

执行下面的代码来理解相同的内容 -

<ins class="adsbygoogle" style="display:inline-block;width:728px;height:90px" data-ad-client="ca-pub-1090193214637198" data-ad-slot="6494738921"></ins>

```
import pandas as pd
import numpy as np

s = pd.Series([1, np.nan, np.nan])
print (s)
print ("=============================")
s.to_sparse()
print (s)
```


执行上面示例代码，得到以下结果 - 

```
0    1.0
1    NaN
2    NaN
dtype: float64
=============================
0    1.0
1    NaN
2    NaN
dtype: float64
```

# Pandas注意事项＆窍门

警告和疑难意味着一个看不见的问题。在使用_Pandas_过程中，需要特别注意的地方。

## 与Pandas一起使用If/Truth语句

当尝试将某些东西转换成布尔值时，_Pandas_遵循了一个错误的惯例。 这种情况发生在使用布尔运算的。 目前还不清楚结果是什么。 如果它是真的，因为它不是`zerolength`？ 错误，因为有错误的值？ 目前还不清楚，_Pandas_提出了一个`ValueError` -

```
import pandas as pd

if pd.Series([False, True, False]):
    print ('I am True')
```


执行上面示例代码，得到以下结果 - 

```
ValueError: The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().
```



在`if`条件，它不清楚如何处理它。错误提示是否使用_None_或任何这些。

```
import pandas as pd
if pd.Series([False, True, False]).any():
    print("I am any")
```


要在布尔上下文中评估单元素_Pandas_对象，请使用方法`.bool()` -

```
import pandas as pd
print (pd.Series([True]).bool())
```


执行上面示例代码，得到以下结果 - 

```
True
```



## 按位布尔值

按位布尔运算符(如`==`和`!=`)将返回一个布尔系列，这几乎总是需要的。

```
import pandas as pd

s = pd.Series(range(5))
print (s==4)
```


执行上面示例代码，得到以下结果 - 

```
0    False
1    False
2    False
3    False
4     True
dtype: bool
```



**isin操作符**

这将返回一个布尔序列，显示系列中的每个元素是否完全包含在传递的值序列中。

```
import pandas as pd

s = pd.Series(list('abc'))
s = s.isin(['a', 'c', 'e'])
print (s)
```


执行上面示例代码，得到以下结果 - 

```
0     True
1    False
2     True
dtype: bool
```



**重构索引与ix陷阱**

许多用户会发现自己使用`ix`索引功能作为从Pandas对象中选择数据的简洁方法 -

```
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(6, 4), columns=['one', 'two', 'three',
'four'],index=list('abcdef'))

print (df)
print ("=============================================")
print (df.ix[['b', 'c', 'e']])
```


执行上面示例代码，得到以下结果 - 

```
one       two     three      four
a -1.174632  0.951047 -0.177007  1.036567
b -0.806324 -0.562209  1.081449 -1.047623
c  0.107607  0.778843 -0.063531 -1.073552
d -0.277602 -0.962720  1.381249  0.868656
e  0.576266  0.986949  0.433569  0.539558
f -0.708917 -0.583124 -0.686753 -2.338110
=============================================
        one       two     three      four
b -0.806324 -0.562209  1.081449 -1.047623
c  0.107607  0.778843 -0.063531 -1.073552
e  0.576266  0.986949  0.433569  0.539558
```



这当然在这种情况下完全等同于使用`reindex`方法 -

<ins class="adsbygoogle" style="display:inline-block;width:728px;height:90px" data-ad-client="ca-pub-1090193214637198" data-ad-slot="6494738921"></ins>

```
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(6, 4), columns=['one', 'two', 'three',
'four'],index=list('abcdef'))
print (df)
print("=============================================")
print (df.reindex(['b', 'c', 'e']))
```


执行上面示例代码，得到以下结果 - 

```
one       two     three      four
a -1.754084 -1.423820 -0.152234 -1.475104
b  1.508714 -0.216916 -0.184434 -2.117229
c -0.409298 -0.224142  0.308175 -0.681308
d  0.938517 -1.626353 -0.180770 -0.470252
e  0.718043 -0.730215 -0.716810  0.546039
f  2.313001  0.371286  0.359952  2.126530
=============================================
        one       two     three      four
b  1.508714 -0.216916 -0.184434 -2.117229
c -0.409298 -0.224142  0.308175 -0.681308
e  0.718043 -0.730215 -0.716810  0.546039
```



有人可能会得出这样的结论，`ix`和`reindex`是基于这个`100％`的等价物。 除了整数索引的情况，它是`true`。例如，上述操作可选地表示为 -

```
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(6, 4), columns=['one', 'two', 'three',
'four'],index=list('abcdef'))

print (df)
print("=====================================")
print (df.ix[[1, 2, 4]])
print("=====================================")
print (df.reindex([1, 2, 4]))
```


执行上面示例代码，得到以下结果 - 

```
one       two     three      four
a  1.017408  0.594357 -0.760587  1.001547
b -1.480067  1.524270  0.455070  1.886959
c -0.136238 -0.165867 -0.589767 -1.078473
d  0.670576  1.600312  0.219578 -1.121352
e -0.224181  0.958156  0.013055 -0.013652
f  1.576155 -0.185003 -0.527204 -0.336275
=====================================
        one       two     three      four
b -1.480067  1.524270  0.455070  1.886959
c -0.136238 -0.165867 -0.589767 -1.078473
e -0.224181  0.958156  0.013055 -0.013652
=====================================
   one  two  three  four
1  NaN  NaN    NaN   NaN
2  NaN  NaN    NaN   NaN
4  NaN  NaN    NaN   NaN
```



重要的是要记住，`reindex`只是严格的标签索引。这可能会导致一些潜在的令人惊讶的结果，例如索引包含整数和字符串的病态情况。

# Pandas与SQL比较

由于许多潜在的Pandas用户对SQL有一定的了解，因此本文章旨在提供一些如何使用_Pandas_执行各种SQL操作的示例。

```
import pandas as pd
url = 'tips.csv'
tips=pd.read_csv(url)
print (tips.head())
```


文件：_tips.csv_ - 

```
total_bill,tip,sex,smoker,day,time,size
0,16.99,1.01,Female,No,Sun,Dinner,2
1,10.34,1.66,Male,No,Sun,Dinner,3
2,21.01,3.50,Male,No,Sun,Dinner,3
3,23.68,3.31,Male,No,Sun,Dinner,2
4,24.59,3.61,Female,No,Sun,Dinner,4
```

Csv

执行上面示例代码，得到以下结果 - 

```
total_bill   tip     sex smoker  day    time  size
0       16.99  1.01  Female     No  Sun  Dinner     2
1       10.34  1.66    Male     No  Sun  Dinner     3
2       21.01  3.50    Male     No  Sun  Dinner     3
3       23.68  3.31    Male     No  Sun  Dinner     2
4       24.59  3.61  Female     No  Sun  Dinner     4
```



## 选择(Select)

在SQL中，选择是使用逗号分隔的列列表(或选择所有列)来完成的，例如 -

```
SELECT total_bill, tip, smoker, time
FROM tips
LIMIT 5;
```

SQL

在_Pandas_中，列的选择是通过传递列名到DataFrame -

```
tips[['total_bill', 'tip', 'smoker', 'time']].head(5)
```


下面来看看完整的程序 -

```
import pandas as pd

url = 'tips.csv'

tips=pd.read_csv(url)
rs = tips[['total_bill', 'tip', 'smoker', 'time']].head(5)
print(rs)
```


执行上面示例代码，得到以下结果 - 

```
total_bill   tip smoker    time
0       16.99  1.01     No  Dinner
1       10.34  1.66     No  Dinner
2       21.01  3.50     No  Dinner
3       23.68  3.31     No  Dinner
4       24.59  3.61     No  Dinner
```



调用没有列名称列表的DataFrame将显示所有列(类似于SQL的`*`)。

## WHERE条件

```
SELECT * FROM tips WHERE time = 'Dinner' LIMIT 5;
```

SQL

数据帧可以通过多种方式进行过滤; 最直观的是使用布尔索引。

```
tips[tips['time'] == 'Dinner'].head(5)
```


下面来看看完整的程序 -

```
import pandas as pd

url = 'tips.csv'

tips=pd.read_csv(url)
rs = tips[tips['time'] == 'Dinner'].head(5)
print(rs)
```


执行上面示例代码，得到以下结果 - 

```
total_bill   tip     sex smoker  day    time  size
0       16.99  1.01  Female     No  Sun  Dinner     2
1       10.34  1.66    Male     No  Sun  Dinner     3
2       21.01  3.50    Male     No  Sun  Dinner     3
3       23.68  3.31    Male     No  Sun  Dinner     2
4       24.59  3.61  Female     No  Sun  Dinner     4
```



上述语句将一系列`True/False`对象传递给DataFrame，并将所有行返回`True`。

## 通过GroupBy分组

此操作将获取整个数据集中每个组的记录数。 例如，一个查询提取性别的数量(即，按性别分组) -

<ins class="adsbygoogle" style="display:inline-block;width:728px;height:90px" data-ad-client="ca-pub-1090193214637198" data-ad-slot="6494738921"></ins>

```
SELECT sex, count(*)
FROM tips
GROUP BY sex;
```

SQL

在_Pandas_中的等值语句将是 -

```
tips.groupby('sex').size()
```


下面来看看完整的程序 -

```
import pandas as pd

url = 'tips.csv'

tips=pd.read_csv(url)
rs = tips.groupby('sex').size()
print(rs)
```


执行上面示例代码，得到以下结果 - 

```
sex
Female    2
Male      3
dtype: int64
```



## 前N行

SQL(MySQL数据库)使用`LIMIT`返回前`n`行 -

```
SELECT * FROM tips
LIMIT 5 ;
```


在_Pandas_中的等值语句将是 -

```
tips.head(5)
```


下面来看看完整的程序 -

```
import pandas as pd

url = 'tips.csv'

tips=pd.read_csv(url)
rs = tips[['smoker', 'day', 'time']].head(5)
print(rs)
```


执行上面示例代码，得到以下结果 - 

```
smoker  day    time
0     No  Sun  Dinner
1     No  Sun  Dinner
2     No  Sun  Dinner
3     No  Sun  Dinner
4     No  Sun  Dinner
```



这些是比较的几个基本操作，在前几章的_Pandas_库中学到的。



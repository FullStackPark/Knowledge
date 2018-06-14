# SciPy 简介

SciPy，发音为`Sigh Pi`，是一个科学的python开源代码，在BSD许可下分发的库，用于执行数学，科学和工程计算。

SciPy库依赖于NumPy，它提供了便捷且快速的`N`维数组操作。 SciPy库的构建与NumPy数组一起工作，并提供了许多用户友好和高效的数字实践，例如:数值积分和优化的例程。 它们一起运行在所有流行的操作系统上，安装快速且免费。 NumPy和SciPy易于使用，但强大到足以依靠世界上一些顶尖的科学家和工程师。

## SciPy子包

SciPy被组织成覆盖不同科学计算领域的子包。 这些总结在下表中 -

| 子包 |            |
| ------ |  ------  | 
| [scipy.cluster](https://docs.scipy.org/doc/scipy/reference/cluster.html#module-scipy.cluster "scipy.cluster")                 | 矢量量化/Kmeans |
| [scipy.constants](https://docs.scipy.org/doc/scipy/reference/constants.html#module-scipy.constants "scipy.constants")         | 物理和数学常数 |    
| [scipy.fftpack](https://docs.scipy.org/doc/scipy/reference/fftpack.html#module-scipy.fftpack "scipy.fftpack")                 | 傅里叶变换 |      
| [scipy.integrate](https://docs.scipy.org/doc/scipy/reference/integrate.html#module-scipy.integrate "scipy.integrate")         | 集成例程 |    
| [scipy.interpolate](https://docs.scipy.org/doc/scipy/reference/interpolate.html#module-scipy.interpolate "scipy.interpolate") | 插值 |      
| [scipy.io](https://docs.scipy.org/doc/scipy/reference/io.html#module-scipy.io "scipy.io")                                     | 数据输入和输出 |
| [scipy.linalg](https://docs.scipy.org/doc/scipy/reference/linalg.html#module-scipy.linalg "scipy.linalg")                     | 线性代数例程 |    
| [scipy.ndimage](https://docs.scipy.org/doc/scipy/reference/ndimage.html#module-scipy.ndimage "scipy.ndimage")                 | n维图像包 |      
| [scipy.odr](https://docs.scipy.org/doc/scipy/reference/odr.html#module-scipy.odr "scipy.odr")                                 | 正交距离回归 |    
| [scipy.optimize](https://docs.scipy.org/doc/scipy/reference/optimize.html#module-scipy.optimize "scipy.optimize")             | 优化 |         
| [scipy.signal](https://docs.scipy.org/doc/scipy/reference/signal.html#module-scipy.signal "scipy.signal")                     | 信号处理 |       
| [scipy.sparse](https://docs.scipy.org/doc/scipy/reference/sparse.html#module-scipy.sparse "scipy.sparse")                     | 稀疏矩阵 |       
| [scipy.spatial](https://docs.scipy.org/doc/scipy/reference/spatial.html#module-scipy.spatial "scipy.spatial")                 | 空间数据结构和算法 |  
| [scipy.special](https://docs.scipy.org/doc/scipy/reference/special.html#module-scipy.special "scipy.special")                 | 任何特殊的数学函数 |  
| [scipy.stats](https://docs.scipy.org/doc/scipy/reference/stats.html#module-scipy.stats "scipy.stats")                         | 统计 |         

## 数据结构

SciPy使用的基本数据结构是由NumPy模块提供的多维数组。 NumPy为线性代数，傅立叶变换和随机数生成提供了一些功能，但与SciPy中等效函数的一般性不同。

# SciPy 开发环境安装

标准Python发行版不捆绑任何SciPy模块。 一个轻量级的选择是使用流行的Python包安装程序安装SciPy，

```
$ pip install pandas
```


如果安装Anaconda Python软件包，默认情况下会安装Pandas。 以下是将它们安装在不同操作系统中的软件包和链接。

## Windows

* **Anaconda**(来自 [https://www.continuum.io](https://www.continuum.io/) )是SciPy堆栈的免费Python发行版。 它也适用于Linux和Mac。

* **Canopy**( https://www.enthought.com/products/canopy/ )免费提供，以及用于Windows，Linux和Mac的完整SciPy堆栈的商业发行。

* **Python(x，y)** - 这是一个免费的Python发行版，其中包含用于Windows操作系统的SciPy堆栈和Spyder IDE。 (可从 https://python-xy.github.io/ 下载)

## Linux

各个Linux发行版的软件包管理器用于在SciPy堆栈中安装一个或多个软件包。

**Ubuntu**  
可以使用以下路径在Ubuntu中安装Python。


```
$ sudo apt-get install python-numpy python-scipy 
python-matplotlibipythonipython-notebook python-pandas python-sympy python-nose
```


**Fedora**

可以使用以下路径在Fedora中安装Python。

```
sudo yum install numpyscipy python-matplotlibipython python-pandas 
sympy python-nose atlas-devel
```

# Scipy基本功能

默认情况下，所有的NumPy函数都可以通过SciPy命名空间获得。 当导入SciPy时，不需要显式导入NumPy函数。 NumPy的主要目标是均匀多维数组。 它是一个元素表(通常是数字)，都是相同类型，由正整数的元组索引。 在NumPy中，大小(尺寸)被称为轴。 轴的数量称为等级。

现在，让修改NumPy中的Vectors和Matrices的基本功能。 由于SciPy构建在NumPy数组之上，因此需要了解NumPy基础知识。 由于线性代数的大多数部分只处理矩阵。

**NumPy向量**

向量(Vector)可以通过多种方式创建。 其中一些描述如下。

将Python数组类对象转换为NumPy中的数组，看看下面的例子。

```
import numpy as np
list = [1,2,3,4]
arr = np.array(list)
print (arr)
```


执行上面示例代码，得到以下结果 - 

```
[1 2 3 4]
```


## 内在NumPy数组创建

NumPy有从头开始创建数组的内置函数。 其中一些函数解释如下。

**使用zeros()**

`zeros(shape)`函数将创建一个用指定形状(shape)填充`0`值的数组。 默认`dtype`是`float64`。 看看下面的例子。

```
import numpy as np
print (np.zeros((2, 3)))
```


执行上面示例代码，得到以下结果 - 

```
array([[ 0., 0., 0.],
[ 0., 0., 0.]])
```


**使用ones()**

`ones(shape)`函数将创建一个填充`1`值的数组。 它在所有其他方面与`0`相同。 看看下面的例子。

```
import numpy as np
print (np.ones((2, 3)))
```


执行上面示例代码，得到以下结果 - 

```
array([[ 1., 1., 1.],
[ 1., 1., 1.]])
```


**使用arange()**

`arange()`函数将创建具有有规律递增值的数组。 看看下面的例子。

```
import numpy as np
print (np.arange(7))
```


执行上面示例代码，得到以下结果 - 

```
array([0, 1, 2, 3, 4, 5, 6])
```


**定义值的数据类型**

看看下面一段示例代码 - 

```
import numpy as np
arr = np.arange(2, 10, dtype = np.float)
print (arr)
print ()"Array Data Type :",arr.dtype)
```


执行上面示例代码，得到以下结果 - 

```
[ 2. 3. 4. 5. 6. 7. 8. 9.]
Array Data Type : float64
```


**使用linspace()**

`linspace()`函数将创建具有指定数量元素的数组，这些元素将在指定的开始值和结束值之间平均间隔。 看看下面的例子。


```
import numpy as np
print (np.linspace(1., 4., 6))
```


执行上面示例代码，得到以下结果 - 

```
array([ 1. , 1.6, 2.2, 2.8, 3.4, 4. ])
```


## 矩阵

矩阵是一个专门的二维数组，通过操作保留其`2-D`特性。 它有一些特殊的运算符，如`*`(矩阵乘法)和`**`(矩阵幂值)。 看看下面的例子。

```
import numpy as np
print (np.matrix('1 2; 3 4'))
```


执行上面示例代码，得到以下结果 - 

```
matrix([[1, 2],
[3, 4]])
```


**矩阵的共轭转置**

此功能返回自我的(复数)共轭转置。 看看下面的例子。

```
import numpy as np
mat = np.matrix('1 2; 3 4')
print (mat.H)
```


执行上面示例代码，得到以下结果 - 

```
matrix([[1, 3],
        [2, 4]])
```


**矩阵的转置**

此功能返回自身的转置。看看下面的例子。

```
import numpy as np
mat = np.matrix('1 2; 3 4')
print (mat.T)
```


执行上面示例代码，得到以下结果 - 

```
matrix([[1, 3],
        [2, 4]])
```


当转置一个矩阵时，我们创建一个新的矩阵，其行是原始的列。 另一方面，共轭转置为每个矩阵元素交换行和列索引。 矩阵的逆矩阵是一个矩阵，如果与原始矩阵相乘，则产生一个单位矩阵。

# Scipy簇聚

K均值聚类是一种在一组未标记数据中查找聚类和聚类中心的方法。 直觉上，我们可以将一个群集(簇聚)看作 - 包含一组数据点，其点间距离与群集外点的距离相比较小。 给定一个K中心的初始集合，K均值算法重复以下两个步骤 -

    - 对于每个中心，比其他中心更接近它的训练点的子集(其聚类)被识别出来。
    - 计算每个聚类中数据点的每个要素的平均值，并且此平均向量将成为该聚类的新中心。

重复这两个步骤，直到中心不再移动或分配不再改变。 然后，可以将新点x分配给最接近的原型的群集。 SciPy库通过集群包提供了K-Means算法的良好实现。 下面来了解如何使用它。

SciPy中实现K-Means
我们来看看并理解如何在SciPy中实现K-Means。

导入K-Means

下面来看看每个导入的函数的实现和用法。

`from SciPy.cluster.vq import kmeans,vq,whiten`

数据生成

我们需要生成(模拟)一些数据来探索聚类。参考以下代码 -

```python

from numpy import vstack,array
from numpy.random import rand

# data generation with three features
data = vstack((rand(100,3) + array([.5,.5,.5]),rand(100,3)))

```

现在，我们来看看生成的模拟数据，上述程序将生成以下输出。

```

[[ 1.34103331  1.13924682  0.68465819]
 [ 1.28481332  0.91318917  0.84225546]
 [ 0.96498008  1.42382266  0.83564809]
 [ 1.37049373  0.66635033  1.46568707]
 [ 0.87424166  0.86090225  1.22545336]
 [ 1.0264795   0.90724604  1.46837972]
 [ 1.40996857  1.37769991  1.39805802]
 [ 0.964556    0.71632157  1.47983347]
 [ 0.69909637  1.21695335  1.46434369]
 [ 1.01887602  0.86448455  1.02242951]
 [ 0.82573176  1.19165063  1.09085707]
 [ 0.64378227  0.70673944  0.69484097]
 [ 1.16087103  0.64371977  0.89720984]
 [ 1.23410673  0.56805382  1.33534058]
 [ 0.50417695  1.29632466  0.96589447]
 [ 0.91395183  1.39173555  1.0748435 ]
 [ 1.04540644  1.20721464  0.97173727]
 ... ...
 [ 0.79250839  0.48689797  0.42250824]
 [ 0.05846914  0.83469742  0.57586067]
 [ 0.0308333   0.8642561   0.1111777 ]
 [ 0.61327069  0.43425013  0.99716439]
 [ 0.81698148  0.91098877  0.12706862]
 [ 0.60665992  0.55999208  0.57454962]
 [ 0.13894142  0.03315365  0.43182983]
 [ 0.62293781  0.34701877  0.61229591]]

```

根据每个要素标准化一组观察值。 在运行K-Means之前，使用白化重新缩放观察集的每个特征维度是有好处的。 每个特征除以所有观测值的标准偏差以给出其单位差异。

美化数据

我们可使用以下代码来美白数据。

```
# whitening of data
data = whiten(data)
print (data)
```

用三个集群计算K均值
现在使用以下代码计算三个群集的K均值。

```
# computing K-Means with K = 3 (2 clusters)
centroids,_ = kmeans(data,3)
```


上述代码对形成K个簇的一组观测向量执行K均值。 K-Means算法调整质心直到不能获得足够的进展，即失真的变化，因为最后一次迭代小于某个阈值。 在这里，可以通过使用下面给出的代码打印centroids变量来观察簇。

```print(centroids)```

上面的代码将生成以下输出。

```

print(centroids)[ [ 2.26034702  1.43924335  1.3697022 ]
                  [ 2.63788572  2.81446462  2.85163854]
                  [ 0.73507256  1.30801855  1.44477558] ]
```

使用下面给出的代码将每个值分配给一个集群。

```
# assign each sample to a cluster
clx,_ = vq(data,centroids)
```

vq函数将'M'中的每个观察向量与'N' obs数组与centroids进行比较，并将观察值分配给最近的聚类。 它返回每个观察和失真的聚类。 我们也可以检查失真。使用下面的代码检查每个观察的聚类。

```
# check clusters of observation
print (clx)
```

上面的代码将生成以下输出。

```

array([1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 2, 0, 2, 0, 1, 1, 1,
0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0,
0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
0, 1,  0, 0, 0, 0, 1, 0, 0, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 0, 2, 2, 2, 2, 2, 0, 0,
2, 2, 2, 1, 0, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 
2, 2, 0, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], dtype=int32)

```

上述数组的不同值 - 0,1,2表示簇。



# Scipy常量

SciPy常量(`constant`)包提供了广泛的常量，用于一般科学领域。

## SciPy常量包

`scipy.constants`包提供了各种常量。必须导入所需的常量并根据需要来使用它们。下面看看这些常量变量是如何导入和使用的。

首先，通过下面的例子来比较`'pi'`值。

```
#Import pi constant from both the packages

import scipy
import math

print("sciPy - pi = %.16f"%scipy.constants.pi)
print("math - pi = %.16f"%math.pi)
```

执行上面示例代码，得到以下结果 - 

```
sciPy - pi = 3.1415926535897931
math - pi = 3.1415926535897931
```

## 可用的常量列表

下表简要介绍了各种常数(常量)。

**数学常量**

| 编号 | 常量       | 描述   |
| -- | -------- | ---- |
| 1  | `pi`     | PI值  |
| 2  | `golden` | 黄金比例 |

**物理常量**

下表列出了最常用的物理常量。

| 编号 | 常量                      | 描述       |
| -- | ----------------------- | -------- |
| 1  | `c`                     | 真空中的光速   |
| 2  | `speed_of_light`        | 真空中的光速   |
| 3  | `h`                     | 普朗克常数    |
| 4  | `Planck`                | 普朗克常数`h` |
| 5  | `G`                     | 牛顿的引力常数  |
| 6  | `e`                     | 基本电荷     |
| 7  | `R`                     | 摩尔气体常数   |
| 8  | `Avogadro`              | 阿伏加德罗常数  |
| 9  | `k`                     | 波尔兹曼常数   |
| 10 | `electron_mass`或者 `m_e` | 电子质量     |
| 11 | `proton_mass`或者`m_p`    | 质子质量     |
| 12 | `neutron_mass`或`m_n`    | 中子质量     |

**单位**

下表列出了SI单位。

| 编号 | 单位      | 值     |
| -- | ------- | ----- |
| 1  | `milli` | 0.001 |
| 2  | `micro` | 1e-06 |
| 3  | `kilo`  | 1000  |

这些单位范围从`yotta`，`zetta`，`exa`，`peta`，`tera ...... kilo`，`hector`，`... nano`，`pico`，`...`到`zepto`。

**其他重要常量**

下表列出了SciPy中使用的其他重要常量。

| 编号 | 单位                  | 值             |
| -- | ------------------- | ------------- |
| 1  | `gram`              | 0.001 kg      |
| 2  | `atomic_mass`       | 原子质量常数        |
| 3  | `degree`            | 弧度            |
| 4  | `minute`            | 一分钟秒数(60)     |
| 5  | `day`               | 一天的秒数         |
| 6  | `inch`              | 一米的英寸数        |
| 7  | `micron`            | 一米的微米数        |
| 8  | `light_year`        | 一光年的米数        |
| 9  | `atm`               | 帕斯卡标准大气压      |
| 10 | `acre`              | 一平方米的英亩数      |
| 11 | `liter`             | 一立方米的升数       |
| 12 | `gallon`            | 一立方米的加仑数      |
| 13 | `kmh`               | 公里每小时，以米/秒为单位 |
| 14 | `degree_fahrenheit` | 一凯尔文的华氏数      |
| 15 | `eV`                | 一焦耳的电子伏特数     |
| 16 | `hp`                | 一瓦特的马力数       |
| 17 | `dyn`               | 一牛顿的达因数       |
| 18 | `lambda2nu`         | 将波长转换为光频率     |

要记住所有这些都有点困难。可使用`scipy.constants.find()`方法获取指定键的简单方法。 看看下面的例子。


```
import scipy.constants
res = scipy.constants.physical_constants["alpha particle mass"]
print (res)
```

执行上面示例代码，得到以下结果 - 

```
(6.64465723e-27, 'kg', 8.2e-35)
```

# Scipy FFTpack

对时域信号计算傅里叶变换以检查其在频域中的行为。 傅里叶变换可用于信号和噪声处理，图像处理，音频信号处理等领域。SciPy提供`fftpack`模块，可让用户计算快速傅立叶变换。

以下是一个正弦函数的例子，它将用于使用`fftpack`模块计算傅里叶变换。

## 快速傅立叶变换

下面来了解一下快速傅立叶变换的细节。

**一维离散傅立叶变换**

长度为`N`的序列`x [n]`的`FFT y [k]`由`fft()`计算，逆变换使用`ifft()`计算。 看看下面的例子

```
#Importing the fft and inverse fft functions from fftpackage
from scipy.fftpack import fft

#create an array with random n numbers
x = np.array([1.0, 2.0, 1.0, -1.0, 1.5])

#Applying the fft function
y = fft(x)
print (y)
```

执行上面示例代码，得到以下结果 - 

```
[ 4.50000000+0.j          2.08155948-1.65109876j -1.83155948+1.60822041j
 -1.83155948-1.60822041j  2.08155948+1.65109876j]
```

再看另一个示例 - 

```
#Importing the fft and inverse fft functions from fftpackage
from scipy.fftpack import fft
from scipy.fftpack import ifft

#create an array with random n numbers
x = np.array([1.0, 2.0, 1.0, -1.0, 1.5])

#Applying the fft function
y = fft(x)
#FFT is already in the workspace, using the same workspace to for inverse transform

yinv = ifft(y)

print (yinv)
```

执行上面示例代码，得到以下结果 - 

```
[ 1.0+0.j  2.0+0.j  1.0+0.j -1.0+0.j  1.5+0.j]
```

`scipy.fftpack`模块允许计算快速傅立叶变换。 作为一个例子，一个(嘈杂的)输入信号可能看起来如下 -

```
import numpy as np
time_step = 0.02
period = 5.
time_vec = np.arange(0, 20, time_step)
sig = np.sin(2 * np.pi / period * time_vec) + 0.5 *np.random.randn(time_vec.size)
print (sig.size)
```

我们正以`0.02`秒的时间步长创建一个信号。 最后一条语句显示信号`sig`的大小。 输出结果如下 -

```
1000
```

我们不知道信号频率; 只知道信号`sig`的采样时间步长。 信号应该来自实际函数，所以傅里叶变换将是对称的。 `scipy.fftpack.fftfreq()`函数将生成采样频率，`scipy.fftpack.fft()`将计算快速傅里叶变换。

下面通过一个例子来理解这一点。

```
from scipy import fftpack
sample_freq = fftpack.fftfreq(sig.size, d = time_step)
sig_fft = fftpack.fft(sig)
print (sig_fft)
```

执行上面示例代码，得到以下结果 - 

```
array([ 
   25.45122234 +0.00000000e+00j,   6.29800973 +2.20269471e+00j,
   11.52137858 -2.00515732e+01j,   1.08111300 +1.35488579e+01j,
   …….])
```

## 离散余弦变换

离散余弦变换(DCT)根据以不同频率振荡的余弦函数的和表示有限数据点序列。 SciPy提供了一个带有函数`idct`的DCT和一个带有函数`idct`的相应IDCT。看看下面的一个例子。

```
from scipy.fftpack import dct
mydict = dct(np.array([4., 3., 5., 10., 5., 3.]))
print(mydict)
```

执行上面示例代码，得到以下结果 - 

```
[ 60.          -3.48476592 -13.85640646  11.3137085    6.          -6.31319305]
```

逆离散余弦变换从其离散余弦变换(DCT)系数重建序列。 `idct`函数是`dct`函数的反函数。 可通过下面的例子来理解这一点。

```
from scipy.fftpack import dct
from scipy.fftpack import idct
d = idct(np.array([4., 3., 5., 10., 5., 3.]))
print(d)
```

执行上面示例代码，得到以下结果 - 

```
[ 39.15085889 -20.14213562  -6.45392043   7.13341236   8.14213562
  -3.83035081]
```

# Scipy积分

当一个函数不能被分析积分，或者很难分析积分时，通常会转向数值积分方法。 SciPy有许多用于执行数值积分的程序。 它们中的大多数都在同一个`scipy.integrate`库中。 下表列出了一些常用函数。

| 编号 | 示例           | 描述                 |
| -- | ------------ | ------------------ |
| 1  | `quad`       | 单积分                |
| 2  | `dblquad`    | 二重积分               |
| 3  | `tplquad`    | 三重积分               |
| 4  | `nquad`      | n倍多重积分             |
| 5  | `fixed_quad` | 高斯积分，阶数`n`         |
| 6  | `quadrature` | 高斯正交到容差            |
| 7  | `romberg`    | Romberg积分          |
| 8  | `trapz`      | 梯形规则               |
| 9  | `cumtrapz`   | 梯形法则累计计算积分         |
| 10 | `simps`      | 辛普森的规则             |
| 11 | `romb`       | Romberg积分          |
| 12 | `polyint`    | 分析多项式积分(NumPy)     |
| 13 | `poly1d`     | 辅助函数polyint(NumPy) |

## 单积分

Quad函数是SciPy积分函数的主力。 数值积分有时称为正交积分，因此称为名称。 它通常是在`a`到`b`给定的固定范围内执行函数`f(x)`的单个积分的默认选择。

![](http://www.yiibai.com/uploads/images/201803/0503/954160341_84044.png)

`quad`的一般形式是`scipy.integrate.quad(f，a，b)`，其中`'f'`是要积分的函数的名称。 而`'a'`和`'b'`分别是下限和上限。 下面来看看一个高斯函数的例子，它的积分范围是`0`和`1`。

首先需要定义这个函数:  
![](http://www.yiibai.com/uploads/images/201803/0503/912160343_74999.png)

这可以使用`lambda`表达式完成，然后在该函数上调用四方法。

```
import scipy.integrate
from numpy import exp
f= lambda x:exp(-x**2)
i = scipy.integrate.quad(f, 0, 1)
print (i)
```

执行上面示例代码，得到以下结果 - 

```
(0.7468241328124271, 8.291413475940725e-15)
```

四元函数返回两个值，其中第一个数字是积分值，第二个数值是积分值绝对误差的估计值。

> 注 - 由于`quad`需要函数作为第一个参数，因此不能直接将`exp`作为参数传递。 Quad函数接受正和负无穷作为限制。 Quad函数可以积分单个变量的标准预定义NumPy函数，如`exp`，`sin`和`cos`。

## 多重积分

双重和三重积分的机制已被包含到函数`dblquad`，`tplquad`和`nquad`中。 这些函数分别积分了四个或六个参数。 所有内积分的界限都需要定义为函数。

## 双重积分

`dblquad`的一般形式是`scipy.integrate.dblquad(func，a，b，gfun，hfun)`。 其中，`func`是要积分函数的名称，`'a'`和`'b'`分别是`x`变量的下限和上限，而`gfun`和`hfun`是定义变量`y`的下限和上限的函数名称。

看看一个执行双重积分方法的示例。

![](http://www.yiibai.com/uploads/images/201803/0503/652160349_12005.png)

使用`lambda`表达式定义函数`f`，`g`和`h`。 请注意，即使`g`和`h`是常数，它们可能在很多情况下必须定义为函数，正如在这里为下限所做的那样。


```
import scipy.integrate
from numpy import exp
from math import sqrt
f = lambda x, y : 16*x*y
g = lambda x : 0
h = lambda y : sqrt(1-4*y**2)
i = scipy.integrate.dblquad(f, 0, 0.5, g, h)
print (i)
```

执行上面示例代码，得到以下结果 - 

```
(0.5, 1.7092350012594845e-14)
```

除上述例程外，`scipy.integrate`还有许多其他积分的程序，其中包括执行`n`次多重积分的nquad以及实现各种集成算法的其他例程。 但是，`quad`和`dblquad`将满足对数值积分的大部分需求。

# Scipy插值

在本章中，我们将讨论插值，及如何在SciPy中使用它。

## 插值是什么？

插值是在直线或曲线上的两点之间找到值的过程。 为了帮助记住它的含义，我们应该将“inter”这个词的第一部分想象为“输入”，表示要查看原来数据的“内部”。 这种插值工具不仅适用于统计学，而且在科学，商业或需要预测两个现有数据点内的值时也很有用。

下面创建一些数据，看看如何使用`scipy.interpolate`包进行插值。

```
import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
x = np.linspace(0, 4, 12)
y = np.cos(x**2/3+4)
print (x,y)
```

执行上面示例代码，得到以下结果 - 

```
[ 0.          0.36363636  0.72727273  1.09090909  1.45454545  1.81818182
  2.18181818  2.54545455  2.90909091  3.27272727  3.63636364  4.        ] [-0.65364362 -0.61966189 -0.51077021 -0.31047698 -0.00715476  0.37976236
  0.76715099  0.99239518  0.85886263  0.27994201 -0.52586509 -0.99582185]
```

现在，有两个数组。 假设这两个数组作为空间点的两个维度，使用下面的程序进行绘图，并看看它们的样子。

```
plt.plot(x, y,’o’)
plt.show()
```

上述程序将生成以下输出 -  
![](http://www.yiibai.com/uploads/images/201803/0503/567170300_31484.jpg)

## 一维插值

`scipy.interpolate`中的`interp1d`类是一种创建基于固定数据点的函数的便捷方法，可以使用线性插值在给定数据定义的域内的任意位置评估该函数。

通过使用上述数据，创建一个插值函数并绘制一个新的插值图。

```
f1 = interp1d(x, y,kind = 'linear')

f2 = interp1d(x, y, kind = 'cubic')
```

使用`interp1d`函数，创建了两个函数`f1`和`f2`。 这些函数对于给定的输入`x`返回`y`。 第三种变量类型表示插值技术的类型。 ‘线性’，’最近’，’零’，’线性’，’二次’，’立方’是一些插值技术。

现在，创建更多长度的新输入以查看插值的明显区别。 对新数据使用旧数据的相同功能。

```
xnew = np.linspace(0, 4,30)

plt.plot(x, y, 'o', xnew, f(xnew), '-', xnew, f2(xnew), '--')

plt.legend(['data', 'linear', 'cubic','nearest'], loc = 'best')

plt.show()
```

上述程序将生成以下输出 - 

![](http://www.yiibai.com/uploads/images/201803/0503/895170303_80894.jpg)

## 样条曲线

为了通过数据点画出平滑的曲线，绘图员曾经使用薄的柔性木条，硬橡胶，金属或塑料称为机械样条。 为了使用机械花键，在设计中沿着曲线明确选择了一些销钉，然后将花键弯曲，以便它们接触到每个销钉。

显然，在这种结构下，样条曲线在这些引脚上插入曲线。 它可以用来在其他图纸中重现曲线。 引脚所在的点称为结。 可以通过调整结点的位置来改变样条线所定义的曲线的形状。

**单变量样条**

一维平滑样条拟合一组给定的数据点。 `Scipy.interpolate`中的`UnivariateSpline`类是创建基于固定数据点类的函数的便捷方法 - `scipy.interpolate.UnivariateSpline(x，y，w = None，bbox = [None，None]，k = 3，s = None，ext = 0，check_finite = False)`。

下面来看看一个例子。


```
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
x = np.linspace(-3, 3, 50)
y = np.exp(-x**2) + 0.1 * np.random.randn(50)
plt.plot(x, y, 'ro', ms = 5)
plt.show()
```

使用平滑参数的默认值。效果如下 -  
![](http://www.yiibai.com/uploads/images/201803/0503/341170306_16966.jpg)

```
spl = UnivariateSpline(x, y)
xs = np.linspace(-3, 3, 1000)
plt.plot(xs, spl(xs), 'g', lw = 3)
plt.show()
```

手动更改平滑量。效果如下 -  
![](http://www.yiibai.com/uploads/images/201803/0503/799170306_90412.jpg)

```
spl.set_smoothing_factor(0.5)
plt.plot(xs, spl(xs), 'b', lw = 3)
plt.show()
```

效果如下 -  
![](http://www.yiibai.com/uploads/images/201803/0503/769170307_64326.jpg)

# Scipy输入和输出

Scipy.io包提供了多种功能来解决不同格式的文件(输入和输出)。 其中一些格式是 -

* Matlab
* IDL
* Matrix Market
* Wave
* Arff
* Netcdf等

这里讨论最常用的文件格式 -

**MATLAB**

以下是用于加载和保存`.mat`文件的函数。

| 编号 | 函数        | 描述             |
| -- | --------- | -------------- |
| 1  | `loadmat` | 加载一个MATLAB文件   |
| 2  | `savemat` | 保存为一个MATLAB文件  |
| 3  | `whosmat` | 列出MATLAB文件中的变量 |

让我们来看看下面的例子。

```
import scipy.io as sio
import numpy as np

#Save a mat file
vect = np.arange(10)
sio.savemat('array.mat', {'vect':vect})

#Now Load the File
mat_file_content = sio.loadmat('array.mat')
print (mat_file_content)
```

上述程序将生成以下输出 - 


```
{
   'vect': array([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]), '__version__': '1.0', 
   '__header__': 'MATLAB 5.0 MAT-file Platform: posix, Created on: Sat Sep 30 
   09:49:32 2017', '__globals__': []
}
```

可以看到数组以及元信息。 如果想在不读取数据到内存的情况下检查MATLAB文件的内容，请使用如下所示的`whosmat`命令。

```
import scipy.io as sio
mat_file_content = sio.whosmat(‘array.mat’)
print (mat_file_content)
```

上述程序将生成以下输出。

```
[('vect', (1, 10), 'int64')]
```


# Scipy Linalg

SciPy是使用优化的ATLAS LAPACK和BLAS库构建的。 它具有非常快的线性代数能力。 所有这些线性代数例程都需要一个可以转换为二维数组的对象。 这些例程的输出也是一个二维数组。

**SciPy.linalg与NumPy.linalg**

`scipy.linalg`包含`numpy.linalg`中的所有函数。 另外，`scipy.linalg`还有一些不在`numpy.linalg`中的高级函数。 在`numpy.linalg`上使用`scipy.linalg`的另一个优点是它总是用`BLAS/LAPACK`支持编译，而对于NumPy，这是可选的。 因此，根据NumPy的安装方式，SciPy版本可能会更快。

## 线性方程组

`scipy.linalg.solve`特征为未知的`x`，`y`值求解线性方程`a * x + b * y = Z`。

作为一个例子，假设需要解下面的联立方程。  
![](http://www.yiibai.com/uploads/images/201803/0503/788090306_94523.png)

要求解`x`，`y`，`z`值的上述方程式，可以使用矩阵求逆来求解向量，如下所示。  
![](http://www.yiibai.com/uploads/images/201803/0503/917090306_49173.png)

但是，最好使用`linalg.solve`命令，该命令可以更快，更稳定。

求解函数采用两个输入`'a'`和`'b'`，其中`'a'`表示系数，`'b'`表示相应的右侧值并返回解矩阵。

现在来看看下面的例子。

```
#importing the scipy and numpy packages
from scipy import linalg
import numpy as np

#Declaring the numpy arrays
a = np.array([[3, 2, 0], [1, -1, 0], [0, 5, 1]])
b = np.array([2, 4, -1])

#Passing the values to the solve function
x = linalg.solve(a, b)

#printing the result array
print (x)
```

执行上面示例代码，得到以下结果 - 

```
[ 2. -2.  9.]
```

## 查找一个行列式

方阵A的行列式通常表示为`| A |`并且是线性代数中经常使用的量。 在SciPy中，这是使用`det()`函数计算的。 它将矩阵作为输入并返回一个标量值。

下面来看看一个例子。

```
#importing the scipy and numpy packages
from scipy import linalg
import numpy as np

#Declaring the numpy array
A = np.array([[1,2],[3,4]])

#Passing the values to the det function
x = linalg.det(A)

#printing the result
print (x)
```

执行上面示例代码，得到以下结果 - 

```
-2.0
```

## 特征值和特征向量

特征值 - 特征向量问题是最常用的线性代数运算之一。 我们可以通过考虑以下关系式来找到方阵(A)的特征值(λ)和相应的特征向量(v)


```
Av = λv
```

`scipy.linalg.eig`从普通或广义特征值问题计算特征值。 该函数返回特征值和特征向量。

让我们来看看下面的例子。

```
#importing the scipy and numpy packages
from scipy import linalg
import numpy as np

#Declaring the numpy array
A = np.array([[1,2],[3,4]])

#Passing the values to the eig function
l, v = linalg.eig(A)

#printing the result for eigen values
print (l)

#printing the result for eigen vectors
print (v)
```

执行上面示例代码，得到以下结果 - 

```
[-0.37228132+0.j  5.37228132+0.j]
[[-0.82456484 -0.41597356]
 [ 0.56576746 -0.90937671]]
```

## 奇异值分解

奇异值分解(SVD)可以被认为是特征值问题扩展到非矩阵的矩阵。

`scipy.linalg.svd`将矩阵`'a'`分解为两个酉矩阵`'U'`和`'Vh'`，以及一个奇异值(实数，非负)的一维数组`'s'`，使得`a == U * S * Vh`，其中`'S'`是具有主对角线`'s'`的适当形状的零点矩阵。

让我们来看看下面的例子。参考以下代码 - 

```
#importing the scipy and numpy packages
from scipy import linalg
import numpy as np

#Declaring the numpy array
a = np.random.randn(3, 2) + 1.j*np.random.randn(3, 2)

#Passing the values to the eig function
U, s, Vh = linalg.svd(a)

# printing the result
print (U, Vh, s)
```

执行上面示例代码，得到以下结果 - 

```
[[-0.60142679+0.28212127j  0.35719830-0.03260559j  0.61548126-0.22632383j]
 [-0.00477296+0.44250532j  0.64058557+0.15734719j -0.40414313+0.45357092j]
 [ 0.46360086+0.38462177j -0.18611686+0.6337182j   0.44311251+0.06747886j]] [[ 0.98724353+0.j         -0.01113675+0.15882756j]
 [-0.15921753+0.j         -0.06905445+0.9848255j ]] [ 2.04228408  1.33798044]
```

# Scipy Ndimage

SciPy的`ndimage`子模块专用于图像处理。 这里，`ndimage`表示一个`n`维图像。

图像处理中一些最常见的任务如下:

* 输入/输出，显示图像
* 基本操作 - 裁剪，翻转，旋转等
* 图像过滤 - 去噪，锐化等
* 图像分割 - 标记对应于不同对象的像素
* 分类
* 特征提取
* 注册

下面来看看如何使用SciPy实现其中的一些功能。

## 打开和写入图像文件

SciPy中的`misc`包附带了一些图像。 在这里，使用这些图像来学习图像操作。请看看下面的例子。

```
from scipy import misc
f = misc.face()
misc.imsave('face.png', f) # uses the Image module (PIL)

import matplotlib.pyplot as plt
plt.imshow(f)
plt.show()
```

执行上面示例代码，得到以下输出结果 -  
![](http://www.yiibai.com/uploads/images/201803/0503/312090323_42130.png)

原始格式的任何图像是由矩阵格式中的数字表示的颜色的组合。 机器只能根据这些数字理解和操作图像。 RGB是一种流行的表示方式。

下面来看看上面图片的统计信息。

```
from scipy import misc
f = misc.face()
misc.imsave('face.png', f) # uses the Image module (PIL)

face = misc.face(gray = False)
print (face.mean(), face.max(), face.min())
```

执行上面示例代码，得到以下结果 - 

```
110.162743886 255 0
```

现在，我们已经知道图像是由数字组成的，所以数字值的任何变化都会改变原始图像。接下来对图像执行一些几何变换。 基本的几何操作是裁剪 - 

```
from scipy import misc
f = misc.face()
misc.imsave('face.png', f) # uses the Image module (PIL)
face = misc.face(gray = True)
lx, ly = face.shape

crop_face = face[int(lx/4): -int(lx/4), int(ly/4): -int(ly/4)]

import matplotlib.pyplot as plt
plt.imshow(crop_face)
plt.show()
```

执行上面示例代码，得到以下结果 - 

![](http://www.yiibai.com/uploads/images/201803/0503/493090332_58963.png)

也可以执行一些基本的操作，例如像下面描述的那样倒置图像。参考以下代码 - 

```
from scipy import misc

face = misc.face()
flip_ud_face = np.flipud(face)

import matplotlib.pyplot as plt
plt.imshow(flip_ud_face)
plt.show()
```

执行上面示例代码，得到以下结果 - 

![](http://www.yiibai.com/uploads/images/201803/0503/427090333_19676.png)

除此之外，还有`rotate()`函数，它以指定的角度旋转图像。

```
# rotation
from scipy import misc,ndimage
face = misc.face()
rotate_face = ndimage.rotate(face, 45)

import matplotlib.pyplot as plt
plt.imshow(rotate_face)
plt.show()
```


执行上面示例代码，得到以下结果 -  
![](http://www.yiibai.com/uploads/images/201803/0503/892090334_93166.png)

## 滤镜

下面来看看滤镜如何应用在图像处理中。

**图像处理中的滤镜是什么？**

滤镜是一种修改或增强图像的技术。 例如，可以过滤图像以强调某些功能或删除其他功能。 通过滤镜实现的图像处理操作包括平滑，锐化和边缘增强。

滤镜是一种邻域操作，其中输出图像中任何给定像素的值是通过对相应输入像素的邻域中的像素的值应用某种算法来确定的。 现在使用SciPy ndimage执行一些操作。

**模糊**

模糊广泛用于减少图像中的噪声。 可以执行过滤操作并查看图像中的更改。看看下面的例子。

<ins class="adsbygoogle" style="display:inline-block;width:728px;height:90px" data-ad-client="ca-pub-1090193214637198" data-ad-slot="6494738921"></ins>

```
from scipy import misc
face = misc.face()
blurred_face = ndimage.gaussian_filter(face, sigma=3)
import matplotlib.pyplot as plt
plt.imshow(blurred_face)
plt.show()
```

执行上面示例代码，得到以下结果 -  
![](http://www.yiibai.com/uploads/images/201803/0503/275090339_80786.png)

`sigma`值表示`5`级模糊程度。 通过调整`sigma`值，可以看到图像质量的变化。

## 边缘检测

讨论边缘检测如何帮助图像处理。

**什么是边缘检测？**

边缘检测是一种用于查找图像内物体边界的图像处理技术。 它通过检测亮度不连续性来工作。 边缘检测用于诸如图像处理，计算机视觉和机器视觉等领域的图像分割和数据提取。

最常用的边缘检测算法包括 - 

* 索贝尔(Sobel)
* 坎尼(Canny)
* 普鲁伊特(Prewitt)
* 罗伯茨Roberts
* 模糊逻辑方法

看看下面的一个例子。

```
import scipy.ndimage as nd
import numpy as np

im = np.zeros((256, 256))
im[64:-64, 64:-64] = 1
im[90:-90,90:-90] = 2
im = ndimage.gaussian_filter(im, 8)

import matplotlib.pyplot as plt
plt.imshow(im)
plt.show()
```

执行上面示例代码，得到以下结果  -  
![](http://www.yiibai.com/uploads/images/201803/0503/414090343_42281.png)

图像看起来像一个方块的颜色。现在，检测这些彩色块的边缘。 这里，`ndimage`提供了一个叫`Sobel`函数来执行这个操作。 而NumPy提供了`Hypot`函数来将两个合成矩阵合并为一个。

看看下面的一个例子。参考以下实现代码 - 

```
import scipy.ndimage as nd
import matplotlib.pyplot as plt

im = np.zeros((256, 256))
im[64:-64, 64:-64] = 1
im[90:-90,90:-90] = 2
im = ndimage.gaussian_filter(im, 8)

sx = ndimage.sobel(im, axis = 0, mode = 'constant')
sy = ndimage.sobel(im, axis = 1, mode = 'constant')
sob = np.hypot(sx, sy)

plt.imshow(sob)
plt.show()
```

执行上面示例代码，得到以下结果 -  
![](http://www.yiibai.com/uploads/images/201803/0503/362090344_12090.png)

# Scipy优化算法

`scipy.optimize`包提供了几种常用的优化算法。 该模块包含以下几个方面 -

* 使用各种算法(例如BFGS，Nelder-Mead单纯形，牛顿共轭梯度，COBYLA或SLSQP)的无约束和约束最小化多元标量函数(`minimize()`)
* 全局(蛮力)优化程序(例如，`anneal()`，`basinhopping()`)
* 最小二乘最小化(`leastsq()`)和曲线拟合(`curve_fit()`)算法
* 标量单变量函数最小化(`minim_scalar()`)和根查找(`newton()`)
* 使用多种算法(例如，Powell，Levenberg-Marquardt混合或Newton-Krylov等大规模方法)的多元方程系统求解(root)

**多变量标量函数的无约束和约束最小化**

`minimize()`函数为`scipy.optimize`中的多变量标量函数提供了无约束和约束最小化算法的通用接口。 为了演示最小化函数，考虑使`NN`变量的`Rosenbrock`函数最小化的问题 -  
![](http://www.yiibai.com/uploads/images/201803/0503/124090349_54034.png)

这个函数的最小值是`0`，当`xi = 1`时达到。

## Nelder–Mead单纯形算法

在下面的例子中，`minimize()`例程与Nelder-Mead单纯形算法(`method ='Nelder-Mead'`)一起使用(通过方法参数选择)。参考下面的例子。

```
import numpy as np
from scipy.optimize import minimize

def rosen(x):

x0 = np.array([1.3, 0.7, 0.8, 1.9, 1.2])
res = minimize(rosen, x0, method='nelder-mead')

print(res.x)
```

上述程序将生成以下输出 - 

```
[7.93700741e+54  -5.41692163e+53  6.28769150e+53  1.38050484e+55  -4.14751333e+54]
```

简单算法只需要函数评估，对于简单的最小化问题是一个不错的选择。 但是，由于它不使用任何梯度评估，因此可能需要较长时间才能找到最小值。

另一种只需要函数调用来寻找最小值的优化算法就是鲍威尔方法，它可以通过在`minimize()`函数中设置`method ='powell'`来实现。

## 　最小二乘

求解一个带有变量边界的非线性最小二乘问题。 给定残差`f(x)`(n个实变量的m维实函数)和损失函数`rho(s)`(标量函数)，最小二乘法找到代价函数`F(x)`的局部最小值。 看看下面的例子。

在这个例子中，`Rosenbrock`函数的最小值不受自变量的限制。

```
#Rosenbrock Function
def fun_rosenbrock(x):
   return np.array([10 * (x[1] - x[0]**2), (1 - x[0])])

from scipy.optimize import least_squares
input = np.array([2, 2])
res = least_squares(fun_rosenbrock, input)

print (res)
```

请注意，我们只提供残差的向量。 该算法将成本函数构造为残差的平方和，这给出了`Rosenbrock()`函数。 确切的最小值是`x = [1.0,1.0]`。

上述程序将生成以下输出 - 

```
active_mask: array([ 0., 0.])
      cost: 9.8669242910846867e-30
      fun: array([ 4.44089210e-15, 1.11022302e-16])
      grad: array([ -8.89288649e-14, 4.44089210e-14])
      jac: array([[-20.00000015,10.],[ -1.,0.]])
   message: '`gtol` termination condition is satisfied.'
      nfev: 3
      njev: 3
   optimality: 8.8928864934219529e-14
      status: 1
      success: True
         x: array([ 1., 1.])
```

## 求根

让我们了解求根如何在SciPy中使用。

**标量函数**

如果有一个单变量方程，则可以尝试四种不同的寻根算法。 这些算法中的每一个都需要预期根的时间间隔的端点(因为函数会改变符号)。 一般来说，`brentq`是最好的选择，但其他方法可能在某些情况下或学术目的有用。

**定点求解**

与找到函数零点密切相关的问题是找到函数的固定点的问题。 函数的固定点是函数评估返回点的点:`g(x)= x`。 显然，`gg`的不动点是`f(x)= g(x)-x`的根。 等价地，`ff`的根是`g(x)= f(x)+ x`的固定点。 例程`fixed_point`提供了一个简单的迭代方法，使用`Aitkens`序列加速度来估计`gg`的固定点，如果给出起点的话。

**方程组**  
使用`root()`函数可以找到一组非线性方程的根。 有几种方法可供选择，其中`hybr`(默认)和`lm`分别使用`Powell`的混合方法和`MINPACK`中的Levenberg-Marquardt方法。

下面的例子考虑了单变量超越方程。  
![](http://www.yiibai.com/uploads/images/201803/0503/486100315_23611.png)

其根可以求解如下 -

```
import numpy as np
from scipy.optimize import root
def func(x):
   return x*2 + 2 * np.cos(x)
sol = root(func, 0.3)
print (sol)
```

执行上面示例代码，得到以下结果 - 

```
fjac: array([[-1.]])
fun: array([ 2.22044605e-16])
message: 'The solution converged.'
   nfev: 10
   qtf: array([ -2.77644574e-12])
      r: array([-3.34722409])
   status: 1
   success: True
      x: array([-0.73908513])
```

# Scipy统计函数

所有的统计函数都位于子包`scipy.stats`中，并且可以使用`info(stats)`函数获得这些函数的完整列表。随机变量列表也可以从`stats`子包的`docstring`中获得。 该模块包含大量的概率分布以及不断增长的统计函数库。

每个单变量分布都有其自己的子类，如下表所述 -

| 编号 | 类               | 描述              |
| -- | --------------- | --------------- |
| 1  | `rv_continuous` | 用于子类化的通用连续随机变量类 |
| 2  | `rv_discrete`   | 用于子类化的通用离散随机变量类 |
| 3  | `rv_histogram`  | 生成由直方图给出的分布     |

## 正态连续随机变量

随机变量X可以取任何值的概率分布是连续的随机变量。 位置(`loc`)关键字指定平均值。 比例(`scale`)关键字指定标准偏差。

作为`rv_continuous`类的一个实例，规范对象从中继承了一系列泛型方法，并通过特定于此特定分发的细节完成它们。

要计算多个点的CDF，可以传递一个列表或一个NumPy数组。 看看下面的一个例子。

```
from scipy.stats import norm
import numpy as np
cdfarr = norm.cdf(np.array([1,-1., 0, 1, 3, 4, -2, 6]))
print(cdfarr)
```

执行上面示例代码，得到以下结果 - 

```
array([ 0.84134475, 0.15865525, 0.5 , 0.84134475, 0.9986501 ,
0.99996833, 0.02275013, 1. ])
```

要查找分布的中位数，可以使用百分点函数(PPF)，它是CDF的倒数。 可通过使用下面的例子来理解。

```
from scipy.stats import norm
ppfvar = norm.ppf(0.5)
print(ppfvar)
```

执行上面示例代码，得到以下结果 - 

```
0.0
```

要生成随机变量序列，应该使用`size`参数，如下例所示。

```
from scipy.stats import norm
rvsvar = norm.rvs(size = 5)
print(rvsvar)
```

执行上面示例代码，得到以下结果 - 

```
[-0.25993892  1.46653546 -0.53932984 -1.22796601  0.06542478]
```

上述输出不可重现。 要生成相同的随机数，请使用`seed()`函数。

## 均匀分布

使用统一函数可以生成均匀分布。 参考下面的一个例子。

```
from scipy.stats import uniform
cvar = uniform.cdf([0, 1, 2, 3, 4, 5], loc = 1, scale = 4)
print(cvar)
```

上述程序将生成以下输出 - 

```
array([ 0. , 0. , 0.25, 0.5 , 0.75, 1. ])
```

**构建离散分布**

生成随机样本，并将观察到的频率与概率进行比较。

**二项分布**  
作为`rv_discrete`类的一个实例，`binom`对象从它继承了一个泛型方法的集合，并通过特定于这个特定分布的细节完成它们。 参考下面的例子。

```
from scipy.stats import uniform
cvar = uniform.cdf([0, 1, 2, 3, 4, 5], loc = 1, scale = 4)

print(cvar)
```

上述程序将生成以下输出 - 

```
array([ 0. , 0. , 0.25, 0.5 , 0.75, 1. ])
```

## 描述性统计

如`Min`，`Max`，`Mean`和`Variance`等基本统计数据将NumPy数组作为输入并返回相应的结果。 下表描述了`scipy.stats`包中的一些基本统计函数。

| 编号 | 函数           | 描述                        |
| -- | ------------ | ------------------------- |
| 1  | `describe()` | 计算传递数组的几个描述性统计信息          |
| 2  | `gmean()`    | 计算沿指定轴的几何平均值              |
| 3  | `hmean()`    | 计算沿指定轴的谐波平均值              |
| 4  | `kurtosis()` | 计算峰度                      |
| 5  | `mode()`     | 返回模态值                     |
| 6  | `skew()`     | 测试数据的偏斜度                  |
| 7  | `f_oneway()` | 执行单向方差分析                  |
| 8  | `iqr()`      | 计算沿指定轴的数据的四分位数范围          |
| 9  | `zscore()`   | 计算样本中每个值相对于样本均值和标准偏差的`z`值 |
| 10 | `sem()`      | 计算输入数组中值的标准误差(或测量标准误差)    |

其中几个函数在`scipy.stats.mstats`中有一个类似的版本，它们用于掩码数组。 参考下面给出的例子来理解这一点。


```
from scipy import stats
import numpy as np
x = np.array([1,2,3,4,5,6,7,8,9])
print (x.max(),x.min(),x.mean(),x.var())
```

上述程序将生成以下输出 - 

```
(9, 1, 5.0, 6.666666666666667)
```

**T-检验**

下面了解`T`检验在SciPy中是如何有用的。

**ttest_1samp**

计算一组分数平均值的`T`检验。 这是对零假设的双面检验，即独立观测值`'a'`样本的期望值(平均值)等于给定总体均值`popmean`，考虑下面的例子。

```
from scipy import stats
rvs = stats.norm.rvs(loc = 5, scale = 10, size = (50,2))
sta = stats.ttest_1samp(rvs,5.0)
print(sta)
```

上述程序将生成以下输出 - 

```
Ttest_1sampResult(statistic = array([-1.40184894, 2.70158009]),
pvalue = array([ 0.16726344, 0.00945234]))
```

**比较两个样本**

在下面的例子中，有两个样本可以来自相同或不同的分布，想要测试这些样本是否具有相同的统计特性。

`ttest_ind` - 计算两个独立样本得分的T检验。 对于两个独立样本具有相同平均(预期)值的零假设，这是一个双侧检验。 该测试假设人口默认具有相同的差异。

如果观察到来自相同或不同人群的两个独立样本，可以使用这个测试。参考下面的例子。

```
from scipy import stats
rvs1 = stats.norm.rvs(loc = 5,scale = 10,size = 500)
rvs2 = stats.norm.rvs(loc = 5,scale = 10,size = 500)
print (stats.ttest_ind(rvs1,rvs2))
```

执行上面示例代码，得到以下结果 - 

```
Ttest_indResult(statistic = -0.67406312233650278, pvalue = 0.50042727502272966)
```

可以使用相同长度的新数组进行测试，但具有不同的含义。 在`loc`中使用不同的值并测试相同的值。

# Scipy CSGraph

CSGraph表示压缩稀疏图，它着重于基于稀疏矩阵表示快速图算法。

## 图表示

首先，让我们了解一个稀疏图是什么以及它在图表示中的作用。

**稀疏图是什么？**

图只是节点的集合，它们之间有链接。 图几乎可以代表任何事物 - 社交网络连接，每个节点都是一个人，并且与熟人相连; 图像，其中每个节点是像素并连接到相邻像素; 指向一个高维分布，其中每个节点连接到最近的邻居; 实际上你可以想象的任何其他东西。

表示图形数据的一种非常有效的方式是在一个稀疏矩阵中: 假设名称为`G`。矩阵`G`的大小为`N×N`，并且`G[i，j]`给出节点`'i'`和节点之间的连接的值`'J'`。 稀疏图形包含大部分零 - 也就是说，大多数节点只有几个连接。

在`scikit-learn`中使用的几种算法激发了稀疏图子模块的创建，其中包括以下内容 - 

* Isomap - 流形学习算法，需要在图中找到最短路径。
* 分层聚类 - 基于最小生成树的聚类算法。
* 谱分解 - 基于稀疏图拉普拉斯算子的投影算法。

作为一个具体的例子，假设想要表示以下无向图 -

![](http://www.yiibai.com/uploads/images/201803/0503/443100357_69868.jpg)

该图有三个节点，其中节点`0`和`1`通过权重`2`的边连接，节点`0`和`2`通过权重`1`的边连接。可以构造如下例所示的稠密，蒙板和稀疏表示，无向图由对称矩阵表示。

```
G_dense = np.array([ [0, 2, 1],
                     [2, 0, 0],
                     [1, 0, 0] ])

G_masked = np.ma.masked_values(G_dense, 0)
from scipy.sparse import csr_matrix

G_sparse = csr_matrix(G_dense)
print (G_sparse.data)
```

上述程序将生成以下输出 - 

```
array([2, 1, 2, 1])
```

![](http://www.yiibai.com/uploads/images/201803/0503/614100359_88362.jpg)

这与前面的图相同，只是节点`0`和`2`通过零权重的边连接。 在这种情况下，上面的稠密表示会导致含糊不清 - 如果零是一个有意义的值，那么如何表示非边缘。 在这种情况下，必须使用蒙版或稀疏表示来消除歧义。

参考下面的例子 - 

```
from scipy.sparse.csgraph import csgraph_from_dense
G2_data = np.array
([
   [np.inf, 2, 0 ],
   [2, np.inf, np.inf],
   [0, np.inf, np.inf]
])
G2_sparse = csgraph_from_dense(G2_data, null_value=np.inf)
print (G2_sparse.data)
```

上述程序将生成以下输出 - 

```
array([ 2., 0., 2., 0.])
```

**使用稀疏图的词梯子**

词梯是刘易斯卡罗尔发明的游戏，其中单词通过在每一步更改单个字母而链接在一起。 例如 -

**APE → APT → AIT → BIT → BIG → BAG → MAG → MAN**

在这里，分七步从`“APE”`到`“MAN”`，每次更换一个字母。 问题是 - 我们能否使用相同的规则在这些词之间找到更短的路径？ 这个问题自然表示为一个稀疏图形问题。 节点将对应于单个单词，并且将创建最多不超过一个字母的单词之间的连接。

## 获取单词列表

首先，当然，我们必须获得有效的单词列表。如果使用Mac，并且Mac在以下代码块中给出的位置具有单词字典。 如果在其它的架构上，可能需要搜索一下才能找到你的系统字典。

```
wordlist = open('/usr/share/dict/words').read().split()
print (len(wordlist))
```

执行上面示例代码，得到以下结果 - 

```
205882
```

现在想看长度为`3`的单词，选择正确长度的单词。 还将消除以大写字母(专有名词)开头的单词或包含撇号和连字符等非字母数字字符的单词。 最后，确保一切都是小写的，以便稍后进行比较。

```
word_list = [word for word in word_list if len(word) == 3]
word_list = [word for word in word_list if word[0].islower()]
word_list = [word for word in word_list if word.isalpha()]
word_list = map(str.lower, word_list)
print (len(word_list))
```

执行上面示例代码，得到以下结果 - 


```
1185
```

现在，列出了`1185`个有效的三个字母的单词(确切的数字可能会根据所使用的特定列表而变化)。 这些单词中的每一个都将成为图中的一个节点，我们将创建连接与每对单词关联的节点的边，这些节点之间的差异只有一个字母。

```
import numpy as np
word_list = np.asarray(word_list)

word_list.dtype
word_list.sort()

word_bytes = np.ndarray((word_list.size, word_list.itemsize),
   dtype = 'int8',
   buffer = word_list.data)
print (word_bytes.shape)
```

执行上面示例代码，得到以下结果 - 

```
(1185,3)
```

我们将使用每个点之间的汉明距离来确定连接哪些单词对。 汉明距离度量两个向量之间的条目分数，它们不同:汉明距离等于`1/N1/N`的任何两个单词，其中`NN`是单词阶梯中连接的字母数。

```
from scipy.spatial.distance import pdist, squareform
from scipy.sparse import csr_matrix
hamming_dist = pdist(word_bytes, metric = 'hamming')
graph = csr_matrix(squareform(hamming_dist < 1.5 / word_list.itemsize))
```

比较距离时，不使用相等性，因为这对于浮点值可能不稳定。 只要字表中没有两个条目是相同的，不平等就会产生所需的结果。 现在，图形已经建立，我们将使用最短路径搜索来查找图形中任何两个单词之间的路径。

```
i1 = word_list.searchsorted('ape')
i2 = word_list.searchsorted('man')
print (word_list[i1],word_list[i2])
```

执行上面示例代码，得到以下结果 -

```
ape, man
```

我们需要检查它们是否匹配，因为如果单词不在列表中，输出中会有错误。 现在，需要在图中找到这两个索引之间的最短路径。使用`dijkstra`算法，因为它能够为一个节点找到路径。

```
from scipy.sparse.csgraph import dijkstra
distances, predecessors = dijkstra(graph, indices = i1, return_predecessors = True)
print (distances[i2])
```

执行上面示例代码，得到以下结果 -

```
5.0
```

因此，我们看到`ape`和`man`之间的最短路径只包含五个步骤。可以使用算法返回的前辈来重构这条路径。

```
path = []
i = i2

while i != i1:
   path.append(word_list[i])
   i = predecessors[i]

path.append(word_list[i1])
print (path[::-1]i2])
```

上述程序将生成以下输出 - 

```
['ape', 'ope', 'opt', 'oat', 'mat', 'man']
```

# Scipy空间

`scipy.spatial`包可以通过利用Qhull库来计算一组点的三角剖分，Voronoi图和凸壳。 此外，它包含用于最近邻点查询的KDTree实现以及用于各种度量中的距离计算的实用程序。

## Delaunay三角

下面来了解Delaunay Triangulations是什么以及如何在SciPy中使用。

**什么是Delaunay三角？**

在数学和计算几何中，对于平面中离散点的给定集合P的Delaunay三角剖分是三角形DT(P)，使得P中的任何点都不在DT(P)中的任何三角形的外接圆内。

可以通过SciPy进行相同的计算。 参考下面的一个例子。

```
from scipy.spatial import Delaunay
points = np.array([[0, 4], [2, 1.1], [1, 3], [1, 2]])
tri = Delaunay(points)
import matplotlib.pyplot as plt
plt.triplot(points[:,0], points[:,1], tri.simplices.copy())
plt.plot(points[:,0], points[:,1], 'o')
plt.show()
```

上述程序将生成以下输出 -

![](http://www.yiibai.com/uploads/images/201803/0503/320110313_53614.png)

## 共面点

下面了解共面点是什么以及它们如何在SciPy中使用。

**什么是共面点？**

共平面点是三个或更多点位于同一平面上。 回想一下，一个平面是平坦的表面，其在所有方向端延伸没有终点。 它通常在数学教科书中显示为**四面体**。

下面来看看如何在SciPy中使用它，参考下面的例子。

```
from scipy.spatial import Delaunay
points = np.array([[0, 0], [0, 1], [1, 0], [1, 1], [1, 1]])
tri = Delaunay(points)
print (tri.coplanar)
```

上述程序将生成以下输出 - 

```
array([[4, 0, 3]], dtype = int32)
```

这意味着顶点`4`位于三角形顶点`0`和顶点`3`附近，但不包含在三角中。

## 凸壳

下面来了解什么是凸壳，以及它们如何在SciPy中使用。

**什么是凸壳？**

在数学中，欧几里德平面或欧几里德空间(或更一般地说，在实数上的仿射空间中)中的一组点`X`的凸包或凸包是包含`X`的最小凸集。

参考下面的例子来详细了解它 - 

```
from scipy.spatial import ConvexHull
points = np.random.rand(10, 2) # 30 random points in 2-D
hull = ConvexHull(points)
import matplotlib.pyplot as plt
plt.plot(points[:,0], points[:,1], 'o')
for simplex in hull.simplices:
   plt.plot(points[simplex,0], points[simplex,1], 'k-')
plt.show()
```

执行上面示例代码得到以下结果 -

![](http://www.yiibai.com/uploads/images/201803/0503/273110321_83517.png)

# Scipy ODR

ODR代表正交距离回归，用于回归研究。 基本线性回归通常用于通过在图上绘制最佳拟合线来估计两个变量`y`和`x`之间的关系。

用于此的数学方法称为最小平方，旨在最小化每个点的平方误差总和。 这里的关键问题是如何计算每个点的误差(也称为残差)？

在一个标准的线性回归中，目的是从`X`值预测`Y`值 - 因此明智的做法是计算`Y`值的误差(如下图所示的灰线所示)。 但是，有时考虑`X`和`Y`的误差(如下图中的红色虚线所示)更为明智。

例如 - 当知道对`X`的测量是不确定的，或者当不想关注一个变量相对于另一个变量的错误时。  
![](http://www.yiibai.com/uploads/images/201803/0503/968110326_76442.jpg)

正交距离回归(ODR)是一种可以做到这一点的方法(正交在这里表示为垂直 - 所以它计算垂直于线的误差，而不仅仅是’垂直’)。

**单变量回归的scipy.odr实现**

以下示例演示单变量回归的`scipy.odr`实现。

```
import numpy as np
import matplotlib.pyplot as plt
from scipy.odr import *
import random

# Initiate some data, giving some randomness using random.random().
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([i**2 + random.random() for i in x])

# Define a function (quadratic in our case) to fit the data with.
def linear_func(p, x):
   m, c = p
   return m*x + c

# Create a model for fitting.
linear_model = Model(linear_func)

# Create a RealData object using our initiated data from above.
data = RealData(x, y)

# Set up ODR with the model and data.
odr = ODR(data, linear_model, beta0=[0., 1.])

# Run the regression.
out = odr.run()

# Use the in-built pprint method to give us results.
out.pprint()
```

上述程序将生成以下输出 - 

```
Beta: [ 5.50355382 -3.88825011]
Beta Std Error: [ 0.77904626  2.33231797]
Beta Covariance: [[  1.92223609  -4.80559051]
 [ -4.80559051  17.22882877]]
Residual Variance: 0.31573284521355344
Inverse Condition #: 0.1465848083469268
Reason(s) for Halting:
  Sum of squares convergence
```

# Scipy特殊包

特殊包中可用的功能是通用功能，它遵循广播和自动数组循环。

下面来看看一些最常用的特殊函数功能 -

* 立方根函数
* 指数函数
* 相对误差指数函数
* 对数和指数函数
* 兰伯特函数
* 排列和组合函数
* 伽马函数

下面来简单地了解这些函数。

**立方根函数**

这个立方根函数的语法是 - `scipy.special.cbrt(x)`。 这将获取`x`的基于元素的立方体根。

参考下面的一个例子 - 

```
from scipy.special import cbrt
res = cbrt([10, 9, 0.1254, 234])
print (res)
```

执行上面示例代码，得到以下结果 - 

```
[ 2.15443469 2.08008382 0.50053277 6.16224015]
```

**指数函数**

指数函数的语法是 - `scipy.special.exp10(x)`。 这将计算`10 ** x`的值。

参考下面的一个例子 - 

```
from scipy.special import exp10
res = exp10([2, 4])
print (res)
```

执行上面示例代码，得到以下结果 - 

```
[   100.  10000.]
```

**相对误差指数函数**

这个函数的语法是 - `scipy.special.exprel(x)`。 它生成相对误差指数，`(exp(x) - 1/x`。

当`x`接近零时，`exp(x)`接近`1`，所以`exp(x)-1`的数值计算可能遭受灾难性的精度损失。 然后`exprel(x)`被实现以避免精度的损失，这在`x`接近于零时发生。

参考下面的一个例子。

```
from scipy.special import exprel
res = exprel([-0.25, -0.1, 0, 0.1, 0.25])
print (res)
```

执行上面示例代码，得到以下结果 - 

```
[0.88479687 0.95162582 1.   1.05170918 1.13610167]
```

**对数和指数函数**

这个函数的语法是 - `scipy.special.logsumexp(x)`。 它有助于计算输入元素指数总和的对数。

参考下面的一个例子 - 

```
from scipy.special import logsumexp
import numpy as np
a = np.arange(10)
res = logsumexp(a)
print (res)
```

执行上面示例代码，得到以下结果 - 

```
9.45862974443
```

**兰伯特函数**

这个函数的语法是 - `scipy.special.lambertw(x)`。 它也被称为兰伯特W函数。 兰伯特W函数`W(z)`定义为`w * exp(w)`的反函数。 换句话说，对于任何复数`z`，`W(z)`的值都是`z = W(z)* exp(W(z))`。

兰伯特W函数是一个具有无限多分支的多值函数。 每个分支给出了方程`z = w exp(w)`的单独解。 这里，分支由整数k索引。

参考下面的一个例子。 这里，兰伯特W函数是`w exp(w)`的逆函数。

```
from scipy.special import lambertw
w = lambertw(1)
print (w)
print (w * np.exp(w))
```

上述程序将生成以下输出 - 

```
(0.56714329041+0j)
(1+0j)
```

**排列和组合**

下面将分开讨论排列和组合，以便清楚地理解它们。

**组合** - 组合函数的语法是 - `scipy.special.comb(N，k)`。参考下面的一个例子 -

```
from scipy.special import comb
res = comb(10, 3, exact = False,repetition=True)
print (res)
```

执行上面示例代码，得到以下结果 - 

```
220.0
```

> 注 - 数组参数仅适用于`exact = False`大小写。 如果`k> N`，`N <0`或`k <0`，则返回`0`。

**排列** - 组合函数的语法是 - `scipy.special.perm(N，k)`。 一次取`k`个`N`个东西的排列，即`N`个`k`个排列。这也被称为“部分排列”。

参考下面的一个例子。

```
from scipy.special import perm
res = perm(10, 3, exact = True)
print (res)
```

上述程序将生成以下输出 - 

```
720
```
**伽马函数**  
由于`z * gamma(z)= gamma(z + 1)`和`gamma(n + 1)= n！`，所以对于自然数`'n'`，伽马函数通常被称为广义阶乘。

组合函数的语法是 - `scipy.special.gamma(x)`。 一次取`k`个`N`个东西的排列，即`N`个`k`个排列。这也被称为“部分排列”。

组合函数的语法是 - `scipy.special.gamma(x)`。 一次取`k`个`N`个东西的排列，即`N`个`k`个排列。这也被称为“部分排列”。

```
from scipy.special import gamma
res = gamma([0, 0.5, 1, 5])
print (res)
```

执行上面示例代码，得到以下结果 - 

```
[inf  1.77245385  1.  24.]
```

## 一、numpy概述

numpy（Numerical Python）提供了python对多维数组对象的支持：ndarray，具有矢量运算能力，快速、节省空间。numpy支持高级大量的维度数组与矩阵运算，此外也针对数组运算提供大量的数学函数库。

## 二、创建ndarray数组

ndarray：N维数组对象（矩阵），所有元素必须是相同类型。   
ndarray属性：ndim属性，表示维度个数；shape属性，表示各维度大小；dtype属性，表示数据类型。

创建ndarray数组函数：

![这里写图片描述](https://img-blog.csdn.net/20170116134958784?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvY3htc2Ni/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/80/gravity/SouthEast)

代码示例：

```has-numbering
# -*- coding: utf-8 -*-

import numpy;

print '使用列表生成一维数组'
data = [1,2,3,4,5,6]
x = numpy.array(data)
print x #打印数组
print x.dtype #打印数组元素的类型

print '使用列表生成二维数组'
data = [[1,2],[3,4],[5,6]]
x = numpy.array(data)
print x #打印数组
print x.ndim #打印数组的维度
print x.shape #打印数组各个维度的长度。shape是一个元组

print '使用zero/ones/empty创建数组:根据shape来创建'
x = numpy.zeros(6) #创建一维长度为6的，元素都是0一维数组
print x
x = numpy.zeros((2,3)) #创建一维长度为2，二维长度为3的二维0数组
print x
x = numpy.ones((2,3)) #创建一维长度为2，二维长度为3的二维1数组
print x
x = numpy.empty((3,3)) #创建一维长度为2，二维长度为3,未初始化的二维数组
print x

print '使用arrange生成连续元素'
print numpy.arange(6) # [0,1,2,3,4,5,] 开区间
print numpy.arange(0,6,2)  # [0, 2，4]
```



## 三、指定ndarray数组元素的类型

NumPy数据类型：

![这里写图片描述](https://img-blog.csdn.net/20170116141839682?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvY3htc2Ni/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/100/gravity/SouthEast)

代码示例：

```has-numbering
print '生成指定元素类型的数组:设置dtype属性'
x = numpy.array([1,2.6,3],dtype = numpy.int64)
print x # 元素类型为int64
print x.dtype
x = numpy.array([1,2,3],dtype = numpy.float64)
print x # 元素类型为float64
print x.dtype

print '使用astype复制数组，并转换类型'
x = numpy.array([1,2.6,3],dtype = numpy.float64)
y = x.astype(numpy.int32)
print y # [1 2 3]
print x # [ 1.   2.6  3. ]
z = y.astype(numpy.float64)
print z # [ 1.  2.  3.]

print '将字符串元素转换为数值元素'
x = numpy.array(['1','2','3'],dtype = numpy.string_)
y = x.astype(numpy.int32)
print x # ['1' '2' '3']
print y # [1 2 3] 若转换失败会抛出异常

print '使用其他数组的数据类型作为参数'
x = numpy.array([ 1., 2.6,3. ],dtype = numpy.float32);
y = numpy.arange(3,dtype=numpy.int32);
print y # [0 1 2]
print y.astype(x.dtype) # [ 0.  1.  2.]
```



## 四、ndarray的矢量化计算

矢量运算：相同大小的数组键间的运算应用在元素上   
矢量和标量运算：“广播”— 将标量“广播”到各个元素

代码示例：

```has-numbering
print 'ndarray数组与标量/数组的运算'
x = numpy.array([1,2,3]) 
print x*2 # [2 4 6]
print x>2 # [False False  True]
y = numpy.array([3,4,5])
print x+y # [4 6 8]
print x>y # [False False False]
```



## 五、ndarray数组的基本索引和切片

一维数组的索引：与Python的列表索引功能相似

多维数组的索引：

* arr[r1:r2, c1:c2]
* arr[1,1] 等价 arr[1][1]
* [:] 代表某个维度的数据

代码示例：

```has-numbering
print 'ndarray的基本索引'
x = numpy.array([[1,2],[3,4],[5,6]])
print x[0] # [1,2]
print x[0][1] # 2,普通python数组的索引
print x[0,1] # 同x[0][1]，ndarray数组的索引
x = numpy.array([[[1, 2], [3,4]], [[5, 6], [7,8]]])
print x[0] # [[1 2],[3 4]]
y = x[0].copy() # 生成一个副本
z = x[0] # 未生成一个副本
print y #  [[1 2],[3 4]]
print y[0,0] # 1
y[0,0] = 0 
z[0,0] = -1
print y # [[0 2],[3 4]]
print x[0] # [[-1 2],[3 4]]
print z # [[-1 2],[3 4]]

print 'ndarray的切片'
x = numpy.array([1,2,3,4,5])
print x[1:3] # [2,3] 右边开区间
print x[:3] # [1,2,3] 左边默认为 0
print x[1:] # [2,3,4,5] 右边默认为元素个数
print x[0:4:2] # [1,3] 下标递增2
x = numpy.array([[1,2],[3,4],[5,6]])
print x[:2] # [[1 2],[3 4]]
print x[:2,:1] # [[1],[3]]
x[:2,:1] = 0 # 用标量赋值
print x # [[0,2],[0,4],[5,6]]
x[:2,:1] = [[8],[6]] # 用数组赋值
print x # [[8,2],[6,4],[5,6]]
```



## 六、ndarray数组的布尔索引和花式索引

布尔索引：使用布尔数组作为索引。arr[condition]，condition为一个条件/多个条件组成的布尔数组。

布尔型索引代码示例：

```has-numbering
print 'ndarray的布尔型索引'
x = numpy.array([3,2,3,1,3,0])
# 布尔型数组的长度必须跟被索引的轴长度一致
y = numpy.array([True,False,True,False,True,False]) 
print x[y] # [3,3,3] 
print x[y==False] # [2,1,0]
print x>=3 # [ True False  True False  True  False]
print x[~(x>=3)] # [2,1,0]
print (x==2)|(x==1) # [False  True False  True False False]
print x[(x==2)|(x==1)] # [2 1]
x[(x==2)|(x==1)] = 0
print x # [3 0 3 0 3 0]
```



花式索引：使用整型数组作为索引。

花式索引代码示例：

```has-numbering
print 'ndarray的花式索引:使用整型数组作为索引'
x = numpy.array([1,2,3,4,5,6])
print x[[0,1,2]] # [1 2 3]
print x[[-1,-2,-3]] # [6,5,4]
x = numpy.array([[1,2],[3,4],[5,6]])
print x[[0,1]] # [[1,2],[3,4]]
print x[[0,1],[0,1]] # [1,4] 打印x[0][0]和x[1][1]
print x[[0,1]][:,[0,1]] # 打印01行的01列 [[1,2],[3,4]]
# 使用numpy.ix_()函数增强可读性
print x[numpy.ix_([0,1],[0,1])] #同上 打印01行的01列 [[1,2],[3,4]]
x[[0,1],[0,1]] = [0,0]
print x # [[0,2],[3,0],[5,6]]
```



## 七、ndarray数组的转置和轴对换

数组的转置/轴对换只会返回源数据的一个视图，不会对源数据进行修改。

代码示例：

```has-numbering
print 'ndarray数组的转置和轴对换'
k = numpy.arange(9) #[0,1,....8]
m = k.reshape((3,3)) # 改变数组的shape复制生成2维的，每个维度长度为3的数组
print k # [0 1 2 3 4 5 6 7 8]
print m # [[0 1 2] [3 4 5] [6 7 8]]
# 转置(矩阵)数组：T属性 : mT[x][y] = m[y][x]
print m.T # [[0 3 6] [1 4 7] [2 5 8]]
# 计算矩阵的内积 xTx
print numpy.dot(m,m.T) # numpy.dot点乘
# 高维数组的轴对象
k = numpy.arange(8).reshape(2,2,2)
print k # [[[0 1],[2 3]],[[4 5],[6 7]]]
print k[1][0][0]
# 轴变换 transpose 参数:由轴编号组成的元组
m = k.transpose((1,0,2)) # m[y][x][z] = k[x][y][z]
print m # [[[0 1],[4 5]],[[2 3],[6 7]]]
print m[0][1][0]
# 轴交换 swapaxes (axes：轴)，参数:一对轴编号
m = k.swapaxes(0,1) # 将第一个轴和第二个轴交换 m[y][x][z] = k[x][y][z]
print m # [[[0 1],[4 5]],[[2 3],[6 7]]]
print m[0][1][0]
# 使用轴交换进行数组矩阵转置
m = numpy.arange(9).reshape((3,3))
print m # [[0 1 2] [3 4 5] [6 7 8]]
print m.swapaxes(1,0) # [[0 3 6] [1 4 7] [2 5 8]]
```



## 八、ndarray通用函数

通用函数（ufunc）是一种对ndarray中的数据执行元素级运算的函数。

一元ufunc：

![这里写图片描述](https://img-blog.csdn.net/20170116155903070?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvY3htc2Ni/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

一元ufunc代码示例：

```has-numbering
print '一元ufunc示例'
x = numpy.arange(6)
print x # [0 1 2 3 4 5]
print numpy.square(x) # [ 0  1  4  9 16 25]
x = numpy.array([1.5,1.6,1.7,1.8])
y,z = numpy.modf(x)
print y # [ 0.5  0.6  0.7  0.8]
print z # [ 1.  1.  1.  1.]
```



二元ufunc：

![这里写图片描述](https://img-blog.csdn.net/20170116160741445?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvY3htc2Ni/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

二元ufunc代码示例：

```has-numbering
print '二元ufunc示例'
x = numpy.array([[1,4],[6,7]])
y = numpy.array([[2,3],[5,8]])
print numpy.maximum(x,y) # [[2,4],[6,8]]
print numpy.minimum(x,y) # [[1,3],[5,7]]
```



## 九、NumPy的where函数使用

np.where(condition, x, y)，第一个参数为一个布尔数组，第二个参数和第三个参数可以是标量也可以是数组。

代码示例：

```has-numbering
print 'where函数的使用'
cond = numpy.array([True,False,True,False])
x = numpy.where(cond,-2,2)
print x # [-2  2 -2  2]
cond = numpy.array([1,2,3,4])
x = numpy.where(cond>2,-2,2)
print x # [ 2  2 -2 -2]
y1 = numpy.array([-1,-2,-3,-4])
y2 = numpy.array([1,2,3,4])
x = numpy.where(cond>2,y1,y2) # 长度须匹配
print x # [1,2,-3,-4]

print 'where函数的嵌套使用'
y1 = numpy.array([-1,-2,-3,-4,-5,-6])
y2 = numpy.array([1,2,3,4,5,6])
y3 = numpy.zeros(6)
cond = numpy.array([1,2,3,4,5,6])
x = numpy.where(cond>5,y3,numpy.where(cond>2,y1,y2))
print x # [ 1.  2. -3. -4. -5.  0.]
```



## 十、ndarray常用的统计方法

可以通过这些基本统计方法对整个数组/某个轴的数据进行统计计算。

![这里写图片描述](https://img-blog.csdn.net/20170117120917206?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvY3htc2Ni/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

代码示例：

```has-numbering
print 'numpy的基本统计方法'
x = numpy.array([[1,2],[3,3],[1,2]]) #同一维度上的数组长度须一致
print x.mean() # 2
print x.mean(axis=1) # 对每一行的元素求平均
print x.mean(axis=0) # 对每一列的元素求平均
print x.sum() #同理 12
print x.sum(axis=1) # [3 6 3]
print x.max() # 3
print x.max(axis=1) # [2 3 2]
print x.cumsum() # [ 1  3  6  9 10 12]
print x.cumprod() # [ 1  2  6 18 18 36]
```



用于布尔数组的统计方法：

* sum : 统计数组/数组某一维度中的True的个数
* any： 统计数组/数组某一维度中是否存在一个/多个True
* all：统计数组/数组某一维度中是否都是True

代码示例：

```has-numbering
print '用于布尔数组的统计方法'
x = numpy.array([[True,False],[True,False]])
print x.sum() # 2
print x.sum(axis=1) # [1,1]
print x.any(axis=0) # [True,False]
print x.all(axis=1) # [False,False]
```


使用sort对数组/数组某一维度进行就地排序（会修改数组本身）。

代码示例：

```has-numbering
print '.sort的就地排序'
x = numpy.array([[1,6,2],[6,1,3],[1,5,2]])
x.sort(axis=1) 
print x # [[1 2 6] [1 3 6] [1 2 5]]
#非就地排序：numpy.sort()可产生数组的副本
```



## 十一、ndarray数组的去重以及集合运算

![这里写图片描述](https://img-blog.csdn.net/20170117123631949?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvY3htc2Ni/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

代码示例：（方法返回类型为一维数组（1d）)

```has-numbering
print 'ndarray的唯一化和集合运算'
x = numpy.array([[1,6,2],[6,1,3],[1,5,2]])
print numpy.unique(x) # [1,2,3,5,6]
y = numpy.array([1,6,5])
print numpy.in1d(x,y) # [ True  True False  True  True False  True  True False]
print numpy.setdiff1d(x,y) # [2 3]
print numpy.intersect1d(x,y) # [1 5 6]
```


## 十二、numpy中的线性代数

import numpy.linalg 模块。线性代数（linear algebra）

常用的numpy.linalg模块函数：

![这里写图片描述](https://img-blog.csdn.net/20170117135917748?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvY3htc2Ni/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

代码示例：

```has-numbering
print '线性代数'
import numpy.linalg as nla
print '矩阵点乘'
x = numpy.array([[1,2],[3,4]])
y = numpy.array([[1,3],[2,4]])
print x.dot(y) # [[ 5 11][11 25]]
print numpy.dot(x,y) # # [[ 5 11][11 25]]
print '矩阵求逆'
x = numpy.array([[1,1],[1,2]])
y = nla.inv(x) # 矩阵求逆（若矩阵的逆存在）
print x.dot(y) # 单位矩阵 [[ 1.  0.][ 0.  1.]]
print nla.det(x) # 求行列式
```


### 十三、numpy中的随机数生成

import numpy.random模块。

常用的numpy.random模块函数：

![这里写图片描述](https://img-blog.csdn.net/20170117141702475?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvY3htc2Ni/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

代码示例：

```has-numbering
print 'numpy.random随机数生成'
import numpy.random as npr

x = npr.randint(0,2,size=100000) #抛硬币
print (x>0).sum() # 正面的结果
print npr.normal(size=(2,2)) #正态分布随机数数组 shape = (2,2)
```


### 十四、ndarray数组重塑

代码示例:

```has-numbering
print 'ndarray数组重塑'
x = numpy.arange(0,6) #[0 1 2 3 4]
print x #[0 1 2 3 4]
print x.reshape((2,3)) # [[0 1 2][3 4 5]]
print x #[0 1 2 3 4]
print x.reshape((2,3)).reshape((3,2)) # [[0 1][2 3][4 5]]
y = numpy.array([[1,1,1],[1,1,1]])
x = x.reshape(y.shape)
print x # [[0 1 2][3 4 5]]
print x.flatten() # [0 1 2 3 4 5]
x.flatten()[0] = -1 # flatten返回的是拷贝
print x # [[0 1 2][3 4 5]]
print x.ravel() # [0 1 2 3 4 5]
x.ravel()[0] = -1 # ravel返回的是视图（引用） 
print x # [[-1 1 2][3 4 5]]
print "维度大小自动推导"
arr = numpy.arange(15)
print arr.reshape((5, -1)) # 15 / 5 = 3
```


### 十五、ndarray数组的拆分与合并

![这里写图片描述](https://img-blog.csdn.net/20170117143943037?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvY3htc2Ni/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

代码示例：

```has-numbering
print '数组的合并与拆分'
x = numpy.array([[1, 2, 3], [4, 5, 6]])
y = numpy.array([[7, 8, 9], [10, 11, 12]])
print numpy.concatenate([x, y], axis = 0)  
# 竖直组合 [[ 1  2  3][ 4  5  6][ 7  8  9][10 11 12]]
print numpy.concatenate([x, y], axis = 1)  
# 水平组合 [[ 1  2  3  7  8  9][ 4  5  6 10 11 12]]
print '垂直stack与水平stack'
print numpy.vstack((x, y)) # 垂直堆叠:相对于垂直组合
print numpy.hstack((x, y)) # 水平堆叠：相对于水平组合
# dstack：按深度堆叠
print numpy.split(x,2,axis=0) 
# 按行分割 [array([[1, 2, 3]]), array([[4, 5, 6]])]
print numpy.split(x,3,axis=1) 
# 按列分割 [array([[1],[4]]), array([[2],[5]]), array([[3],[6]])]

# 堆叠辅助类
import numpy as np
arr = np.arange(6)
arr1 = arr.reshape((3, 2))
arr2 = np.random.randn(3, 2)
print 'r_用于按行堆叠'
print np.r_[arr1, arr2]
'''
[[ 0.          1.        ]
 [ 2.          3.        ]
 [ 4.          5.        ]
 [ 0.22621904  0.39719794]
 [-1.2201912  -0.23623549]
 [-0.83229114 -0.72678578]]
'''
print 'c_用于按列堆叠'
print np.c_[np.r_[arr1, arr2], arr]
'''
[[ 0.          1.          0.        ]
 [ 2.          3.          1.        ]
 [ 4.          5.          2.        ]
 [ 0.22621904  0.39719794  3.        ]
 [-1.2201912  -0.23623549  4.        ]
 [-0.83229114 -0.72678578  5.        ]]
'''
print '切片直接转为数组'
print np.c_[1:6, -10:-5]
'''
[[  1 -10]
 [  2  -9]
 [  3  -8]
 [  4  -7]
 [  5  -6]]
'''
```


### 十六、数组的元素重复操作

代码示例：

```has-numbering
print '数组的元素重复操作'
x = numpy.array([[1,2],[3,4]])
print x.repeat(2) # 按元素重复 [1 1 2 2 3 3 4 4]
print x.repeat(2,axis=0) # 按行重复 [[1 2][1 2][3 4][3 4]]
print x.repeat(2,axis=1) # 按列重复 [[1 1 2 2][3 3 4 4]]
x = numpy.array([1,2])
print numpy.tile(x,2) # tile瓦片：[1 2 1 2]
print numpy.tile(x, (2, 2))  # 指定从低维到高维依次复制的次数。 
# [[1 2 1 2][1 2 1 2]]
```


#### 全部代码：[Github](https://github.com/cxmscb/numpy-The-basic-use/)
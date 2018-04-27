```
 本 NumPy 测试题旨在为大家提供参考，让大家可以使用 NumPy 的更多功能。问题共分为四个等级，L1 最简单，难度依次增加。机器之心对该测试题进行了编译介绍，希望能对大家有所帮助。每个问题之后附有代码答案，参见原文。
```

原文链接：https://www.machinelearningplus.com/101-numpy-exercises-python/

![NumPy能力大评估：这里有70道测试题](http://p3.pstatp.com/large/66c0000594c0db501e22)

如果你想先回顾一下 NumPy 的知识，推荐阅读：

* NumPy 基础：https://www.machinelearningplus.com/numpy-tutorial-part1-array-python-examples

* NumPy 高级教程：https://www.machinelearningplus.com/numpy-tutorial-python-part2

1. 将 NumPy 导入为 np，并查看版本

难度：L1

问题：将 NumPy 导入为 np，并输出版本号。

2. 如何创建 1 维数组？

难度：L1

问题：创建数字从 0 到 9 的 1 维数组。

期望输出：

```
#> array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
```

3. 如何创建 boolean 数组？

难度：L1

问题：创建所有 True 的 3×3 NumPy 数组。

![NumPy能力大评估：这里有70道测试题](http://p3.pstatp.com/large/66bd00063808679cadd4)

4. 如何从 1 维数组中提取满足给定条件的项？

难度：L1

问题：从 arr 中提取所有奇数。

输入：

```
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])`
```

期望输出：

```
#> array([1, 3, 5, 7, 9])
```

5. 如何将 NumPy 数组中满足给定条件的项替换成另一个数值？

难度：L1

问题：将 arr 中的所有奇数替换成 -1。

输入：

```
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
```

期望输出：

```
#> array([ 0, -1, 2, -1, 4, -1, 6, -1, 8, -1])
```

6. 如何在不影响原始数组的前提下替换满足给定条件的项？

难度：L2

问题：将 arr 中所有奇数替换成 -1，且不改变 arr。

输入：

```
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
```

期望输出：

```
out

#> array([ 0, -1, 2, -1, 4, -1, 6, -1, 8, -1])

arr

#> array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])`
```

![NumPy能力大评估：这里有70道测试题](http://p3.pstatp.com/large/66bf0005f363be0828fd)

7. 如何重塑（reshape）数组？

难度：L1

问题：将 1 维数组转换成 2 维数组（两行）。

输入：

```
np.arange(10)

#> array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
```

期望输出

```
#> array([[0, 1, 2, 3, 4],

#> [5, 6, 7, 8, 9]])
```

8. 如何垂直堆叠两个数组？

难度：L2

问题：垂直堆叠数组 a 和 b。

输入：

```
a = np.arange(10).reshape(2,-1)

b = np.repeat(1, 10).reshape(2,-1)
```

期望输出：

```
#> array([[0, 1, 2, 3, 4],

#> [5, 6, 7, 8, 9],

#> [1, 1, 1, 1, 1],

#> [1, 1, 1, 1, 1]])
```

9. 如何水平堆叠两个数组？

难度：L2

问题：水平堆叠数组 a 和 b。

输入：

```
a = np.arange(10).reshape(2,-1)

b = np.repeat(1, 10).reshape(2,-1)
```

期望输出：

```
#> array([[0, 1, 2, 3, 4, 1, 1, 1, 1, 1],

#> [5, 6, 7, 8, 9, 1, 1, 1, 1, 1]])
```

10. 在不使用硬编码的前提下，如何在 NumPy 中生成自定义序列？

难度：L2

问题：在不使用硬编码的前提下创建以下模式。仅使用 NumPy 函数和以下输入数组 a。

输入：

```
a = np.array([1,2,3])`
```

期望输出：

```
#> array([1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])
```

11. 如何获得两个 Python NumPy 数组中共同的项？

难度：L2

问题：获取数组 a 和 b 中的共同项。

输入：

```
a = np.array([1,2,3,2,3,4,3,4,5,6])

b = np.array([7,2,10,2,7,4,9,4,9,8])
```

期望输出：

```
array([2, 4])
```

12. 如何从一个数组中移除与另一个数组重复的项？

难度：L2

问题：从数组 a 中移除出现在数组 b 中的所有项。

输入：

```
a = np.array([1,2,3,4,5])

b = np.array([5,6,7,8,9])
```

期望输出：

```
array([1,2,3,4])
```

13. 如何获取两个数组匹配元素的位置？

难度：L2

问题：获取数组 a 和 b 中匹配元素的位置。

输入：

```
a = np.array([1,2,3,2,3,4,3,4,5,6])

b = np.array([7,2,10,2,7,4,9,4,9,8])
```

期望输出：

```
#> (array([1, 3, 5, 7]),)
```

14. 如何从 NumPy 数组中提取给定范围内的所有数字？

难度：L2

问题：从数组 a 中提取 5 和 10 之间的所有项。

输入：

```
a = np.arange(15)
```

期望输出：

```
(array([ 5, 6, 7, 8, 9, 10]),)
```

15. 如何创建一个 Python 函数以对 NumPy 数组执行元素级的操作？

难度：L2

问题：转换函数 maxx，使其从只能对比标量而变为对比两个数组。

输入：

```
def maxx(x, y):

"""Get the maximum of two items"""

if x >= y:

return x

else:

return y

maxx(1, 5)

#> 5
```

期望输出：

```
a = np.array([5, 7, 9, 8, 6, 4, 5])

b = np.array([6, 3, 4, 8, 9, 7, 1])

pair_max(a, b)

#> array([ 6., 7., 9., 8., 9., 7., 5.])
```

16. 如何在 2d NumPy 数组中交换两个列？

难度：L2

问题：在数组 arr 中交换列 1 和列 2。

```
arr = np.arange(9).reshape(3,3)

arr
```

17. 如何在 2d NumPy 数组中交换两个行？

难度：L2

问题：在数组 arr 中交换行 1 和行 2。

```
arr = np.arange(9).reshape(3,3)

arr
```

18. 如何反转 2D 数组的所有行？

难度：L2

问题：反转 2D 数组 arr 中的所有行。

```
# Input

arr = np.arange(9).reshape(3,3)
```

19. 如何反转 2D 数组的所有列？

难度：L2

问题：反转 2D 数组 arr 中的所有列。

```
# Input

arr = np.arange(9).reshape(3,3)
```

20. 如何创建一个包含 5 和 10 之间随机浮点的 2 维数组？

难度：L2

问题：创建一个形态为 5×3 的 2 维数组，包含 5 和 10 之间的随机十进制小数。

21. 如何在 Python NumPy 数组中仅输出小数点后三位的数字？

难度：L1

问题：输出或显示 NumPy 数组 rand_arr 中小数点后三位的数字。

输入：

```
rand_arr = np.random.random((5,3))
```

22. 如何通过禁用科学计数法（如 1e10）打印 NumPy 数组？

难度：L1

问题：通过禁用科学计数法（如 1e10）打印 NumPy 数组 rand_arr。

输入：

```
# Create the random array

np.random.seed(100)

rand_arr = np.random.random([3,3])/1e3

rand_arr

#> array([[ 5.434049e-04, 2.783694e-04, 4.245176e-04],

#> [ 8.447761e-04, 4.718856e-06, 1.215691e-04],

#> [ 6.707491e-04, 8.258528e-04, 1.367066e-04]])
```

期望输出：

```
#> array([[ 0.000543, 0.000278, 0.000425],

#> [ 0.000845, 0.000005, 0.000122],

#> [ 0.000671, 0.000826, 0.000137]])
```

23. 如何限制 NumPy 数组输出中项的数目？

难度：L1

问题：将 Python NumPy 数组 a 输出的项的数目限制在最多 6 个元素。

输入：

```
a = np.arange(15)

#> array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
```

期望输出：

```
#> array([ 0, 1, 2, ..., 12, 13, 14])
```

24. 如何在不截断数组的前提下打印出完整的 NumPy 数组？

难度：L1

问题：在不截断数组的前提下打印出完整的 NumPy 数组 a。

输入：

```
np.set_printoptions(threshold=6)

a = np.arange(15)

a

#> array([ 0, 1, 2, ..., 12, 13, 14])
```

期望输出：

```
a

#> array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
```

25. 如何向 Python NumPy 导入包含数字和文本的数据集，同时保持文本不变？

难度：L2

问题：导入 iris 数据集，保持文本不变。

26. 如何从 1 维元组数组中提取特定的列？

难度：L2

问题：从前一个问题导入的 1 维 iris 中提取文本列 species。

输入：

```
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

iris_1d = np.genfromtxt(url, delimiter=',', dtype=None)
```

27. 如何将 1 维元组数组转换成 2 维 NumPy 数组？

难度：L2

问题：忽略 species 文本字段，将 1 维 iris 转换成 2 维数组 iris_2d。

输入：

```
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

iris_1d = np.genfromtxt(url, delimiter=',', dtype=None)
```

28. 如何计算 NumPy 数组的平均值、中位数和标准差？

难度：L1

问题：找出 iris sepallength（第一列）的平均值、中位数和标准差。

```
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

iris = np.genfromtxt(url, delimiter=',', dtype='object')
```

29. 如何归一化数组，使值的范围在 0 和 1 之间？

难度：L2

问题：创建 iris sepallength 的归一化格式，使其值在 0 到 1 之间。

输入：

```
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

sepallength = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0])
```

30. 如何计算 softmax 分数？

难度：L3

问题：计算 sepallength 的 softmax 分数。

```
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

sepallength = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0])
```

31. 如何找到 NumPy 数组的百分数？

难度：L1

问题：找出 iris sepallength（第一列）的第 5 个和第 95 个百分数。

```
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

sepallength = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0])
```

32. 如何在数组的随机位置插入值？

难度：L2

问题：在 iris_2d 数据集中的 20 个随机位置插入 np.nan 值。

```
# Input

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

iris_2d = np.genfromtxt(url, delimiter=',', dtype='object')
```

33. 如何在 NumPy 数组中找出缺失值的位置？

难度：L2

问题：在 iris_2d 的 sepallength（第一列）中找出缺失值的数目和位置。

```
# Input

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

iris_2d = np.genfromtxt(url, delimiter=',', dtype='float')

iris_2d[np.random.randint(150, size=20), np.random.randint(4, size=20)] = np.nan
```

34. 如何基于两个或以上条件过滤 NumPy 数组？

难度：L3

问题：过滤 iris_2d 中满足 petallength（第三列）> 1.5 和 sepallength（第一列）< 5.0 的行。

```
# Input

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])
```

35. 如何在 NumPy 数组中删除包含缺失值的行？

难度：L3

问题：选择 iris_2d 中不包含 nan 值的行。

```
# Input

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])
```

36. 如何找出 NumPy 数组中两列之间的关联性？

难度：L2

问题：找出 iris_2d 中 SepalLength（第一列）和 PetalLength（第三列）之间的关联性。

```
# Input

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])
```

37. 如何确定给定数组是否有空值？

难度：L2

问题：确定 iris_2d 是否有缺失值。

```
# Input

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])
```

38. 如何在 NumPy 数组中将所有缺失值替换成 0？

难度：L2

问题：在 NumPy 数组中将所有 nan 替换成 0。

```
# Input

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])

iris_2d[np.random.randint(150, size=20), np.random.randint(4, size=20)] = np.nan
```

39. 如何在 NumPy 数组中找出唯一值的数量？

难度：L2

问题：在 iris 的 species 列中找出唯一值及其数量。

```
# Input

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

iris = np.genfromtxt(url, delimiter=',', dtype='object')

names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
```

40. 如何将一个数值转换为一个类别（文本）数组？

难度：L2

问题：将 iris_2d 的 petallength（第三列）转换以构建一个文本数组，按如下规则进行转换：

* Less than 3 –> ‘small’

* 3-5 –> 'medium'

* '>=5 –> 'large'

```
# Input

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

iris = np.genfromtxt(url, delimiter=',', dtype='object')

names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
```

41. 如何基于 NumPy 数组现有列创建一个新的列？

难度：L2

问题：为 iris_2d 中的 volume 列创建一个新的列，volume 指 (pi x petallength x sepal_length^2)/3。

```
# Input

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

iris_2d = np.genfromtxt(url, delimiter=',', dtype='object')

names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
```

42. 如何在 NumPy 中执行概率采样？

难度：L3

问题：随机采样 iris 数据集中的 species 列，使得 setose 的数量是 versicolor 和 virginica 数量的两倍。

```
# Import iris keeping the text column intact

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

iris = np.genfromtxt(url, delimiter=',', dtype='object')
```

43. 如何在多维数组中找到一维的第二最大值？

难度：L2

问题：在 species setosa 的 petallength 列中找到第二最大值。

```
# Input

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

iris = np.genfromtxt(url, delimiter=',', dtype='object')

names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
```

44. 如何用给定列将 2 维数组排序？

难度：L2

问题：基于 sepallength 列将 iris 数据集排序。

```
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

iris = np.genfromtxt(url, delimiter=',', dtype='object')

names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
```

45. 如何在 NumPy 数组中找到最频繁出现的值？

难度：L1

问题：在 iris 数据集中找到 petallength（第三列）中最频繁出现的值。

```
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

iris = np.genfromtxt(url, delimiter=',', dtype='object')

names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
```

46. 如何找到第一个大于给定值的数的位置？

难度：L2

问题：在 iris 数据集的 petalwidth（第四列）中找到第一个值大于 1.0 的数的位置。

```
# Input:

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

iris = np.genfromtxt(url, delimiter=',', dtype='object')
```

47. 如何将数组中所有大于给定值的数替换为给定的 cutoff 值？

难度：L2

问题：对于数组 a，将所有大于 30 的值替换为 30，将所有小于 10 的值替换为 10。

输入：

```
np.random.seed(100)

np.random.uniform(1,50, 20)
```

48. 如何在 NumPy 数组中找到 top-n 数值的位置？

难度：L2

问题：在给定数组 a 中找到 top-5 最大值的位置。

```
np.random.seed(100)

a = np.random.uniform(1,50, 20)
```

49. 如何逐行计算数组中所有值的数量？

难度：L4

问题：逐行计算唯一值的数量。

输入：

```
np.random.seed(100)

arr = np.random.randint(1,11,size=(6, 10))

arr

> array([[ 9, 9, 4, 8, 8, 1, 5, 3, 6, 3],

> [ 3, 3, 2, 1, 9, 5, 1, 10, 7, 3],

> [ 5, 2, 6, 4, 5, 5, 4, 8, 2, 2],

> [ 8, 8, 1, 3, 10, 10, 4, 3, 6, 9],

> [ 2, 1, 8, 7, 3, 1, 9, 3, 6, 2],

> [ 9, 2, 6, 5, 3, 9, 4, 6, 1, 10]])
```

期望输出：

```
> [[1, 0, 2, 1, 1, 1, 0, 2, 2, 0],

> [2, 1, 3, 0, 1, 0, 1, 0, 1, 1],

> [0, 3, 0, 2, 3, 1, 0, 1, 0, 0],

> [1, 0, 2, 1, 0, 1, 0, 2, 1, 2],

> [2, 2, 2, 0, 0, 1, 1, 1, 1, 0],

> [1, 1, 1, 1, 1, 2, 0, 0, 2, 1]]
```


输出包含 10 个列，表示从 1 到 10 的数字。这些数值分别代表每一行的计数数量。例如，Cell(0,2) 中有值 2，这意味着，数字 3 在第一行出现了两次。

50. 如何将 array_of_arrays 转换为平面 1 维数组？

难度：L2

问题：将 array_of_arrays 转换为平面线性 1 维数组。

```
# Input:

arr1 = np.arange(3)

arr2 = np.arange(3,7)

arr3 = np.arange(7,10)

array_of_arrays = np.array([arr1, arr2, arr3])

array_of_arrays#> array([array([0, 1, 2]), array([3, 4, 5, 6]), array([7, 8, 9])], dtype=object)
```

期望输出：

```
#> array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
```

51. 如何为 NumPy 数组生成 one-hot 编码？

难度：L4

问题：计算 one-hot 编码。

输入：

```
np.random.seed(101)

arr = np.random.randint(1,4, size=6)

arr

#> array([2, 3, 2, 2, 2, 1])
```

输出：

```
 #> array([[ 0., 1., 0.],

 #> [ 0., 0., 1.],

 #> [ 0., 1., 0.],

 #> [ 0., 1., 0.],

 #> [ 0., 1., 0.],

 #> [ 1., 0., 0.]])
```

52. 如何创建由类别变量分组确定的一维数值？

难度：L3

问题：创建由类别变量分组的行数。使用以下来自 iris species 的样本作为输入。

输入：

```
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

species = np.genfromtxt(url, delimiter=',', dtype='str', usecols=4)

species_small = np.sort(np.random.choice(species, size=20))

species_small

#> array(['Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa',

#> 'Iris-setosa', 'Iris-setosa', 'Iris-versicolor', 'Iris-versicolor',

#> 'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor',

#> 'Iris-versicolor', 'Iris-virginica', 'Iris-virginica',

#> 'Iris-virginica', 'Iris-virginica', 'Iris-virginica',

#> 'Iris-virginica', 'Iris-virginica', 'Iris-virginica'],

#> dtype='<U15')
```

期望输出：

```
#> [0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 6, 7]
```

53. 如何基于给定的类别变量创建分组 id？

难度：L4

问题：基于给定的类别变量创建分组 id。使用以下来自 iris species 的样本作为输入。

输入：

```
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

species = np.genfromtxt(url, delimiter=',', dtype='str', usecols=4)

species_small = np.sort(np.random.choice(species, size=20))

species_small

#> array(['Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa',

#> 'Iris-setosa', 'Iris-setosa', 'Iris-versicolor', 'Iris-versicolor',

#> 'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor',

#> 'Iris-versicolor', 'Iris-virginica', 'Iris-virginica',

#> 'Iris-virginica', 'Iris-virginica', 'Iris-virginica',

#> 'Iris-virginica', 'Iris-virginica', 'Iris-virginica'],

#> dtype='<U15')
```

期望输出：

```
#> [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2]
```

54. 如何使用 NumPy 对数组中的项进行排序？

难度：L2

问题：为给定的数值数组 a 创建排序。

输入：

```
np.random.seed(10)

a = np.random.randint(20, size=10)print(a)#> [ 9 4 15 0 17 16 17 8 9 0]
```

期望输出：

```
[4 2 6 0 8 7 9 3 5 1]
```

55. 如何使用 NumPy 对多维数组中的项进行排序？

难度：L3

问题：给出一个数值数组 a，创建一个形态相同的排序数组。

输入：

```
np.random.seed(10)

a = np.random.randint(20, size=[2,5])print(a)#> [[ 9 4 15 0 17]#> [16 17 8 9 0]]
```

期望输出：

```
#> [[4 2 6 0 8]

#> [7 9 3 5 1]]
```

56. 如何在 2 维 NumPy 数组中找到每一行的最大值？

难度：L2

问题：在给定数组中找到每一行的最大值。

```
np.random.seed(100)

a = np.random.randint(1,10, [5,3])

a

#> array([[9, 9, 4],

#> [8, 8, 1],

#> [5, 3, 6],

#> [3, 3, 3],

#> [2, 1, 9]])
```

57. 如何计算 2 维 NumPy 数组每一行的 min-by-max？

难度：L3

问题：给定一个 2 维 NumPy 数组，计算每一行的 min-by-max。

```
np.random.seed(100)

a = np.random.randint(1,10, [5,3])

a

#> array([[9, 9, 4],

#> [8, 8, 1],

#> [5, 3, 6],

#> [3, 3, 3],

#> [2, 1, 9]])
```

58. 如何在 NumPy 数组中找到重复条目？

难度：L3

问题：在给定的 NumPy 数组中找到重复条目（从第二次出现开始），并将其标记为 True。第一次出现的条目需要标记为 False。

```
# Input

np.random.seed(100)

a = np.random.randint(0, 5, 10)

print('Array: ', a)

#> Array: [0 0 3 0 2 4 2 2 2 2]
```

期望输出：

```
#> [False True False True False False True True True True]
```

59. 如何找到 NumPy 的分组平均值？

难度：L3

问题：在 2 维 NumPy 数组的类别列中找到数值的平均值。

输入：

```
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

iris = np.genfromtxt(url, delimiter=',', dtype='object')

names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
```

期望解：

```
#> [[b'Iris-setosa', 3.418],

#> [b'Iris-versicolor', 2.770],

#> [b'Iris-virginica', 2.974]]
```

60. 如何将 PIL 图像转换成 NumPy 数组？

难度：L3

问题：从以下 URL 中导入图像，并将其转换成 NumPy 数组。

```
URL = 'https://upload.wikimedia.org/wikipedia/commons/8/8b/Denali_Mt_McKinley.jpg'
```

61. 如何删除 NumPy 数组中所有的缺失值？

难度：L2

问题：从 1 维 NumPy 数组中删除所有的 nan 值。

输入：

```
np.array([1,2,3,np.nan,5,6,7,np.nan])
```

期望输出：

```
array([ 1., 2., 3., 5., 6., 7.])
```

62. 如何计算两个数组之间的欧几里得距离？

难度：L3

问题：计算两个数组 a 和 b 之间的欧几里得距离。

输入：

```
a = np.array([1,2,3,4,5])

b = np.array([4,5,6,7,8])
```

63. 如何在一个 1 维数组中找到所有的局部极大值（peak）？

难度：L4

问题：在 1 维数组 a 中找到所有的 peak，peak 指一个数字比两侧的数字都大。

输入：

```
a = np.array([1, 3, 7, 1, 2, 6, 0, 1])
```

期望输出：

```
#> array([2, 5])
```

64. 如何从 2 维数组中减去 1 维数组，从 2 维数组的每一行分别减去 1 维数组的每一项？

难度：L2

问题：从 2 维数组 a_2d 中减去 1 维数组 b_1d，即从 a_2d 的每一行分别减去 b_1d 的每一项。

输入：

```
a_2d = np.array([[3,3,3],[4,4,4],[5,5,5]])

b_1d = np.array([1,1,1]
```

期望输出：

```
#> [[2 2 2]

#> [2 2 2]

#> [2 2 2]]
```

65. 如何在数组中找出某个项的第 n 个重复索引？

难度：L2

问题：找到数组 x 中数字 1 的第 5 个重复索引。

```
x = np.array([1, 2, 1, 1, 3, 4, 3, 1, 1, 2, 1, 1, 2])
```

66. 如何将 NumPy 的 datetime64 对象（object）转换为 datetime 的 datetime 对象？

难度：L2

问题：将 NumPy 的 datetime64 对象（object）转换为 datetime 的 datetime 对象。

```
# Input: a numpy datetime64 object

dt64 = np.datetime64('2018-02-25 22:10:10')
```

67. 如何计算 NumPy 数组的移动平均数？

难度：L3

问题：给定 1 维数组，计算 window size 为 3 的移动平均数。

输入：

```
np.random.seed(100)

Z = np.random.randint(10, size=10)
```

68. 给定起始数字、length 和步长，如何创建一个 NumPy 数组序列？

难度：L2

问题：从 5 开始，创建一个 length 为 10 的 NumPy 数组，相邻数字的差是 3。

69. 如何在不规则 NumPy 日期序列中填充缺失日期？

难度：L3

问题：给定一个非连续日期序列的数组，通过填充缺失的日期，使其变成连续的日期序列。

输入：

```
# Input

dates = np.arange(np.datetime64('2018-02-01'), np.datetime64('2018-02-25'), 2)

print(dates)

#> ['2018-02-01' '2018-02-03' '2018-02-05' '2018-02-07' '2018-02-09'

#> '2018-02-11' '2018-02-13' '2018-02-15' '2018-02-17' '2018-02-19'

#> '2018-02-21' '2018-02-23']
```

70. 如何基于给定的 1 维数组创建 strides？

难度：L4

问题：给定 1 维数组 arr，使用 strides 生成一个 2 维矩阵，其中 window length 等于 4，strides 等于 2，例如 [[0,1,2,3], [2,3,4,5], [4,5,6,7]..]。

输入：

```
arr = np.arange(15)

arr

#> array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
```

期望输出：

```
#> [[ 0 1 2 3]

#> [ 2 3 4 5]

#> [ 4 5 6 7]

#> [ 6 7 8 9]

#> [ 8 9 10 11]

#> [10 11 12 13]]
```

所有问题的解决方案参见原文：[https://www.machinelearningplus.com/101-numpy-exercises-python/](https://www.machinelearningplus.com/101-numpy-exercises-python/)

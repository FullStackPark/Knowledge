Python 面向对象
===========

   Python从设计之初就已经是一门面向对象的语言，正因为如此，在Python中创建一个类和对象是很容易的。本章节我们将详细介绍Python的面向对象编程。 

  如果你以前没有接触过面向对象的编程语言，那你可能需要先了解一些面向对象语言的一些基本特征，在头脑里头形成一个基本的面向对象的概念，这样有助于你更容易的学习Python的面向对象编程。 

  接下来我们先来简单的了解下面向对象的一些基本特征。 

   面向对象技术简介
--------

  * **类(Class): **用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
 * **类变量：**类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
 * **数据成员：**类变量或者实例变量, 用于处理类及其实例对象的相关的数据。
 * **方法重写：**如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
 * **实例变量：**定义在方法中的变量，只作用于当前实例的类。
 * **继承：**即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
 * **实例化：**创建一个类的实例，类的具体对象。
 * **方法：**类中定义的函数。
 * **对象：**通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。
   创建类
---

  使用 class 语句来创建一个新类，class 之后为类的名称并以冒号结尾:

 
```

class ClassName:
   '类的帮助信息'   #类文档字符串
   class_suite  #类体

```

 类的帮助信息可以通过ClassName.\_\_doc\_\_查看。

  class\_suite 由类成员，方法，数据属性组成。

 ### 实例

  以下是一个简单的 Python 类的例子:

  实例
--

 <pre>

#!/usr/bin/python
# -*- coding: UTF-8 -*-
class Employee:
   '所有员工的基类'
empCount = 0
def __init__(self, name, salary):
      self.name = name
self.salary = salary
Employee.empCount += 1
def displayCount(self):
     print "Total Employee %d" % Employee.empCount
def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary
</pre>

   * empCount 变量是一个类变量，它的值将在这个类的所有实例之间共享。你可以在内部类或外部类使用 Employee.empCount 访问。


 * 第一种方法\_\_init\_\_()方法是一种特殊的方法，被称为类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法


 * self 代表类的实例，self 在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数。


  ### self代表类的实例，而非类

 类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的**第一个参数名称**, 按照惯例它的名称是 self。

  <pre>

class Test:
    def prt(self):
        print(self)
print(self.__class__)
t = Test()
t.prt()
</pre>

  以上实例执行结果为：

 
```

<__main__.Test instance at 0x10d066878>
__main__.Test

```

 从执行结果可以很明显的看出，self 代表的是类的实例，代表当前对象的地址，而 self.class 则指向类。

 self 不是 python 关键字，我们把他换成 runoob 也是可以正常执行的:

  实例
--

 <pre>

class Test:
    def prt(runoob):
        print(runoob)
print(runoob.__class__)
t = Test()
t.prt()
</pre>

 以上实例执行结果为：

 
```

<__main__.Test instance at 0x10d066878>
__main__.Test

```

 创建实例对象
------

 实例化类其他编程语言中一般用关键字 new，但是在 Python 中并没有这个关键字，类的实例化类似函数调用方式。

  以下使用类的名称 Employee 来实例化，并通过 \_\_init\_\_ 方法接收参数。

 
```

"创建 Employee 类的第一个对象"
emp1 = Employee("Zara", 2000)
"创建 Employee 类的第二个对象"
emp2 = Employee("Manni", 5000)

```

 访问属性
----

 您可以使用点号 . 来访问对象的属性。使用如下类的名称访问类变量:

 
```

emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount

```

 完整实例：

  实例
--

 <pre>

#!/usr/bin/python
# -*- coding: UTF-8 -*-
class Employee:
   '所有员工的基类'
empCount = 0
def __init__(self, name, salary):
      self.name = name
self.salary = salary
Employee.empCount += 1
def displayCount(self):
     print "Total Employee %d" % Employee.empCount
def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary
"创建 Employee 类的第一个对象"
emp1 = Employee("Zara", 2000)
"创建 Employee 类的第二个对象"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount
</pre>

  执行以上代码输出结果如下：

 
```

Name :  Zara ,Salary:  2000
Name :  Manni ,Salary:  5000
Total Employee 2

```

 你可以添加，删除，修改类的属性，如下所示：

 
```

emp1.age = 7  # 添加一个 'age' 属性
", u"emp1.age = 8  # 修改 'age' 属性
", u"del emp1.age  # 删除 'age' 属性

```

 你也可以使用以下函数的方式来访问属性：

  * getattr(obj, name[, default]) : 访问对象的属性。
 * hasattr(obj,name) : 检查是否存在一个属性。
 * setattr(obj,name,value) : 设置一个属性。如果属性不存在，会创建一个新属性。
 * delattr(obj, name) : 删除属性。
   <pre>

hasattr(emp1, 'age') # 如果存在 'age' 属性返回 True。
getattr(emp1, 'age') # 返回 'age' 属性的值
setattr(emp1, 'age', 8) # 添加属性 'age' 值为 8
delattr(emp1, 'age') # 删除属性 'age'
</pre>

   Python内置类属性
-----------

  * \_\_dict\_\_ : 类的属性（包含一个字典，由类的数据属性组成） 
 * \_\_doc\_\_ :类的文档字符串 
 * \_\_name\_\_: 类名 
 * \_\_module\_\_: 类定义所在的模块（类的全名是'\_\_main\_\_.className'，如果类位于一个导入模块mymod中，那么className.\_\_module\_\_ 等于 mymod） 
 * \_\_bases\_\_ : 类的所有父类构成元素（包含了一个由所有父类组成的元组） 
  Python内置类属性调用实例如下：

  实例
--

 <pre>

#!/usr/bin/python
# -*- coding: UTF-8 -*-
class Employee:
   '所有员工的基类'
empCount = 0
def __init__(self, name, salary):
      self.name = name
self.salary = salary
Employee.empCount += 1
def displayCount(self):
     print "Total Employee %d" % Employee.empCount
def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary
print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__
</pre>

  执行以上代码输出结果如下：

 
```

Employee.__doc__: 所有员工的基类
Employee.__name__: Employee
Employee.__module__: __main__
Employee.__bases__: ()
Employee.__dict__: {'__module__': '__main__', 'displayCount': <function displayCount at 0x10a939c80>, 'empCount': 0, 'displayEmployee': <function displayEmployee at 0x10a93caa0>, '__doc__': '\xe6\x89\x80\xe6\x9c\x89\xe5\x91\x98\xe5\xb7\xa5\xe7\x9a\x84\xe5\x9f\xba\xe7\xb1\xbb', '__init__': <function __init__ at 0x10a939578>}

```

  python对象销毁(垃圾回收)
----------------

  Python 使用了引用计数这一简单技术来跟踪和回收垃圾。

 在 Python 内部记录着所有使用中的对象各有多少引用。
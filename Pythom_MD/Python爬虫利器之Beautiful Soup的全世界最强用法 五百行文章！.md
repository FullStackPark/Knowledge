# Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！

<!---->python蔷薇 2017-11-02 12:45:18

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p9.pstatp.com/large/4358000386daf6889a5b)

# 0. 前言<br>

爬虫是一个非常有意思的东西，比如自己做的一个网页上面什么数据都没有就可以爬虫别人的 然后进行去重 数据分析等等 在这里因为爬虫涉及到的方面非常多 所以小编推荐一个群 如果遇到问题也找不到人解决？ 或是交流技术都可以加入群内貌似也有两千多人了，有很多热爱python聚集在了一起，并整理了大量的学习资料和爬虫方面上传到了群文件当中，喜欢python的朋友可以加入python群：526929231欢迎大家交流讨论各种技术，一起快速成长

---

# **1. Beautiful Soup的简介**

先来了解下，Beautiful Soup是python的一个库，是一个框架，并且是第三方的所以西药安装，最主要的功能是从网页抓取数据。官方解释如下：

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p3.pstatp.com/large/435600037968f54bb73e)

# **2. Beautiful Soup 安装**

现在通常使用的版本基本上都是Beautiful Soup4 之前的版本已经被移植了过来，也就是说我们需要导入的事import bs4.我们这里版本所介绍的事Beautiful Soup 4.3.2（BS4） 需要了解的是bs4对py3的版本支持不是特别友好，现在也已经慢慢在过度到py3还没有完全实现这个过程，如果需要使用py3的通过可以下载bs3的版本会好一些  

**pip进行安装或easy_install进行安装**

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p1.pstatp.com/large/43540003a3e9e60a29a9)

**离线下载安装：**

**\#BS3**

```
https://www.crummy.com/software/BeautifulSoup/bs3/download//
```

**\#BS4**  

```
https://www.crummy.com/software/BeautifulSoup/bs4/download/
```


最新版本是BS4.6 今年五月份发布的 **官网**


 **https://www.crummy.com/software/BeautifulSoup/**

下载完成之后解压

运行下面的命令即可完成安装

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p3.pstatp.com/large/4357000379c703c88321)

然后需要安装 lxml

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p3.pstatp.com/large/43590002032c7cb841e3)

一般情况下 lxml安装会出现一些问题导致安装不上 所以会去现在whl离线包或源码来进行安装，另外解释器是纯Python实现的HTML5lib，解析方式和浏览器相同，会自动补全结束标签 等等 一系列的渲染操作，可以进行选择性的安装 类似于一个工具更加方便操作不使用它也是可以的

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p3.pstatp.com/large/435700037d91c49f9db0)

除此之外BS支持python标准库中的HTML解析器，支持第三方的解析器，如果想要放弃它，python会使用默认的解析器，lxml解析器使用起来速度更快，更加方便与强大。

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p1.pstatp.com/large/435a00018eee7c49d6d1)

# **3. 开始Beautiful Soup的旅程**<br>

以上工作准备之后就可以开启深渊之旅了

# **4. 创建Beautiful Soup对象**<br>

首先导入BS4的库

```
from bs4 import BeautifulSoup
```

这里我们创建一个字符的HTML节点代码，以供后面的例子使用

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p9.pstatp.com/large/4359000216d73a38dfb3)

创建BS对象

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p1.pstatp.com/large/43550003b1fe1674c12e)

当然可以使用loca本地的HTML文件来进行创建，比如

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p3.pstatp.com/large/43550003b27472bcd4bc)

上面这句代码便是将本地 index.html 文件打开，打开之后创建一个BS实例对象以供后面调用。

来试着输出打印一下 soup 对象的内容

**\#输出**

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p3.pstatp.com/large/435900021875a09783dd)

上面 prettify()这个格式化函数会常常用

# **5. 四大对象种类**

Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,所有对象可以归纳为4种:

* Tag

* NavigableString

* BeautifulSoup

* Comment

下面我们进行一一介绍

**（1）Tag**

Tag 是什么？通俗点讲就是 HTML 中的一个个标签，例如

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p9.pstatp.com/large/435600039a051e2ce0bf)

上面的 title a 等等 HTML 标签加上里面包括的内容就是 Tag，下面我们来感受一下怎样用 Beautiful Soup 来方便地获取 Tags

下面每一段代码中注释部分即为运行结果

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p1.pstatp.com/large/435800038cdd6c439796)

我们可以利用 soup加标签名轻松地获取这些标签的内容，是不是感觉比正则表达式方便多了？不过有一点是，它查找的是在所有内容中的第一个符合要求的标签，如果要查询所有的标签，我们在后面进行介绍。

我们可以验证一下这些对象的类型

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p3.pstatp.com/large/4357000390b94e74aee9)

对于 Tag，它有两个重要的属性，是 name 和 attrs，下面我们分别来感受一下

**name**

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p3.pstatp.com/large/43540003c11660ecd77e)

soup 对象本身比较特殊，它的 name 即为 [document]，对于其他内部标签，输出的值便为标签本身的名称。

**attrs**

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p1.pstatp.com/large/435600039b100ccc056a)

在这里，我们把 p 标签的所有属性打印输出了出来，得到的类型是一个dict字典。

如果我们想要单独获取某个属性，可以这样，例如我们获取它的 class 叫什么

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p3.pstatp.com/large/435600039b5ff3c29a04)

还可以这样，利用get方法，传入属性的名称，两个完全相等

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p1.pstatp.com/large/435900021b81749a840c)

这下可以对这个属性或是内容进行修改

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p3.pstatp.com/large/43540003c2e753dd36eb)

**删除**

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p1.pstatp.com/large/43550003b70765ed4687)

不过，对于修改删除的操作，不是我们的主要用途，在此不做详细介绍了，如果有需要，请查看前面提供的官方文档

**（2）NavigableString**

既然我们已经得到了标签的内容，那么问题来了，我们要想获取标签内部的文字怎么办呢？很简单，用 .string 即可，例如

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p9.pstatp.com/large/435600039df273f27462)

这样我们就轻松获取到了标签里面的内容，想想如果用正则表达式要多麻烦。它的类型是一个 NavigableString，翻译过来叫 可以遍历的字符串，不过我们最好还是称它英文名字吧。

**来检查一下它的类型**

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p3.pstatp.com/large/435900021d84e7c2a20e)

**（3）BeautifulSoup**

BeautifulSoup对象表示的是一个文档的全部内容.大部分时候,可以把它当作Tag对象，是一个特殊的 Tag，我们可以分别获取它的类型，名称，以及属性来感受一下

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p3.pstatp.com/large/435900021dad2ccb55e1)

**（4）Comment**

Comment对象是一个特殊类型的NavigableString对象，其实输出的内容仍然不包括注释符号，但是如果不好好处理它，可能会对我们的文本处理造成意想不到的麻烦。

我们找一个带注释的标签

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p1.pstatp.com/large/435900021dde1525afe3)

**结果如下**

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p3.pstatp.com/large/43540003c4df8b2fc56b)

a 标签里的内容实际上是注释，但是如果我们利用 .string 来输出它的内容，我们发现它已经把注释符号去掉了，所以这可能会给我们带来不必要的麻烦。

另外我们打印输出下它的类型，发现它是一个 Comment 类型，所以，我们在使用前最好做一下判断，判断代码如下

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p3.pstatp.com/large/43540003c50354431db7)

上面的代码中，我们首先判断了它的类型，是否为 Comment 类型，然后再进行其他操作，如打印输出。

# **6. 遍历文档树**

**（1）直接子节点**

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p1.pstatp.com/large/43540003c56fe800b310)

**.contents**

tag 的 .content 属性可以将tag的子节点以列表的方式输出

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p1.pstatp.com/large/435900021ec52b49c451)

输出方式为列表，我们可以用列表索引来获取它的某一个元素

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p3.pstatp.com/large/43540003c5b6f05a7a67)

**.children**

它返回的不是一个 list，不过我们可以通过遍历获取所有子节点。

我们打印输出 .children 看一下，可以发现它是一个 list 生成器对象

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p3.pstatp.com/large/435a0001a449d3b85644)

我们怎样获得里面的内容呢？很简单，遍历一下就好了，代码及结果如下

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p1.pstatp.com/large/43540003c60e71601f33)

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p3.pstatp.com/large/43540003c63de4c3e9eb)

**（2）所有子孙节点**

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p3.pstatp.com/large/435a0001a4c8f811427c)

**.descendants**

.contents和.children属性仅包含tag的直接子节点，.descendants属性可以对所有tag的子孙节点进行递归循环，和 children类似，我们也需要遍历获取其中的内容。

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p3.pstatp.com/large/435800039315a3982398)

运行结果如下，可以发现，所有的节点都被打印出来了，先生最外层的 HTML标签，其次从 head 标签一个个剥离，以此类推。

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p1.pstatp.com/large/435a0001a508b5f61f5f)

**（3）节点内容**

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p3.pstatp.com/large/435700039705cf3d83c6)

如果tag只有一个NavigableString类型子节点,那么这个tag可以使用.string得到子节点。如果一个tag仅有一个子节点,那么这个tag也可以使用.string方法,输出结果与当前唯一子节点的.string结果相同。

通俗点说就是：如果一个标签里面没有标签了，那么 .string 就会返回标签里面的内容。如果标签里面只有唯一的一个标签了，那么 .string 也会返回最里面的内容。例如

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p3.pstatp.com/large/43550003bb04e629bbb9)

如果tag包含了多个子节点,tag就无法确定，string 方法应该调用哪个子节点的内容, .string 的输出结果是 None

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p3.pstatp.com/large/43550003bb20c93986d6)

**（4）多个内容**

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p9.pstatp.com/large/43550003bb53ef43c47e)

**.strings**

获取多个内容，不过需要遍历获取，比如下面的例子

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p9.pstatp.com/large/43560003a1f0f693682f)

**.stripped_strings**

输出的字符串中可能包含了很多空格或空行,使用.stripped_strings可以去除多余空白内容

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p1.pstatp.com/large/43560003a22d5d0cc4ba)

**（5）父节点**

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p3.pstatp.com/large/43560003a29f02908cd1)

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p3.pstatp.com/large/4358000395dfa9baaae8)

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p1.pstatp.com/large/43570003999836497def)

**（6）全部父节点**

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p3.pstatp.com/large/435a0001a8231d2226af)

通过元素的.parents属性可以递归得到元素的所有父辈节点，例如

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p3.pstatp.com/large/435800039673ece671ae)

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p3.pstatp.com/large/435800039688aae0285a)

**（7）兄弟节点**

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p9.pstatp.com/large/43550003bdf47de09edf)

兄弟节点可以理解为和本节点处在统一级的节点，.next_sibling 属性获取了该节点的下一个兄弟节点，.previous_sibling 则与之相反，如果节点不存在，则返回 None

注意：实际文档中的tag的 .next_sibling 和 .previous_sibling 属性通常是字符串或空白，因为空白或者换行也可以被视作一个节点，所以得到的结果可能是空白或者换行

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p3.pstatp.com/large/435a0001a88b8acacf7e)

**（8）全部兄弟节点**

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p3.pstatp.com/large/435900022528168ece3b)

通过.next_siblings和.previous_siblings属性可以对当前节点的兄弟节点迭代输出

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p1.pstatp.com/large/43590002256270d39de4)

**（9）前后节点**

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p1.pstatp.com/large/435900022580bc3220f8)

与 .next_sibling .previous_sibling 不同，它并不是针对于兄弟节点，而是在所有节点，不分层次

比如 head 节点为

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p3.pstatp.com/large/43540003cc355c33ba88)

那么它的下一个节点便是 title，它是不分层次关系的

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p3.pstatp.com/large/435a0001aaee27653924)

**（10）所有前后节点**

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p1.pstatp.com/large/43580003995ca222d5a3)

通过.next_elements和.previous_elements的迭代器就可以向前或向后访问文档的解析内容,就好像文档正在被解析一样

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p9.pstatp.com/large/43550003c0e420773f2e)

以上是遍历文档树的基本用法。

# **7.搜索文档树**

（1）find_all( name , attrs , recursive , text , **kwargs )

find_all()方法搜索当前tag的所有tag子节点,并判断是否符合过滤器的条件

**1）name 参数**

name参数可以查找所有名字为name的tag,字符串对象会被自动忽略掉

**A.传字符串**

最简单的过滤器是字符串.在搜索方法中传入一个字符串参数,Beautiful Soup会查找与字符串完整匹配的内容,下面的例子用于查找文档中所有的<b>标签

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p3.pstatp.com/large/4358000399cc403a3a59)

**B.传正则表达式**

如果传入正则表达式作为参数,Beautiful Soup会通过正则表达式的match()来匹配内容.下面例子中找出所有以b开头的标签,这表示<body>和<b>标签都应该被找到

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p3.pstatp.com/large/43560003a712d41f3bcb)

**C.传列表**

如果传入列表参数,Beautiful Soup会将与列表中任一元素匹配的内容返回.下面代码找到文档中所有<a>标签和<b>标签

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p3.pstatp.com/large/43550003c14e2dade0b7)

**D.传 True**

True可以匹配任何值,下面代码查找到所有的tag,但是不会返回字符串节点

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p3.pstatp.com/large/435a0001abfbfb15c31e)

**E.传方法**

如果没有合适过滤器,那么还可以定义一个方法,方法只接受一个元素参数[4],如果这个方法返回True表示当前元素匹配并且被找到,如果不是则反回False

下面方法校验了当前元素,如果包含class属性却不包含id属性,那么将返回True:

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p3.pstatp.com/large/4359000226e65be02d49)

将这个方法作为参数传入find_all()方法,将得到所有<p>标签:

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p3.pstatp.com/large/435700039e1d7923806f)

**2）keyword 参数**

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p3.pstatp.com/large/435800039a9927087af6)

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p1.pstatp.com/large/435700039e5728755d53)

如果传入href参数,Beautiful Soup会搜索每个tag的”href”属性

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p3.pstatp.com/large/435a0001ac98b0954bc2)

使用多个指定名字的参数可以同时过滤tag的多个属性

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p1.pstatp.com/large/435a0001acd6e3b66140)

在这里我们想用 class 过滤，不过 class 是 python 的关键词，这怎么办？加个下划线就可以

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p3.pstatp.com/large/435700039ed195a87bfc)

有些tag属性在搜索不能使用,比如HTML5中的 data-* 属性

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p3.pstatp.com/large/43540003ce9811d4d946)

但是可以通过find_all()方法的attrs参数定义一个字典参数来搜索包含特殊属性的tag

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p3.pstatp.com/large/43560003a8af391ca0b5)

**3）text 参数**

通过text参数可以搜搜文档中的字符串内容.与name参数的可选值一样,text参数接受 字符串 , 正则表达式 , 列表, True

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p3.pstatp.com/large/435700039f3aab0ec906)

**4）limit 参数**

find_all()方法返回全部的搜索结构,如果文档树很大那么搜索会很慢.如果我们不需要全部结果,可以使用limit参数限制返回结果的数量.效果与SQL中的limit关键字类似,当搜索到的结果数量达到limit的限制时,就停止搜索返回结果.

文档树中有3个tag符合搜索条件,但结果只返回了2个,因为我们限制了返回数量

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p3.pstatp.com/large/435a0001ad8ef32fab39)

**5）recursive 参数**

调用tag的find_all()方法时,Beautiful Soup会检索当前tag的所有子孙节点,如果只想搜索tag的直接子节点,可以使用参数recursive=False.

一段简单的文档:

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p3.pstatp.com/large/4359000228917532f264)

是否使用recursive参数的搜索结果:

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p3.pstatp.com/large/435800039bf601f145b7)

（2）find( name , attrs , recursive , text , \**kwargs )

它与 find_all() 方法唯一的区别是find_all()方法的返回结果是值包含一个元素的列表,而find()方法直接返回结果

（3）find_parents() find_parent()

find_all()和find()只搜索当前节点的所有子节点,孙子节点等.find_parents()和find_parent()用来搜索当前节点的父辈节点,搜索方法与普通tag的搜索方法相同,搜索文档搜索文档包含的内容

（4）find_next_siblings() find_next_sibling()

这2个方法通过 .next_siblings 属性对当 tag 的所有后面解析的兄弟 tag 节点进行迭代,find_next_siblings()方法返回所有符合条件的后面的兄弟节点,find_next_sibling()只返回符合条件的后面的第一个tag节点

（5）find_previous_siblings() find_previous_sibling()

这2个方法通过 .previous_siblings 属性对当前 tag 的前面解析的兄弟 tag 节点进行迭代,find_previous_siblings()方法返回所有符合条件的前面的兄弟节点,find_previous_sibling()方法返回第一个符合条件的前面的兄弟节点

（6）find_all_next() find_next()

这2个方法通过 .next_elements 属性对当前 tag 的之后的 tag 和字符串进行迭代,find_all_next()方法返回所有符合条件的节点,find_next()方法返回第一个符合条件的节点

（7）find_all_previous() 和 find_previous()

这2个方法通过 .previous_elements 属性对当前节点前面的 tag 和字符串进行迭代,find_all_previous()方法返回所有符合条件的节点,find_previous()方法返回第一个符合条件的节点

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p3.pstatp.com/large/43560003a97fb4f85bb1)

# **8.CSS选择器**

我们在写 CSS 时，标签名不加任何修饰，类名前加点，id名前加 #，在这里我们也可以利用类似的方法来筛选元素，用到的方法是 **soup.select()，返回类型是list**

（1）通过标签名查找

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p3.pstatp.com/large/43570003a069ac2eff9d)

（2）通过类名查找

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p3.pstatp.com/large/43550003c4397e0c623c)

（3）通过 id 名查找

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p3.pstatp.com/large/435a0001aed0444bbaa6)

（4）组合查找

组合查找即和写 class 文件时，标签名与类名、id名进行的组合原理是一样的，例如查找 p 标签中，id 等于 link1的内容，二者需要用空格分开

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p1.pstatp.com/large/43540003d05b73a93f40)

直接子标签查找

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p1.pstatp.com/large/43550003c4b34a5ff606)

（5）属性查找

查找时还可以加入属性元素，属性需要用中括号括起来，注意属性和标签属于同一节点，所以中间不能加空格，否则会无法匹配到。

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p3.pstatp.com/large/43540003d0c2e5cc4313)

同样，属性仍然可以与上述查找方式组合，不在同一节点的空格隔开，同一节点的不加空格

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p1.pstatp.com/large/43540003d0e516f5bf76)

以上的 select 方法返回的结果都是列表形式，可以遍历形式输出，然后用 get_text() 方法来获取它的内容。

![Python爬虫利器之Beautiful Soup的全世界最强用法 五百行文章！](http://p9.pstatp.com/large/435a0001af979c448872)

好，这就是另一种与 find_all 方法有异曲同工之妙的查找方法，是不是感觉很方便？如果说有遇到任何问题可以加一下在前面所说的企鹅群哦！

如果手机上显示代码错乱，请分享到QQ或者其他地方，用电脑查看！！！

---

python能干的东西有很多，这里不再过多叙述，直接重点干货。

爬虫入门之后，我们有两条路可以走。

一个是继续深入学习，以及关于设计模式的一些知识，强化Python相关知识，自己动手造轮子，继续为自己的爬虫增加分布式，多线程等功能扩展。另一条路便是学习一些优秀的框架，先把这些框架用熟，可以确保能够应付一些基本的爬虫任务，也就是所谓的解决温饱问题，然后再深入学习它的源码等知识，进一步强化。

就个人而言，前一种方法其实就是自己动手造轮子，前人其实已经有了一些比较好的框架，可以直接拿来用，但是为了自己能够研究得更加深入和对爬虫有更全面的了解，自己动手去多做。后一种方法就是直接拿来前人已经写好的比较优秀的框架，拿来用好，首先确保可以完成你想要完成的任务，然后自己再深入研究学习。第一种而言，自己探索的多，对爬虫的知识掌握会比较透彻。第二种，拿别人的来用，自己方便了，可是可能就会没有了深入研究框架的心情，还有可能思路被束缚。

![Python搭配Mongo学习心得，爬取知乎用户信息完整教程（干货附源码）](http://p1.pstatp.com/large/402a0001d7d2e167f46f)

。。。

接触了几个爬虫框架，其中比较好用的是 Scrapy 和PySpider。就个人而言，pyspider上手更简单，操作更加简便，因为它增加了 WEB 界面，写爬虫迅速，集成了phantomjs，可以用来抓取js渲染的页面。Scrapy自定义程度高，比 PySpider更底层一些，适合学习研究，需要学习的相关知识多，不过自己拿来研究分布式和多线程等等是非常合适的。

从爬虫必要的几个基本需求来讲：

1.抓取

py的urllib不一定去用，但是要学，如果还没用过的话。

比较好的替代品有requests等第三方更人性化、成熟的库，如果pyer不了解各种库，那就白学了。

抓取最基本就是拉网页回来。

如果深入做下去，会发现要面对不同的网页要求，比如有认证的，不同文件格式、编码处理，各种奇怪的url合规化处理、重复抓取问题、cookies跟随问题、多线程多进程抓取、多节点抓取、抓取调度、资源压缩等一系列问题。

所以第一步就是拉网页回来，慢慢会发现各种问题待优化。

2.存储

抓回来一般会用一定策略存下来，而不是直接分析，个人觉得更好的架构应该是把分析和抓取分离，更加松散，每个环节出了问题能够隔离另外一个环节可能出现的问题，好排查也好更新发布。

那么存文件系统、SQLorNOSQL数据库、内存数据库，如何去存就是这个环节的重点。

可以选择存文件系统开始，然后以一定规则命名。

3.分析

对网页进行文本分析，提取链接也好，提取正文也好，总之看的需求，但是一定要做的就是分析链接了。

可以用认为最快最优的办法，比如正则表达式。

然后将分析后的结果应用与其他环节：）

4.展示

要是做了一堆事情，一点展示输出都没有，如何展现价值。

所以找到好的展示组件，去show出肌肉也是关键。

如果为了做个站去写爬虫，抑或要分析某个东西的数据，都不要忘了这个环节，更好地把结果展示出来给别人感受。

---

前言

其实写这个 **MongoDB心得** 的初衷和我当年整理的 js大脑图 比较一致,而且确实对于我个人而言，每个时间段还是希望要有一些整理性质的东西输出出来，分享给需要的人。

这个系列题目和我自己目前在写的 yc (a fancy node develop platform) 一样，架子都很庞大，但是我还是会坚持写下去，希望感兴趣的同学多多关注。

简介

本文介绍一些基本概念，涉及到文档、集合和数据库，以及一些基本的操作。

那MongoDB是干嘛的呢？其实关键词还是`NoSQL`

安装

本文只介绍mac上的安装更多可以猛戳：官方文档,本文不做过多描述，只是提醒需要手动地创建一个数据目录，后面会介绍它的作用。

基础的概念

文档

先看一个我们熟悉的js里面的对象：

<pre>
shell{"name" : "yaochun" , "company" : "wandoujia" , "group" : "w3cplus" , "job" : "fe"}
</pre>

其实这也是MongoDB里面的核心概念：**文档**

就是键值对，但是有一些特有的特性：

**一、**这个键值对是有序的：

<pre>
shell{ "name" : "yaochun" , "company" : "wandoujia" }{ "company" : "wandoujia" , "name" : "yaochun" }
</pre>

所以以上两个文档是不一样的。

**二、**键是字符串，不能还有``，`.` 和 `$` 有特别的意义，`_`开头的是保留的

**三、**值可以是双引号的字符串，也可以是其他几种数据类型。

**四、**区分类型和大小写：

<pre>
shell{ "name" : "yaochun" , "company" : "wandoujia" , "age" : 50 }{ "company" : "wandoujia" , "name" : "yaochun" , "age" : "50" }
</pre>

所以以上两个文档也是不一样的。

**五、**文档里面的键不能重复，否则视为非法。

集合

集合其实就是**一组**文档。

集合的命名也有规则：

1.  不能是空字符串

2.  也不能还有``字符

3.  不能以一些系统集合的保留的前缀，比如`system.`这样开头

4.  也不能包含$

集合里面有没有数学里面的子集合呢？可以用`.`来划分子集合。

数据库

数据库其实是由多个集合组成。数据库之间是相对独立的，存储在不同的文件中。

数据库的命名同样也有规则：

1.  不能是空字符串

2.  也不能还有`` 、`$`类似这些字符

3.  小写

4.  最多64字节

因为数据库名其实最终都会变成文件系统的文件，所以命名有一定的约束。

保留的数据库名词：

1.  admin

2.  local

3.  config

数据类型介绍

其实大家发现没有，文档的结构类似我们常用的**JSON**。那在MongoDB里面的有哪些数据类型呢？

null

<pre>
shell{ "freetime" : null }
</pre>

日期

<pre>
shell{ "date" : new Date() }
</pre>

数组

实例：

<pre>
shell{ "keywords" : [ "yaochun" , "wandoujia" , "w3cplus" ] }
</pre>

内嵌文档

实例：

<pre>
shell{ "info" : {"yaochun" , "company" : "wandoujia" , "group" : "w3cplus" } }
</pre>

其实就是文档包含某个文档

正则

实例：

<pre>
shell{ "name" : /yaochun/i }
</pre>

代码

实例：

<pre>
shell{ "code" : function() {/*..*/} }
</pre>

其他的比较基础的比如：布尔、字符串等就不在这里介绍了。

基础的操作

一般包含：插入、更新、删除和查询

插入

实例：

<pre>
shell//welcome to join us: http://www.wandoujia.com/joindb.wandoujia.fe.insert({ "name" : "yourname" })
</pre>

其实插入从上面的实例直观的看到：

1.  也是用insert

2.  insert方法里面传入的其实就是一个文档

那没有什么主键吗？MongoDB的插入操作默认会给文档加一个 `_id` 。

删除

实例1：

<pre>
shelldb.book.mongodb.remove()
</pre>

这个代表我把book这个集合的子集合mongodb的所有文档都删除掉，但是子集合mongodb本身还在，索引也会保留。

实例2：

`shell db.book.mongodb.remove({ "part" : "primary" })`

这里给remove这个操作传递了一个文档，做查询和筛选用的。符合条件的文档才会被删除。

这个代表我把book这个集合的子集合mongodb中所有part为primary的删除掉。

查询

初级教程里面我们只是简单地看看基本的查询方式，在中级里面会全面地去学习一下。

实例1：

`shell //welcome to join us: http://www.wandoujia.com/join db.wandoujia.jobs.find()`

实例2：

`shell //welcome to join us: http://www.wandoujia.com/join db.wandoujia.jobs.find({ "category", "fe" , "level" : 2 })`

从上面的实例中，我们看出，最基本的查询可以用**find**

而且find里面可以传递参数，比如某个或者某几个文档来指定查询的条件。

多维度的查询

find

前面我们简单介绍了一下find的第一个参数，它其实就是一个文档，用来做筛选条件

实例1：

<pre>
shell//welcome to join us: http://www.wandoujia.com/joindb.wandoujia.jobs.find()
</pre>

实例2：

<pre>
shell//welcome to join us: http://www.wandoujia.com/joindb.wandoujia.jobs.find({"category", "fe" , "level" : 2})
</pre>

那么其实我们日期查询里面都有一些对返回的查询结果需要指定或者过滤掉一些无用的键值，如何处理呢？

实例1 ：

<pre>
shelldb.wandoujia.jobs.find({} , {"category" : 1, "base" : 1})
</pre>

实例2 ：

<pre>
shelldb.wandoujia.jobs.find({} , {"level" : 0})
</pre>

上面这段其实我们看到：

1.  find可以指定第二个参数

2.  可以只返回第二个参数文档里面指定的字段，这里对应的值是 1

3.  剔除查询结果里面的某个键的化，对应的值设置为 0 就可以了

这样的好处其实很明显啦：

1.  减少数据的大小

2.  节省传输的数据量

3.  客户端也能减少解码文档的时间和内存消耗

查询条件

其实我们日常为了做到精确定位，会指定一些查询条件，比如：

1.  `<`

2.  `<=`

3.  `>`

4.  `>=`

5.  `!=`

那在MongoDB里面用什么来表示这些比较操作符呢？

1.  `$lt`

2.  `$lte`

3.  `$gt`

4.  `$gte`

5.  `$ne`

我们直接看一个实例：

<pre>
shell//比如我们找工作有的人只看2级到3级的db.wandoujia.jobs.find({"level" , {"$gte" : 2, "$lte" : 3})
</pre>

这里，我们给find传递了一个内嵌文档，内层的文档的key就是$gte和$lte

实例2：

<pre>
shell//比如我们找工作有的人不看帝都的db.wandoujia.jobs.find({"base" , {"$ne" : "beijing"})
</pre>

这里，`$ne`就代表**不等于**

所以大致的规则：

1.  `$lt`、`$lte`、`$gt`、`$gte`、`$ne`都是以`$`开头，这也验证了我们前面为什么在命名其他的时候不推荐使用 `$`

2.  `$lt`、`$lte`、`$gt`、`$gte`、`$ne`这些一般都在内层文档里面。

管理MogoDB

其实大家看了很多之后，一定比较想自己动手，去实践一下这些操作。

启动

一般都是作为网络服务器来运行的，客户端可以连接到这个服务器上。

命令行

<pre>
shell./mongod
</pre>

我这里并没有指定任何参数，其实可以从

<pre>
shell./mongod -h
</pre>

控制台会打出一堆的帮助命令，还是很多的，我这边只是简单提几个：

<pre>
--dbpath
</pre>

![Python搭配Mongo学习心得，爬取知乎用户信息完整教程（干货附源码）](http://p1.pstatp.com/large/4705000335488f71f7b5)

可以指定数据目录，默认都是`/data/db`(根目录下的)，每一个mongod实例都需要独立的数据目录。而且当mongod启动的时候，数据里面里面都创建一个mongod.lock的文件，防止其他mongod进程来使用这个数据目录。

感兴趣的化，大家可以自己打开对应的数据目录看看。

<pre>
--logpath 和 --logappend
</pre>

![Python搭配Mongo学习心得，爬取知乎用户信息完整教程（干货附源码）](http://p3.pstatp.com/large/47010003995ac89e92de)

可以指定日志输出的路径，而且最好配合logappend，大多数情况下，我们还是希望保留原来的日志，做加法，而不是覆盖。

<pre>
-f可以指定某个配置文件来加载命令
</pre>

那配置文件的书写有没有什么要求呢？

<pre>
shell# config by yaochun 2013-08-07 pm 07:10logpath = mongodb.log
</pre>

* 一般都是#开头的注释

* 注意大小写

当然里面还有很多其他有用的设置，比如：

* port

* jsonp

* ipv6

* noauth

* rest

* httpinterface

等等，有需求的可以直接去看 `-h` 里面的说明。

MongoDB客户端

服务器启动后，我们需要一个客户端来操作，那么这个客户端是什么呢？

![Python搭配Mongo学习心得，爬取知乎用户信息完整教程（干货附源码）](http://p1.pstatp.com/large/470000039ebd7e13aee3)

看图上，我们在命令行输入了以下命令：

<pre>
shell./mongo
</pre>

它就是MongoDB shell，也是一个js shell，可以完成与MongoDB实例的交互

注释：其实如果你只是想体验js shell的化，可以输入：

<pre>
shell./mongo --nodb
</pre>

这样的化，就不会连接数据库。

它默认会自动连接到服务器的test数据库，并把这个数据库连接赋值给全局的db变量

如图：

![Python搭配Mongo学习心得，爬取知乎用户信息完整教程（干货附源码）](http://p3.pstatp.com/large/470700018caaed66db4b)

当然如果你希望有帮助文档来看看里面到底有什么命令，可以输入：

<pre>
shellhelp
</pre>

如图：

![Python搭配Mongo学习心得，爬取知乎用户信息完整教程（干货附源码）](http://p9.pstatp.com/large/4705000335495d5f9bf4)

一般常用的：

<pre>
show dbs
</pre>

返回当前所有的数据库名称

如图：

![Python搭配Mongo学习心得，爬取知乎用户信息完整教程（干货附源码）](http://p1.pstatp.com/large/4704000354b866f73893)

<pre>
show collections
</pre>

返回当前数据库里面的所有集合（注意：里面包含`system.*` 这个系统的集合）

<pre>
use wandoujia
</pre>

比如我现在默认进去在test这个数据库，我现在要切换到wandoujia这个数据库

如图：db.fe

这样就能访问上面进入的wandoujia这个数据库的fe集合。

shell执行插入

<pre>
shelluse wandoujiadb.fe.insert({ "name" : "yourname" })
</pre>

这样wandoujia这个数据库的fe集合里面就多了一个文档

shell执行查询

<pre>
shelldb.fe.find()
</pre>

会返回包含刚才插入的那个文档的集合。

shell执行更新

<pre>
shelldb.fe.update( { "name" : "yourname" }, { "name" : "yourname", "recommender" : "yaochun" })
</pre>

update至少接受两个参数，第一个是限定条件对应的文档，第二个是新的文档。

你测试后会发现，其实这个更新就是第二个新文档直接覆盖第一个，当然你可以先定义一个变量，这样update的时候，去修改那个变量，然后传递给update就不需要这样写了。

shell执行删除

<pre>
shelldb.fe.remove({ "recommender" : "yaochun" })
</pre>

强大的聚合工具

其实简单地讲：计算一些集合里面文档的个数

count

返回某个集合文档的个数

<pre>
shell//比如现在wandoujia一共的员工数目db.wandoujia.staff.count()
</pre>

那比如我就像知道fe-team里面的人员个数呢？

<pre>
shell//比如现在wandoujia一共的员工数目db.wandoujia.staff.count({ "category" : "fe" })
</pre>

以上内容是我最近使用MongoDB的一些心得，如果有不正确之处，还希望大家多多指点，如果您有相关的使用经验，欢迎在下面的评论中与我们一起分享。  

---

# **知乎用户信息爬取的思路**

首先我们应该找到一个账号，这个账号被关注的人和关注的人都相对比较多的，就是下图中金字塔顶端的人，然后通过爬取这个账号的信息后，再爬取他关注的人和被关注的人的账号信息，然后爬取被关注人的账号信息和被关注信息的关注列表，爬取这些用户的信息，通过这种递归的方式从而爬取整个知乎的所有的账户信息。整个过程通过下面两个图表示：

![Python搭配Mongo学习心得，爬取知乎用户信息完整教程（干货附源码）](http://p1.pstatp.com/large/46fa00028c3b14f1c1c6)

￼

![Python搭配Mongo学习心得，爬取知乎用户信息完整教程（干货附源码）](http://p1.pstatp.com/large/46fa00028c3cf16e2987)

￼

爬虫分析过程

这里我们找的账号地址是：https://www.zhihu.com/people/excited-vczh/answers

我们抓取的大V账号的主要信息是：

![Python搭配Mongo学习心得，爬取知乎用户信息完整教程（干货附源码）](http://p3.pstatp.com/large/46ff00000d1efe99e26f)

￼

其次我们要获取这个账号的关注列表和被关注列表

![Python搭配Mongo学习心得，爬取知乎用户信息完整教程（干货附源码）](http://p3.pstatp.com/large/46fa00028c33bc367ff8)

￼

这里我们需要通过抓包分析如果获取这些列表的信息以及用户的个人信息内容

当我们查看他关注人的列表的时候我们可以看到他请求了如下图中的地址，并且我们可以看到返回去的结果是一个json数据，而这里就存着一页关乎的用户信息。

![Python搭配Mongo学习心得，爬取知乎用户信息完整教程（干货附源码）](http://p1.pstatp.com/large/46ff00000d1fd43955b0)

￼

![Python搭配Mongo学习心得，爬取知乎用户信息完整教程（干货附源码）](http://p3.pstatp.com/large/46f9000293e4090132b6)

￼

![Python搭配Mongo学习心得，爬取知乎用户信息完整教程（干货附源码）](http://p3.pstatp.com/large/46fb000276637a16c1e0)

￼

上面虽然可以获取单个用户的个人信息，但是不是特别完整，这个时候我们获取一个人的完整信息地址是当我们将鼠标放到用户名字上面的时候，可以看到发送了一个请求：

![Python搭配Mongo学习心得，爬取知乎用户信息完整教程（干货附源码）](http://p3.pstatp.com/large/46fc00024e4b2c40e145)

￼

我们可以看这个地址的返回结果可以知道，这个地址请求获取的是用户的详细信息：

![Python搭配Mongo学习心得，爬取知乎用户信息完整教程（干货附源码）](http://p9.pstatp.com/large/46fb0002766879dc50fa)

￼

通过上面的分析我们知道了以下两个地址：
```
获取用户关注列表的地址：https://www.zhihu.com/api/v4/members/excited-vczh/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=0&limit=20
```
```
获取单个用户详细信息的地址：https://www.zhihu.com/api/v4/members/excited-vczh?include=locations%2Cemployments%2Cgender%2Ceducations%2Cbusiness%2Cvoteup_count%2Cthanked_Count%2Cfollower_count%2Cfollowing_count%2Ccover_url%2Cfollowing_topic_count%2Cfollowing_question_count%2Cfollowing_favlists_count%2Cfollowing_columns_count%2Cavatar_hue%2Canswer_count%2Carticles_count%2Cpins_count%2Cquestion_count%2Ccolumns_count%2Ccommercial_question_count%2Cfavorite_count%2Cfavorited_count%2Clogs_count%2Cmarked_answers_count%2Cmarked_answers_text%2Cmessage_thread_token%2Caccount_status%2Cis_active%2Cis_bind_phone%2Cis_force_renamed%2Cis_bind_sina%2Cis_privacy_protected%2Csina_weibo_url%2Csina_weibo_name%2Cshow_sina_weibo%2Cis_blocking%2Cis_blocked%2Cis_following%2Cis_followed%2Cmutual_followees_count%2Cvote_to_count%2Cvote_from_count%2Cthank_to_count%2Cthank_from_count%2Cthanked_count%2Cdescription%2Chosted_live_count%2Cparticipated_live_count%2Callow_message%2Cindustry_category%2Corg_name%2Corg_homepage%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics
```

这里我们可以从请求的这两个地址里发现一个问题，关于用户信息里的url_token其实就是获取单个用户详细信息的一个凭证也是请求的一个重要参数，并且当我们点开关注人的的链接时发现请求的地址的唯一标识也是这个url_token

![Python搭配Mongo学习心得，爬取知乎用户信息完整教程（干货附源码）](http://p9.pstatp.com/large/46fd0002311d58afd2bc)

￼

![Python搭配Mongo学习心得，爬取知乎用户信息完整教程（干货附源码）](http://p3.pstatp.com/large/46f9000293e639410983)

￼

创建项目进行再次分析

通过命令创建项目

scrapy startproject zhihu_user

cd zhihu_user

scrapy genspider zhihu www.zhihu.com

直接通过scrapy crawl zhihu启动爬虫会看到如下错误：

![Python搭配Mongo学习心得，爬取知乎用户信息完整教程（干货附源码）](http://p1.pstatp.com/large/46fc00024e4f3f7a94c7)

￼

这个问题其实是爬取网站的时候经常碰到的问题，大家以后见多了就知道是怎么回事了，是请求头的问题，应该在请求头中加User-Agent,在settings配置文件中有关于请求头的配置默认是被注释的，我们可以打开，并且加上User-Agent,如下：

![Python搭配Mongo学习心得，爬取知乎用户信息完整教程（干货附源码）](http://p3.pstatp.com/large/46fa00028c3e6b898fdf)

￼

关于如何获取User-Agent，可以在抓包的请求头中看到也可以在谷歌浏览里输入：chrome://version/ 查看

这样我们就可以正常通过代码访问到知乎了

然后我们可以改写第一次的请求，这个我们前面的scrapy文章关于spiders的时候已经说过如何改写start_request，我们让第一次请求分别请求获取用户列表以及获取用户信息

![Python搭配Mongo学习心得，爬取知乎用户信息完整教程（干货附源码）](http://p3.pstatp.com/large/46fa00028c3f65afbddd)

￼

这个时候我们再次启动爬虫

![Python搭配Mongo学习心得，爬取知乎用户信息完整教程（干货附源码）](http://p1.pstatp.com/large/46ff00000d226184395e)

￼

我们会看到是一个401错误，而解决的方法其实还是请求头的问题，从这里我们也可以看出请求头中包含的很多信息都会影响我们爬取这个网站的信息，所以当我们很多时候直接请求网站都无法访问的时候就可以去看看请求头，看看是不是请求头的哪些信息导致了请求的结果，而这里则是因为如下图所示的参数：

![Python搭配Mongo学习心得，爬取知乎用户信息完整教程（干货附源码）](http://p3.pstatp.com/large/46fd00023120765275a2)

￼

所以我们需要把这个参数同样添加到请求头中：

![Python搭配Mongo学习心得，爬取知乎用户信息完整教程（干货附源码）](http://p3.pstatp.com/large/46f9000293e7fdc3a5bc)

￼

然后重新启动爬虫，这个时候我们已经可以获取到正常的内容。

---

---

下面是代码的实现，完整代码在：

https://github.com/pythonsite/spider

---

items中的代码主要是我们要爬取的字段的定义

```
class UserItem(scrapy.Item): id = Field()name = Field()account_status = Field()allow_message= Field()answer_count = Field()articles_count = Field()avatar_hue = Field()avatar_url = Field()avatar_url_template = Field() badge = Field() business = Field()employments = Field()columns_count = Field()commercial_question_count = Field()cover_url = Field()description = Field()educations = Field()favorite_count = Field()favorited_count = Field()follower_count = Field()following_columns_count = Field()following_favlists_count = Field()following_question_count = Field()following_topic_count = Field()gender = Field()headline = Field()hosted_live_count = Field()is_active = Field()is_bind_sina = Field()is_blocked = Field()is_advertiser = Field()is_blocking = Field()is_followed = Field()is_following = Field()is_force_renamed = Field()is_privacy_protected = Field()locations = Field()is_org = Field()type = Field()url = Field()url_token = Field()user_type = Field()logs_count = Field() marked_answers_count = Field() marked_answers_text = Field()message_thread_token = Field()mutual_followees_count = Field()participated_live_count = Field()pins_count = Field()question_count = Field()show_sina_weibo = Field()thank_from_count = Field()thank_to_count = Field()thanked_count = Field()type = Field()vote_from_count = Field()vote_to_count = Field()voteup_count = Field()
```

这些字段的是在用户详细信息里找到的，如下图所示，这里一共有58个字段，可以详细研究每个字段代表的意思：

![Python搭配Mongo学习心得，爬取知乎用户信息完整教程（干货附源码）](http://p1.pstatp.com/large/46fa00028d570a536afd)

￼

关于spiders中爬虫文件zhihu.py中的主要代码

这段代码是非常重要的，主要的处理逻辑其实都是在这里

```
class ZhihuSpider(scrapy.Spider):name = "zhihu"allowed_domains = ["www.zhihu.com"]start_urls = ['http://www.zhihu.com/'] #这里定义一个start_user存储我们找的大V账号start_user = "excited-vczh"#这里把查询的参数单独存储为user_query,user_url存储的为查询用户信息的url地址user_url = "https://www.zhihu.com/api/v4/members/{user}?include={include}"user_query = "locations,employments,gender,educations,business,voteup_count,thanked_Count,follower_count,following_count,cover_url,following_topic_count,following_question_count,following_favlists_count,following_columns_count,avatar_hue,answer_count,articles_count,pins_count,question_count,columns_count,commercial_question_count,favorite_count,favorited_count,logs_count,marked_answers_count,marked_answers_text,message_thread_token,account_status,is_active,is_bind_phone,is_force_renamed,is_bind_sina,is_privacy_protected,sina_weibo_url,sina_weibo_name,show_sina_weibo,is_blocking,is_blocked,is_following,is_followed,mutual_followees_count,vote_to_count,vote_from_count,thank_to_count,thank_from_count,thanked_count,description,hosted_live_count,participated_live_count,allow_message,industry_category,org_name,org_homepage,badge[?(type=best_answerer)].topics"#follows_url存储的为关注列表的url地址,fllows_query存储的为查询参数。这里涉及到offset和limit是关于翻页的参数，0，20表示第一页follows_url = "https://www.zhihu.com/api/v4/members/{user}/followees?include={include}&offset={offset}&limit={limit}"follows_query = "data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics"#followers_url是获取粉丝列表信息的url地址，followers_query存储的为查询参数。followers_url = "https://www.zhihu.com/api/v4/members/{user}/followers?include={include}&offset={offset}&limit={limit}"followers_query = "data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics"def start_requests(self): '''这里重写了start_requests方法，分别请求了用户查询的url和关注列表的查询以及粉丝列表信息查询:return:'''yield Request(self.user_url.format(user=self.start_user,include=self.user_query),callback=self.parse_user) yield Request(self.follows_url.format(user=self.start_user,include=self.follows_query,offset=0,limit=20),callback=self.parse_follows) yield Request(self.followers_url.format(user=self.start_user,include=self.followers_query,offset=0,limit=20),callback=self.parse_followers) def parse_user(self, response): '''因为返回的是json格式的数据，所以这里直接通过json.loads获取结果:param response::return:'''result = json.loads(response.text)item = UserItem() #这里循环判断获取的字段是否在自己定义的字段中，然后进行赋值for field in item.fields:if field in result.keys():item[field] = result.get(field) #这里在返回item的同时返回Request请求，继续递归拿关注用户信息的用户获取他们的关注列表yield item yield Request(self.follows_url.format(user = result.get("url_token"),include=self.follows_query,offset=0,limit=20),callback=self.parse_follows) yield Request(self.followers_url.format(user = result.get("url_token"),include=self.followers_query,offset=0,limit=20),callback=self.parse_followers) def parse_follows(self, response): '''用户关注列表的解析，这里返回的也是json数据 这里有两个字段data和page，其中page是分页信息:param response::return:'''results = json.loads(response.text) if 'data' in results.keys(): for result in results.get('data'): yield Request(self.user_url.format(user = result.get("url_token"),include=self.user_query),callback=self.parse_user) #这里判断page是否存在并且判断page里的参数is_end判断是否为False，如果为False表示不是最后一页，否则则是最后一页if 'page' in results.keys() and results.get('is_end') == False:next_page = results.get('paging').get("next") #获取下一页的地址然后通过yield继续返回Request请求，继续请求自己再次获取下页中的信息yield Request(next_page,self.parse_follows) def parse_followers(self, response): '''这里其实和关乎列表的处理方法是一样的用户粉丝列表的解析，这里返回的也是json数据 这里有两个字段data和page，其中page是分页信息:param response::return:'''results = json.loads(response.text) if 'data' in results.keys(): for result in results.get('data'): yield Request(self.user_url.format(user = result.get("url_token"),include=self.user_query),callback=self.parse_user) #这里判断page是否存在并且判断page里的参数is_end判断是否为False，如果为False表示不是最后一页，否则则是最后一页if 'page' in results.keys() and results.get('is_end') == False:next_page = results.get('paging').get("next") #获取下一页的地址然后通过yield继续返回Request请求，继续请求自己再次获取下页中的信息yield Request(next_page,self.parse_followers)
```
上述的代码的主要逻辑用下图分析表示：

![Python搭配Mongo学习心得，爬取知乎用户信息完整教程（干货附源码）](http://p3.pstatp.com/large/46fc00024f923757b17a)

￼

关于上图的一个简单描述：

1. 当重写start_requests，一会有三个yield，分别的回调函数调用了parse_user,parse_follows,parse_followers，这是第一次会分别获取我们所选取的大V的信息以及关注列表信息和粉丝列表信息

2. 而parse分别会再次回调parse_follows和parse_followers信息，分别递归获取每个用户的关注列表信息和分析列表信息

3. parse_follows获取关注列表里的每个用户的信息回调了parse_user，并进行翻页获取回调了自己parse_follows

4. parse_followers获取粉丝列表里的每个用户的信息回调了parse_user，并进行翻页获取回调了自己parse_followers

通过上面的步骤实现所有用户信息的爬取，最后是关于数据的存储

关于数据存储到mongodb

这里主要是item中的数据存储到mongodb数据库中，这里主要的一个用法是就是插入的时候进行了一个去重检测

```
class MongoPipeline(object):def __init__(self, mongo_uri, mongo_db): self.mongo_uri = mongo_uri self.mongo_db = mongo_db@classmethod def from_crawler(cls, crawler): return cls(mongo_uri=crawler.settings.get('MONGO_URI'),mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')) def open_spider(self, spider): self.client = pymongo.MongoClient(self.mongo_uri) self.db = self.client[self.mongo_db] def close_spider(self, spider): self.client.close() def process_item(self, item, spider): #这里通过mongodb进行了一个去重的操作，每次更新插入数据之前都会进行查询，判断要插入的url_token是否已经存在，如果不存在再进行数据插入，否则放弃数据self.db['user'].update({'url_token':item["url_token"]},{'$set':item},True) return item
```



以上是全部代码，只是善于分享，不足之处请包涵！爬虫基本的原理就是，获取源码，进而获取网页内容。一般来说，只要你给一个入口，通过分析，可以找到无限个其他相关的你需要的资源，进而进行爬取。



我也写了很多其他的非常简单的入门级的爬虫详细教程，关注后，点击我的头像，就可以查看到。

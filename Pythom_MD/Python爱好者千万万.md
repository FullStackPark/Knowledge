# Python爱好者千万万，此文应运而生！最长最全的资料型博文！

<!---->python凡梦 2018-04-09 16:11:56

本文的分享主要围绕以下几个方面：

1. Python能做什么?(常见应用场景介绍)

2. 如何学习Python？

3. Python语法基础实战

4. Python面向对象编程实战

**一、Python能做什么?**

一种编程语言往往可以应用于多方面，有些方面比较常用，有些方面极为常用。首先，利用Python可以进行简单脚本编程，

![Python爱好者千万万，此文应运而生！最长最全的资料型博文！](http://p1.pstatp.com/large/pgc-image/1523261451491c89c9084bf)

比如使用Python编写2048小游戏或12306的自动抢票软件。其次，可以使用Python进行系统编程，开发系统应用。第三点，Python一个较为常用的功能就是开发网络爬虫。网络爬虫的用途是进行数据采集，也就是将互联网中的数据采集过来。网络爬虫的难点其实并不在于爬虫本身，由于网站方为了避免被爬取回采取各种各样的反爬虫措施，而如果想要继续从网站爬取数据就需要解决这些反爬虫措施，所以网络爬虫的难点在于反爬的攻克和处理。第四点，Python极常用于WEB开发，可以借助Python开发WEB站点，比如个人博客、在线教育网站以及论坛等。第五点，在运维方面，Python可以用于自动化运维，可以通过写Python脚本实现对于服务器集群进行自动化管理。第六点，Python可以用于网络编程，比如Socket编程等。第七点，Python极常用的一个方向就是数据挖掘、机器学习等大数据与人工智能领域方向的程序开发，比如在人工智能领域，使用Python就可以很容易地实现算法模型，并且借助Python可以很容易地处理相应的数据。  

![Python爱好者千万万，此文应运而生！最长最全的资料型博文！](http://p3.pstatp.com/large/pgc-image/1523260593269c9622138fc)

![Python爱好者千万万，此文应运而生！最长最全的资料型博文！](http://p3.pstatp.com/large/pgc-image/1523260738422255c0faa79)

![Python爱好者千万万，此文应运而生！最长最全的资料型博文！](http://p3.pstatp.com/large/pgc-image/15232607522477c4359b0eb)

![Python爱好者千万万，此文应运而生！最长最全的资料型博文！](http://p1.pstatp.com/large/pgc-image/1523260762954dab67c120d)

![Python爱好者千万万，此文应运而生！最长最全的资料型博文！](http://p3.pstatp.com/large/pgc-image/1523260778754c8d7baaead)

**三、Python语法基础实战**

在Python语法的基础实战这部分将与大家分享数据类型、控制结构、函数与模块、文件操作与数据库操作以及异常处理等内容。

**Python基础知识入门**

在Python中输出直接使用print()函数，如果在Python文件中重复四次print("Hello Python")，那么输出时就是四次“Hello Python”。如果想让某一行代码不起作用，可以使用注释。在Python中有两种比较常见的注释方案，第一种是单行注释，在行首加“#”，这样就会注释掉这一行代码；第二种是多行注释，多行注释一般使用“'''”或“"""”(三引号)实现，直接将需要注释的代码段的首部和尾部加上三个引号即可。

**数据类型**

在学习任何一门编程语言时，都需要了解这门编程语言有哪些数据类型。在Python中，常见的数据类型有数、字符串、列表、元祖、集合以及字典等。

![Python爱好者千万万，此文应运而生！最长最全的资料型博文！](http://p3.pstatp.com/large/pgc-image/1523260821271fdf8477da8)

![Python爱好者千万万，此文应运而生！最长最全的资料型博文！](http://p3.pstatp.com/large/pgc-image/1523260842920cc303e4517)

![Python爱好者千万万，此文应运而生！最长最全的资料型博文！](http://p3.pstatp.com/large/pgc-image/15232608546887388a9f26f)

![Python爱好者千万万，此文应运而生！最长最全的资料型博文！](http://p3.pstatp.com/large/pgc-image/15232608700166f3ba26025)

![Python爱好者千万万，此文应运而生！最长最全的资料型博文！](http://p3.pstatp.com/large/pgc-image/15232608844211fa301cd63)

```
 a=1000

 b=1

 if(a>19 and a<30):

 print(a)

 if(b<9):

 print(b)

 elif(a>9 and a<=19):

 print("a>9 and a<=19")

 elif(a<9):

 print("a<9")

 else:

 print("gsdajk")
```

![Python爱好者千万万，此文应运而生！最长最全的资料型博文！](http://p3.pstatp.com/large/pgc-image/152326091137448338f8893)

![Python爱好者千万万，此文应运而生！最长最全的资料型博文！](http://p1.pstatp.com/large/pgc-image/15232609220944a7054f21f)

![Python爱好者千万万，此文应运而生！最长最全的资料型博文！](http://p3.pstatp.com/large/pgc-image/15232609372346690767bfe)

![Python爱好者千万万，此文应运而生！最长最全的资料型博文！](http://p3.pstatp.com/large/pgc-image/1523260949596349c193cac)

![Python爱好者千万万，此文应运而生！最长最全的资料型博文！](http://p3.pstatp.com/large/pgc-image/152326096035815980f72b1)

![Python爱好者千万万，此文应运而生！最长最全的资料型博文！](http://p3.pstatp.com/large/pgc-image/1523260970428262d6938c3)

![Python爱好者千万万，此文应运而生！最长最全的资料型博文！](http://p3.pstatp.com/large/pgc-image/15232609830539acefd9ff9)

![Python爱好者千万万，此文应运而生！最长最全的资料型博文！](http://p9.pstatp.com/large/pgc-image/1523260994131f033502dae)

![Python爱好者千万万，此文应运而生！最长最全的资料型博文！](http://p3.pstatp.com/large/pgc-image/15232610044528e2007b8bc)

![Python爱好者千万万，此文应运而生！最长最全的资料型博文！](http://p1.pstatp.com/large/pgc-image/152326101221774c45634fd)

![Python爱好者千万万，此文应运而生！最长最全的资料型博文！](http://p1.pstatp.com/large/pgc-image/1523261023698e78241b162)

![Python爱好者千万万，此文应运而生！最长最全的资料型博文！](http://p9.pstatp.com/large/pgc-image/1523261038263538fd666c4)

![Python爱好者千万万，此文应运而生！最长最全的资料型博文！](http://p3.pstatp.com/large/pgc-image/15232610511404924797e6f)

![Python爱好者千万万，此文应运而生！最长最全的资料型博文！](http://p3.pstatp.com/large/pgc-image/1523261061407171727e941)

![Python爱好者千万万，此文应运而生！最长最全的资料型博文！](http://p1.pstatp.com/large/pgc-image/15232610677001955a674b3)

![Python爱好者千万万，此文应运而生！最长最全的资料型博文！](http://p9.pstatp.com/large/pgc-image/1523261085609679a342105)

![Python爱好者千万万，此文应运而生！最长最全的资料型博文！](http://p3.pstatp.com/large/pgc-image/1523261099526e10c5d1afa)

![Python爱好者千万万，此文应运而生！最长最全的资料型博文！](http://p3.pstatp.com/large/pgc-image/15232611075145d47bf0469)

![Python爱好者千万万，此文应运而生！最长最全的资料型博文！](http://p3.pstatp.com/large/pgc-image/1523261116556f3779501b5)

![Python爱好者千万万，此文应运而生！最长最全的资料型博文！](http://p1.pstatp.com/large/pgc-image/15232611285918eaa2ca76c)

![Python爱好者千万万，此文应运而生！最长最全的资料型博文！](http://p1.pstatp.com/large/pgc-image/1523261139630e043743881)

![Python爱好者千万万，此文应运而生！最长最全的资料型博文！](http://p1.pstatp.com/large/pgc-image/1523261156449062ca5a65b)

![Python爱好者千万万，此文应运而生！最长最全的资料型博文！](http://p9.pstatp.com/large/pgc-image/15232611663812f0ed61c24)

![Python爱好者千万万，此文应运而生！最长最全的资料型博文！](http://p3.pstatp.com/large/pgc-image/152326117546215b9f59437)

使用Python进行数据库的操作的前提是需要一个MySQL数据库，至于MySQL数据库的安装和配置不是本文所关心的对象，大家可以自行学习。在拥有了MySQL数据库之后首先应该进行数据库的连接。  

```
 import pymysqlconn=pymysql.connect(host="127.0.0.1",user="root",passwd="root",db="mypydb")#执行sql语句-无返回

 conn.query("INSERT INTO mytb(title,keywd) VALUES('new title','23456')")

 conn.commit()#执行SQL语句-有返回

 cs=conn.cursor()

 cs.execute("select * from mytb")

 for i in cs:

 print("当前是第"+str(cs.rownumber)+"行")

 print("标题是："+i[0])

 print("关键词是："+i[1])

 conn.close()
```

![Python爱好者千万万，此文应运而生！最长最全的资料型博文！](http://p1.pstatp.com/large/pgc-image/15232612186839f7373e0c6)

![Python爱好者千万万，此文应运而生！最长最全的资料型博文！](http://p3.pstatp.com/large/pgc-image/1523261225793f4f89f877b)

![Python爱好者千万万，此文应运而生！最长最全的资料型博文！](http://p9.pstatp.com/large/pgc-image/15232612351892d91301649)

![Python爱好者千万万，此文应运而生！最长最全的资料型博文！](http://p1.pstatp.com/large/pgc-image/15232612430246a5cb9e0d6)

![Python爱好者千万万，此文应运而生！最长最全的资料型博文！](http://p3.pstatp.com/large/pgc-image/1523261249523f42e0224f4)

![Python爱好者千万万，此文应运而生！最长最全的资料型博文！](http://p1.pstatp.com/large/pgc-image/1523261259550bd016f249b)

![Python爱好者千万万，此文应运而生！最长最全的资料型博文！](http://p1.pstatp.com/large/pgc-image/152326127184693705589af)

![Python爱好者千万万，此文应运而生！最长最全的资料型博文！](http://p3.pstatp.com/large/pgc-image/1523261279224c4108ac2a3)

![Python爱好者千万万，此文应运而生！最长最全的资料型博文！](http://p3.pstatp.com/large/pgc-image/15232612905049ee7789ec7)

![Python爱好者千万万，此文应运而生！最长最全的资料型博文！](http://p1.pstatp.com/large/pgc-image/152326129717825d08e0315)

![Python爱好者千万万，此文应运而生！最长最全的资料型博文！](http://p3.pstatp.com/large/pgc-image/15232613069603b57ec0d42)

![Python爱好者千万万，此文应运而生！最长最全的资料型博文！](http://p3.pstatp.com/large/pgc-image/1523261316614057a3cf7fb)

![Python爱好者千万万，此文应运而生！最长最全的资料型博文！](http://p1.pstatp.com/large/pgc-image/1523261327817e44ce9caeb)

![Python爱好者千万万，此文应运而生！最长最全的资料型博文！](http://p1.pstatp.com/large/pgc-image/152326133618180da762f99)

![Python爱好者千万万，此文应运而生！最长最全的资料型博文！](http://p3.pstatp.com/large/pgc-image/1523261348261430918d79c)

![Python爱好者千万万，此文应运而生！最长最全的资料型博文！](http://p3.pstatp.com/large/pgc-image/15232613586069cc285173f)

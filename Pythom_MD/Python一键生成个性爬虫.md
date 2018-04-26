# Python一键生成个性爬虫，想爬哪就点哪！

![Python一键生成个性爬虫，想爬哪就点哪！](http://p1.pstatp.com/large/pgc-image/1523444828387e92ee207da)

![Python一键生成个性爬虫，想爬哪就点哪！](http://p3.pstatp.com/large/pgc-image/1523444838944cfe68ac3ac)

![Python一键生成个性爬虫，想爬哪就点哪！](http://p1.pstatp.com/large/pgc-image/152344579806403e534321d)

首先，一键安装structure-spider

<pre>
dev@ubuntu:~$ pip install structure-spider
</pre>

scrapy做为主要依赖

![Python一键生成个性爬虫，想爬哪就点哪！](http://p1.pstatp.com/large/pgc-image/15234448940112aecc2db10)

![Python一键生成个性爬虫，想爬哪就点哪！](http://p3.pstatp.com/large/pgc-image/1523444918994fb837f1b69)

![Python一键生成个性爬虫，想爬哪就点哪！](http://p1.pstatp.com/large/pgc-image/1523444958913c5e9b44b4f)

![Python一键生成个性爬虫，想爬哪就点哪！](http://p3.pstatp.com/large/pgc-image/15234455272891b687363a7)

![Python一键生成个性爬虫，想爬哪就点哪！](http://p1.pstatp.com/large/pgc-image/1523445569731982e0318e3)

![Python一键生成个性爬虫，想爬哪就点哪！](http://p3.pstatp.com/large/pgc-image/1523445578161f3da71f439)

![Python一键生成个性爬虫，想爬哪就点哪！](http://p1.pstatp.com/large/pgc-image/15234455920533fdb64ccd7)

![Python一键生成个性爬虫，想爬哪就点哪！](http://p3.pstatp.com/large/pgc-image/1523445605122911e06fbbc)

![Python一键生成个性爬虫，想爬哪就点哪！](http://p3.pstatp.com/large/pgc-image/152344561693438e5d3bdd4)

![Python一键生成个性爬虫，想爬哪就点哪！](http://p1.pstatp.com/large/pgc-image/1523445622835b9ff59807a)

最后，运行spider

<pre>
dev@ubuntu:~/myapp/myapp$ scrapy crawl zhaopin
</pre>

添加任务

![Python一键生成个性爬虫，想爬哪就点哪！](http://p9.pstatp.com/large/pgc-image/1523445650053d3506bf440)

spider开始运行

![Python一键生成个性爬虫，想爬哪就点哪！](http://p1.pstatp.com/large/pgc-image/1523445673361eec9c7feef)

![Python一键生成个性爬虫，想爬哪就点哪！](http://p3.pstatp.com/large/pgc-image/152344568078267896aee76)

完成！

当然，说完全没有python代码是不可能的。在createspider时，程序已经为我们自动生成两个Py文件

![Python一键生成个性爬虫，想爬哪就点哪！](http://p3.pstatp.com/large/pgc-image/1523445717921099c378fb5)

![Python一键生成个性爬虫，想爬哪就点哪！](http://p3.pstatp.com/large/pgc-image/152344572579502bf11eff5)

在编写比较简单的python爬虫时，以上几步完全够用。当你想使用高级特性时，比如structure-spider的核心特性多请求组合抓取时，还是需要手动编写少量python代码来完成。

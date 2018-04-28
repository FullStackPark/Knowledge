# 最常问的MySQL面试题——每个开发人员都应该知道
![最常问的MySQL面试题——每个开发人员都应该知道](http://p1.pstatp.com/large/pgc-image/15233739387266e266bf100)

根据我的个人经验，在做Web应用程序的面试时，MySQL相关面试题是经常被问到的。同时，小编觉得一篇文章阅读50-60个问题会让读者很疲劳，因此还是一次发6，7个问题，这样大家也能更好的记住，更有耐心看下去，印象也更深刻些。根据这一点，本文首先介绍以下6个最常问的MySQL面试题，我想每个开发人员都应该知道这些。

# MySQL面试题：<br>

**问题1**：char、varchar的区别是什么？

**答**：varchar是变长而char的长度是固定的。

提示：如果你的内容是固定大小的，你会得到更好的性能。

**问题2**: TRUNCATE和DELETE的区别是什么？

**答**：DELETE命令从一个表中删除某一行，或多行，TRUNCATE命令永久地从表中删除每一行。

**问题3**：什么是触发器，MySQL中都有哪些触发器？

**答**：触发器是指一段代码，当触发某个事件时，自动执行这些代码。在MySQL数据库中有如下六种触发器：

```
 Before Insert

 After Insert

 Before Update

 After Update

 Before Delete

 After Delete
```

**问题4**：FLOAT和DOUBLE的区别是什么？

**答**：FLOAT类型数据可以存储至多8位十进制数，并在内存中占4字节。

DOUBLE类型数据可以存储至多18位十进制数，并在内存中占8字节。

**问题5**：如何在MySQL种获取当前日期？

**答**：SELECT CURRENT_DATE();

**问题6**：如何查询第n高的工资？

**答**：SELECT DISTINCT(salary) from employee ORDER BY salary DESC LIMIT n-1,1

是不是觉得意犹未尽，但您是否发现读这篇文章，可能只花了您几分钟时间。比您花半个小时看50到60个问题，但只记住很少问题要强一些。

感谢您阅读全文，希望能够对您的开发或面试有些帮助。

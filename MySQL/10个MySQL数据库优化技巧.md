WEB开发者不光要解决程序的效率问题，对数据库的快速访问和相应也是一个大问题。希望本文能对大家掌握MySQL优化技巧有所帮助。

1. 优化你的MySQL查询缓存

在MySQL服务器上进行查询，可以启用高速查询缓存。让数据库引擎在后台悄悄的处理是提高性能的最有效方法之一。当同一个查询被执行多次时，如果结果是从缓存中提取，那是相当快的。

但主要的问题是，它是那么容易被隐藏起来以至于我们大多数程序员会忽略它。在有些处理任务中，我们实际上是可以阻止查询缓存工作的。

// query cache does NOT work

$r = mysql_query("SELECT username FROM user WHERE signup_date >= CURDATE()");

// query cache works!

$today = date("Y-m-d");

$r = mysql_query("SELECT username FROM user WHERE signup_date >= '$today'");

// query cache does NOT work

$r = mysql_query("SELECT username FROM user WHERE signup_date >= CURDATE()");

// query cache works!

$today = date("Y-m-d");

$r = mysql_query("SELECT username FROM user WHERE signup_date >= '$today'");

2. 用EXPLAIN使你的SELECT查询更加清晰

使用EXPLAIN关键字是另一个MySQL优化技巧，可以让你了解MySQL正在进行什么样的查询操作，这可以帮助你发现瓶颈的所在，并显示出查询或表结构在哪里出了问题。

EXPLAIN查询的结果，可以告诉你那些索引正在被引用，表是如何被扫描和排序的等等。

实现一个SELECT查询(最 好是比较复杂的一个，带joins方式的)，在里面添加上你的关键词解释，在这里我们可以使用phpMyAdmin，他会告诉你表中的结果。举例来说，假如当我在执行joins时，正忘记往一个索引中添加列，EXPLAIN能帮助我找到问题的所在。

![10个MySQL数据库优化技巧](http://p3.pstatp.com/large/3e660002cd2bd9ecb0a8)

添加索引到group_id field后

![10个MySQL数据库优化技巧](http://p3.pstatp.com/large/3ec9000091eb91843f4f)

3. 利用LIMIT 1取得唯 一行

有时，当你要查询一张表是，你知道自己只需要看一行。你可能会去的一条十分独特的记录，或者只是刚好检查了任何存在的记录数，他们都满足了你的WHERE子句。

在这种情况下，增加一个LIMIT 1会令你的查询更加有效。这样数据库引擎发现只有1后将停止扫描，而不是去扫描整个表或索引。

// do I have any users from Alabama?

// what NOT to do:

$r = mysql_query("SELECT * FROM user WHERE state = 'Alabama'");

if (mysql_num_rows($r) > 0) {

// ...

}

// much better:

$r = mysql_query("SELECT 1 FROM user WHERE state = 'Alabama' LIMIT 1");

if (mysql_num_rows($r) > 0) {

// ...

}

4. 索引中的检索字段

索引不仅是主键或唯 一键。如果你想搜索表中的任何列，你应该一直指向索引。

![10个MySQL数据库优化技巧](http://p9.pstatp.com/large/3ec80000924beed06edb)

5. 保 证连接的索引是相同的类型

如果应用程序中包含多个连接查询，你需要确保你链接的列在两边的表上都被索引。这会影响MySQL如何优化内部联接操作。

此外，加入的列，必须是同一类型。例如，你加入一个DECIMAL列，而同时加入另一个表中的int列，MySQL将无法使用其中至少一个指标。即使字符编码必须同为字符串类型。

// looking for companies in my state

$r = mysql_query("SELECT company_name FROM users

LEFT JOIN companies ON (users.state = companies.state)

WHERE users.id = $user_id");

// both state columns should be indexed

// and they both should be the same type and character encoding

// or MySQL might do full table scans

6. 不要使用BY RAND()命令

这是一个令很多新手程序员会掉进去的陷阱。你可能不知不觉中制造了一个可怕的平静。这个陷阱在你是用BY RAND()命令时就开始创建了。

如果您真的需要随机显示你的结果，有很多更好的途径去实现。诚然这需要写更多的代码，但是能避免性能瓶颈的出现。问题在于，MySQL可能会为表中每一个独立的行执行BY RAND()命令(这会消耗处理器的处理能力)，然后给你仅仅返回一行。

// what NOT to do:

$r = mysql_query("SELECT username FROM user ORDER BY RAND() LIMIT 1");

// much better:

$r = mysql_query("SELECT count(\*) FROM user");

$d = mysql_fetch_row($r);

$rand = mt_rand(0,$d[0] - 1);

$r = mysql_query("SELECT username FROM user LIMIT $rand, 1");

7. 尽量避免SELECT \*命令

从表中读取越多的数据，查询会变得更慢。他增加了磁盘需要操作的时间，还是在数据库服务器与WEB服务器是独立分开的情况下。你将会经历非常漫长的网络延迟，仅仅是因为数据不必要的在服务器之间传输。

始终指 定你需要的列，这是一个非常良好的习惯。

// not preferred

$r = mysql_query("SELECT * FROM user WHERE user_id = 1");

$d = mysql_fetch_assoc($r);

echo "Welcome {$d['username']}";

// better:

$r = mysql_query("SELECT username FROM user WHERE user_id = 1");

$d = mysql_fetch_assoc($r);

echo "Welcome {$d['username']}";

// the differences are more significant with bigger result sets

8. 从PROCEDURE ANALYSE()中获得建议

PROCEDURE ANALYSE()可让MySQL的柱结构分析和表中的实际数据来给你一些建议。如果你的表中已经存在实际数据了，能为你的重大决策服务。

![10个MySQL数据库优化技巧](http://p3.pstatp.com/large/3eb200036ec29451f21b)

9. 准备好的语句

准备好的语句，可以从性能优化和安全两方面对大家有所帮助。

准备好的语句在过滤已经绑定的变量默认情况下，能给应用程序以有效的保护，防止SQL注入攻击。当然你也可以手动过滤，不过由于大多数程序员健忘的性格，很难达到效果。

// create a prepared statement

if ($stmt = $mysqli->prepare("SELECT username FROM user WHERE state=?")) {

// bind parameters

$stmt->bind_param("s", $state);

// execute

$stmt->execute();

// bind result variables

$stmt->bind_result($username);

// fetch value

$stmt->fetch();

printf("%s is from %s
", $username, $state);

$stmt->close();

}

10. 将IP地址存储为无符号整型

许多程序员在创建一个VARCHAR(15)时并没有意识到他们可以将IP地址以整数形式来存储。当你有一个INT类型时，你只占用4个字节的空间，这是一个固定大小的领域。

你必须确定你所操作的列是一个UNSIGNED INT类型的,因为IP地址将使用32位unsigned integer。

$r = "UPDATE users SET ip = INET_ATON('{$\_SERVER['REMOTE_ADDR']}') WHERE user_id = $user_id";

十大MySQL优化技巧就介绍到这里。

资料来源：厚学网　　 https://www.houxue.com/news/387960.html

对于想学习相关课程的朋友来说，可以到厚学网结合自身实际情况找一家专业的培训机构来进行系统有效的学习，目前厚学网共计入驻了多家国学领域的知名培训机构，这里可以让让客户了解全新全面的课程信息及真实的用户评价，让客户能够更放心，省心的选择到想学的课程。

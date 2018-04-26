一、命令行连接数据库

Windows操作系统进入CMD命令行，进入mysql.exe所在目录，运行命令

mysql.exe -h主机名 -u用户名 -p密码

注意：参数名与值之间没有空格 ， 如：-h127.0.0.1

二、数据库命令

1. 创建数据库

create database 数据库名;

如：

create database itsource;

2. 切换到指定数据库

use 数据库名;

如：

use itsource;

3. 显示数据库列表

show databases;

4. 显示数据库建立语句

show create database 数据库名;

如：

show create database itsource;

5. 修改数据库

alter database 数据库名 选项;

如：

alter database itsource charset=gbk;

6. 删除数据库

drop database 数据库名;

如：

drop database itsource;

三、数据表命令

1. 创建数据表

create table 数据表名(

字段名1 类型 修饰符,

字段名2 类型 修饰符,

字段名n 类型 修饰符

);

如：

create table news(

id int primary key auto_increment,

title varchar(50),

author varchar(20),

content text

);

2. 查看数据表列表

show tables;

3. 查看数据表结构

desc 数据表名;

例如：

desc news;

4. 查看数据表建表语句

show create table 数据表名;

如：

show create table news;

5. 删除数据表

drop table 数据表名;

如：

drop table news;

6. 修改数据表

alter table 数据表名 选项;

如：

alter table news charset=utf8;

7. 新增字段

alter table 数据表名 add column 字段名 类型 修饰语句 位置

如：

alter table news add column newstime timestamp default current_timestamp after content;

8. 修改字段定义

alter table 数据表名 modify column 字段名 新的定义

如：

alter table news modify column content longtext;

9. 修改字段名及定义

alter table 数据表名 change column 旧字段名 新字段名 新的定义;

10. 删除字段

alter table 数据表名 drop column 字段名;

如：

alter table news drop column title;

四、记录操作命令

1. 新增记录

insert into 数据表名(字段1,字段2,字段n) values(值1,值2,值n);

如：

insert into news(title,author,content) values('新闻标题','作者','新闻详细内容');

注意：值的数量与类型必须与字段列表数量与类型定义一致

2. 查看记录

select 字段列表 from 数据表名 where 条件 order by 字段名 desc limit m,n

如：

select * from news;

select * from news where id=10;

select * from news order by id desc limit 10;

注意：select语句是SQL中最为强大与复杂的查询语句，有七大子句，每段子句都可以省略，如果出现必须在正确的位置顺序上，不可调换先后位置。

3. 修改记录

update 数据表名 set 字段1=值1 and 字段2=值2 where 条件;

如：

update news set title='新的新闻标题' where id=1;

4. 删除记录

delete from 数据表名 where 条件;

如：

delete from news where id=10;

五、其它常用命令

set names gbk

由于CMD命令行只支持系统当前编码，所以一般需要将CMD与MYSQL服务器的交互编码设置为gbk才能正常显示utf8的数据。

![新手入门MYSQL数据库命令大全](http://p1.pstatp.com/large/pgc-image/1523615654368cc8ba699c2)

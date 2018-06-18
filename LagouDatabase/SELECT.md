### 一.简介<br>

Insert是T-sql中常用语句，Insert INTO table(field1,field2,...) values(value1,value2,...)这种形式的在应

用程序开发中必不可少。 

但我们在开发、测试过程中，经常会遇到需要表复制的情况，如将一个table1的数据的部分字段复制到

table2中，或者将整个table1复制到table2中，这时候我们就要使用select into  from和 insert into select 表复制语句了。

### 二.方式1（常用）：insert into select

1、语句形式：

```hljs
Insert into Table2(field1,field2,...) select value1,value2,... from Table1
```

2、要求：

目标表Table2必须存在；

由于目标表Table2已经存在，所以我们除了插入源表Table1的字段外，还可以插入常量；

3、例子：

```hljs
--1.创建测试表 
    create TABLE Table1 
    ( 
        a varchar(10), 
        b varchar(10), 
        c varchar(10), 
        CONSTRAINT [PK_Table1] PRIMARY KEY CLUSTERED 
        ( 
            a ASC 
        ) 
    ) ON [PRIMARY] 
    create TABLE Table2 
    ( 
        a varchar(10), 
        c varchar(10), 
        d int, 
        CONSTRAINT [PK_Table2] PRIMARY KEY CLUSTERED 
        ( 
            a ASC 
        ) 
    ) ON [PRIMARY] 
    GO 
    --2.创建测试数据 
    Insert into Table1 values('赵','asds','90') 
    Insert into Table1 values('钱','asds','100') 
    Insert into Table1 values('孙','asds','80') 
    Insert into Table1 values('李','asds',null) 
    GO 
    select * from Table2 
    --3.INSERT INTO SELECT语句复制表数据 
    Insert into Table2(a, c, d) select a,c,5 from Table1 
    GO 
    --4.显示更新后的结果 
    select * from Table2 
    GO 
    --5.删除测试表 
    drop TABLE Table1 
    drop TABLE Table2
```

也可参考一下sql：

```hljs
INSERT INTO `um_region`(`region_id`,`parent_id`,`name`,`sort`,`type`)
SELECT `region_id`,`parent_id`,`name`,`sort`,`type` FROM `省$`
```

### 三.方式2：select into from

1、语句形式：

```hljs
SELECT vale1, value2 into Table2 from Table1
```

2、要求：

目标表Table2不存在；

因为在插入时会自动创建表Table2，并将Table1中指定字段数据复制到Table2中。

3、例子：

```hljs
--1.创建测试表 
    create TABLE Table1 
    ( 
        a varchar(10), 
        b varchar(10), 
        c varchar(10), 
        CONSTRAINT [PK_Table1] PRIMARY KEY CLUSTERED 
        ( 
            a ASC 
        ) 
    ) ON [PRIMARY] 
    GO 
    --2.创建测试数据 
    Insert into Table1 values('赵','asds','90') 
    Insert into Table1 values('钱','asds','100') 
    Insert into Table1 values('孙','asds','80') 
    Insert into Table1 values('李','asds',null) 
    GO 
    --3.SELECT INTO FROM语句创建表Table2并复制数据 
    select a,c INTO Table2 from Table1 
    GO 
    --4.显示更新后的结果 
    select * from Table2 
    GO 
    --5.删除测试表 
    drop TABLE Table1 
    drop TABLE Table2
```

### 四.是否复制表结构、数据到新表

#### 1、复制表结构以及数据

```hljs
CREATE TABLE 新表  
SELECT * FROM 旧表
```

#### 2、只复制表结构

a、      CREATE TABLE 新表  

SELECT * FROM 旧表 WHERE 1=2

即:让WHERE条件不成立.  
b、:(低版本的mysql不支持，mysql4.0.25 不支持，mysql5已经支持了)  
CREATE TABLE 新表  
LIKE 旧表

#### 3、复制旧表数据到新表（两表结构一样）

```hljs
INSERT INTO 新表
    SELECT * FROM 旧表
```

#### 4、复制旧表数据到新表（两表结构不一样）<br>

```hljs
INSERT INTO 新表(字段1,字段2,…….)
     SELECT 字段1,字段2,…… FROM 旧表
```
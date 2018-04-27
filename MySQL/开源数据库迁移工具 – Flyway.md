**数据库变更过程中的问题**

![开源数据库迁移工具 – Flyway](http://p3.pstatp.com/large/43560003ee46cce6a12a)

在软件开发迭代过程中，一般有两类变化，一是代码程序的变化，二是数据库（数据结构等）的变化，代码部分的变化我们通过二进制包的版本来定义每次的变化，我们可以快速了解到不同环境（开发、测试、生产等）的软件版本，并替换升级到最新版本，而不同于代码管理，数据库是有状态的，通常我们需要从某状态升级到最新版本，我们在上生产环境时常常会遇到在测试环境变更的脚本在生产环境未执行，甚至是漏掉一些数据库变更操作，出现数据库不一致，导致线上问题。因此数据库管理侧，我们需要考虑以下几个问题：

1. 在某台机器或环境上数据库是什么状态

2. 该环境是否应用了某数据库升级脚本

3. 应用到生产环境的脚本是否在测试环境经过测试

4. 如何快速搭建一个新的数据库实例

针对以上问题，Flyway 提供了一个便利的管理工具帮助我们轻松的管理数据库变更和迁移问题。

**Flyway 特性**

l 自动升级：Flyway 会根据当前数据库状态升级到最新版本。

l 规约优于配置：Flyway 定义了一套默认的规约，不需要修改任何配置就可以正常使用。

l 跨平台：Windows, Mac OSX, Linux, Java 和 Android

l 兼容多种数据库：Oracle, SQL Server, SQL Azure, DB2, DB2 z/OS, MySQL, MariaDB, Google Cloud SQL, PostgreSQL, Redshift, Greenplum, Vertica, EnterpriseDB, H2, Hsql, Derby, SQLite

l 高可靠性：在集群环境下进行数据库升级是安全可靠的。

l 支持失败修复：提供了Repair 功能，用于解决数据库更新操作失败问题。

**Flyway 如何工作**

![开源数据库迁移工具 – Flyway](http://p3.pstatp.com/large/43580003e0baf3c057d5)

按照 Flyway 规范，我们需要对每一次的数据变更记录对应一个脚本升级文件，并通过文件名称描述脚本版本号，脚本文件名规范 V<version>[_<SEQ>][__description]，

如：V1__Initial_Setup.sql，V2__First_Changes.sql，V2_1__Second_Changes.sql 。在创建一个新的数据库时，Flyway 会初始化一个表SCHEMA_VERSION，该表记录了数据库变更历史记录，之后会按找脚本的版本号顺序执行相应脚本。下图为 SCHEMA_VERSION 记录表的数据:

![开源数据库迁移工具 – Flyway](http://p3.pstatp.com/large/43570003e6064f689019)

当我们在一个已存在环境进行数据库升级时，我们只需要按照版本命名规范，创建一个新的脚本文件V2_1__Refactoring.sql，Flyway 会根据当前数据库版本状态，自动过滤已经执行的脚本，只执行版本号大于当前版本号的脚本，如下图：

![开源数据库迁移工具 – Flyway](http://p3.pstatp.com/large/4354000415c65da8b21e)

![开源数据库迁移工具 – Flyway](http://p3.pstatp.com/large/435500040965fb641909)

**Flyway 使用方法**

Flyway 支持多种工作方式，可以轻松与现有系统进行集成：

l Command Line 命令行方式

l API（Java Interface）

l Maven

l Gradle

l Ant

l SBT

以通用的命令行方式为例

1. 下载 Flyway 并解压

![开源数据库迁移工具 – Flyway](http://p3.pstatp.com/large/43580003e0c624c41c40)

2. 配置 Flyway

修改 /conf/flyway.conf 文件，配置数据库源

![开源数据库迁移工具 – Flyway](http://p1.pstatp.com/large/43580003e0c725a4be76)

3. 创建第一个数据脚本

在 sql/ 目录根据规范创建脚本文件 V1__Create_person_table.sql:

![开源数据库迁移工具 – Flyway](http://p1.pstatp.com/large/43550004096a143353c5)

4. 迁移数据到指定数据库

![开源数据库迁移工具 – Flyway](http://p1.pstatp.com/large/435900026e9e377fcb55)

执行日志如下：

![开源数据库迁移工具 – Flyway](http://p3.pstatp.com/large/43550004096d4472c359)

5. 创建第二个数据库升级脚本，并执行升级

在 sql/ 目录根据规范创建脚本文件 V2__Add_people.sql:

![开源数据库迁移工具 – Flyway](http://p3.pstatp.com/large/43550004096ebe01ac41)

执行迁移操作结果：

![开源数据库迁移工具 – Flyway](http://p9.pstatp.com/large/43570003e60b1fa7a68d)

可以看到我们将当前数据库从 Version 1升级到了Version 2版本。

**Flyway事务处理**

在最新4.2.0 版本中增加了 Group 的概念，可以将多个 Pending 状态的升级脚本放在同一个事务中执行，对于支持事务的数据库，如果其中有失败的语句，可以快速回滚到迁移前状态，保证一致性。

![开源数据库迁移工具 – Flyway](http://p3.pstatp.com/large/43570003e60db4168689)

**总结**

在日常软件版本迭代过程中，常常遇到开发测试时变更的数据库操作没有完整记录，在生产环境出现代码与数据库不一致问题，甚至在没有开发和测试环境测试的前提下，直接在生产环境进行数据库变更，出现问题很难排查，提高了管理复杂度，通过使用 Flyway 提供的规范和工具，我们可以轻松跟踪数据库版本状态，以及升级的记录，升级代码的同时升级数据库，降低对数据库变更管理的复杂度，减少人工操作带来的失误。


作者：刘永强

JFrog 中国技术支持负责人，曾在 HPE，亿玛等公司担任高级工程师，专注系统架构、软件CI/CD及devops领域，在互联网平台建设上有着丰富的经验，曾服务的客户有中兴通讯，宜人贷，易保科技，顺丰等等，并负责过多个互联网平台和移动应用的研发和运维工作。



![开源数据库迁移工具 – Flyway](http://p1.pstatp.com/large/435a000202a5300a435c)

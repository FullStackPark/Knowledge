日志服务 最近在原有30+种数据采集渠道 基础上，新增MySQL Binlog、MySQL select等数据库方案，仍然主打快捷、实时、稳定、所见即所得的特点。

以下我们以用户登录数据库作为案例。公司内非常多的人员依赖于用户登录数据以及其衍生出来的相关数据：

* 老板要看大屏，每天UV、PV增长在哪里？

* 安全要监控登录是否异常，现在用户账户是否遭到集体攻击？

* 客户小二接到用户反馈，如何实时查询用户登录信息？

* BI需要分析用户行为，数据分析如何关联用户登录数据？

* 审计上门了，请把您3年前用户的登录数据拿出来吧？

![10分钟搭建MySQL Binlog分析+可视化方案](http://p1.pstatp.com/large/568c00024204e9d59e93)

接下来我们将演示如何在10分钟内手把手完成从binlog采集到查询、告警、搭建报表等全过程，满足各个老板们的需求：

1.  MySQL Binlog采集

2.  关键字段索引+统计设置

3.  对异常账号进行查询分析

4.  对异常登录进行告警

5.  配置可视化仪表盘

6.  对历史登录信息备份以备数据审计

# 环境准备

**数据库**

mysql类型数据库（使用mysql协议，例如RDS、DRDS等），数据库开启binlog，且配置binlog类型为ROW模式（RDS默认开启）

**用户登录表结构**

<pre>
CREATE TABLE `user_login` ( `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'id', `login_time` datetime NOT NULL, `login_ip` varchar(10) NOT NULL DEFAULT '', `dev_type` varchar(10) NOT NULL, `usr_id` int(11) unsigned NOT NULL,`login_result` varchar(10) unsigned NOT NULL,`login_err_times` int(10) unsigned NOT NULL,`next_verify_type` varchar(10) NOT NULL,PRIMARY KEY (`id`), KEY `usr_id_index` (`usr_id`) )
</pre>

用户登录表中记录了登录id、登录时间、登录ip、登录设备、用户id、登录结果、连续登录失败次数、下一次校验类型等信息。其中登录验证规则如下：

* 正常情况只验证账号密码匹配

* 若用户连续登录失败超过3次或者当前ip和上次登录ip不在同一省，下次登录将弹出验证码

* 若用户连续登录失败超过5次，则下次登录将使用手机验证码

**用户登录时表的更新方案**

* 方案1：

    每次用户登录，在`user_login`中新增一条记录，记录登录的ip、设备类型、时间信息

* 方案2：

    考虑到用户数量非常多，如果每次用户登录都在`user_login`中新增一条记录，数据量会非常大，所以每次用户登录时，只会根据`usr_id`更新`update`表中的数据

对于方案1，优点是数据库中保存了所有用户的登录信息，缺点是`user_login`表会存在爆掉的问题，需要定期删除历史的数据；对于方案2，优点是`user_login`表的大小可控，缺点是会丢失历史用户的登录信息。

这里我们推荐使用方案2+logtail binlog采集组成最优的方案3：用户最近一次登录信息依然保存在数据库中，通过logtail的binlog功能采集`user_login`表，logtail会将表中的每次修改事件上传到日志服务，日志服务中的数据可设置保存时间，超时自动删除。同时在日志服务中，可以对实时采集上来的数据进行查询、统计、查看报表、监控报警，也支持将数据对接下游流计算、导入Max Compute/OSS等。

![10分钟搭建MySQL Binlog分析+可视化方案](http://p1.pstatp.com/large/568800029ebf422c5cc2)

---------| 方案1       | 方案2        |案3                                   
-------- | ------------ | ------------ | -------
数据库数据量  | 用户数 * 运行时间 / 登录率       | 用户数          | 用户数                                   
数据库压力    | 支撑写入以及分析，压力大           | 只更新，压力最小     | 更新+binlog采集，压力较小                      
分析能力     | 基于sql进行分析，数据量大时对数据库影响大 | 无历史数据，基本不能分析 | 使用日志服务分析，TB级数据实时查询分析无压力，支持众多分析扩展函数    
报表&监控    | 手动搭建&运维                | 手动搭建&运维      | 基于日志服务快速创建仪表盘、配置自定义报警                 
上下游对接扩展性 | 手动对接上下游                | 手动对接上下游      | 对接流计算实时处理、导入OSS归档存储、对接Max Compute离线分析等

# 数据采集

**安装logtail**

根据文档安装logtail，确认版本号在0.16.0及以上。若低于0.16.0版本请根据文档提示升级到最新版本。

**采集配置**

1.  在日志服务控制台创建一个新的Logstore，采集向导中选择自建软件中的Mysql binlog

![10分钟搭建MySQL Binlog分析+可视化方案](http://p3.pstatp.com/large/568800029ec06dfc9989)

1.  在配置页面中输入binlog采集配置，如下：

<pre>
{ "inputs": [ { "type": "service_canal", "detail": { "Host": "************.mysql.rds.aliyuncs.com", "User" : "root", "Password": "*******", "IncludeTables": [ "user_info\.user_login" ] } } ]}
</pre>

* 注意：

* 数据库开启binlog且为ROW模式（RDS默认支持），使用的账户具有mysql slave权限以及需要采集的数据表的select权限。

* binlog支持`IncludeTables`和`ExcludeTables`过滤，格式均为正则表达式

* 其他请参考binlog采集中使用限制

**建立索引**

配置应用到机器组后，进入索引查询配置页面。在键值索引属性中配置以下索引项：

字段名                    | 类型   | 别名 | 分词符 | 开启统计
---------------------- | ---- | -- | --- | ----
`_event_`              | text |    |     | 是   
`dev_type`             | text |    |     | 是   
`login_ip`             | text |    |     | 是   
`usr_id`               | text |    |     | 是   
`next_verify_type`     | text |    |     | 是   
`login_err_times`      | long |    |     | 是   
`login_result`         | text |    |     | 是   
`old_dev_type`         | text |    |     | 是   
`old_login_ip`         | text |    |     | 是   
`old_usr_id`           | text |    |     | 是   
`old_next_verify_type` | text |    |     | 是   
`old_login_err_times`  | long |    |     | 是   
`old_login_result`     | text |    |     | 是   

**数据预览**

应用配置1分钟后，点击预览可以看到状态数据已经采集上来（logtail的binlog采集会额外上传数据操作类型、GTID等信息）：

* 对于修改的事件，Logtail会同时采集修改前和修改后的数据，修改前的数据以`old_`开头。因此我们可以基于修改前后的数据对比查找登录ip变化的相关记录。

![10分钟搭建MySQL Binlog分析+可视化方案](http://p9.pstatp.com/large/568d00007a2b01391430)

注意： 若无数据，请检查配置是否为合法json；若配置正常，请参考数据采集异常排查文档自助排查

# 自定义查询与分析

到这一步我们就可以满足客服和BI的需求了：查询/关联查询。例如：

1.  用户反馈账号信息被篡改了，客服通过日志服务，查询该用户从上次登录到现在的登录信息：`login_id : 256525`，发现其中有一条登录日志；继续查询登录地址`login_id : 256525 | select ip_tp_province(login_ip) as login_province, ip_tp_country(login_ip) as login_country`，发现是在国外登录的，因此很有可能该用户账号泄漏或被攻破了。

2.  用户反馈自己的账号被限制登录了，客服通过日志服务，查询该用户限制登录前的相关登录信息：`login_id : 256525 | select ip_tp_province(login_ip) as login_province, login_result， count(1) as total group by (login_province,login_result) order by total desc limit 100`，发现该用户在多个省异常登录失败了很多次。

* 查询相关使用帮助参见日志服务查询

# 用户登录大盘

现在我们来搭建CEO要的大盘，先准备一些基础的统计信息：

* 统计一天的UV&PV

<pre>
* | select count(distinct(usr_id)) as uv, count(1) as pv
</pre>

* 查看登录设备分布

<pre>
* | select dev_type, count(1) as count group by dev_type
</pre>

* 每5分钟统计UV&PV分布

<pre>
* | select count(1) as uv, count(distinct(usr_id)) as pv, from_unixtime( __time__ - __time__ % 300) as time group by __time__ - __time__ % 300 order by time limit 1440
</pre>

**统计地理位置分布**

由于原始的数据中没有用户登录的地理位置分布信息，但我们可以通过ip地址定位到用户登录的省市，这里我们使用日志服务自带的ip地址转换函数（具体参见分析语法IP识别函数章节）

* 统计top10的city（使用`ip_to_city`）

<pre>
* | select ip_to_city(login_ip) as login_city, count(1) as count group by login_city order by count desc limit 10
</pre>

* 统计省份分布（使用`ip_tp_province`）

<pre>
* | select ip_tp_province(login_ip) as login_province, count(1) as count group by login_province order by count desc limit 100
</pre>

**用户登录大盘搭建**

根据上一节的统计结果，我们搭建出了用户登录信息的仪表盘，可以向CEO汇报了。

* 仪表盘搭建参见日志服务仪表盘设置

![10分钟搭建MySQL Binlog分析+可视化方案](http://p3.pstatp.com/large/568b000231f52ee8890b)

# 异常登录告警

异常登录都会有误判的可能性，因此正常情况下会有少部分异常登录的情况，但异常登录占比要小于1%。这里我们为用户登录设置一个异常登录的告警：若当异常登录占总登录的1%则触发告警。

<pre>
* | SELECT sum( CASE WHEN ip_tp_province(login_ip)!=ip_tp_province(old_login_ip) then 1 ELSE 0 end ) \*1.0 / count(1) as abnormal_login_percentage
</pre>

将该查询存为快速查询`abnormal_login`，并设置告警。

* 告警设置参见日志服务告警设置

配置项        | 内容                                          
---------- | --------------------------------------------
报警规则名称     | abnormal_login_alarm                        
快速查询名称     | abnormal_login                              
数据查询时间（分钟） | 5                                           
检查间隔（分钟）   | 5                                           
触发次数       | 1                                           
字段名称       | abnormal_login_percentage                   
比较符        | 大于                                          
检查阈值       | 0.01                                        
通知类型       | 通知中心                                        
通知内容       | user abnormal login percentage exceed limit.

# 数据备份

用户登录数据，一般建议在日志服务存储一段时间（30天、半年、1年等）用于实时的查询和分析，但对于历史数据还需要保存下来，便于后续的审计、大数据挖掘与分析等。这里我们使用日志服务的投递功能，将数据投递到OSS进行长期的归档存储。审计员来了想看多少年前的数据都有！

![10分钟搭建MySQL Binlog分析+可视化方案](http://p9.pstatp.com/large/568b000231f4c6f3de47)

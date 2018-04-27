**前言碎语**

曾几何时，你为了一条sql效率寻遍互联网的每个角落，也许，你会读到这么一篇sql优化的文章《MySQL索引原理及慢查询优化》，然后你恍然大悟，sql索引还有一个叫最左前缀匹配的原则，并不是一味的建索引就可以解决慢查询的问题。今天，有这样一个工具，在你还在思考如何最左前匹配的时候 ，他已经帮你解析快速分析出你的sql，并给出索引优化建议，是不是很nice，好了，废话不多说了，重点在下面啦

**SQLAdvisor是什么？**

SQLAdvisor是由美团点评公司技术工程部DBA团队（北京）开发维护的一个分析SQL给出索引优化建议的工具。它基于MySQL原生态词法解析，结合分析SQL中的where条件、聚合条件、多表Join关系 给出索引优化建议。目前SQLAdvisor在美团点评广泛应用，包括美团支付、酒店旅游、外卖、团购等产品线，公司内部对SQLAdvisor的开发全面转到github上，开源和内部使用保持一致。

开源地址：https://github.com/Meituan-Dianping/SQLAdvisor

**SQLAdvisor详细说明**

SQLAdvisor快速入门教程

SQLAdvisor架构和实践

SQLAdvisor release notes

SQLAdvisor开发规范

**SQLAdvisor 的优点**

* 基于 MySQL 原生词法解析，充分保证词法解析的性能、准确定以及稳定性；

* 支持常见的 SQL(Insert/Delete/Update/Select)；

* 支持多表 Join 并自动逻辑选定驱动表；

* 支持聚合条件 Order by 和 Group by；

* 过滤表中已存在的索引。

**SQLAdvisor使用举例**

sql: SELECT id FROM crm_loan WHERE id_card = '1234567'

cmd: ./sqladvisor -h xx -P xx -u xx -pxx -d xx -q "SELECT id FROM crm_loan WHERE id_card = '1234567'"

SQLAdvisor输出: alter table crm_loan add index idx_id_card(id_card)

ps:除了命令行输入外，还支持文件的方式输入，格式如下

![SQL解析优化神器-SQLAdvisor](http://p1.pstatp.com/large/402c0003cad5dd83970b)

另附Sqladvisor的解析过程输出图如下：

![SQL解析优化神器-SQLAdvisor](http://p1.pstatp.com/large/402f00026441131bbfd0)

**SQLAdvisor架构流程图**

**![SQL解析优化神器-SQLAdvisor](http://p1.pstatp.com/large/40310001f8ee76946c4c)**

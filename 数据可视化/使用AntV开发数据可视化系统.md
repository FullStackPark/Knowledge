![使用AntV开发数据可视化系统](http://p3.pstatp.com/large/436c0000eba1622f6345)

AntV

# AntV

```
一套专业、简单、无限可能的可视化解决方案。
```

官网地址：https://antv.alipay.com/

该框架提供丰富的图表组件，在实际项目开发使用中，如果你对图表不太熟悉的话，在"可视化基础"里面有对各个图表的说明，什么情况下使用什么样的图标也有简单说明。

![使用AntV开发数据可视化系统](http://p3.pstatp.com/large/436d0000e6ccddc28e2c)

可视化基础

# 例子

图标分移动端和PC端，根据自己需求选择使用，下面列出几个常用的图表样例：  

![使用AntV开发数据可视化系统](http://p1.pstatp.com/large/436d0000f519321e2037)

分组柱状图

![使用AntV开发数据可视化系统](http://p3.pstatp.com/large/436d0000f4e281899607)

嵌套饼图

![使用AntV开发数据可视化系统](http://p1.pstatp.com/large/436900012bc1f95d6a7c)

分时折线图

# 开发

下面以PC端开发为例进行简单介绍一下使用步骤

1、引入JS库（也可以直接下载到本地项目在引入）

```
<script src="https://a.alipayobjects.com/g/datavis/g2/2.3.13/index.js"></script>
```

2、创建图表容器

```
<div id="g2-box"></div>
```

3、创建图标对象信息，并制定容器ID

```
var chart = new G2.Chart({ id: 'g2-box', forceFit: true, height: 450 });
```

4、生产本地图标数据（也可以通过AJAX请求从服务获取数据）

```
var data = [ {month: 'Jan', temperature: 7.0}, {month: 'Feb', temperature: 6.9}, {month: 'Mar', temperature: 9.5}, {month: 'Apr', temperature: 14.5}, {month: 'May', temperature: 18.2}, {month: 'Jun', temperature: 21.5}, {month: 'Jul', temperature: 25.2}, {month: 'Aug', temperature: 26.5}, {month: 'Sep', temperature: 23.3}, {month: 'Oct', temperature: 18.3}, {month: 'Nov', temperature: 13.9}, {month: 'Dec', temperature: 9.6} ];
```

5、设置图标数据格式

```
chart.source(data, { month: { alias: '月份', range: [0, 1] }, temperature: { alias: '平均温度(°C)' } });
```

6、设置线条样式（折线图）

```
chart.line().position('month*temperature').size(1);
```

7、渲染数据显示

```
chart.render();
```

具体开发说明，可参考官方文档，网站 https://antv.alipay.com/g2/doc （G2）

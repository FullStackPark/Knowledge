![156个Python网络爬虫资源，妈妈再也不用担心你找不到资源了](http://p1.pstatp.com/large/pgc-image/1520921868542b31a408901)

本列表包含Python网页抓取和数据处理相关的库。

**网络相关**

* 通用

* urllib – 网络库(标准库)

* requests – 网络库

* grab – 网络库(基于pycurl)

* pycurl – 网络库 (与libcurl绑定)

* urllib3 – 具有线程安全连接池、文件psot支持、高可用的Python HTTP库

* httplib2 – 网络库

* RoboBrowser – 一个无需独立浏览器即可访问网页的简单、pythonic的库

* MechanicalSoup – 能完成自动网站交互的Python库

* mechanize – 有状态、可编程的网页浏览库。

* socket – 底层网络接口(标准库)

* Unirest for Python – 一套支持多种语言的轻量级HTTP库

* hyper – Python HTTP/2客户端

* PySocks – SocksiPy持续更新并维护的版本，指出bug修复和一些其他功能，可以作为socket模块的替代品

* 异步

* treq – 基于twisted、与requests类似的API

* aiohttp – asyncio的HTTP客户端/服务器 (PEP-3156)

**网络爬虫框架**

* 全能型爬虫

* grab – 网络爬虫框架(基于pycurl/multicurl)

* scrapy – 网络爬虫框架(基于twisted)

* pyspider – 一个强力的爬虫系统

* cola – 一个分布式爬虫框架

* 其他

* portia – 基于Scrapy的可视化爬虫

* restkit – Python的HTTP资源库。允许影虎简单的访问HTTP资源并用来创建项目

* demiurge – 基于PyQuery的微型爬虫框架

**HTML/XML解析**

* 通用

* lxml – 高效的HTML/XML处理库。支持XPATH，用C语言写成

* cssselect – 解析DOM树和css选择器

* pyquery – 解析DOM树和jQuery选择器

* BeautifulSoup – Python写成的低效HTML/XMl处理库

* html5lib – 根据WHATWG规范生成HTML/ XML文档的DOM。WHATWG规范是现在浏览器的通行规范

* feedparser – 解析RSS/ATOM信息流

* MarkupSafe – Python的XML/HTML/XHTML安全转义字符串工具

* xmltodict – 让你处理XML如同处理JSON一样

* xhtml2pdf – HTML/CSS to PDF转化器

* untangle – 讲XML文档转化为Python项目以简化处理难度

* hodor – 支持lxml and cssselect的配置驱动包装工具

* 清理

* Bleach – 清理HTML (需求html5lib)

* sanitize – 将混乱的数据世界恢复清楚

**文本处理**

解析及操作文本的库

* 通用

* difflib – 差异化计算工具(Python标准库)

* Levenshtein – 快速计算编辑距离及字符串相似度

* fuzzywuzzy – 模糊字符串比匹配

* esmre – 正则表达式加速器.

* ftfy – 将Unicode文本自动整理减少碎片化

* 转换

* unidecode – Unicode转化为ASCII文本

* 字符编码

* uniout – 将转移字符串输出为可读形式

* chardet – Python 2/3兼容字符编码检测器

* xpinyin – 讲汉字转为拼音的库

* pangu.py – CJK及字母数字文本间距格式化

* Slug化

* awesome-slugify – 可保留Unicode的Python slugify库

* python-slugify – 讲Unicode转为ASCII的Python slugify库

* unicode-slugify – unicode slugs生成工具

* pytils – 处理俄语字符串的小工具(包含pytils.translit.slugify)

* 通用解析器

* PLY – Python lex和yacc解析工具

* pyparsing – 用于生成解析器的通用框架

* 人名

* python-nameparser – 姓名解析组件

* 电话号码

* phonenumbers – 处理、格式化、存储、验证全球电话号码

* 用户代理字符串

* python-user-agents – 浏览器用户代理解析器

* HTTP Agent Parser – Python HTTP代理解析器

* fake-useragent – 基于全球浏览器统计的Python用户代理欺骗器

* user_agent – 用户代理数据生成器

**特殊格式处理**

处理特编辑特殊字符格式的库

* 通用

* tablib – 处理XLS, CSV, JSON, YAML等表格数据的库

* textract – 从任何文档中提取文本，支持Word, PowerPoint, PDF等

* messytables – 杂乱的表格数据解析

* rows – 支持多种格式的通用且美观的表格数据处理器(现有CSV, HTML, XLS, TXT — 即将支持更多)

* Office

* python-docx – 阅读，查询和修改Microsoft Word 2007/2008 docx文件

* xlwt / xlrd – 从Excel读取及写入数据和格式化信息

* XlsxWriter – 用于穿件Excel .xlsx文件的Python模块

* xlwings – 一个BSD许可的库，是Excel与Python互相调用更加简单

* openpyxl – 可读取、编辑Excel 2010xlsx/xlsm/xltx/xltm文件的库

* Marmir – 提取Python数据结构并将其转化为表格的库

* PDF

* PDFMiner – 从PDF文档中提取信息的工具

* PyPDF2 – 一个分割、合并、转换PDF文件的库

* ReportLab – 可以快速创建大量PDF文档

* pdftables – 从PDF文件中精准提取表格

* Markdown

* Python-Markdown – 一个用Python实现的John Gruber的Markdown

* Mistune – 速度最快，功能全面的Markdown纯Python解析器

* markdown2 – 一个完全用Python实现的快速的Markdown

* YAML

* PyYAML – 一个Python的YAML解析器

* CSS

* cssutils – 一个Python的CSS库

* ATOM/RSS

* feedparser – 通用的feed解析器

* SQL

* sqlparse – 一个无验证的SQL语句分析器

* HTTP

* http-parser – C语言实现的HTTP请求/响应消息解析器

* Microformats

* opengraph – 一个用来解析Open Graph协议标签的Python模块

* 可移植的执行体

* pefile – 一个多平台的用于解析和处理可移植执行体（即PE）文件的模块

* PSD

* psd-tools – 将Adobe Photoshop PSD（即PE）文件读取到Python数据结构

**自然语言处理**

自然语言处理库

* NLTK – Python自然语言处理领先者

* Pattern – Python的网络挖掘模块。他有自然语言处理工具，机器学习以及其它

* TextBlob – 为深入处理自然语言的项目提供API，参考了NLTK及其他

* jieba – 中文分词

* SnowNLP – 汉字文本处理库

* loso – 中文分词库

* genius -基于条件随机域的中文分词

* langid.py – 独立的语言识别系统

* Korean – 韩文形态库

* pymorphy2 – 俄语形态分析器（词性标注+词形变化引擎）

* PyPLN – 用Python编写的分布式自然语言处理通道。这个项目的目标是创建一种简单的方法使用NLTK通过网络接口处理大语言库

* langdetect – Python的谷歌语言检测库端口

**浏览器自动化与仿真**

* 浏览器

* selenium – 自动化真实浏览器(Chrome, Firefox, Opera, IE)

* Ghost.py – QtWebKit封装(需求PyQT)

* Spynner – 具备AJAX支持的程序化网页浏览模块

* Splinter – 通用API浏览器模拟器（selenium web驱动，Django客户端，Zope）

* Headless工具

* xvfbwrapper – 用于在X虚拟帧缓冲区（Xvfb）中运行显示的Python包装器

**多进程并发**

* threading – Python标准库的多线程运行。因为python GIL限制，对于I/O密集型任务很有效，对于CPU绑定的任务没用

* multiprocessing – 多进程标准库

* celery – 基于分布式消息传递的异步任务队列/作业队列

* concurrent-futures – concurrent.futures模块提供用于异步执行callable的高级接口

**异步**

异步网络编程库

* asyncio – 异步I/O，时间循环，协同程序和任务(Python 3.4以上版本的Python标准库)

* Twisted – 基于事件驱动的网络引擎框架

* Tornado – 一个Web框架及异步网络库

* pulsar – Python事件驱动的并发框架

* diesel – Python的基于Greenlet的I/O框架

* gevent – 一个基于协同程序的Python网络库，使用greenlet

* eventlet – 有WSGI支持的异步框架

* Tomorrow – 异步代码的魔法

**队列**

* celery – 基于分布式消息传递的异步任务队列/作业队列

* huey – 小型多线程任务队列

* mrq – Mr. Queue – 使用redis & Gevent 的Python分布式工作任务队列

* RQ – 基于Redis的轻量级任务队列管理器

* simpleq – 一个简单的，可无限扩展，基于Amazon SQS的队列

* python-gearman – Gearman的Python API

**云计算**

* picloud – 在云端执行Python

* dominoup.com – 在云端执行R, Python及matlab代码

**电子邮件**

电子邮件处理库

* flanker – 电子邮件及MIME处理库

* Talon – Mailgun库用于提取消息的报价和签名

**URL和网络地址操作**

URL和网络地址操作库

* URL

* furl – 一个小的Python库，使得操纵URL简单化

* purl – 一个简单的不可改变的URL以及一个干净的用于调试和操作的API

* urllib.parse – 用于打破统一资源定位器（URL）的字符串在组件（寻址方案，网络位置，路径等）之间的隔断，为了结合组件到一个URL字符串，并将“相对URL”转化为一个绝对URL，称之为“基本URL”（标准库）

* tldextract – 使用公共后缀列表从URL的注册域和子域中准确分离TLD

* 网络地址

* netaddr – 用于显示和操纵网络地址的Python库

**网页内容提取**

网页内容提取库

* HTML页面的文本和元数据

* newspaper – 用Python进行新闻提取、文章提取和内容策展

* html2text – 将HTML转为Markdown格式文本

* python-goose – HTML内容/文章提取器

* lassie – 人性化的网页内容检索工具

* micawber – 一个从网址中提取丰富内容的小型库

* sumy -一个自动汇总文本文件和HTML网页的模块

* Haul – 一个可扩展的图像爬虫

* python-readability – arc90 readability工具的快速Python接口

* scrapely – 从HTML网页中提取结构化数据的库。给出了一些Web页面和数据提取的示例，scrapely为所有类似的网页构建一个分析器

* libextract – 从网站提取数据

* 视频

* youtube-dl – 一个从YouTube下载视频的小型命令行工具

* you-get – Python3写成的YouTube/Youku/Niconico视频下载工具

* Wiki

* WikiTeam – 下载并保存wkiks的工具

**WebSocket**

用于WebSocket的库

* Crossbar – 开源的应用消息传递路由器（Python实现的用于Autobahn的WebSocket和WAMP）

* AutobahnPython – 提供了WebSocket协议和WAMP协议的Python实现并且开源

* WebSocket-for-Python – Python 2和3以及PyPy的WebSocket客户端和服务器库

**DNS解析**

* dnsyo – 在全球超过1500个的DNS服务器上检查你的DNS

* pycares – ic-ares的接口。c-ares是进行DNS请求和异步名称决议的C语言库

**计算机视觉**

* OpenCV – 开源计算机视觉库

* SimpleCV – 用于照相机、图像处理、特征提取、格式转换的简介，可读性强的接口（基于OpenCV）

* mahotas – 快速计算机图像处理算法（完全使用 C++ 实现），完全基于 numpy 的数组作为它的数据类型

**代理服务器**

* shadowsocks – 一个快速隧道代理，可帮你穿透防火墙（支持TCP和UDP，TFO，多用户和平滑重启，目的IP黑名单）

* tproxy – tproxy是一个简单的TCP路由代理（第7层），基于Gevent，用Python进行配置

**杂项**

* user_agent – 此模块用于生成随机，有效的Web导航器的配置和用户代理HTTP header

**其他**

* awesome-python

* pycrumbs

* python-github-projects

* python_reference

* pythonidae

# 写在最后

前几天有私信小编要Python的学习资料，小编整理了一些有深度的Python教程和参考资料，从入门到高级的都有，文件已经打包好了，正在学习Python的同学可以下载学习学习。文件下载方式：点击小编头像，关注后私信回复“资料”即可下载。首先把代码撸起来！首先把代码撸起来！首先把代码撸起来！重要的事说三遍，哈哈。“编程是门手艺活”。什么意思？得练啊。

![156个Python网络爬虫资源，妈妈再也不用担心你找不到资源了](http://p1.pstatp.com/large/pgc-image/1520917971099102b545093)

<!---->

__

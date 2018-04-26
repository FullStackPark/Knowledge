前端时间闲的无聊， 对Python兴趣徒增。学习这事儿吧，光看没用，还是要是实战，顺手搜了一些写的不错的开源库，也看了些博客。总结一些，分享给大家。

![Python库大全（涵盖了Python应用的方方面面），建议收藏留用！](http://p1.pstatp.com/large/pgc-image/1523787973779f7a7f6bb4b)

学Python，想必大家都是从爬虫开始的吧。毕竟网上类似的资源很丰富，开源项目也非常多。

Python学习网络爬虫主要分3个大的版块：**抓取**，**分析**，**存储**

当我们在浏览器中输入一个url后回车，后台会发生什么？比如说你输入http://www.tuotiao.com，你就会看到头条站首页。

简单来说这段过程发生了以下四个步骤：

* 查找域名对应的IP地址。

* 向IP对应的服务器发送请求。

* 服务器响应请求，发回网页内容。

* 浏览器解析网页内容。

网络爬虫要做的，简单来说，就是实现浏览器的功能。通过指定url，直接返回给用户所需要的数据，而不需要一步步人工去操纵浏览器获取。

抓取这一步，你要明确要得到的内容是什么？是HTML源码，还是Json格式的字符串等。将得到内容逐一解析就好。具体的如何解析，以及如何处理数据，文章后面提供了非常详细的且功能强大的开源库列表。

当然了，爬去别人家的数据，很有可能会遭遇反爬虫机制的，怎么办**？使用代理。**

适用情况：限制IP地址情况，也可解决由于“频繁点击”而需要输入验证码登陆的情况。

这种情况最好的办法就是维护一个代理IP池，网上有很多免费的代理IP，良莠不齐，可以通过筛选找到能用的。

对于“频繁点击”的情况，我们还可以通过限制爬虫访问网站的频率来避免被网站禁掉。

有些网站会检查你是不是真的浏览器访问，还是机器自动访问的。这种情况，加上User-Agent，表明你是浏览器访问即可。有时还会检查是否带Referer信息还会检查你的Referer是否合法，一般再加上Referer。也就是**伪装成浏览器，或者反“反盗链”。**

对于网站有验证码的情况，我们有三种办法：

* 使用代理，更新IP。

* 使用cookie登陆。

* 验证码识别。

接下来我们重点聊聊**验证码识别。**

**可以利用开源的Tesseract-OCR系统进行验证码图片的下载及识别，将识别的字符传到爬虫系统进行模拟登陆。当然也可以将验证码图片上传到打码平台上进行识别。如果不成功，可以再次更新验证码识别，直到成功为止。**

好了，爬虫就简单聊到这儿，有兴趣的朋友可以去网上搜索更详细的内容。

文末附上本文重点：实用Python库大全。

**网络**

* urllib -网络库(stdlib)。

* requests -网络库。

* grab – 网络库（基于pycurl）。

* pycurl – 网络库（绑定libcurl）。

* urllib3 – Python HTTP库，安全连接池、支持文件post、可用性高。

* httplib2 – 网络库。

* RoboBrowser – 一个简单的、极具Python风格的Python库，无需独立的浏览器即可浏览网页。

* MechanicalSoup -一个与网站自动交互Python库。

* mechanize -有状态、可编程的Web浏览库。

* socket – 底层网络接口(stdlib)。

**网络爬虫框架**

* grab – 网络爬虫框架（基于pycurl/multicur）。

* scrapy – 网络爬虫框架。

* pyspider – 一个强大的爬虫系统。

* cola – 一个分布式爬虫框架。

**HTML/XML解析器**

* lxml – C语言编写高效HTML/ XML处理库。支持XPath。

* cssselect – 解析DOM树和CSS选择器。

* pyquery – 解析DOM树和jQuery选择器。

* BeautifulSoup – 低效HTML/ XML处理库，纯Python实现。

* html5lib – 根据WHATWG规范生成HTML/ XML文档的DOM。该规范被用在现在所有的浏览器上。

* feedparser – 解析RSS/ATOM feeds。

* MarkupSafe – 为XML/HTML/XHTML提供了安全转义的字符串。

**文本处理**

用于解析和操作简单文本的库。

* difflib – （Python标准库）帮助进行差异化比较。

* Levenshtein – 快速计算Levenshtein距离和字符串相似度。

* fuzzywuzzy – 模糊字符串匹配。

* esmre – 正则表达式加速器。

* ftfy – 自动整理Unicode文本，减少碎片化。

**自然语言处理**

处理人类语言问题的库。

* NLTK -编写Python程序来处理人类语言数据的最好平台。

* Pattern – Python的网络挖掘模块。他有自然语言处理工具，机器学习以及其它。

* TextBlob – 为深入自然语言处理任务提供了一致的API。是基于NLTK以及Pattern的巨人之肩上发展的。

* jieba – 中文分词工具。

* SnowNLP – 中文文本处理库。

* loso – 另一个中文分词库。

**浏览器自动化与仿真**

* selenium – 自动化真正的浏览器（Chrome浏览器，火狐浏览器，Opera浏览器，IE浏览器）。

* Ghost.py – 对PyQt的webkit的封装（需要PyQT）。

* Spynner – 对PyQt的webkit的封装（需要PyQT）。

* Splinter – 通用API浏览器模拟器（selenium web驱动，Django客户端，Zope）。

**多重处理**

* threading – Python标准库的线程运行。对于I/O密集型任务很有效。对于CPU绑定的任务没用，因为python GIL。

* multiprocessing – 标准的Python库运行多进程。

* celery – 基于分布式消息传递的异步任务队列/作业队列。

* concurrent-futures – concurrent-futures 模块为调用异步执行提供了一个高层次的接口。

**异步**

异步网络编程库

* asyncio – （在Python 3.4 +版本以上的 Python标准库）异步I/O，时间循环，协同程序和任务。

* Twisted – 基于事件驱动的网络引擎框架。

* Tornado – 一个网络框架和异步网络库。

* pulsar – Python事件驱动的并发框架。

* diesel – Python的基于绿色事件的I/O框架。

* gevent – 一个使用greenlet 的基于协程的Python网络库。

* eventlet – 有WSGI支持的异步框架。

* Tomorrow – 异步代码的奇妙的修饰语法。

**队列**

* celery – 基于分布式消息传递的异步任务队列/作业队列。

* huey – 小型多线程任务队列。

* mrq – Mr. Queue – 使用redis & Gevent 的Python分布式工作任务队列。

* RQ – 基于Redis的轻量级任务队列管理器。

* simpleq – 一个简单的，可无限扩展，基于Amazon SQS的队列。

* python-gearman – Gearman的Python API。

**云计算**

* picloud – 云端执行Python代码。

* dominoup.com – 云端执行R，Python和matlab代码

**网页内容提取**

提取网页内容的库。

* HTML页面的文本和元数据

* newspaper – 用Python进行新闻提取、文章提取和内容策展。

* html2text – 将HTML转为Markdown格式文本。

* python-goose – HTML内容/文章提取器。

* lassie – 人性化的网页内容检索工具

**WebSocket**

用于WebSocket的库。

* Crossbar – 开源的应用消息传递路由器（Python实现的用于Autobahn的WebSocket和WAMP）。

* AutobahnPython – 提供了WebSocket协议和WAMP协议的Python实现并且开源。

* WebSocket-for-Python – Python 2和3以及PyPy的WebSocket客户端和服务器库。

**DNS解析**

* dnsyo – 在全球超过1500个的DNS服务器上检查你的DNS。

* pycares – c-ares的接口。c-ares是进行DNS请求和异步名称决议的C语言库。

**计算机视觉**

* OpenCV – 开源计算机视觉库。

* SimpleCV – 用于照相机、图像处理、特征提取、格式转换的简介，可读性强的接口（基于OpenCV）。

* mahotas – 快速计算机图像处理算法（完全使用 C++ 实现），完全基于 numpy 的数组作为它的数据类型。

**代理服务器**

* shadowsocks – 一个快速隧道代理，可帮你穿透防火墙（支持TCP和UDP，TFO，多用户和平滑重启，目的IP黑名单）。

* tproxy – tproxy是一个简单的TCP路由代理（第7层），基于Gevent，用Python进行配置。

另：

Python有很多Web开发框架,大而全的开发框架非Django莫属,用得也最广泛.有很多公司有使用Django框架,如某狐,某讯等。以简洁著称的web.py,flask都非常易于上手,以异步高性能著称的tornado,源代码写得美如画,知乎,Quora都在用。

最后祝大家学的愉快，学的神速。

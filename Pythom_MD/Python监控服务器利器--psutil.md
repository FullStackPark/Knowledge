![Python监控服务器利器--psutil](http://p3.pstatp.com/large/6c3200042b23f3cbc22b)

服务器的监控通过安装一些常用的监控软件之外，有时也需要运行一些shell或Python脚本；shell下可以使用系统自带的ps/free/top/df等shell命令，Python可以调用subprocess等模块来运行shell命令，不过这么做就比较麻烦。这里有一个比较好用的第三方模块：psutil。

psutil是一个跨平台的库，用于在Python中检索有关运行进程和系统利用率（CPU，内存，磁盘，网络，传感器）的信息。它主要用于系统监视，分析，限制进程资源和运行进程的管理。它实现了UNIX命令行工具提供的许多功能，例如：ps，top，lsof，netstat，ifconfig，who，df，kill，free，nice，ionice，iostat，iotop，uptime，pidof，tty，taskset，pmap。 psutil目前支持以下平台：

```
 Linux

 Windows

 OSX,

 FreeBSD, OpenBSD, NetBSD

 Sun Solaris

 AIX

 ...
```

等装有Python2.6至3.6的32-bit和64-bit架构. 也可以在PyPy上运行。  

**安装**

文中示例均在Python版本3.6环境下运行；

```
 \# pip3 install psutil
```

**常用模块**  

获取psutil版本信息

```
 In [1]: import psutil

 In [2]: psutil.version_info

 Out[2]: (5, 4, 3)
```

获取CPU信息

```
 In [3]: psutil.cpu_count() # 逻辑CPU核数

 Out[3]: 4

 In [4]: psutil.cpu_count(logical=False) # 物理CPU核数

 Out[4]: 2

 In [5]: psutil.cpu_times() # CPU的用户、系统、空闲时间

 Out[5]: scputimes(user=240773.0, nice=0.0, system=96416.32, idle=1161930.41)

 In [9]: psutil.cpu_percent(percpu=True) # 获取每个CPU的使用率，类似TOP命令

 Out[9]: [43.3, 22.0, 42.0, 23.0]

 In [10]: top = [psutil.cpu_percent(interval=i, percpu=True) for i in range(10)] #设置每秒刷新时间间隔，统计十次的结果

 In [11]: top

 Out[11]:

 [[40.8, 19.7, 38.5, 20.7],

 [25.7, 5.9, 13.0, 5.0],

 [35.0, 15.6, 30.0, 14.4],

 [23.7, 7.0, 18.3, 7.4],

 [38.5, 17.0, 34.2, 17.5],

 [37.2, 19.6, 36.3, 20.0],

 [29.6, 16.6, 28.8, 16.8],

 [37.7, 19.0, 35.4, 18.7],

 [30.8, 16.3, 26.9, 16.5],

 [44.2, 27.9, 41.5, 28.6]]
```

获取内存信息

```
 In [13]: psutil.virtual_memory() #获取内存统计数据，单位bytes，我这里8G内存

 Out[13]: svmem(total=8589934592, available=1891045376, percent=78.0, used=6053986304, free=15130624, active=1878392832, inactive=1875914752, wired=2299678720)

 In [14]: psutil.swap_memory() # 获取swap的统计数据

 Out[14]: sswap(total=2147483648, used=1340866560, free=806617088, percent=62.4, sin=126090076160, sout=3524710400)
```

获取磁盘信息  

```
 In [17]: psutil.disk_partitions() #获取磁盘分区信息

 Out[17]: [sdiskpart(device='/dev/disk1', mountpoint='/', fstype='hfs', opts='rw,local,rootfs,dovolfs,journaled,multilabel')]

 In [20]: psutil.disk_usage('/') # 获取分区使用情况，这里使用了25.4%

 Out[20]: sdiskusage(total=499055067136, used=126482944000, free=372309979136, percent=25.4)

 In [22]: psutil.disk_io_counters() #磁盘IO情况

 Out[22]: sdiskio(read_count=7364142, write_count=6510641, read_bytes=282106464256, write_bytes=261763244544, read_time=2608778, write_time=1095259)
```

获取网络信息  

```
 In [23]: psutil.net_if_stats() # 获取网卡接口状态

 Out[23]:

 {'awdl0': snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_UNKNOWN: 0>, speed=0, mtu=1484),

 'bridge0': snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_UNKNOWN: 0>, speed=0, mtu=1500),

 'en0': snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_UNKNOWN: 0>, speed=0, mtu=1500),

 'en1': snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=0, mtu=1500),

 'en2': snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=0, mtu=1500),

 'gif0': snicstats(isup=False, duplex=<NicDuplex.NIC_DUPLEX_UNKNOWN: 0>, speed=0, mtu=1280),

 'lo0': snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_UNKNOWN: 0>, speed=0, mtu=16384),

 'p2p0': snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_UNKNOWN: 0>, speed=0, mtu=2304),

 'stf0': snicstats(isup=False, duplex=<NicDuplex.NIC_DUPLEX_UNKNOWN: 0>, speed=0, mtu=1280),

 'utun0': snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_UNKNOWN: 0>, speed=0, mtu=2000),

 'utun1': snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_UNKNOWN: 0>, speed=0, mtu=1352)}

 In [25]: psutil.net_if_stats().get("en0") #获取单个网卡en0的状态

 Out[25]: snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_UNKNOWN: 0>, speed=0, mtu=1500)

 In [26]: psutil.net_if_addrs() # 获取所有网卡的地址信息

 Out[26]:

 {'awdl0': [snic(family=<AddressFamily.AF_LINK: 18>, address='36:7d:f3:80:6e:4e', netmask=None, broadcast=None, ptp=None),

 snic(family=<AddressFamily.AF_INET6: 30>, address='fe80::347d:f3ff:fe80:6e4e%awdl0', netmask='ffff:ffff:ffff:ffff::', broadcast=None, ptp=None)],

 'bridge0': [snic(family=<AddressFamily.AF_LINK: 18>, address='4a:00:02:c0:33:70', netmask=None, broadcast=None, ptp=None)],

 'en0': [snic(family=<AddressFamily.AF_INET: 2>, address='192.168.0.101', netmask='255.255.255.0', broadcast='192.168.0.255', ptp=None),

 snic(family=<AddressFamily.AF_LINK: 18>, address='ac:bc:32:91:32:8b', netmask=None, broadcast=None, ptp=None),

 snic(family=<AddressFamily.AF_INET6: 30>, address='fe80::1476:ce7e:210a:2e32%en0', netmask='ffff:ffff:ffff:ffff::', broadcast=None, ptp=None)],

 'en1': [snic(family=<AddressFamily.AF_LINK: 18>, address='4a:00:02:c0:33:70', netmask=None, broadcast=None, ptp=None)],

 'en2': [snic(family=<AddressFamily.AF_LINK: 18>, address='4a:00:02:c0:33:71', netmask=None, broadcast=None, ptp=None)],

 'lo0': [snic(family=<AddressFamily.AF_INET: 2>, address='127.0.0.1', netmask='255.0.0.0', broadcast=None, ptp=None),

 snic(family=<AddressFamily.AF_INET6: 30>, address='::1', netmask='ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff', broadcast=None, ptp=None),

 snic(family=<AddressFamily.AF_INET6: 30>, address='fe80::1%lo0', netmask='ffff:ffff:ffff:ffff::', broadcast=None, ptp=None)],

 'p2p0': [snic(family=<AddressFamily.AF_LINK: 18>, address='0e:bc:32:91:32:8b', netmask=None, broadcast=None, ptp=None)],

 'utun0': [snic(family=<AddressFamily.AF_INET6: 30>, address='fe80::583c:77a0:6b93:b045%utun0', netmask='ffff:ffff:ffff:ffff::', broadcast=None, ptp=None)],

 'utun1': [snic(family=<AddressFamily.AF_INET: 2>, address='10.5.200.244', netmask=None, broadcast=None, ptp='10.5.200.244')]}

 \# 获取en0网卡的地址， 这里包括mac和ipv6地址

 In [40]: for addr in psutil.net_if_addrs().get("en0"):

 ...: print(addr.address)

 192.168.0.101

 ac:bc:32:91:32:8b

 fe80::1476:ce7e:210a:2e32%en0

 In [43]: psutil.net_io_counters() # 获取网络读写字节/包的个数

 Out[43]: snetio(bytes_sent=174614221, bytes_recv=586279725, packets_sent=863903, packets_recv=873583, errin=0, errout=0, dropin=0, dropout=0)

 In [45]: psutil.net_connections() # 获取网络连接信息，注意这里需要root权限。
```

获取进程信息：

```
 In [46]: psutil.pids() # 获取所有进程ID

 In [47]: psutil.Process(61) # 获取指定PID的进程信息

 Out[47]: psutil.Process(pid=61, name='dsAccessService', started='2018-02-26 09:57:04')

 In [49]: psutil.Process(45573).exe() # 获取进程的exe路径

 Out[49]: '/usr/local/Cellar/python3/3.6.3/Frameworks/Python.framework/Versions/3.6/Resources/Python.app/Contents/MacOS/Python'

 In [50]: psutil.Process(45573).name() # 获取进程名称

 Out[50]: 'Python'

 In [52]: psutil.Process(45573).cmdline() # 获取进程启动的命令

 Out[52]:

 ['/usr/local/Cellar/python3/3.6.3/Frameworks/Python.framework/Versions/3.6/Resources/Python.app/Contents/MacOS/Python',

 '/usr/local/bin/ptipython']

 In [56]: psutil.Process(45573).num_threads() # 获取进程的线程数量

 Out[56]: 3

 In [57]: psutil.Process(45573).environ() # 获取进程的环境变量信息
```

总结：  

使用psutil模块可以做到比较全面的对系统的监控，如果你正在考虑用Python做一个监控系统或者脚本工具，可以有些考虑此模块

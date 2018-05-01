### 安装 brew   

如果没有 brew，/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" 


### 启动和停止

#### 服务端启动

* 默认启动  
    如上，在命令redis-server即启动redis服务端。且接受客户端连接

* 根据设置启动
* 在 /usr/local/redis目录下建立bin，etc，db三个目录
* 把/usr/local/redis/src目录下的mkreleasehdr.sh，redis-benchmark， redis-check-rdb， redis-cli， redis-server拷贝到bin目录
* 在etc下,新建配置redis.conf，内容如下。
* /usr/local/redis下新建日志文件log-redis.log，并修改当前用户使用权限。sudo chown -R shoren /usr/local/redis/
* 启动服务端：redis-server /usr/local/redis/etc/redis.conf



```

                _._                                                  
           _.-``__ ''-._                                             
      _.-``    `.  `_.  ''-._           Redis 3.2.5 (00000000/0) 64 bit
  .-`` .-```.  ```\/    _.,_ ''-._                                   
 (    '      ,       .-`  | `,    )     Running in standalone mode
 |`-._`-...-` __...-.``-._|'` _.-'|     Port: 6379
 |    `-._   `._    /     _.-'    |     PID: 14447
  `-._    `-._  `-./  _.-'    _.-'                                   
 |`-._`-._    `-.__.-'    _.-'_.-'|                                  
 |    `-._`-._        _.-'_.-'    |           http://redis.io        
  `-._    `-._`-.__.-'_.-'    _.-'                                   
 |`-._`-._    `-.__.-'    _.-'_.-'|                                  
 |    `-._`-._        _.-'_.-'    |                                  
  `-._    `-._`-.__.-'_.-'    _.-'                                   
      `-._    `-.__.-'    _.-'                                       
          `-._        _.-'                                           
              `-.__.-'                                               

14447:M 24 Apr 17:57:33.215 # Server started, Redis version 3.2.5
14447:M 24 Apr 17:57:33.215 * The server is now ready to accept connections on port 6379
14447:M 24 Apr 17:57:33.215 - 0 clients connected (0 slaves), 956832 bytes in use
14447:M 24 Apr 17:57:38.257 - 0 clients connected (0 slaves), 956832 bytes in use

```


#### 关闭服务端

* 强行关闭  

    强行终止redis进程可能会导致数据丢失，因为redis可能正在将内存数据同步到硬盘中。

```hljs
ps axu|grep redis  ## 查找redis-server的PID
 kill -9 PID
```

* 命令关闭  

    向redis发送SHUTDOWN命令，即 `redis-cli SHUTDOWN` 。Redis收到命令后，服务端会断开所有客户端的连接，然后根据配置执行持久化，最后退出。

```hljs
## 启动redis-server，后台线程
AT8775:redis shoren$ redis-server /usr/local/redis/etc/redis.conf 
## 启动成功
AT8775:redis shoren$ ps axu|grep redis
shoren           14948   0.0  0.0  2434840    760 s000  S+   10:18上午   0:00.00 grep redis
shoren           14946   0.0  0.0  2452968   1492   ??  Ss   10:18上午   0:00.01 redis-server *:6379 
## 关闭服务器
AT8775:redis shoren$ redis-cli shutdown
##关闭成功
AT8775:redis shoren$ ps axu|grep redis
shoren           14952   0.0  0.0  2435864    772 s000  S+   10:19上午   0:00.01 grep redis
```

#### 启动客户端

* 默认启动  
    使用命令`redis-cli`启动客户端，按照默认配置连接Redis（127.0.0.1:6379）。

* 指定地址和端口号  
    使用命令 `redis-cli -h 127.0.0.1 -p 6379`

#### 关闭客户端

交互模式使用quit

```hljs
AT8775:redis shoren$ redis-cli -h 127.0.0.1 -p 6379
## 简单使用set、get命令
127.0.0.1:6379> set key value12
OK
127.0.0.1:6379> get key
"value12"
## 退出
127.0.0.1:6379> quit
AT8775:redis shoren$
```

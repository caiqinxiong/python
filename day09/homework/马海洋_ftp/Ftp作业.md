# Ftp作业

## 简介

> 客户端的每一次功能，都是整合服务端需要的数据，通过字典组合起来，`json`序列化，struct打包起来 然后发送给服务端，(解决了粘包问题) ，
>
> 服务端收到请求后，解包，获得需要的信息后，执行对应的功能
>
> 服务端的反射功能，是根据客户端发送的字典中，`cmd`对应的`value`执行。

## 测试账号

现只有一个测试账号。如果需要可以自行创建

+ 账号：mhy
+ 密码:   123



## Server端

### 程序结构：

#### **bin目录**：

+ **server_setup.py ** : 程序入口  初始化将项目导入了`sys.path`中

#### **conf目录**：

+ **settings.py**  : 配置文件  

#### **core目录**：(核心代码逻辑)

+ **action.py**：存放了程序的主要功能代码，解决客户端的功能请求
+ **file_read_write.py** :  文件读取和写入，主要设计的功能在于用户注册，和登陆时，和`userinfo`文件的交互
+ **get_md5.py** :  获取MD5值，主要有用户登陆时密码需要加密的get_md5函数，以及文件校验所需要的file_get_md5函数
+ **log4.py** : 存放了自定义的日志格式，别的地方调用，导入
+ **main.py **: 永远运行服务端
+ **send_recv.py**: 发送信息(指令) 和 接收信息。 以及 文件上传和下载需要的函数
+ server.py  :  构建了一个`socketserver` 服务端 

#### db目录：存放了home用户家目录   

+ userinfo文件 ： 用户登录信息
+ home  :  存放了用户的家目录 

#### log目录： 

+ program.log: log存放地

## Client端

### 程序结构

#### bin目录：


+ client_setup.py : 程序入口
#### conf目录：
+ settings.py ： 程序配置文件

#### core目录：

+ combination.py  一些组合功能   用户登录和主功能都继承的功能
+ main.py  客户端 主要逻辑代码
+  program.py   客户端主要功能代码，都需要请求服务端
+  user_login.py  用户登陆和注册功能
+ warpper.py   格式整理的一个装饰器函数



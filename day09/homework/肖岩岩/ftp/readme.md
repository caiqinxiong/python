# 作业题目：FTP（01）

### 作业需求

    1.多用户同时登陆
    2. 用户登陆，加密认证
    3. 上传/下载文件，保证文件一致性
    4. 传输过程中现实进度条
    5. 不同用户家目录不同，且只能访问自己的家目录
    6. 对用户进行磁盘配额、不同用户配额可不同
    7. 用户登陆server后，可在家目录权限下切换子目录
    8. 查看当前目录下文件，新建文件夹
    9. 删除文件和空文件夹
    10. 充分使用面向对象知识
    11. 支持断点续传

### 基本实现
    1.实现文件的上传、下载功能
    2.实现c/s端 密文登陆功能
    3.有效处理大文件
    4.md5进行文件已执行校验
    5.实现进度条功能
    6.充分使用面向对象的知识
    7.目录结构、流程图和readme
    代码写的清晰、健壮、可扩展


### 目录结构
* ftp
    * client (客户端)    
        * download_incomplete (记录未完成下载文件信息)
        * download (下载文件目录)
        * upload (待上传的文件)
        * client.py (客户端执行程序)

    * server (服务端)
        * bin
            * start.py (服务端启动程序)
        * conf
            * config.py (配置文件)
        * core
            * server.py (服务端程序)
        * db
            * userinfo (用户信息文件 用户名|md5加盐加密后的密码|空间配额)
        * home
            * root (用户家目录)
        * log
            * register.log(用户注册登录日志)
        * upload_incomplete(记录未完成上传文件信息)
        * upload(上传中的临时文件)

### 命令使用
+ help 命令帮助
+ mkdir folder 创建文件夹
+ rmdir folder 删除空文件夹
+ rmtree folder 删除文件夹
+ remove file 删除文件
+ unlink file 删除文件
+ mv old_file new_file 修改文件(夹)名
+ touch file 新建文件
+ cd folder 切换目录
+ ls 查看当前目录下的文件和文件夹
+ get file 下载文件
+ get_incomplete 未完成下载的文件
+ put file 上传文件
+ put_incomplete 未完成上传的文件
+ used 查看用户空间配额使用情况
+ pwd 查看当前目录
+ bye 退出程序

### 用户名root 密码1qazxsw2
### 用户名lily 密码1qazxsw2

### 执行顺序 
* 先执行服务端 ftp/server/bin/start.py
* 再执行服务端 ftp/client/client.py

* 默认存在的用户名:root 密码:1qazxsw2
* 选择用户登录或者新用户注册
* 登录或注册成功后,直接进入用户的家目录
* 可以通过help来查看都有哪些命令

### 上传下载说明
* 下载服务端的文件命令: get file_name
* 下载成功后,会在客户端的client/download/目录下看到已下载的文件

* 把上传的文件先放到客户端的client/upload/目录中
* 上传文件到服务端命令: put file_name
* 上传完成后,可以在用户的当前目录下看到已上传的文件


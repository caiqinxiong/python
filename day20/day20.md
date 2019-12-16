CMDB

管理资产信息

为了今后开发自动化运维的平台

代码架构:

 1. 客户端  client

    python

    ​	bin  conf  core(src)  lib log db

    1. sys.path  加入当前项目的目录

    2. importlib  导入模块  + 反射 

       兼容三种模式  + 可扩展 

       采集硬件资产可插拔式

    3. requests  发请求

       res= requests.post(url,data={})  

       res.text  res.json() res.content 

    4. 类的约束

       1. 抽象类 abc  
       2. 抛出异常

    5. 不同的模式下执行命令的方式不同

       agent    subprocess.getoutput()

       ssh   paramiko  

       salt   salt的接口

    6. 开放封闭原则

       开放 配置文件

       封闭  源码

    7. 错误详情

       ```
       import traceback
       traceback.format_exc()  # 更加详细的错误
       ```

 2. 服务端  server 

     django 

     api     

     fbv    cbv  

    1. from django.views.decorators.csrf import csrf_exempt, csrf_protect	

       csrf_exempt 不需要校验    CBV只能加在diapatch 上

       csrf_protect 需要进行校验

3. djangorestframework

   url  :  add_book    edit_book   

   url /v1/books/

   不同的请求方式 对应不同的操作

   get   /v1/books/      返回所有的书籍数据 {} 

   get   /v1/books/1    返回一个的书籍数据 {} 

   post    /v1/books/     返回一个的书籍数据 {} 
   put     /v1/books/1    返回一个的书籍数据 {} 
   delete      /v1/books/1   可以不返回数据

   出错后返回错误信息

   

   

   

   

   SSH 连接

   ssh-keygen  生成一对公钥和密钥

   ssh-copy-id root@c1.com  将公钥推送到c1.com的主机上  登录的用户名是root 

   

   

   ssh模式:

   1. 各个主机 和中控机 配置好ssh的连接
   2. 往数据库中录入新的主机名,中控机上的hosts文件需要修改 
   3.  每天定时启动中控机上的agent

    

主机名变更了:

c1.com    =>  c3.com 

主机名做唯一标识

注意:所有的主机名不能重复


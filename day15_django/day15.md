python基础

面向对象

网络并发

数据库

前端



网络



osi7 

应用层

表示层

会话层

传输层

网络层

数据链路层

物理层



socket 套接字 位于应用层和传输层之间的一个虚拟层,是一个接口

C/S   B/S  



百度的服务器   socket服务端

1. 起一个socket服务端
2. 绑定ip和端口
3. 监听
4. 接受数据
5. 返回数据
6. 断开连接

浏览器 socket客户端

4. 发送连接
5. 发送数据
6. 接受数据
7. 断开连接



<https://www.cnblogs.com/maple-shaw/articles/9060408.html>

http  端口 80

https 端口 443



```
'GET / HTTP/1.1
Host: 127.0.0.1:8000
Connection: keep-alive
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
Sec-Fetch-Site: none
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9

'
```



HTTP 规定了请求和应答的标准

请求方法:  8种  GET POST PUT DELETE HEAD OPTIONS TRACE CONNECT

发送 GET  获取数据

发送POST 提交数据



状态码  

1xx  请求接受了需进一步处理

2xx   成功

3xx  重定向  

4xx  请求的错误

5xx  服务器错误



url  

协议  域名(ip)  端口(http默认80  https 443 )   路径  查询参数(?k1=v1&k2=v2) 

请求的格式(request)

"请求方法 路径 HTTP/1.1

k1: v1

k2:v2



请求数据(请求体)"



响应的格式(response)

"HTTP/1.1 状态码 状态描述

k1: v1

k2:v2



响应数据(响应体)"



web框架的功能:

1. socket收发消息
2. 根据不同的路径返回不同的内容 
3. 返回动态页面(字符串的替换  模板渲染) 



django   2  3 (jinja2) 

flask   2  jinja2 

### django

1.下载

1. 命令行

   ```
   pip install django==1.11.25 -i https://pypi.tuna.tsinghua.edu.cn/simple/
   ```

   

2.创建项目

1. 命令行

   ```
   django-admin startproject 项目名称
   ```

   

2. pycharm创建

   file _>   new project   _>  django  _>  输入项目的目录 _> 选择解释器  _> create  

3.启动项目

 1. 命令行

    切换到项目的根目录下

    python manage.py runserver   #  127.0.0.1:8000

    python manage.py runserver 80   #  127.0.0.1:80

    python manage.py runserver 0.0.0.0:80   #  0.0.0.0:80

    

	2. pycharm

    选择django项目  点绿三角  (切记 没有右键启动项目)

4.django的配置

​	BASE_DIR  项目的根目录

​	INSTALLED_APPS  APP 

​	TEMPLATES  模板的配置

​		DIRS [ os.path.join(BASE_DIR, 'templates') ]

​	DATABASES  数据库

​	STATIC_URL = '/static/'  # 静态文件的别名

5.urls.py

​	url和函数的对应关系

```
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', index),
]
```

6.函数

```
from django.shortcuts import HttpResponse, render


def index(request):  # request请求对象 必须有
    # 业务逻辑
    # return HttpResponse('<h1>ok</h1>')   # 返回字符串
    return render(request, 'index.html')   # 返回模板  (模板写在templates文件夹中)
```

7.APP

新建APP

​	python manage.py startapp app名称

注册APP

settings.py

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app01.apps.App01Config',
]
```

​	

8.在settings中

注释掉csrf的中间件   可以提交POST请求

ORM

对应关系

类   _>    表

对象   _>   记录(数据行)

属性  _>   字段



9. ORM 



```python
ret = models.User.objects.all()  # QuerySet 对象列表
for i in ret:
    print(i.username,i.password,type(i.username))
    print(ret, type(ret))
ret = models.User.objects.get(password='123')  # 返回多个 查不到也报错
ret = models.User.objects.filter(password='123') # 获取所有满足条件的对象
```



10. 作业：

    完成登录示例和出版社的增删改查

    


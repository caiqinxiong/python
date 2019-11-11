## 内容回顾

### 1.django的命令

1. 下载

   pip  install  django==1.11.25 -i  源

2. 创建项目

   django-admin startproject 项目名称

3. 启动项目

   cd 项目的根目录

   python  manage.py  runserver  # 127.0.0.1:8000

   python  manage.py  runserver 80  # 127.0.0.1:80

   python  manage.py  runserver 0.0.0.0:80  #  0.0.0.0:80 

4. 创建app

   python manage.py  startapp  app名称

5. 数据库迁移的命令

   python manage.py  makemigrations  检测已经注册app下的models.py的变更记录

   python manage.py migrate   数据库迁移 

### 2.配置

BASE_DIR   项目的根目录

INSTALLED_APPS   注册的APP

```
'app01.apps.App01Config',  # app01
```

MIDDLEWARE

​	注释掉csrf   可以提交POST请求

TEMPLATES

​	'DIRS': [os.path.join(BASE_DIR, 'templates')]

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 连接什么样的数据库
        'NAME': 'bookmanager',			# 数据库的名称
        'HOST': '127.0.0.1',			# IP
        'PORT': 3306,				    # 端口	
        'USER': 'root',					# 用户名
        'PASSWORD': "123456"			# 密码
    }
}

替换MySQLdb模块
import pymysql
pymysql.install_as_MySQLdb()
```

静态文件的配置

```
STATIC_URL = '/static/'  # 静态文件的别名
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
```

## 今日内容

### 路由

<https://www.cnblogs.com/maple-shaw/articles/9282718.html>

动态路由

​	[0-9]  [a-zA-Z0-9]{5,9}  ^ $   \d   \w  ?  +  *  .  

分组:

​	url(r'^publisher_del/(\d+)/$', views.publisher_del),

​	从url地址上捕获参数,并且按照位置传参的方式传递给函数

命名分组:

​	url(r'^publisher_del/(?P<pk>\d+)/$', views.publisher_del),

​	从url地址上捕获参数,并且按照 关键字传参 的方式传递给函数

路由分发:

​	root_urlconf

```
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # /publisher/
    url(r'^app01/', include('app01.urls')),
    # url(r'^app02/', include('app02.urls')),


]
```

​	app01 urlconf

```
urlpatterns = [
    # 出版社的展示
    # publisher/
    url(r'^publisher/$', views.publisher_list),
    # 出版社的增加
    url(r'^publisher/add/$', views.publisher_add),
    # 出版社的删除
    url(r'^publisher_del/(?P<pk>\d+)/$', views.publisher_del),
    # 出版社的编辑
    url(r'^publisher_edit/$', views.publisher_edit),

]
```

URL的命名和反向解析

命名:

```
url(r'^publisher/add/$', views.publisher_add, name='pub_add'),
```

反向解析

模板:

​	{% url 'pub_add' %}    _>   '/app01/publisher/add/'

py文件:

​	from django.urls import reverse

​	reverse('pub')     _>   '/app01/publisher/'

分组

命名:

```
url(r'^publisher/del/(\d+)$', views.publisher_del, name='pub_del'),
```

反向解析

模板:

​	{% url 'pub_del' '10' %}    _>   '/app01/publisher/del/10/'

py文件:

​	from django.urls import reverse

​	reverse('pub_del',args=(11,))     _>    '/app01/publisher/del/11/'

命名分组

命名:

```
url(r'^publisher/del/(?P<pk>\d+)$', views.publisher_del, name='pub_del'),
```

反向解析

模板:

​	{% url 'pub_del' '10' %}    _>   '/app01/publisher/del/10/'   位置传参

​	{% url 'pub_del' pk='10' %}    _>   '/app01/publisher/del/10/'   关键字传参

py文件:

​	from django.urls import reverse

​	reverse('pub_del',args=(11,))     _>    '/app01/publisher/del/11/'     位置传参

​	reverse('pub_del',kwargs={'pk':'11'})     _>    '/app01/publisher/del/11/'   关键字传参

namespace

避免name重名

```
url(r'^app01/', include('app01.urls',namespace='app01')),
```

反向解析

reverse('app01:pub_del',args=(11,)) 

{% url 'app01:pub_del' '10' %}



### 视图

<https://www.cnblogs.com/maple-shaw/articles/9285269.html>

FBV  (function based view ) 

~~~
def index(request):
	# 逻辑
	return reponse
~~~



CBV (class based view ) 

```
from django.views import View
class PublisherAdd(View):
    
    def get(self,request,*args,**kwargs):
        # 处理GET请求的逻辑
        return response
    
    def post(self,request,*args,**kwargs):
        # 处理GET请求的逻辑
        return response
```

路由:

```
url(r'^publisher/add/$', views.PublisherAdd.as_view(), name='pub_add'),
```

as_view()的流程:

1. self.request= request
2. 通过反射获取对应请求方式(GET)对应的方法(get)



给CBV加装饰器的方法:

```
from django.utils.decorators import method_decorator  # 推荐使用
```

1. 加在方法上:

   ```python
   @method_decorator(timer)
   def get(self, request, *args, **kwargs):
   ```

2. 加在dispatch方法上

   ```python
   @method_decorator(timer)
   def dispatch(self, request, *args, **kwargs):
       ret = super().dispatch(request, *args, **kwargs)
       return ret
       
   @method_decorator(timer,name='dispatch')
   class PublisherAdd(View):
   ```

3. 加在类上

   ```pyhton 
   @method_decorator(timer,name='post')
   @method_decorator(timer,name='get')
   class PublisherAdd(View):
   ```

request

```
request.method  # 请求方法 GET POST
request.GET     # url上的查询参数  /dd/?id=1&name=alex
request.POST    # POST请求提交的数据  {}  编码是urlencode才有数据
request.path_info  # 路径信息   不包含IP和端口 也不包含查询参数
request.body    # 请求体  原始数据
request.COOKIES   cookie
request.session   session
request.FILES   # 上传的文件
request.META   # 头信息   HTTP_  - _> _ 大写

request.get_full_path()    # 路径信息   不包含IP和端口 包含查询参数  
request.is_ajax()   # 是否ajax请求
```

response

```
HttpReponse('字符串')  # 返回字符串
render(request,'模板的路径',{})   #  返回一个HTML页面 
redirect(重定向的地址)   重定向 # 响应头  Location:地址
JsonResponse(ret,safe=False)   # json序列化  默认传字典   非字典 safe=False 
```





### 模板

<https://www.cnblogs.com/maple-shaw/articles/9333821.html>

{{  变量 }}   # 没有 []  ()  写法

{{ 变量.   }}    .索引  .key   .属性 .方法

.key   >   .属性 .方法  >    .索引

filter 过滤器

{{ 变量|filter  }}   {{ 变量|filter:'参数'  }}

内置的过滤器

default 

```
{{ xxx|default:"没有这个变量" }}  # 变量不存在或者为空时候使用默认值
```

filesizeformat 

文件大小的格式化   最小单位bytes  最大PB 

add

```
{{ a|add:b }}  # 数字的加减法  字符串的拼接  列表的拼接
```

length 

{{ [1,32,]|length }}   # 2 

slice  切片

```
{{ l1|slice:'::-1' }}
```

first  last 

取第一个或最后一个元素

truncatechars  truncatewords

```
{{ "如果字符串字符多于指定的字符数量，那么会被截断。截断的字符串将以可翻译的省略号"|truncatechars:'10' }}

{{ "如果 字符串 字符 多于 指定的字符数量，那么会被截断。截断的字符串将以可翻译的省略号"|truncatewords:'4' }}
```

date 

```
{{ now|date:'Y-m-d H:i:s' }}
```

可以配置:

```
USE_L10N = False
DATETIME_FORMAT = 'Y-m-d H:i:s'
DATE_FORMAT = 'Y-m-d'
TIME_FORMAT = 'H:i:s'
```

safe

告诉django,当前的内容是安全的,不需要做转义





标签  tag



{% for  i  in list %}

​	{{ forloop.counter }}

​	{{   i  }}

{%  endfor %}







if 

```
{% if 3 < 1 %}
    真
{% elif 3 > 2 %}
        elif
{% else %}
    假
{% endif %}
```

if 判断不支持算数运算  不支持连续判断



在form标签中使用{% csrf_token %}标签,就可以提交POST请求.

母版和继承

定义母版:

 	1. 定义一个HTML页面,页面包含多个页面的公共部分
 	2. 定义block块,让子页面进行复写.

继承:

 	1. 子页面在第一行写{% extends '母版的文件名' %}
 	2. 复写母版中定义的block块.

注意点:

1. {% extends "base.html" %} 母版的名字带引号  不带引号会当成变量

2. {% extends "base.html" %} 的上面不要写内容,要显示的内容只写到block块中
3. 在母版中多定义写block块  , css  js 


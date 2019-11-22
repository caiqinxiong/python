## 内容回顾

路由

url和函数的对应关系

urls.py

```
url(r'^publisher/$', views.publisher_list, name='pub'),
```

正则表达式

^  $  \d  \w {}  ? + *   

分组和命名分组     \?pk=2

^publisher/(\d+)\      按照位置传参

^publisher/(?P<pk>\d+)\      按照关键字传参

路由分发

```
url(r'^app01/', include('app01.urls')),
```

url的命名和反向解析

```
url(r'^publisher/$', views.publisher_list, name='pub'),
url(r'^publisher_deit/(\d+)/$', views.publisher_deit, name='pub_edit'),
url(r'^publisher_del/(?P<pk>\d+)/$', views.publisher_del, name='pub_del'),
```

反向解析

 模板 

{% url  'pub'  %}   _>  /app01/publisher/

{% url  'pub_edit'  pub.pk  %}   _>  /app01/publisher_deit/1/

{% url  'publisher_del'  pub.pk  %}   _>  /app01/publisher_del/1/

{% url  'publisher_del'  pk=pub.pk  %}   _>  /app01/publisher_del/1/



py文件

from django.urls import reverse

reverse('pub')  _> /app01/publisher/

reverse('pub_edit',args=('1',))   _>  /app01/publisher_deit/1/

reverse('publisher_del',args=('1',))   _>  /app01/publisher_del/1/

reverse('publisher_del',kwargs={'pk':1}   _>  /app01/publisher_del/1/

namespace

url(r'^app01/', include('app01.urls',namespace='app01')),

reverse('app01:pub')  _> /app01/publisher/

视图

FBV  

```python
def publisher_add(request,*args,**kwargs):
	
	return reposnse

url(r'^publisher_add/$', views.publisher_add, name='pub_add'),

```

CBV

```python 
from django.views import View
class PublisherAdd(View):

	def get(self,request,*args,**kwargs):
        self.request
        return reposnse
    
    def post(self,request,*args,**kwargs):
        return reposnse
    
 url(r'^publisher_add/$', views.PublisherAdd.as_view(), name='pub_add'),
```

加装饰器

from django.utils.decorators import method_decorator

1. 加在方法上

   ```python 
   @method_decorator(timmer)
   def get(self,request,*args,**kwargs):
   ```

2. 加在类上

   ```python 
   @method_decorator(timmer,name='post')
   @method_decorator(timmer,name='get')
   class PublisherAdd(View):
   ```

3. 加在dispatch方法上

   ```python
   @method_decorator(timmer,name='dispatch')
   class PublisherAdd(View)
   ```

request

```python
request.method   # 请求方法  GET POST
request.GET      #  查询参数   /xxx/?id=1&name=alex   {}
request.POST     # post请求提交的参数   {}  urlencode
request.FILES    # 上传的文件 form-data 
request.body     # 请求体  bytes 原始的数据
request.path_info  #  路径信息  路径  不包含IP和端口  也不包含参数
request.COOKIES  # cookie 
request.session  # session 
request.META     # {}  请求头相关的信息  HTTP_ 小写_>大写  - _> _

request.get_full_path()  # 路径信息  路径  不包含IP和端口  包含参数
request.is_ajax()   # 是否是ajax请求
```

response 

```
render(request,'模板的文件名',{})  # 返回一个HTML页面
redirect('地址')  # 重定向  Location:地址
HttpResponse('字符串')   # 简单返回字符串 text/html
JsonResponse({})    JsonResponse([],safe=False) content-type: app/json
```

模板

{{ 变量  }}    {%%}  标签

变量      不再有[]  ()

render(request,'模板的文件名',{'k1':v1})

{{ k1 }}  

.key   .属性或方法  .索引

过滤器

{{ k1|filter }}    {{ k1|filter:'arg' }}  

内置的过滤器

default     add   slice:'::'   filesizeformat  date:'Y-m-d H:i:s'  safe 

```python
USE_L10N = False
DATETIME_FORMAT = 'Y-m-d H:i:s'
DATE_FORMAT = 'Y-m-d'
TIME_FORMAT = 'H:i:s'
```

标签

```
{% for i in list %}
	{{ i }}  {{ forloop }}
{% endfor %}

{% for i in list %}
	{{ i }}  {{ forloop }}
	
{% empty %}
	
{% endfor %}



{% if 条件 %}

{% elif 条件 %}

{% else %}

{% endif %}

if的注意点:不支持算数运算  不支持连续判断  


{% csrf_token %}
放在form表单中,有一个隐藏的input标签,name='csrfmiddlewaretoken'

```

母版和继承

母版:

1. 定义一个HTML页面,将多个页面的公共部分过来    base.html
2. 在页面中定义多个block块

继承:

1. 写子页面,在第一行写{% extends 'base.html' %}
2. 重写block块

组件

将一小段HTML代码写入文件 nav.html

{% include 'nav.html' %}

静态文件的引入

```
{% load static %}
{% static '相对路径' %}
```



外键

描述一对多的关系

```python
class Book(models.Model):
    title = models.CharField(max_length=32)
    pub = models.ForeignKey('Publisher', on_delete=models.CASCADE)
    #  CASCADE 级连删除   on_delete 2.0 版本后是必填项
    # SET
    # SET_DEFAULT
    # SET_NULL    null=True
    # DO_NOTHING
    # PROTECT
```

查询:

```python 
all_books = models.Book.objects.all()  # [book_obj]
    for book in all_books:
        print(book.pk)
        print(book.title)
        print(book.pub,type(book.pub))   # book.外键  _>  所关联的对象
        print(book.pub_id)   # 从数据库中获取所关联的对象id
```

新增

```python 
models.Book.objects.create(title=title,pub=models.Publisher.objects.get(pk=pub_id))
models.Book.objects.create(title=title, pub_id=pub_id)
```

编辑

```python
book_obj.title = title
# book_obj.pub = models.Publisher.objects.get(pk=pub_id)
book_obj.pub_id = pub_id
book_obj.save()

models.Book.objects.filter(pk=pk).update(title=title, pub_id=pub_id)

```

删除

```python
def delete(request,table,pk):

    model_class = getattr(models,table.capitalize())
    model_class.objects.get(pk=pk).delete()
    return redirect(reverse(table))

```



ORM

对应关系

类   _>   表

对象   _>   数据

属性  _>   字段

常用字段:

AutoField

IntegerField  整数

CharField  字符串

DateField   DatetimeField

​	auto_now：每次修改时修改为当前日期时间。

​	auto_now_add：新创建对象时自动添加当前日期时间。

BooleanField  布尔值

TextField     文本类型

ImageField   图片

FloatField   浮点型

DecimalField  10进制小数

字段的参数

```
      null                数据库中字段是否可以为空
    ``db_column           数据库中字段的列名
    ``default             数据库中字段的默认值
    ``primary_key         数据库中字段是否为主键
    ``db_index            数据库中字段是否可以建立索引
    ``unique              数据库中字段是否可以建立唯一索引
 
```

```
    ``verbose_name      字段名称
    ``blank             否允许用户输入为空
    ``editable          是否可以编辑
    ``choices           显示选择框的内容，
```

表

```python
class Meta:
    # 数据库中生成的表名称 默认 app名称 + 下划线 + 类名
    db_table = "user"

    # admin中显示的表名称
    verbose_name = '个人信息'

    # verbose_name加s
    verbose_name_plural = '所有用户信息'
	
    # 联合索引
    # index_together = [
    #     ("name", "age"),  # 应为两个存在的字段
    # ]
    #
    # # 联合唯一索引
    # unique_together = (("name", "age"),)  # 应为两个存在的字段
```



```python
# 执行原生SQL
#更高灵活度的方式执行原生SQL语句
from django.db import connection, connections
cursor = connection.cursor() 
# cursor = connections['default'].cursor()
cursor.execute("""SELECT * from auth_user where id = %s""", [1])
row = cursor.fetchone()
```









使用admin的步骤

1. 创建超级用户

   python manage.py createsuperuser

   输入用户名和密码

2. 在APP下的admin.py中注册model

   ```
   from django.contrib import admin
   from app02 import models
   # Register your models here.
   admin.site.register(models.User)
   ```

3. 登录admin

   对表做增删改查
















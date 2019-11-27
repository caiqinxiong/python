ORM

对象关系映射

对应关系:

​	类   _>   表

​	对象 _>  数据

​	属性 _> 字段

```
class Book(models.Model):
	name = models.CharField(max_length=32)
```

常用的字段:

```
AutoField
CharField
BooleanField
DateTimeField  DateField   auto_now  auto_now_add
DecimalField   十进制小数
IntegerField  整型
TextField  文本类型
```

```
max_length  指定长度
null   True 数据库可以为空
blank  True 用户可以输入为空(form)
verbose_name   提示的中文
unique    唯一约束
db_index  索引
default   默认值
choices   可以选择的内容 ((1,'xxx'),())
db_column  列名 
```

model的参数

```
class Book(models.Model):
	name = models.CharField(max_length=32)
	
	class Meta:
		db_table = 'book'
		
		index_together = ('name', 'xxx')
        unique_together = ('name', 'xxx')
```

查询 必知必会13条

返回对象列表  QuerySet

```
all()   查询所有的数据
filter()   查询所有满足条件的对象
exclude()  查询所有不满足条件的对象
values()   [{}]    获取字段的名和值 
values_list()   [()]    获取字段的值 
order_by()  排序  降序 -  
reverse()  对已经排序的列表进行翻转
distinct()  去重 
```

返回对象

```
get()  获取一个满足条件的对象  获取不到或者多个就报错
first()   获取第一个对象
last()    获取最后一个对象
```

返回布尔值的

```
exists()  查询数据是否存在
```

返回数字

```
count()  计数
```

单表的双下划线

```
field__gt  大于
field__gte  大于等于
field__lt  小于于
field__lte  小于等于
field__range=[3,6]    3-6
field__in=[3,6]     
field__contains    包含  like  
field__icontains   包含  like  忽略大小写
field__startswith    以什么开头 
field__istartswith   以什么开头   忽略大小写
field__endswith    以什么结尾   like  
field__iendswith   以什么结尾 忽略大小写
field__isnull = False 
field__year  
```

多对多

```
class Author(models.Model):
    name = models.CharField(max_length=32)
    books = models.ManyToManyField('Book')  # 这个属性不会生成字段  但是会生成第三张表
```

查询 

```
author_obj.name 
author_obj.books   # 关系管理对象 
author_obj.books.all()   # 关联的所有的书籍对象  对象列表

book_obj.pub   #  出版社的对象
```

新增

```
author_obj =Author.objects.create(name='小强')
author_obj.books.set([id,id])   # 设置多对多关系
author_obj.books.set([对象,对象])   # 设置多对多关系
```

编辑

```
author_obj =Author.objects.filter(name='小强').first()
author_obj.name= 'xxx'
author_obj.save()

author_obj.books.set([id,id])   # 设置多对多关系
author_obj.books.set([对象,对象])   # 设置多对多关系
```

删除

```
Author.objects.filter(name='小强').delete()
Author.objects.filter(name='小强').first().delete()
```





cookie 

定义:

保存在浏览器本地上的一组组键值对

特性:

1. 由服务器让浏览器进行设置的
2. 访问相应的网站携带对应的cookie

Django的操作:

1. 设置

   ```
   response.set_cookie(key,value,max_age=5,path)
   response.set_signed_cookie(key,value,salt='xxxx',...)
   
   ```

2. 获取

   ```
   request.COOKIES  {}   value是字符串 
   request.get_signed_cookie('is_login',salt='xxxx',default='')
   ```

3. 删除



session 

定义:

保存在服务器上的一组组键值对,必须依赖cookie

为什么要有session?

1. cookie在浏览器本地,不安全
2. cookie的大小收到限制

Django中操作session

1. 设置

   ```
   request.session[key] =value
   request.session.setdefault('k1',123) # 存在则不设置
   ```

2. 获取

   ```
   request.session[key]
   request.session.get(key)
   ```

3. 删除

   ```
   del request.session['k1']
   request.session.pop('k1')
   
   request.session.delete()  # 删除所有的session数据  不删除cookie 
   request.session.flush()   # 删除所有的session数据  删除cookie 
   ```

   

4. 其他

   ```
   # 将所有Session失效日期小于当前日期的数据删除
   request.session.clear_expired()
   request.session.set_expiry(value) #如果value是个整数，session会在些秒数后失效。
   ```

5. 配置

   ```
   from django.conf import global_settings
   
   SESSION_COOKIE_NAME = 'session'   	# cookie的名字
   SESSION_SAVE_EVERY_REQUEST = True    # 每次请求都更新session数据
   SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # 浏览器关闭session失效
   SESSION_ENGINE = 'django.contrib.sessions.backends.db'   # 存储的位置
   #  数据库 文件  缓存 缓存+数据库 加密cookie
   ```

额外的使用redis存储session

https://django-redis-chs.readthedocs.io/zh_CN/latest/





中间件:

五个方法  4个特点

process_request(self,request)

参数: 

​			request  请求对象 

执行时间:  

​			视图执行之前

执行顺序:

​			按照注册的顺序  顺序执行

返回值

​			None:   正常流程

​			HttpResponse : 后面的中间件的process_request 、路由、视图都不执行,执行当前中间的process_response方法



process_response(self,request,response)

参数: 

​			request  请求对象 

​			response   响应对象

执行时间:  

​			视图执行之后

执行顺序:

​			按照注册的顺序  倒叙执行

返回值

​			HttpResponse : 必须返回





process_view(self, request, view_func, view_args, view_kwargs)

参数: 

​			request  请求对象 

​			view_func  视图函数

​			view_args   视图函数的位置参数

​			view_kwargs 视图函数的关键字参数

执行时间:  

​			视图执行之前,路由匹配之后的

执行顺序:

​			按照注册的顺序  顺序执行

返回值

​			None:   正常流程

​			HttpResponse : 后面的中间件的process_view、视图都不执行,执行最后一个中间件的process_response方法



process_exception(self, request, exception)

参数: 

​			request  请求对象 

​			exception  错误对象

执行时间(触发条件):  

​			视图函数报错的时候

执行顺序:

​			按照注册的顺序  倒叙执行

返回值

​			None:   当前中间件没有处理异常,交由下一个中间件处理.如果所有的中间件都没有处理,Django处理异常

​			HttpResponse : 已经处理好异常,后续的中间件的process_exception不用执行了,执行所有中间件的process_response



process_template_response(self,request,response)

```
from django.template.response import TemplateResponse
```

参数: 

​			request  请求对象 

​			response   TemplateResponse对象

执行时间(触发条件):  

​			视图函数返回TemplateResponse对象

执行顺序:

​			按照注册的顺序  倒叙执行

返回值

​			Response : 必须返回

在方法内可以修改模板和变量:

```
response.template_name = 'index1.html'
response.context_data['age'] = 1000
```


















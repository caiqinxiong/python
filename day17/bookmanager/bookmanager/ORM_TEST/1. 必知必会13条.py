import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bookmanager.settings")

import django

django.setup()

from app02 import models

# all()  获取所有的数据  QuerySet   [ 对象,对象]
ret = models.User.objects.all()

# get()  获取一条数据  对象    查询不到或者多个的时候就报错
ret = models.User.objects.get(pk=1)

# filter()  获取满足条件的所有对象  QuerySet   [ 对象,对象]
ret = models.User.objects.filter(pk=1)

# exclude()  获取不满足条件的所有对象  QuerySet   [ 对象,对象]
ret = models.User.objects.exclude(pk=1)

# order_by() 排序  QuerySet   [ 对象,对象]   默认升序  降序给字段前+负号
ret = models.User.objects.order_by('age','uid')

# reverse() 反转  QuerySet   [ 对象,对象]  对已经排序的QuerySet生效
ret = models.User.objects.all().order_by('uid').reverse()

#  values()   不加参数 获取所有的字段名和值   QuerySet   [ 字典,字典]
#  values('uid','name')    指定参数   获取指定字段的名和值
ret  = models.User.objects.all().values('uid','name')
# for i in ret:
# #     print(i)
# #     print(i['uid'],i['name']) # i.uid i.name


#  values_list()   不加参数 获取所有的字段值   QuerySet   [ (),()]
#  values_list('name','uid')    指定参数   获取指定字段的值
ret  = models.User.objects.all().values_list('name','uid')
# for i in ret:
#     print(i)

# distinct  去重
ret  = models.User.objects.all().values('age').distinct()

#  first  取第一个元素  没有的话就是None
ret  = models.User.objects.filter(name='alex',age=85).first()

#  last  取最后一个元素  没有的话就是None
ret  = models.User.objects.filter(name='alex',age=85).last()

#  count  计数  len() __len__  count 比 len效率高
ret  = models.User.objects.all().count()

# exists  判断查询结果是否存在
ret = models.User.objects.filter(name='alex',age=84).exists()

print(ret)


"""
返回是QuerySet
all  
filter
exclude
order_by
reverse
values
values_list
distinct

返回对象
get
first
last 

返回数字
count

返回布尔值
exists
"""




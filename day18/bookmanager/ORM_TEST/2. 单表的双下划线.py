import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bookmanager.settings")

import django

django.setup()

from app02 import models
ret = models.User.objects.filter(pk=2)
ret = models.User.objects.filter(pk__gt=2)  # greater than  大于
ret = models.User.objects.filter(pk__gte=2)  # greater than  equal  大于等于
ret = models.User.objects.filter(pk__lt=2)  # less than  小于
ret = models.User.objects.filter(pk__lte=2)  # less than equal 小于等于
ret = models.User.objects.filter(pk__in=[1,3])  # 成员判断
ret = models.User.objects.filter(pk__range=[1,3])  # 范围
ret = models.User.objects.filter(name__contains='alex')  # like
ret = models.User.objects.filter(name__icontains='alex')  # 忽略大小写  包含

ret = models.User.objects.filter(name__startswith='alex')  # 以莫某开头
ret = models.User.objects.filter(name__istartswith='alex')  # 以莫某开头  忽略大小写

ret = models.User.objects.filter(name__endswith='alex')  # 以莫某开头
ret = models.User.objects.filter(name__iendswith='alex')  # 以莫某开头  忽略大小写

ret = models.User.objects.filter(age__isnull=False)  # name字段是否为null

ret = models.User.objects.filter(bitrh__year='2020')  # year

ret = models.User.objects.filter(bitrh__contains='2020-11-17')
print(ret)
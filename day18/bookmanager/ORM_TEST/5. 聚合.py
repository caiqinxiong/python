import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bookmanager.settings")

import django

django.setup()

from app01 import models

from django.db.models import Max, Min, Sum, Avg, Count

ret = models.Book.objects.filter(pk__lte=2).aggregate(min=Min('price'), max=Max('price'), )

# 统计每一本书的作者个数
ret = models.Book.objects.annotate(Count('author')).values()

# 统计出每个出版社买的最便宜的书的价格
ret = models.Publisher.objects.annotate(Min('book__price')).values()

ret = models.Book.objects.values('pub__name').annotate(min=Min('price'))

# 统计不止一个作者的图书

ret = models.Book.objects.annotate(count=Count('author')).filter(count__gt=1)

# 查询各个作者出的书的总价格
ret = models.Author.objects.annotate(Sum('books__price')).values()

ret = models.Book.objects.values('author__name', 'author').annotate(Sum('price'))

print(ret)

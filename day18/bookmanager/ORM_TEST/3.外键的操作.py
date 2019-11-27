import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bookmanager.settings")

import django

django.setup()

from  app01 import models

# 基于对象的查询
# 正向查询  多_> 一
book_obj = models.Book.objects.get(pk=1)
# print(book_obj)
# print(book_obj.pub)
#  反向查询  一 _>  多
# 没有指定related_name
# 表名_set 关系管理对象
# 表名_set.all() 关系所有的对象
pub_obj = models.Publisher.objects.get(pk=1)
# print(pub_obj.book_set,type(pub_obj.book_set))  # 关系管理对象
# print(pub_obj.book_set.all())  # 关系所有的对象

# related_name = 'books'
# print(pub_obj.books)  # 关系管理对象
# print(pub_obj.books.all())  # 关系管理对象


# 基于字段的查询
ret = models.Book.objects.filter(pub__name='马蓉出版社')

# 不指定 related_name='books'
# ret = models.Publisher.objects.filter(book__title='小强和马蓉的幸福生活')
# 指定 related_name='books'
# ret = models.Publisher.objects.filter(books__title='小强和马蓉的幸福生活')
# 指定 related_query_name='book'
ret = models.Publisher.objects.filter(book__title='小强和马蓉的幸福生活').first()


ret.books.all()
# ret.books.set(models.Book.objects.filter(pk__in=[1,2]))   # 对象
# ret.books.remove(*models.Book.objects.filter(pk__in=[3,]))
ret.books.clear()

print(ret)



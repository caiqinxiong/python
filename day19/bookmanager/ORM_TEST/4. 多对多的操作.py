import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bookmanager.settings")

import django

django.setup()

from app01 import models

author_obj = models.Author.objects.get(name='小强')
print(author_obj.books.all())

# book_obj = models.Book.objects.get(title='小强和马蓉的幸福生活')
# print(book_obj.author_set.all())

# all()   获取所有关联的对象

# set()  设置多对多关系 重新设置
# author_obj.books.set([])
# add()  新增关系
# author_obj.books.add(1,2)
# author_obj.books.add(*models.Book.objects.filter(id__in=[1, 2]))

# remove() 删除关系

# author_obj.books.remove(1,2)
# author_obj.books.remove(*models.Book.objects.filter(id__in=[1, 2]))

# clear() 清空所有的关系
# author_obj.books.clear()

# create()
# author_obj.books.create(title='小强的夜生活',pub_id=1)

book_obj = models.Book.objects.get(title='小强的夜生活')
book_obj.author_set.create(name='渣哥')


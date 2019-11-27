import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_homework.settings")

import django
django.setup()
from app01 import models

# 查找所有书名里包含金老板的书
ret = models.Book.objects.filter(title__contains='金老板')

# 查找出版日期是2018年的书

ret = models.Book.objects.filter(publish_date__year='2018')
ret = models.Book.objects.filter(publish_date__contains='2018')

# 查找出版日期是2017年的书名
ret = models.Book.objects.filter(publish_date__contains='2017').values('title')
ret = models.Book.objects.filter(publish_date__contains='2017').values_list('title')

# 查找价格大于10元的书
ret= models.Book.objects.filter(price__gt=10)
# 查找价格大于10元的书名和价格
ret= models.Book.objects.filter(price__gt=10).values_list('title','price')

# 查找memo字段是空的书

ret= models.Book.objects.filter(memo__isnull=True)

#
# 查找在北京的出版社
# 查找名字以沙河开头的出版社
#
# 查找“沙河出版社”出版的所有书籍
# 查找每个出版社出版价格最高的书籍价格
# 查找每个出版社的名字以及出的书籍数量
#
# 查找作者名字里面带“小”字的作者
# 查找年龄大于30岁的作者
# 查找手机号是155开头的作者
# 查找手机号是155开头的作者的姓名和年龄
#
# 查找每个作者写的价格最高的书籍价格
# 查找每个作者的姓名以及出的书籍数量
#
# 查找书名是“跟金老板学开车”的书的出版社
# 查找书名是“跟金老板学开车”的书的出版社所在的城市
# 查找书名是“跟金老板学开车”的书的出版社的名称
# 查找书名是“跟金老板学开车”的书的出版社出版的其他书籍的名字和价格
#
# 查找书名是“跟金老板学开车”的书的所有作者
# 查找书名是“跟金老板学开车”的书的作者的年龄
# 查找书名是“跟金老板学开车”的书的作者的手机号码
# 查找书名是“跟金老板学开车”的书的作者们的姓名以及出版的所有书籍名称和价钱
#
print(ret)
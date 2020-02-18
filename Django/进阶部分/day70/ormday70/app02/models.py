from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


# 出版社
class Publisher(models.Model):
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=32)

    def __str__(self):
        return self.name


# 书
class Book(models.Model):
    title = models.CharField(max_length=32)
    publish_date = models.DateField(auto_now_add=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    # 创建外键，关联publish
    publisher = models.ForeignKey(to="Publisher")

    def __str__(self):
        return self.title


# 作者
class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    phone = models.IntegerField()
    detail = models.OneToOneField(to="AuthorDetail")

    def __str__(self):
        return self.name


# 自己动手 创建作者和书关联的第三张表
# 此时 在ORM层面 作者和书就没有多对多的关系了
class Author2Book(models.Model):
    id = models.AutoField(primary_key=True)
    # 作者id
    author = models.ForeignKey(to="Author")
    # 书id
    book = models.ForeignKey(to="Book")

    class Meta:
        # 建立唯一约束
        unique_together = ("author", "book")


# 作者详情
class AuthorDetail(models.Model):
    # 爱好
    hobby = models.CharField(max_length=32)
    # 地址
    addr = models.CharField(max_length=128)


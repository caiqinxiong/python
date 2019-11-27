from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=32,unique=True)

    def __str__(self):
        return self.name

    __repr__ = __str__


class Book(models.Model):
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=5,decimal_places=2) # 999.99
    kucun = models.IntegerField()
    sale = models.IntegerField()
    pub = models.ForeignKey('Publisher', null=True,on_delete=models.CASCADE,related_name='books',related_query_name='book' )  # pub_id
    # authors = models.ManyToManyField('Author')
    #  CASCADE 级连删除   on_delete 2.0 版本后是必填项
    # SET(1)
    # SET_DEFAULT    default=1, 默认值
    # SET_NULL    null=True  blank=True
    # DO_NOTHING
    # PROTECT

    def __str__(self):
        return self.title

    __repr__ = __str__


class Author(models.Model):
    name = models.CharField(max_length=32)
    books = models.ManyToManyField('Book')  # 这个属性不会生成字段  但是会生成第三张表

    def show_books(self):
        return ' '.join(["《{}》".format(book.title) for book in self.books.all()])

    def __str__(self):
        return self.name

    __repr__ = __str__

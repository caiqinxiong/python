from django.db import models

# Create your models here.


class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, unique=True, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "publisher"


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    # 外键
    publisher = models.ForeignKey(to="Publisher", on_delete=models.CASCADE, db_constraint=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "book"


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    books = models.ManyToManyField(to="Book")

    def __str__(self):
        return self.name


class FixedCharField(models.Field):
    """
    自定义的char类型的字段类
    """
    def __init__(self, max_length, *args, **kwargs):
        self.max_length = max_length
        super(FixedCharField, self).__init__(max_length=max_length, *args, **kwargs)

    def db_type(self, connection):
        """
        限定生成数据库表的字段类型为char，长度为max_length指定的值
        """
        return 'char(%s)' % self.max_length


class Person(models.Model):
    name = models.CharField(max_length=32)
    new_name = FixedCharField(max_length=64, default="张三")  # char(64)
    age = models.IntegerField(default=18)
    birthday = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "person"

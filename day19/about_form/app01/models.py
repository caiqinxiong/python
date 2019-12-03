from django.db import models


# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField('书名',max_length=32,unique=True)
    pub = models.ForeignKey(Publisher, on_delete=models.CASCADE,verbose_name='出版社')
    authors = models.ManyToManyField('Author',verbose_name='作者')

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

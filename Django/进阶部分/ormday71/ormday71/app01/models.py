from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=16)
    age = models.IntegerField()
    salary = models.IntegerField()
    province = models.CharField(max_length=32)
    dept = models.CharField(max_length=16)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "employee"


class Employee2(models.Model):
    name = models.CharField(max_length=16)
    age = models.IntegerField()
    salary = models.IntegerField()
    province = models.CharField(max_length=32)
    dept = models.ForeignKey(to="Dept")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "employee2"


class Dept(models.Model):
    name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.name


    class Meta:
        db_table = "dept2"



class Author(models.Model):
    name = models.CharField(max_length=32)
    books = models.ManyToManyField(to="Book")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "author"


class Book(models.Model):
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "book"




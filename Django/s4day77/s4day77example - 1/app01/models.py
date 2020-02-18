from django.db import models

class Classes(models.Model):
    title = models.CharField(max_length=32)


class Student(models.Model):
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    age = models.IntegerField(max_length=32)
    cls = models.ForeignKey('Classes')


class Teacher(models.Model):
    tname = models.CharField(max_length=32)
    c2t = models.ManyToManyField('Classes')

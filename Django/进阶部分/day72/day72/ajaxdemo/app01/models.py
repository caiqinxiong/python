from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=16)
    age = models.IntegerField()
    birthday = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

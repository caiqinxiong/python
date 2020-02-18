from django.db import models

# Create your models here.


class UserInfo(models.Model):
    name = models.CharField(max_length=32, unique=True, null=False)
    pwd = models.CharField(max_length=32, default="doushidsb")
    email = models.EmailField(null=True)
    mobile = models.CharField(max_length=11, null=True)

    def __str__(self):
        return self.name



class City(models.Model):
    name = models.CharField(max_length=16, null=False, unique=True)

    def __str__(self):
        return self.name


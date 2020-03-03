from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    college = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    tel = models.CharField(max_length=11)
    email = models.EmailField(default=None,blank=True,null=True,unique=True, verbose_name='邮箱')

    class Meta(AbstractUser.Meta):
        pass



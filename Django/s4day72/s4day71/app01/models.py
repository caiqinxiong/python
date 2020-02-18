from django.db import models


class UserType(models.Model):
    """
    用户类型
    """
    title = models.CharField(max_length=32)

class UserInfo(models.Model):
    """
    用户表
    """
    name = models.CharField(max_length=16)
    age = models.IntegerField()
    ut = models.ForeignKey('UserType')

    def __str__(self):
        return "%s-%s" %(self.id,self.name,)
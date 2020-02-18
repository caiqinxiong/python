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


class Boy(models.Model):
    name = models.CharField(max_length=32)
    m = models.ManyToManyField('Girl',through="Love",through_fields=('b','g',))


class Girl(models.Model):
    nick = models.CharField(max_length=32)
    # m = models.ManyToManyField('Boy')

class Love(models.Model):
    b = models.ForeignKey('Boy')
    g = models.ForeignKey('Girl')

    class Meta:
        unique_together = [
            ('b','g'),
        ]















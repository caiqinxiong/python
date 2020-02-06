from django.db import models

# Create your models here.
# ORM相关的只能写在这个文件里,写到别的文件里Django找不到


class UserInfo(models.Model):
    id = models.AutoField(primary_key=True)  # 创建一个自增的主键字段
    name = models.CharField(null=False, max_length=32)   # 创建一个varchar(20)类型的不能为空的字段

    def __str__(self):
        return "<{}-{}>".format(self.id, self.name)



# Book表
class Book(models.Model):
    id = models.AutoField(primary_key=True)  # 创建一个自增的主键字段
    title = models.CharField(max_length=64, null=False)
from django.db import models


# Create your models here.
# 类   ——》  表
# 对象 ——》  数据行（记录）
# 属性 ——》  字段

class User(models.Model):
    username = models.CharField(max_length=32)  # varchar(32)
    password = models.CharField(max_length=32)  # varchar(32)

    class Meta:
        db_table = 'user'

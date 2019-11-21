from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

    __repr__ = __str__


class Book(models.Model):
    title = models.CharField(max_length=32)
    pub = models.ForeignKey('Publisher', on_delete=models.CASCADE)
    #  CASCADE 级连删除   on_delete 2.0 版本后是必填项
    # SET
    # SET_DEFAULT
    # SET_NULL    null=True
    # DO_NOTHING
    # PROTECT

from django.db import models


class MyCharField(models.Field):

    def __init__(self, max_length, *args, **kwargs):
        self.max_length = max_length
        super(MyCharField, self).__init__(max_length=max_length, *args, **kwargs)

    def db_type(self, connection):
        return 'char(%s)' % self.max_length


# Create your models here.
class User(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='用户名',max_length=32,db_column='username',unique=True)  # varchar(32)
    age = models.IntegerField(verbose_name='年龄',blank=True, null=True)  # 整数
    bitrh = models.DateTimeField(verbose_name='生日',auto_now=True)
    # auto_now_add=True  新增数据时保存当前的时间
    # auto_now=True      新增和编辑数据时保存当前的时间
    phone = MyCharField(11,verbose_name='手机号')
    gender = models.BooleanField(choices=((True,'男'),(False,'女')))

    def __str__(self):
        return "< User object: {} {} -{} > ".format(self.pk,self.name,self.age)

    __repr__ = __str__
    class Meta:
        # 数据库中生成的表名称 默认 app名称 + 下划线 + 类名
        db_table = "user"

        # admin中显示的表名称
        verbose_name = '个人信息'

        # verbose_name加s
        verbose_name_plural = '所有用户信息'

        # 联合索引
        # index_together = [
        #     ("name", "age"),  # 应为两个存在的字段
        # ]
        #
        # # 联合唯一索引
        # unique_together = (("name", "age"),)  # 应为两个存在的字段
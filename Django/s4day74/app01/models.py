from django.db import models
from django.core.validators import RegexValidator
from django.core.validators import EmailValidator,URLValidator,DecimalValidator,\
MaxLengthValidator,MinLengthValidator,MaxValueValidator,MinValueValidator
# Create your models here.
class UserAdmin(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)




class UserInfo(models.Model):

    username = models.CharField(max_length=32)

    email = models.EmailField(null=True,default='1111',unique=True,blank=True,verbose_name='用户名',editable=True,help_text='熬枯受淡发送到发送到')
    ctime = models.DateTimeField(null=True)
    test = models.CharField(
            max_length=32,
            error_messages={
                'c1': '优先错信息1',
            },
            validators=[RegexValidator(regex='root_\d+', message='错误了', code='c1')],
            null=True
        )
    color_list = (
        (1,'黑色'),
        (2,'白色'),
        (3,'蓝色')
    )
    color = models.IntegerField(choices=color_list)

    # class Meta:
        # unique_together = (
        #     ('email','ctime'),
        # )
        # index_together = (
        #     ('email','ctime'),
        # )
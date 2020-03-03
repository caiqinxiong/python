from django.db import models
# from django.contrib.auth.models import User
from users.models import User
from datetime import datetime
from django.utils import timezone
# Create your models here.

class Team_info(models.Model):
    team_name = models.CharField(max_length=50,unique=True, verbose_name='队伍名')
    leader = models.CharField(max_length=50, default=None, blank=True, verbose_name='队长')
    leader_college = models.CharField(max_length=50, default=None, blank=True, verbose_name='学院')
    leader_tel = models.CharField(max_length=11, default=None, blank=True, verbose_name='手机号')
    leader_id = models.CharField(max_length=9, default=None, blank=True,unique=True, verbose_name='学号')
    leader_email = models.EmailField(default=None, blank=True,unique=True, verbose_name='邮箱')
    member1 = models.CharField(max_length=50,default=None,blank=True,null=True, verbose_name='队员一')
    college1 = models.CharField(max_length=50,default=None,blank=True,null=True, verbose_name='学院')
    tel1 = models.CharField(max_length=11,default=None,blank=True,null=True, verbose_name='手机号')
    student_id1 = models.CharField(max_length=9,default=None,blank=True,unique=True,null=True, verbose_name='学号')
    email1 = models.EmailField(default=None,blank=True,null=True,unique=True, verbose_name='邮箱')
    member2 = models.CharField(max_length=50,default=None,blank=True,null=True, verbose_name='队员二')
    college2 = models.CharField(max_length=50,default=None,blank=True,null=True, verbose_name='学院')
    tel2 = models.CharField(max_length=11,default=None,blank=True,null=True, verbose_name='手机号')
    student_id2 = models.CharField(max_length=9,default=None,blank=True,unique=True,null=True, verbose_name='学号')
    email2 = models.EmailField(default=None,blank=True,null=True,unique=True, verbose_name='邮箱')
    team_key = models.CharField(default=None,max_length=10,unique=True, verbose_name='队伍密钥')
    date_added = models.DateField(auto_now_add=True, verbose_name='队伍创建时间')
    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        verbose_name = u"队伍信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.team_name


class Actor_info(models.Model):
    actor_id = models.CharField(max_length=100,default=None, verbose_name='学号')
    team_name = models.CharField(max_length=100,blank=True,default=None, verbose_name='所参与队伍名')
    is_added = models.BooleanField(default=False, verbose_name='是否已参加')

    class Meta:
        verbose_name = u"参与者状态"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.actor_id


class EmailVerifyRecord(models.Model):
    # 验证码
    code = models.CharField(max_length=20, verbose_name=u"验证码")
    email = models.EmailField(max_length=50, verbose_name=u"邮箱")
    # 包含注册验证和找回验证
    send_time = models.DateTimeField(verbose_name=u"发送时间", default=timezone.now)
    class Meta:
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.email



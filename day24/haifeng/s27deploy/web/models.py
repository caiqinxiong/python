from django.db import models

class Server(models.Model):
    """
    服务器表
    """
    hostname = models.CharField(verbose_name='主机名',max_length=32)


class Project(models.Model):
    """
    项目表
    """
    title = models.CharField(verbose_name='项目名',max_length=32)

    repo = models.CharField(verbose_name='仓库地址',max_length=128)

    env_choices = (
        ('prod','正式'),
        ('test','测试'),
    )
    env = models.CharField(verbose_name='环境',max_length=16,choices=env_choices,default='test')
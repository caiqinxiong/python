from django.db import models

class Server(models.Model):
    """
    服务器表
    """
    hostname = models.CharField(verbose_name='主机名',max_length=32)

    def __str__(self):
        return self.hostname

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

    path = models.CharField(verbose_name='线上项目地址',max_length=128)
    servers = models.ManyToManyField(verbose_name='关联服务器',to='Server')



class DeployTask(models.Model):
    """ 发布任务单
        2  v1
        2  v2
        2  v3
        3  v3
        3  v4
        3  v5
    """
    uid = models.CharField(verbose_name='标识',max_length=64) # luffy-test-v1-202001111111
    project = models.ForeignKey(verbose_name='项目环境',to='Project')
    tag = models.CharField(verbose_name='版本',max_length=32)
    status_choices = (
        (1,'待发布'),
        (2, '发布中'),
        (3, '成功'),
        (4, '失败'),
    )
    status = models.IntegerField(verbose_name='状态',choices=status_choices,default=1)

    before_download_script = models.TextField(verbose_name='下载前脚本', null=True, blank=True)
    after_download_script = models.TextField(verbose_name='下载后脚本', null=True, blank=True)
    before_deploy_script = models.TextField(verbose_name='发布前脚本', null=True, blank=True)
    after_deploy_script = models.TextField(verbose_name='发布后脚本', null=True, blank=True)
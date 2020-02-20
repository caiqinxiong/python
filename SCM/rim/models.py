from django.db import models

# Create your models here.


class Project(models.Model):
    '''项目'''
    pid = models.AutoField(primary_key=True)
    pname = models.CharField(max_length=64,verbose_name='项目名称')
    kname = models.CharField(max_length=64,verbose_name='键值')


class ReleaseInfo(models.Model):
    '''发布信息'''
    taskname = models.CharField(max_length=32,verbose_name='任务名称')
    svnversion = models.IntegerField(verbose_name='渠道svn版本号',null=True,blank=True)
    createtime = models.DateTimeField(verbose_name='创建日期',auto_now_add=True)
    branch = models.CharField(max_length=128, verbose_name='分支名称')
    release_info = models.CharField(max_length=512, verbose_name='发布信息')
    build_cmd = models.CharField(max_length=512, verbose_name='编译命令',null=True,blank=True)
    versionname = models.CharField(max_length=16, verbose_name='versionname',null=True,blank=True)
    versioncode = models.CharField(max_length=16, verbose_name='versioncode',null=True,blank=True)
    issue = models.CharField(max_length=32, verbose_name='JIRA链接',null=True,blank=True)
    project = models.ForeignKey(to='Project', on_delete=models.CASCADE,verbose_name='项目')


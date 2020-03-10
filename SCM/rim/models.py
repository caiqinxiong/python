from django.db import models

# Create your models here.


class Project(models.Model):
    '''项目'''
    pid = models.AutoField(primary_key=True)
    pname = models.CharField(max_length=64,verbose_name='项目名称')
    kname = models.CharField(max_length=64,verbose_name='键值')
    def __str__(self):
        return self.pname

    class Meta:
        ordering = ["pid"] # 按什么排序展示
        verbose_name_plural = "项目" # 类名展示,在admin账户里显示的


class ReleaseInfo(models.Model):
    '''发布信息'''
    project = models.ForeignKey(to='Project', on_delete=models.CASCADE, verbose_name='项目')
    taskname = models.CharField(max_length=64,verbose_name='任务名称')
    svnversion = models.IntegerField(verbose_name='渠道svn版本号',null=True,blank=True)
    createtime = models.DateTimeField(verbose_name='创建日期',auto_now_add=True)
    branch = models.CharField(max_length=128, verbose_name='分支名称')
    versionname = models.CharField(max_length=16, verbose_name='versionname',null=True,blank=True)
    versioncode = models.CharField(max_length=16, verbose_name='versioncode',null=True,blank=True)
    build_cmd = models.CharField(max_length=512, verbose_name='编译命令',null=True,blank=True)
    release_info = models.CharField(max_length=512, verbose_name='发布信息')
    issue = models.CharField(max_length=128, verbose_name='JIRA链接',null=True,blank=True)

    def __str__(self):
        return self.taskname

    class Meta:
        ordering = ["-createtime"] # 按什么排序展示
        verbose_name_plural = "发布信息" # 类名展示,在admin账户里显示的


class User(models.Model):
    '''用户表'''
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    username = models.CharField(max_length=128, unique=True, verbose_name='用户名')
    password = models.CharField(max_length=256, verbose_name='密码')
    email = models.EmailField(unique=True, verbose_name='邮箱')
    sex = models.CharField(max_length=32, choices=gender, default="男",verbose_name='性别')
    createtime = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')

    def __str__(self):
        return self.username

    class Meta:
        ordering = ["id"]
        verbose_name_plural = "用户" # 类名展示


class Group(models.Model):
    '''用户组'''
    gname = models.CharField(max_length=128, unique=True,verbose_name='组名')
    createtime = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')
    u2g = models.ManyToManyField(to='User',verbose_name='关联用户',blank=True,null=True)

    def __str__(self):
        return self.gname

    class Meta:
        ordering = ["id"]
        verbose_name_plural = "用户组" # 类名展示

class Permission(models.Model):
    """
    权限表
    """
    title = models.CharField(verbose_name='标题', unique=True, max_length=128)
    url = models.CharField(verbose_name="含正则URL", unique=True, max_length=256)
    # is_menu = models.BooleanField(verbose_name="是否是菜单")
    menu_gp = models.ForeignKey(verbose_name="组内菜单", to="Permission", null=True, blank=True, on_delete=models.CASCADE)
    code = models.CharField(max_length=32, verbose_name="代码", default="list",  null=True, blank=True)
    p2g = models.ManyToManyField(verbose_name="所属组", to="Group", default=1)

    class Meta:
        verbose_name_plural = "权限表"

    def __str__(self):
        return self.title













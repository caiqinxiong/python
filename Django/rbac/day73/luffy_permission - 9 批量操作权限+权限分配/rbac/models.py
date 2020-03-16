from django.db import models


class Menu(models.Model):
    """
    菜单表   一级菜单
    """
    title = models.CharField('菜单', max_length=32)
    icon = models.CharField('图标', max_length=108, null=True, blank=True)
    wight = models.IntegerField('权重',default=1)

    def __str__(self):
        return self.title


class Permission(models.Model):
    """
    权限表
    关联menu    ——》 二级菜单
    不关联menu  ——》 普通的权限

    有parent_id   ——》 子权限
    没有parent_id ——》 父权限

    """
    url = models.CharField('权限', max_length=32)
    name = models.CharField('URL别名', max_length=32, unique=True)
    title = models.CharField('标题', max_length=32)
    menu = models.ForeignKey('Menu', null=True, blank=True)
    parent = models.ForeignKey('Permission', null=True, blank=True)

    def __str__(self):
        return self.title


class Role(models.Model):
    """
    角色表
    """
    name = models.CharField('角色名称', max_length=32)
    permissions = models.ManyToManyField('Permission', verbose_name='角色所拥有的权限', blank=True)

    def __str__(self):
        return self.name


class User(models.Model):
    """
    用户表
    """
    name = models.CharField('用户名', max_length=32)
    pwd = models.CharField('密码', max_length=32)
    roles = models.ManyToManyField('Role', verbose_name='用户所拥有的角色', blank=True)

    def __str__(self):
        return self.name

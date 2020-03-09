from django.db import models


# ========================= 菜单权限 =========================

class MenuOne(models.Model):
    pass

    class Meta:
        db_table = 'menu_one'
        verbose_name = '菜单一'
        verbose_name_plural = verbose_name


class MenuTwo(models.Model):
    pass

    class Meta:
        db_table = 'menu_two'
        verbose_name = '菜单二'
        verbose_name_plural = verbose_name


class MenuThe(models.Model):
    pass

    class Meta:
        db_table = 'menu_the'
        verbose_name = '菜单三'
        verbose_name_plural = verbose_name

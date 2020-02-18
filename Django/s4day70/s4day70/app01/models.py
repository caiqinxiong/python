from django.db import models

class UserGroup(models.Model):
    """
    部门
    """
    title = models.CharField(max_length=32)
"""
models.UserGroup.objects.create(title='销售部')
models.UserGroup.objects.filter(id=2).delete()
models.UserGroup.objects.filter(id=2).update(title='公关部')
group_list = models.UserGroup.objects.all()
group_list = models.UserGroup.objects.filter(id=1)
group_list = models.UserGroup.objects.filter(id__gt=1)
group_list = models.UserGroup.objects.filter(id__lt=1)
"""

class UserInfo(models.Model):
    """
    员工
    """
    nid = models.BigAutoField(primary_key=True)
    user = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField(default=1)
    # ug_id
    ug = models.ForeignKey("UserGroup",null=True)

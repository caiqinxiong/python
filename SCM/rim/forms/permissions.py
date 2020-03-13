# 为了做表单验证,引入ModelForm的功能
# 1. 自动生成HTML标签
# 2. 表单验证
from django.forms import ModelForm
from django.forms import fields
from django.forms import widgets
from rim import models
from .base import BootStrapModelForm

class PermissionsModelForm(BootStrapModelForm):

    class Meta:
        model = models.Permission
        fields = "__all__"

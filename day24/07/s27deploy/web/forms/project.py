# 为了做表单验证,引入ModelForm的功能
# 1. 自动生成HTML标签
# 2. 表单验证
from django.forms import ModelForm
from web import models
from .base import BootStrapModelForm

class ProjectModelForm(BootStrapModelForm):
    class Meta:
        model = models.Project
        fields = "__all__"


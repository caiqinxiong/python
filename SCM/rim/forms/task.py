# 为了做表单验证,引入ModelForm的功能
# 1. 自动生成HTML标签
# 2. 表单验证
from django.forms import ModelForm
from django.forms import fields
from django.forms import widgets
from rim import models
from .base import BootStrapModelForm

class TasktModelForm(BootStrapModelForm):
    build_cmd = fields.CharField(widget=widgets.Textarea(
        attrs={'class': 'form-control','rows':6}),
        label='编译命令',
    )
    release_info = fields.CharField(widget=widgets.Textarea(
        attrs={'class': 'form-control','rows':6}),
        label='发布信息'
    )
    class Meta:
        model = models.ReleaseInfo
        fields = "__all__"
        # exclude = ['project',]


# 为了做表单验证,引入ModelForm的功能
# 1. 自动生成HTML标签
# 2. 表单验证
from web import models
from .base import BootStrapModelForm

class ServerModelForm(BootStrapModelForm):
    class Meta:
        model = models.Server
        fields = "__all__"

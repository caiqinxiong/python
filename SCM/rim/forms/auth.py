# 为了做表单验证,引入ModelForm的功能
# 1. 自动生成HTML标签
# 2. 表单验证
from django.forms import ModelForm
from django.forms import fields
from django.forms import widgets
from rim import models
from .base import BootStrapModelForm
from captcha.fields import CaptchaField

class AuthModelForm(BootStrapModelForm):
    captcha = CaptchaField(label='验证码')
    class Meta:
        model = models.User
        fields = "__all__"


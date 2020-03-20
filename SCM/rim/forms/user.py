# 为了做表单验证,引入ModelForm的功能
# 1. 自动生成HTML标签
# 2. 表单验证
from django.forms import ModelForm
from django.forms import fields
from django.forms import widgets
from django import forms
from rim import models
from .base import BootStrapModelForm
from captcha.fields import CaptchaField

class UserModelForm(BootStrapModelForm):
    group = forms.ModelMultipleChoiceField(label='用户组',
                                           required=False, #required是否可以为空,如果为False说明可以为空
                                           widget=forms.SelectMultiple,
                                           queryset=models.Group.objects.all())

    captcha = CaptchaField(label='验证码',required=True, error_messages={"invalid": "验证码错误!"})
    class Meta:
        model = models.User
        # fields = "__all__"
        # fields = ['email','password']
        exclude = ['avatar']


from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username','email','college','name','tel']
        labels = {
            'username':'请输入学号',
            'email':'请输入邮箱',
            'college':'请输入学院',
            'name':'请输入姓名',
            'tel':'请输入手机号',
        }

from django.shortcuts import render, HttpResponse
import random
from utils.tencent.sms import send_sms_single
from django.conf import settings
from django_redis import get_redis_connection
from django import forms
from app01 import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

class RegisterModelForm(forms.ModelForm):
    password = forms.CharField(label='密码',widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='重复密码',widget=forms.PasswordInput())
    mobile_phone = forms.CharField(label='手机号',validators=[RegexValidator(r'^(1[3|4|5|6|7|8|9])\d{9}$', '手机号格式错误'), ])
    code = forms.CharField(label='验证码', widget=forms.TextInput())
    class Meta:
        model = models.UserInfo
        #OrderedDict
        fields = ['username','email','password','confirm_password','mobile_phone','code']
        error_messages = {
            'username': {
                'required': '用户名不能为空!!',
            },
            'password': {
                'required': '密码不能为空!!',
            }
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name,field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = f'请输入{field.label}'


def send_sms(request):
    """ 发送短信
        ?tpl=login  -> 548762
        ?tpl=register -> 548760
    """
    tpl = request.GET.get('tpl')
    template_id = settings.TENCENT_SMS_TEMPLATE.get(tpl)
    if not template_id:
        return HttpResponse('模板不存在')

    code = random.randrange(1000, 9999)
    res = send_sms_single('15201446433', template_id, [code,1])
    if res['result'] == 0:
        return HttpResponse('成功')
    else:
        return HttpResponse(res['errmsg'])

def register(request):
    form = RegisterModelForm()
    if request.method == 'POST':
        print('xxx')
        return HttpResponse('注册成功')
    return render(request, 'app01/register.html', {'form':form})

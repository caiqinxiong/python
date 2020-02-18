from django.shortcuts import render, HttpResponse
import json
from app01 import models
# Create your views here.


def test(request):
    if request.method == "POST":
        name = request.POST.get("name")
        sb = request.POST.getlist("sb")
        print(name)
        print(sb, type(sb))

        # ret = {
        #     "status": 0,
        #     "data": [
        #         {"name": "alex", "age": 18},
        #         {"name": "xiaohei", "age": 28},
        #     ]
        # }

        ret = {
            "status": 1,
            "error": "用户名已被注册！"
        }
        ret_str = json.dumps(ret)
        return HttpResponse(ret_str)

    return render(request, "test.html")


def check_user(request):
    if request.method == "POST":
        name = request.POST.get("name")
        # 去数据库中查询用户名是否已经被注册
        ret = models.UserInfo.objects.filter(name=name)
        if ret:
            # 用户名已经存在
            msg = "用户名已被注册！"
        else:
            msg = "用户名可用"

        return HttpResponse(msg)


def reg(request):
    error = {"pwd": "", "user": ""}
    if request.method == "POST":
        name = request.POST.get("username")
        pwd = request.POST.get("pwd")

        if len(pwd) < 6:
            error["pwd"] = "密码不能小于6位"

    return render(request, "reg.html", {"error": error})


#          Django Form组件的使用
from django import forms
from django.forms import widgets
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
class RegForm(forms.Form):
    name = forms.CharField(
        # 校验规则相关
        max_length=16,
        label="用户名",
        error_messages={
            "required": "该字段不能为空",
        },
        # widget控制的是生成html代码相关的
        widget=widgets.TextInput(attrs={"class": "form-control"})
    )
    pwd = forms.CharField(
        label="密码",
        min_length=6,
        max_length=10,
        widget=widgets.PasswordInput(attrs={"class": "form-control"}, render_value=True),
        error_messages={
            "min_length": "密码不能少于6位！",
            "max_length": "密码最长10位！",
            "required": "该字段不能为空",
        }
    )
    re_pwd = forms.CharField(
        label="确认密码",
        min_length=6,
        max_length=10,
        widget=widgets.PasswordInput(attrs={"class": "form-control"}, render_value=True),
        error_messages={
            "min_length": "密码不能少于6位！",
            "max_length": "密码最长10位！",
            "required": "该字段不能为空",
        }
    )

    email = forms.EmailField(
        label="邮箱",

        widget=widgets.EmailInput(attrs={"class": "form-control"}),
        error_messages={
            "required": "该字段不能为空",
        }
    )
    mobile = forms.CharField(
        label="手机",
        # 自己定制校验规则
        validators=[
            RegexValidator(r'^[0-9]+$', '手机号必须是数字'),
            RegexValidator(r'^1[3-9][0-9]{9}$', '手机格式有误')
        ],
        widget=widgets.TextInput(attrs={"class": "form-control"}),
        error_messages={
            "required": "该字段不能为空",
        }
    )

    city = forms.ChoiceField(
        choices=models.City.objects.all().values_list("id", "name"),
        label="城市",
        initial=1,
        widget=forms.widgets.Select
    )

    # 重写父类的init方法
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["city"].widget.choices = models.City.objects.all().values_list("id", "name")


    def clean_name(self):
        value = self.cleaned_data.get("name")
        if "金瓶梅" in value:
            raise ValidationError("不符合社会主义核心价值观！")
        return value

    # 重写父类的clean方法
    def clean(self):
        # 此时 通过检验的字段的数据都保存在 self.cleaned_data
        pwd = self.cleaned_data.get("pwd")
        re_pwd = self.cleaned_data.get("re_pwd")
        if pwd != re_pwd:
            self.add_error("re_pwd", ValidationError("两次密码不一致"))
            raise ValidationError("两次密码不一致")
        return self.cleaned_data
    # gender = forms.ChoiceField(
    #     choices=((1, "男"), (2, "女"), (3, "保密")),
    #     label="性别",
    #     initial=1,
    #     widget=forms.widgets.RadioSelect
    # )
    # hobby = forms.ChoiceField(
    #     choices=((1, "篮球"), (2, "足球"), (3, "双色球"),),
    #     label="爱好",
    #     initial=3,
    #     widget=forms.widgets.Select
    # )
    # hobby2 = forms.MultipleChoiceField(
    #     choices=((1, "篮球"), (2, "足球"), (3, "双色球"),),
    #     label="爱好",
    #     initial=[1, 3],
    #     widget=forms.widgets.SelectMultiple()
    # )
    #
    # keep = forms.ChoiceField(
    #     label="是否记住密码",
    #     initial="checked",
    #     widget=forms.widgets.CheckboxInput
    # )
    # hobby3 = forms.MultipleChoiceField(
    #     choices=((1, "篮球"), (2, "足球"), (3, "双色球"),),
    #     label="爱好",
    #     initial=[1, 3],
    #
    #     widget=forms.widgets.CheckboxSelectMultiple(attrs={"class": "c1"})
    # )

def reg2(request):
    form_obj = RegForm()

    if request.method == "POST":
        form_obj = RegForm(request.POST)
        # 让form帮我们做校验
        if form_obj.is_valid():
            # 校验通过
            # 把数据存到数据库
            # 所有经过校验的数据都保存在 form_obj.cleaned_data
            print(form_obj.cleaned_data)
            del form_obj.cleaned_data["re_pwd"]
            models.UserInfo.objects.create(**form_obj.cleaned_data)
            return HttpResponse("注册成功！")
        print(form_obj.errors["__all__"][0])
        print(form_obj.errors["re_pwd"])

    return render(request, "reg2.html", {"form_obj": form_obj})
from django.shortcuts import render,redirect,HttpResponse
from django.forms import Form
from django.forms import fields
from django.forms import widgets

class LoginForm(Form):
    user = fields.CharField(required=True)
    pwd = fields.CharField(min_length=18)


def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        obj = LoginForm(request.POST)
        if obj.is_valid():
            print(obj.cleaned_data)
            return redirect('http://www.baidu.com')
        return render(request,'login.html',{'obj': obj})

def ajax_login(request):
    import json
    ret = {'status': True,'msg': None}
    obj = LoginForm(request.POST)
    if obj.is_valid():
        print(obj.cleaned_data)
    else:
        # print(obj.errors) # obj.errors对象
        ret['status'] = False
        ret['msg'] = obj.errors
    v = json.dumps(ret)
    return HttpResponse(v)

#
# class TestForm(Form):
#     t1 = fields.CharField(
#         required=True,
#         max_length=8,
#         min_length=2,
#         error_messages={
#             'required': '不能为空',
#             'max_length': '太长',
#             'min_length': '太短',
#         }
#     )
#     t2 = fields.IntegerField(
#         min_value=10,
#         max_value=1000,
#         error_messages={
#             'required': 't2不能为空',
#             'invalid': 't2格式错误，必须是数字',
#             'min_value': '必须大于10',
#             'max_value': '必须小于1000',
#         },
#     )
#     t3 = fields.EmailField(
#         error_messages={
#             'required': 't3不能为空',
#             'invalid': 't3格式错误，必须是邮箱格式',
#         }
#     )





class TestForm(Form):
    t1 = fields.CharField(required=True,max_length=8,min_length=2,
        error_messages={
            'required': '不能为空',
            'max_length': '太长',
            'min_length': '太短',
        }
    )
    t2 = fields.EmailField()

def test(request):
    if request.method == "GET":
        obj = TestForm()
        return render(request,'test.html',{'obj': obj})
    else:
        obj = TestForm(request.POST)
        if obj.is_valid():
            print(obj.cleaned_data)
        else:
            print(obj.errors)
        return render(request,'test.html',{'obj':obj})



class RegiterForm(Form):
    user = fields.CharField(min_length=8)
    email = fields.EmailField()
    password = fields.CharField()
    phone = fields.RegexField('139\d+')


def register(request):
    if request.method == 'GET':
        obj = RegiterForm()
        return render(request,'register.html',{'obj':obj})
    else:
        obj = RegiterForm(request.POST)
        if obj.is_valid():
            print(obj.cleaned_data)
        else:
            print(obj.errors)
        return render(request,'register.html',{'obj':obj})











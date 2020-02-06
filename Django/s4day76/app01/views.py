from django.shortcuts import render,HttpResponse,redirect

class JSONResponse:
    def __init__(self,req,status,msg):
        self.req = req
        self.status = status
        self.msg = msg
    def render(self):
        import json
        ret = {
            'status': self.status,
            'msg':self.msg
        }
        return HttpResponse(json.dumps(ret))

def test(request):
    # print('test')
    # return HttpResponse('...')
    ret = {}
    return JSONResponse(request,True,"错误信息")

from django.forms import Form
from django.forms import fields
class LoginForm(Form):
    # 正则验证: 不能为空,6-18
    username = fields.CharField(
        max_length=18,
        min_length=6,
        required=True,
        error_messages={
            'required': '用户名不能为空',
            'min_length': '太短了',
            'max_length': '太长了',
        }
    )
    # 正则验证: 不能为空，16+
    password = fields.CharField(min_length=16,required=True)
    # email = fields.EmailField()
    # email = fields.GenericIPAddressField()
    # email = fields.IntegerField()


def login(request):
    if request.method == "GET":
        return render(request,'login.html')
    else:
       obj = LoginForm(request.POST)
       if obj.is_valid():
           # 用户输入格式正确
           print(obj.cleaned_data) # 字典类型
           return redirect('http://www.baidu.com')
       else:
           # 用户输入格式错误
           return render(request,'login.html',{'obj':obj})

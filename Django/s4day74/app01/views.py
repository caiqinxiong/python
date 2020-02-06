from django.shortcuts import render,HttpResponse,redirect
from app01 import models
def test(request):

    # models.UserInfo.objects.create(username='root',email='qweqweq')
    # models.UserInfo.objects.create(username='xxx',email='xxx',ctime='2011-11-11')
    # return HttpResponse('...')
    # v = {'k1':'v1','k2':'v2'}
    # for i in v.values():
    #
    # return render(request,'test.html',{'name':'fangsaowei'})
    response = HttpResponse('内容')
    response.set_cookie('k1','v1')
    response.set_cookie('k2','v2')
    response.set_cookie('k3','v3')
    response.set_cookie('k4','v4')
    return response


def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        obj = models.UserAdmin.objects.filter(username=u,password=p).first()
        if obj:
            # 1. 生成随机字符串
            # 2. 通过cookie发送给客户端
            # 3. 服务端保存
            # {
            #   随机字符串1: {'username':'alex','email':x''...}
            # }
            request.session['username'] = obj.username
            return redirect('/index/')
        else:
            return render(request,'login.html',{'msg':'用户名或密码错误'})


def index(request):
    # 1. 获取客户端端cookie中的随机字符串
    # 2. 去session中查找有没有随机字符
    # 3. 去session对应key的value中查看是否有 username
    v = request.session.get('username')
    if v:
        return HttpResponse('登录成功:%s' %v)
    else:
        return redirect('/login/')



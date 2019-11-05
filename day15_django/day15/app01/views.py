from django.shortcuts import render, HttpResponse, redirect
from app01 import models


# Create your views here.
def index(request):
    # 业务逻辑
    ret = models.User.objects.all()  # QuerySet 对象列表
    for i in ret:
        print(i.username,i.password,type(i.username))
        print(ret, type(ret))
    ret = models.User.objects.get(password='123')  # 返回多个 查不到也报错
    ret = models.User.objects.filter(password='123') # 获取所有满足条件的对象

    print(ret,type(ret))

    # 获取所有的数据

    # return HttpResponse('<h1>ok</h1>')
    return render(request, 'index.html')


def login(request):
    # print(request.method,type(request.method))
    if request.method == 'POST':
        # 获取用户提交的数据
        # print(request.POST,type(request.POST))
        user = request.POST.get('user')
        pwd = request.POST.get('password')
        # print(user,type(user))
        # print(pwd,type(pwd))
        # 校验
        if models.User.objects.filter(username=user,password=pwd):
            # 校验成功跳转
            return redirect('/index/')
        # 校验失败回复错误信息
        return render(request, 'login.html', {'error': '用户名或密码错误'})
    # 返回页面
    return render(request, 'login.html')

from django.shortcuts import render, redirect, reverse
from rbac.models import User
from django.conf import settings
from rbac.service.permission import init_permission


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        # 获取用户名和密码
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        # 去数据库进行筛选
        obj = User.objects.filter(name=user, pwd=pwd).first()
        if not obj:
            return render(request, 'login.html', {'error': '用户名或密码错误'})

        # 认证成功 进行权限信息初始化（权限、菜单）
        init_permission(request, obj)

        return redirect(reverse('index'))

    return render(request, 'login.html')

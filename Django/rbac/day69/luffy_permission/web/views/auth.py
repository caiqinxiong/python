from django.shortcuts import render, redirect, reverse
from rbac.models import User


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

        # 认证成功 保存权限信息

        # ORM获取到权限信息 去除权限为空的权限  去重
        permission_query = obj.roles.filter(permissions__url__isnull=False).values('permissions__url',
                                                                                   'permissions__title').distinct()

        request.session['permission'] = list(permission_query)  # json的序列化
        request.session['is_login'] = True

        return redirect(reverse('index'))

    return render(request, 'login.html')

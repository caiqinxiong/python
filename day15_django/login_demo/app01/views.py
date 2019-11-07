from django.shortcuts import render, redirect
from app01 import models


# Create your views here.
def login(request):
    # 业务逻辑
    if request.method == 'POST':
        # 获取用户输入的用户名和密码
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        # 到数据库进行校验
        if models.User.objects.filter(username=user, password=pwd):
            # 正确  跳转到首页
            return redirect('http://www.luffycity.com')
        # 不正确 返回错误信息
        return render(request, 'html/login.html', {'error': '用户名和密码错误'})
    return render(request, 'html/login.html', )

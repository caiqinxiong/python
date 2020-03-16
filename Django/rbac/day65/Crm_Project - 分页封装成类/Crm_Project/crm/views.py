from django.shortcuts import render, redirect, reverse, HttpResponse
from crm import models
from crm.froms import RegForm
import hashlib
from utils.pagination import Pagination


def index(request):
    return HttpResponse('index')


def login(request):
    if request.method == 'POST':
        user = request.POST.get('username')
        pwd = request.POST.get('password')

        md5 = hashlib.md5()
        md5.update(pwd.encode('utf-8'))
        pwd = md5.hexdigest()

        obj = models.UserProfile.objects.filter(username=user, password=pwd, is_active=True).first()
        if obj:
            # 登录成功 跳转到主页面
            return redirect(reverse('index'))
        else:
            # 登录失败
            return render(request, 'login.html', {'error': '用户名或密码错误'})
    return render(request, 'login.html')


# 注册
def reg(request):
    # 判断请求方式
    if request.method == 'POST':
        form_obj = RegForm(request.POST)
        # 对数据进行校验
        if form_obj.is_valid():
            # 数据正确 插入数据库
            # print(form_obj.cleaned_data)
            # form_obj.cleaned_data.pop('re_password')
            # models.UserProfile.objects.create(**form_obj.cleaned_data)
            form_obj.save()
            return redirect(reverse('login'))

    else:
        form_obj = RegForm()

    return render(request, 'reg.html', {'form_obj': form_obj})


# 展示客户列表
def customer_list(request):
    all_customer = models.Customer.objects.all()

    return render(request, 'customer_list.html', {'all_customer': all_customer})


users = [{'name': 'alex{}'.format(i), 'pwd': '123'} for i in range(1, 302)]


# 分页
def user_list(request):
    """
    一页显示20

    第1页  0      20
    第2页  20     40

      n   (n-1)*20   20*n

    :param request:
    :return:
    """
    page = Pagination(request.GET.get('page', '1'), len(users), )

    return render(request, 'user_list.html', {'users': users[page.start:page.end],
                                              'page_html': page.page_html})

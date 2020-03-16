from django.shortcuts import render, redirect, reverse, HttpResponse
from crm import models
from crm.froms import RegForm
import hashlib


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
    # 获取页码

    try:
        page_num = int(request.GET.get('page', '1'))
        if page_num <= 0:
            page_num = 1
    except Exception as e:
        page_num = 1

    # 每页显示的数据量
    per_num = 10

    # 总数据量
    all_count = len(users)

    # 总页码数
    page_count, more = divmod(all_count, per_num)
    if more:
        page_count += 1

    # 最大显示页码数
    max_show = 11
    half_show = max_show // 2

    # 总页码数 < 最大显示页码数
    if page_count < max_show:
        page_start = 1
        page_end = page_count
    else:
        # 处理左边极值
        if page_num <= half_show:
            page_start = 1
            page_end = max_show
        elif page_num + half_show >= page_count:
            page_start = page_count - max_show + 1
            page_end = page_count
        else:
            page_start = page_num - half_show  # 2
            page_end = page_num + half_show  # 7 + 5  12

    page_list = []
    if page_num == 1:
        page_list.append('<li class="disabled"><a>上一页</a></li>')
    else:
        page_list.append('<li><a href="?page={}">上一页</a></li>'.format(page_num-1, ))

    for i in range(page_start, page_end + 1):
        if i == page_num:
            page_list.append('<li class="active"><a href="?page={}">{}</a></li>'.format(i, i))
        else:
            page_list.append('<li><a href="?page={}">{}</a></li>'.format(i, i))

    if page_num == page_count:
        page_list.append('<li class="disabled"><a>下一页</a></li>')
    else:
        page_list.append('<li><a href="?page={}">下一页</a></li>'.format(page_num+1, ))


    page_html = ''.join(page_list)

    # return render(request, 'user_list.html', {'users': users[(page_num - 1) * per_num:per_num * page_num],
    #                                           'page_count': range(page_start, page_end + 1)})
    return render(request, 'user_list.html', {'users': users[(page_num - 1) * per_num:per_num * page_num],
                                              'page_html':page_html})

from django.shortcuts import render
from .forms import UserForm
from sign_up.models import Actor_info
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect
from django.core.mail import send_mail
from . import models

from random import Random # 用于生成随机码
from django.core.mail import send_mail # 发送邮件模块
from sign_up.models import EmailVerifyRecord # 邮箱验证model
from sacc_sign.settings import DEFAULT_FROM_EMAIL  # setting.py添加的的配置信息

# Create your views here.

#登录函数
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            user = models.User.objects.get(username=username)
            if user.is_active == False:
                context = {"type": "active"}
                return render(request, 'users/active_error.html', context)
            login(request, user)
            return HttpResponseRedirect(reverse('sign_up:index'))
        else:
            return HttpResponseRedirect(reverse('users:login'))
    return render(request,'users/login.html')


def register(request):
    if request.method != 'POST':
        form = UserForm()
    else:
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()
            new_user = form.save()
            # 如果认证信息有效，会返回一个  User  对象。authenticate()会在User 对象上设置一个属性标识那种认证后端认证了该用户，
            # 且该信息在后面的登录过程中是需要的。当我们试图登陆一个从数据库中直接取出来不经过authenticate()的User对象会报错的！！
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            actor_info = Actor_info()
            actor_info.actor_id = new_user.username
            actor_info.team_name = '无'
            actor_info.is_added = False
            actor_info.save()
            user = request.user
            user.is_active = False
            user.save()
            email = user.email
            email_record = EmailVerifyRecord()
            # 将给用户发的信息保存在数据库中
            code = random_str(16)
            email_record.code = code
            email_record.email = email
            email_record.save()
            # 初始化为空
            email_title = ""
            email_body = ""
            email_title = "注册激活链接"
            email_body = str(user.username)+" 同学你好，欢迎参加本次计算机基础知识大赛，"+"请点击下面的链接激活你的账号:http://*****.com/users/active/{0}".format(code)
            # 发送邮件
            send_status = send_mail(email_title, email_body, DEFAULT_FROM_EMAIL, [email])
            context = {"type":"register"}
            return render(request,'users/active_error.html',context)
    context = {'form':form}
    return render(request,'users/register.html',context)


#注销函数
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('sign_up:index'))


# 生成随机字符串用来验证邮箱
def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str


#点击邮箱链接，通过URL进行邮箱验证
def user_active(request,active_code):
    print("可以1")
    all_records = EmailVerifyRecord.objects.filter(code=active_code)
    if all_records:
        for record in all_records:
            email = record.email
            # 通过邮箱查找到对应的用户
            user = models.User.objects.get(email=email)
            # 激活用户
            user.is_active = True
            user.save()
        print("可以")
        return render(request, "sign_up/home.html")
    print("不行")
    return render(request, "sign_up/home.html")








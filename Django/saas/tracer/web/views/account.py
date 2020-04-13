"""
用户账户相关功能：注册、短信、登录、注销
"""
from io import BytesIO
from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from web.forms.account import RegisterModelForm,SendSmsForm,LoginSMSForm,LoginForm
from django.conf import settings
from web import models
from django.db.models import Q
from utils.image_code import check_code
import uuid
import datetime

def register(request):
    if request.method == 'GET':
        form = RegisterModelForm()
        return render(request, 'register.html', {'form': form})

    form_obj = RegisterModelForm(data=request.POST)
    if form_obj.is_valid():
        instance = form_obj.save()
        # username = request.POST.get('username')
        # user_obj = models.UserInfo.objects.get(username=username)
        # models.Transaction.objects.create(state=True, user=user_obj, price='0', actual_pay='0', quantity='1',
        #                                   order_nb='1')
        policy_object = models.PricePolicy.objects.filter(category=1,title="个人免费版").first()
        models.Transaction.objects.create(
            status=2,
            order=str(uuid.uuid4()),
            user=instance,
            price_policy=policy_object,
            count=0,
            price=0,
            start_time=datetime.datetime.now()
        )
        return JsonResponse({'status': True, 'data':'/login/'})

    return JsonResponse({'status':False,'error':form_obj.errors})


def send_sms(request):
    # mobile_phone = request.GET.get('mobile_phone')
    # tpl = request.GET.get('tpl')
    form = SendSmsForm(request, data=request.GET)

    #只能校验手机号:不为空,格式是否正确
    if form.is_valid():
        return JsonResponse({'status':True})

    return JsonResponse({'status':False,'error':form.errors})


def login_sms(request):
    if request.method == 'GET':
        form = LoginSMSForm()
        return render(request,'login_sms.html',{'form':form})
    form = LoginSMSForm(request.POST)
    if form.is_valid():
        mobile_phone = form.cleaned_data['mobile_phone']
        user_object = models.UserInfo.objects.filter(mobile_phone=mobile_phone).first()
        request.session['user_id'] = user_object.id
        request.session['user_name'] = user_object.username
        return JsonResponse({'status':True, 'data':"/index/"})
    return JsonResponse({'status':False, 'error': form.errors})

def login(request):
    """ 用户名和密码登录 """
    if request.method == 'GET':
        form = LoginForm(request)
        return render(request, 'login.html', {'form': form})
    form = LoginForm(request, data=request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        # user_object = models.UserInfo.objects.filter(username=username, password=password).first()
        #  (手机=username and pwd=pwd) or (邮箱=username and pwd=pwd)

        user_object = models.UserInfo.objects.filter(Q(email=username) | Q(mobile_phone=username)).filter(
            password=password).first()
        if user_object:
            # 登录成功为止1
            request.session['user_id'] = user_object.id
            request.session.set_expiry(60 * 60 * 24 * 14)

            return redirect('index')

        form.add_error('username', '用户名或密码错误')

    return render(request, 'login.html', {'form': form})


def image_code(request):
    """ 生成图片验证码 """

    image_object, code = check_code()

    request.session['image_code'] = code
    request.session.set_expiry(60)  # 主动修改session的过期时间为60s

    stream = BytesIO()
    image_object.save(stream, 'png')
    return HttpResponse(stream.getvalue())


def logout(request):
    request.session.flush()
    return redirect('index')
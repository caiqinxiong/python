# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
#2020/2/26 11:51
import json
from django.shortcuts import render,redirect,HttpResponse,reverse
from django.http import JsonResponse
from rim import models
from rim.forms.user import UserModelForm
from utils.mail_hander import SendMail
from django.conf import settings

def user_list(request):
    '''用户信息'''
    email = request.session.get("email")
    user_obj = models.User.objects.filter(email=email).first()
    return render(request ,'user_list.html',{'user_obj':user_obj})

def change_password(request):
    '''修改密码'''
    email = request.session.get("email")
    user_obj = models.User.objects.filter(email=email).first()
    ret = {'status': True, 'msg': None, 'url': ''}
    try:
        password = request.POST.get('password')
        user_obj.password = password
        user_obj.save()
        ret['msg'] = "密码修改成功！"+'\n新密码为：%s' % password
        # ret['url'] = '/rim/user/list/'#request.path_info
    except Exception as e:
        ret['status'] = False
        ret['msg'] = "密码修改失败！"

    sendMail = request.POST.get('sendMail')
    if sendMail == 'true':# 发送通知邮件
        title = '密码变更通知'
        context = {
            'username': user_obj.username,
            'password': user_obj.password,
            'email': user_obj.email,
            'title': title,
        }
        smail = SendMail(title, context, settings.EMAIL_HOST_USER, user_obj.email)  # 实例化邮件类，传4个必要参数
        smail.html_mail('mail/user_mail.html')  # 发送HTML邮件，传入HTML模板
    return HttpResponse(json.dumps(ret))


def user_list_all(request):
    '''所有用户信息'''
    search = request.POST.get('search')
    if search:
        user_obj = models.User.objects.filter(username__contains=search).all()
        return render(request, 'user_list_all.html', {'user_obj': user_obj})
    else:
        user_obj = models.User.objects.all()
        return render(request ,'user_list_all.html',{'user_obj':user_obj})


def user_add(request):
    '''添加用户'''
    if request.method == 'GET':
        form = UserModelForm()
        return render(request, 'user_add.html', {'form': form})
    # 接收用户提交的数据并进行表单验证
    form = UserModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        sendMail = request.POST.get('sendMail')
        # print(form.cleaned_data['email'])
        if sendMail == 'on':  # 发送通知邮件
            title = '账号创建通知'
            context = {
                'username': form.cleaned_data['username'],
                'password': form.cleaned_data['password'],
                'email': form.cleaned_data['email'],
                'title': title,
            }
            smail = SendMail(title,context,settings.EMAIL_HOST_USER,form.cleaned_data['email']) # 实例化邮件类，传4个必要参数
            smail.html_mail('mail/user_mail.html') # 发送HTML邮件，传入HTML模板

        return redirect(reverse('user_list_all'))
    else:
        return render(request, 'user_add.html', {'form': form})

def user_edit(request,pk):
    '''编辑用户'''
    # 编辑用户不需要密码和验证码
    # from rim.forms.base import BootStrapModelForm
    # class EditUserForm(BootStrapModelForm):
    #     class Meta:
    #         model = models.User
    #         fields = "__all__"
    #         exclude = ['password',]

    user_obj = models.User.objects.filter(id=pk).first()
    if request.method == 'GET':
        form = UserModelForm(instance=user_obj)
        return render(request, 'form.html', {'form': form})

    # 接收用户提交的数据并进行表单验证
    form = UserModelForm(data=request.POST,instance=user_obj)
    if form.is_valid():
        form.save()
        return redirect(reverse('user_list_all'))
    else:
        return render(request, 'form.html', {'form': form})


def user_del(request,pk):
    '''删除用户'''
    models.User.objects.filter(id=pk).delete()
    return JsonResponse({"status": True})











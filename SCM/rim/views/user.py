# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
#2020/2/26 11:51
import json

from django.shortcuts import render,redirect,HttpResponse,reverse
from django.http import JsonResponse
from rim import models
from rim.forms.user import UserModelForm
from rim.views.mail_hander import SendMail

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
        smail = SendMail('密码变更通知',  # 邮件标题
                         ret['msg'],  # 邮件txt内容
                         'caiqinxiong_cai@qq.com',  # 发件人
                         [email])  # 收件人列表
        smail.start()

    # print(ret)
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
        return render(request, 'form.html', {'form': form})

    # 接收用户提交的数据并进行表单验证
    form = UserModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('user_list_all'))
    else:
        return render(request, 'form.html', {'form': form})

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











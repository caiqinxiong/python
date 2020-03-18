# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
#2020/2/26 11:51

from django.shortcuts import render,redirect,HttpResponse,reverse
from django.http import JsonResponse
from rim import models
from rim.forms.auth import AuthModelForm

def login(request):
    '''登录'''
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        obj = models.User.objects.filter(email=email, password=password).first()
        if obj:
            request.session['email'] = obj.email
            # 获取相关权限
            permission_url_list = obj.group_set.filter(permission__url__isnull=False).values('permission__title',
                                        "permission__name",
                                        # "permission__id",
                                        'permission__url',
                                        # 'permissions__menu_gp_id',
                                        # "permission__group__id",
                                        # "permissions__group__menu_id",
                                        # "permissions__group__menu__title",
                                        ).distinct()

            url_list = [] # 转换为list才能写入session，并去重
            for i in permission_url_list:
                if i not in url_list:url_list.append(i)
            request.session['permission_url_list'] = url_list # 将权限信息写入session，不支持直接写入对象

            keep = request.POST.get('keep') # 默认保持登录两周，setting里配置
            # print(keep)
            if not keep:request.session.set_expiry(0) # 0关闭浏览器Session过期
            next_url = request.GET.get("next")
            # 如果有，就跳转回登陆之前的URL
            if next_url:
                return redirect(next_url)
            # 否则默认跳转到index页面
            else:
                return redirect('project_list')
        else:
            return render(request, 'login.html', {'error': '用户名或密码错误！'})

def logout(request):
    ret = redirect(reverse('login'))
    # ret.delete_cookie('is_login')
    # request.session.pop('is_login')
    request.session.flush()
    return ret
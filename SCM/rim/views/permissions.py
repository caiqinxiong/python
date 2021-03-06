# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
#2020/2/26 11:51
import json
from django.shortcuts import render,redirect,HttpResponse,reverse
from django.http import JsonResponse
from rim import models
from rim.forms.permissions import PermissionsModelForm
from utils.mail_hander import SendMail
from django.conf import settings
from utils.get_all_url import get_all_url_dict
from utils.pager import PageInfo

def permissions_list(request):
    '''权限列表'''
    search = request.POST.get('search')
    if search:
        permission_obj = models.Permission.objects.filter(title__contains=search).all()
        return render(request, 'permissions.html', {'permission_obj': permission_obj})
    else:
        permission_obj = models.Permission.objects.all()
        all_count = permission_obj.count()  # 获取所有数据行数
        page_info = PageInfo(request.GET.get('page'), all_count, per_page=20, base_url='/rim/permissions/list/',show_page=11)  # 添加分页展示功能
        permission_obj = permission_obj.order_by('id')[page_info.start():page_info.end()]  # 将查找到的数据按id反向排序，只展示某个区间的数据
        return render(request, 'permissions.html', {'permission_obj': permission_obj,'page_info':page_info})


def permissions_add(request):
    '''权限添加'''
    if request.method == "GET":
        # 传入ModelForm对象
        url_list = get_all_url_dict()
        permission_obj = models.Permission.objects.all()
        for i in permission_obj:# 已经添加了的权限就不再展示了
            try:
                url_list.remove((i.name, i.url))
            except Exception as e:
                print(i.name)
                print(e)
        group_obj = models.Group.objects.all()
        return render(request, 'add_permission.html', {'select_form': url_list,'group_obj':group_obj})
    else:
        title = request.POST.get('title')
        url_value = request.POST.get('url_name')# 名称跟路径刚好反过来
        url_name = request.POST.get('url_value')
        group = request.POST.getlist('group')
        # print(title,url_name,url_value,group)
        if title:
            try:
                p_obj=models.Permission.objects.create(title=title, name=url_name,url=url_value)
                p_obj.p2g.add(*group) # 多对多添加
                return redirect(reverse('permissions_list'))
            except:
                return HttpResponse('不能重复添加权限！')
        else:
            return HttpResponse('标题不能为空！')


def permissions_edit(request, pk):
    p_obj = models.Permission.objects.filter(id=pk).first() # 展示已选项 组
    url_list = get_all_url_dict()
    permission_obj = models.Permission.objects.all()
    for i in permission_obj:  # 已经添加了的权限就不再展示了
        try:
            if i.name != p_obj.name:url_list.remove((i.name, i.url))
        except Exception as e:
            print(i.name)
            print(e)
    group_obj = models.Group.objects.all()
    group_list = []# 展示可选项 组
    for j in group_obj:
        if j not in p_obj.p2g.all():
            group_list.append(j)
    if request.method == 'GET':
        return render(request, 'edit_permission.html', {'p_obj': p_obj,'select_form':url_list,'group_obj':group_list})
    else:
        title = request.POST.get('title')
        url_value = request.POST.get('url_name')  # 名称跟路径刚好反过来
        url_name = request.POST.get('url_value')
        group = request.POST.getlist('group')
        # print(title,url_name,url_value,group)
        if title:
            try:
                p_obj.title = title
                p_obj.url = url_value
                p_obj.name = url_name
                if group == []:
                    p_obj.p2g.clear()
                else:
                    p_obj.p2g.set(group)  # 这里存入列表
                p_obj.save()
                return redirect(reverse('permissions_list'))
            except Exception as e:
                print(e)
                return HttpResponse('不能重复添加权限！')
        else:
            return HttpResponse('标题不能为空！')


def permissions_del(request, pk):
    models.Permission.objects.filter(id=pk).delete()
    return JsonResponse({"status": True})

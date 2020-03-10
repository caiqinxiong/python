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

def permissions_list(request):
    '''权限列表'''
    permission_obj = models.Permission.objects.all()
    return render(request, 'permissions.html', {'permission_obj': permission_obj})


def permissions_add(request):
    '''权限添加'''
    if request.method == "GET":
        # 传入ModelForm对象
        form = PermissionsModelForm()
        return render(request, 'form.html', {'form': form})
    else:
        form = PermissionsModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse(PermissionsModelForm))
        else:
            return render(request, 'form.html', {'form': form})


def permissions_edit(request, pk):
    permission_obj = models.Permission.objects.filter(id=pk).first()
    if request.method == 'GET':
        form = PermissionsModelForm(instance=permission_obj)
        return render(request, 'form.html', {'form': form})
    else:
        form = PermissionsModelForm(request.POST, instance=permission_obj)
        if form.is_valid():
            form.save()
            return redirect(reverse(permissions_list))
        else:
            return render(request, 'form.html', {'form': form})


def permissions_del(request, pk):
    permission_obj = models.Permission.objects.filter(id=pk).first()
    permission_obj.delete()
    return redirect(reverse(permissions_list))

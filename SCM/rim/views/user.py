# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
#2020/2/26 11:51

from django.shortcuts import render,redirect,HttpResponse,reverse
from django.http import JsonResponse
from rim import models
from rim.forms.user import UserModelForm

def user_list(request):
    '''用户信息'''
    email = request.session.get("email")
    user_obj = models.User.objects.filter(email=email).first()
    return render(request ,'user_list.html',{'user_obj':user_obj})

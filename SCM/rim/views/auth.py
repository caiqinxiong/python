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
        form = AuthModelForm()
        return render(request, 'login.html', {'form': form})
    
    return render(request,'login.html')
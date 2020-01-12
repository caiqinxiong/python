from django.shortcuts import render,redirect
from app01 import models
# Create your views here.

def index(request):
    return render(request,'index.html')

def login(request):
    if request.method == 'POST':
        if models.User.objects.filter(username='caiqinxiong',password='cai'):
            return redirect('/index/')
        else:
            return render(request,'login.html',{'error':'用户名或密码错误！'})

    return render(request, 'login.html')
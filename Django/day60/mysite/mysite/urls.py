"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from django.shortcuts import HttpResponse, render


def yimi(request):
    # request参数保存了所有和用户浏览器请求相关的数据
    # with open("templates/xxx/yimi.html", "r", encoding="utf-8") as f:
    #     data = f.read()
    # return HttpResponse(data)
    return render(request, "xxx/yimi.html")

def xiaohei(request):
    # request参数保存了所有和用户浏览器请求相关的数据
    return HttpResponse('hello xiaohei! haha 小黑真黑啊!')

def login(request):
    return render(request, "login.html")


# 保存了路径和函数的对应关系
urlpatterns = [
    url(r'^yimi/', yimi),
    url(r'^xiaohei/', xiaohei),
    url(r'^login/', login),
]

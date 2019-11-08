"""myBookManager URL Configuration

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
from app01 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 登录认证
    url(r'^login/', views.login),

    #首页
    url(r'^index/', views.index),

    # 出版社的展示
    url(r'^publisher_list/', views.publisher_list),

    # 出版社的增加
    url(r'^publisher_add/', views.publisher_add),

    # 出版社的删除
    url(r'^publisher_del/', views.publisher_del),

    # 出版社的编辑
    url(r'^publisher_edit/', views.publisher_edit),

    # 出版社的查找
    url(r'^publisher_find/', views.publisher_find),

]

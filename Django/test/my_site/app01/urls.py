# -*- coding:utf-8 -*-
# Author:caiqinxiong
from django.urls import path,re_path
from app01 import views
urlpatterns = [
    path('test/', views.test_views),
    path('index/', views.index)
]
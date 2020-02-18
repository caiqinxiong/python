"""mysiteday62 URL Configuration

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
    # 出版社相关的对应关系
    url(r'^publisher_list/', views.publisher_list),
    url(r'^add_publisher/', views.add_publisher),
    url(r'^delete_publisher/', views.delete_publisher),
    url(r'^edit_publisher/', views.edit_publisher),
    # 书相关的对应关系
    url(r'^book_list/', views.book_list),
    url(r'^add_book/', views.add_book),  # 添加书籍
    url(r'^delete_book/', views.delete_book),  # 删除书籍
    url(r'^edit_book/', views.edit_book),  # 编辑书籍
    # 作者相关的对应关系
    url(r'^author_list/', views.author_list),  # 展示作者
    url(r'^add_author/', views.add_author),  # 添加作者
    url(r'^delete_author/', views.delete_author),  # 删除作者
    url(r'^edit_author/', views.edit_author),  # 编辑作者


    url(r'^test/', views.test),
    url(r'^book_test/', views.book_test),
]

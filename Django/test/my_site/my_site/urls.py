"""my_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include
from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app01/', include("app01.urls")),
    #path('test', views.test_views),
    # path('login',views.login_views),
    # re_path(r'^article/2003/$',views.article_2003),
    # #re_path(r'^article/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$',views.archive),# 动态路由，正则匹配，分组，返回字典，接收为**agr格式
    # re_path(r'^article/([0-9]{4})/([0-9]{2})/$',views.archive2),# 还是分组，但不需要返回字典
    # re_path(r'^article/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<slug>[\w-]+)$',views.archive3),# 自由匹配最后一个字符\w任意字符和 - 字符
    # Django2.0版本，可以直接用year，month，slug（任意匹配）
    # path('article/<int:year>/<int:month>/',views.archive),
    # path('article/<int:year>/<int:month>/<slug:slug>/',views.archive3),
    # path('article/<str:name>/',views.archive_name),# 任意匹配，包括*等特殊字符
    #path('article/<path:name>/',views.archive_name),# 任意匹配，包括*等特殊字符,包括／路径
]

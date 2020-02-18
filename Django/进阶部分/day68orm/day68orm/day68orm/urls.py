"""day68orm URL Configuration

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
    # url(r'^delete/表名/id值/'),


    url(r'^delete/([a-zA-Z]+)/(\d+)/$', views.delete),



    url(r'^home/([a-zA-Z]+)/$', views.home, name="home"),

    url(r'^index/(?P<name>[a-zA-Z]+)/$', views.index, name="index"),



    url(r'^test/$', views.test),

    # 什么都没有我们默认执行home函数
    url(r'^$', views.home),

]


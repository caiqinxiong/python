"""s4day70 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from app01 import views
from django.shortcuts import HttpResponse
def default(request):
    return HttpResponse('哥们，走错了。。')

urlpatterns = [
    url(r'^app01/', include('app01.urls')),
    # 127.0.0.1:8000/app01/index.html
    # 127.0.0.1:8000/app02/index.html
    # url(r'^admin/', admin.site.urls),
    # url(r'^index/asdf/asd/dffd/', views.index,name='n1'),
    # url(r'^index/fdss/asaad/dffdf/', views.index,name='n2'),
    # url(r'^inddex/fdss/asaad/dffdf/', views.index,name='n3'),
    # url(r'^inddex/fdsfs/asaad/dffdf/', views.index,name='n4'),
    # url(r'^inddex/fdsffs/asaad/dffdf/', views.index,name='n5'),
    # url(r'^inddexf/fdsffs/asaad/dffdf/', views.index,name='n6'),
    # url(r'^inddexf/fdsffs/fasaad/dffdf/', views.index,name='n7'),
    #
    # url(r'^index/', views.index,name='n1'),
    # url(r'^edit/(\w+)/(\w+)/', views.edit,name='n2'),
    # url(r'^login/', views.login,name='m1'),
    # url(r'^app01/', include('app01.urls')),
    # url(r'^app02/', include('app02.urls')),
    # url(r'^', views.index),

    # url(r'^index/', views.index),
    # url(r'^edit/', views.edit),
    #url(r'^edit/(\w+)/(\w+)/', views.edit),
    #url(r'^edit/(?P<a1>\w+)/(?P<a2>\w+)/', views.edit),
    # url(r'^edit/', views.edit),
    # url(r'^edit/(\w+).html$', views.edit),
]

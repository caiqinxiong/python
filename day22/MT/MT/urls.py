"""MT URL Configuration

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
    url(r'^index/', views.index, name='index'),
    url(r'^add_project/', views.add_project, name='add_project'),
    url(r'^edit_project/(\d+)$', views.edit_project, name='edit_project'),
    # 用例相关
    url(r'^case_list/(\d+)$', views.case_list, name='case_list'),
    url(r'^add_case/(\d+)$', views.add_case, name='add_case'),
    url(r'^add_case_all/(\d+)$', views.add_case_all, name='add_case_all'),
    url(r'^edit_case/(\d+)$', views.edit_case, name='edit_case'),
    url(r'^execute/', views.execute, name='execute'),
]

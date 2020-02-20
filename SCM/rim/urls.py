"""SCM URL Configuration

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
from rim import views

urlpatterns = [
    url(r'^index/', views.index),
    url(r'^project_list/', views.project_list,name='project_list'),
    url(r'^add_project/', views.add_project,name='add_project'),
    url(r'^edit_project/', views.edit_project,name='edit_project'),
    url(r'^project/del/(?P<pk>\d+)/$', views.del_project,name='del_project'),

    url(r'^task/list/(?P<project_id>\d+)/$', views.task_list,name='task_list'),
    url(r'^task/add/(?P<project_id>\d+)/$', views.task_add,name='task_add'),
    url(r'^task/edit/(?P<project_id>\d+)/$', views.task_edit,name='task_edit'),
    url(r'^task/del/(?P<project_id>\d+)/$', views.task_del,name='task_del'),

    url(r'^release_info/(?P<project_id>\d+)/$', views.release_info,name='release_info'),
    
]


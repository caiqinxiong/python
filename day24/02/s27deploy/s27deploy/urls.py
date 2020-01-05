"""s27deploy URL Configuration

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
from web.views import server
from web.views import project
from web.views import task

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^server/list/$', server.server_list,name='server_list'),
    url(r'^server/add/$', server.server_add,name='server_add'),
    url(r'^server/edit/(?P<pk>\d+)/$', server.server_edit,name='server_edit'),
    url(r'^server/del/(?P<pk>\d+)/$', server.server_del,name='server_del'),


    url(r'^project/list/$', project.project_list,name='project_list'),
    url(r'^project/add/$', project.project_add,name='project_add'),
    url(r'^project/edit/(?P<pk>\d+)/$', project.project_edit,name='project_edit'),
    url(r'^project/del/(?P<pk>\d+)/$', project.project_del,name='project_del'),

    url(r'^task/list/(?P<project_id>\d+)/$', task.task_list, name='task_list'),
    url(r'^task/add/(?P<project_id>\d+)/$', task.task_add, name='task_add'),
]

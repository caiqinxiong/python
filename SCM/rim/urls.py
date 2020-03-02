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
from rim.views import project
from rim.views import task
from rim.views import auth
from rim.views import user

urlpatterns = [
    url(r'^index/', project.index, name='index'),

    url(r'^project_list/', project.project_list, name='project_list'),
    url(r'^add_project/', project.add_project, name='add_project'),
    url(r'^edit_project/', project.edit_project, name='edit_project'),
    url(r'^project/del/(?P<pk>\d+)/$', project.del_project, name='del_project'),

    url(r'^task/list/(?P<pk>\d+)/$', task.task_list, name='task_list'),
    url(r'^task/add/(?P<pk>\d+)/$', task.task_add, name='task_add'),
    url(r'^task/edit/(?P<pk>\d+)/$', task.task_edit, name='task_edit'),
    url(r'^task/del/(?P<pk>\d+)/$', task.task_del, name='task_del'),
    url(r'^release_info/(?P<pk>\d+)/$', task.release_info, name='release_info'),

    url(r'^login/', auth.login, name='login'),
    url(r'^logout/$', auth.logout, name='logout'),

    url(r'^user/list/$', user.user_list, name='user_list'),
    url(r'^user/list_all/$', user.user_list_all, name='user_list_all'),
    url(r'^user/add/$', user.user_add, name='user_add'),
    url(r'^user/edit/(?P<pk>\d+)/$', user.user_edit, name='user_edit'),
    url(r'^user/del/(?P<pk>\d+)/$', user.user_del, name='user_del'),
    url(r'^change_password/$', user.change_password, name='change_password'),

]


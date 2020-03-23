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
from rim.views import group
from rim.views import permissions
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # url(r'^index/', project.index, name='index'),

    url(r'^project_list/$', project.project_list, name='project_list'),
    url(r'^add_project/$', project.add_project, name='add_project'),
    url(r'^edit_project/$', project.edit_project, name='edit_project'),
    url(r'^project/del/(?P<pk>\d+)/$', project.del_project, name='del_project'),

    url(r'^task/list/(?P<pk>\d+)/$', task.task_list, name='task_list'),
    url(r'^task/add/(?P<pk>\d+)/$', task.task_add, name='task_add'),
    url(r'^task/edit/(?P<pk>\d+)/$', task.task_edit, name='task_edit'),
    url(r'^task/del/(?P<pk>\d+)/$', task.task_del, name='task_del'),
    url(r'^release_info/(?P<pk>\d+)/$', task.release_info, name='release_info'),

    url(r'^login/$', auth.login, name='login'),
    url(r'^logout/$', auth.logout, name='logout'),

    url(r'^user/list/$', user.user_list, name='user_list'),
    url(r'^user/list_all/$', user.user_list_all, name='user_list_all'),
    url(r'^user/add/$', user.user_add, name='user_add'),
    url(r'^user/edit/(?P<pk>\d+)/$', user.user_edit, name='user_edit'),
    url(r'^user/del/(?P<pk>\d+)/$', user.user_del, name='user_del'),
    url(r'^change_password/$', user.change_password, name='change_password'),
    url(r'^upload_avatar/$', user.upload_avatar, name='upload_avatar'),

    url(r'^group_list/$', group.group_list, name='group_list'),
    # url(r'^add_group/$', group.add_group, name='add_group'),
    url(r'^add_group_ajax/$', group.add_group_ajax, name='add_group_ajax'),
    url(r'^edit_group_ajax/$', group.edit_group_ajax, name='edit_group_ajax'),
    # url(r'^edit_group/(?P<pk>\d+)/$', group.edit_group, name='edit_group'),
    url(r'^group/del/(?P<pk>\d+)/$', group.del_group, name='del_group'),

    url(r'^permissions/list/$', permissions.permissions_list, name='permissions_list'),
    url(r'^permissions/add/$', permissions.permissions_add, name='permissions_add'),
    url(r'^permissions/edit/(?P<pk>\d+)/$', permissions.permissions_edit, name='permissions_edit'),
    url(r'^permissions/del/(?P<pk>\d+)/$', permissions.permissions_del, name='permissions_del'),

]

# 配置上传的图片URL路径
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
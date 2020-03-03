from django.conf.urls import url
from . import views
# from django.contrib.auth import login

app_name = 'users'

urlpatterns=[
    url(r'^login/$',views.login_view,name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),  # 此处使用logout_view是为了与其中将调用的logout函数区分开
    url(r'^register/$',views.register,name='register'),
    url(r'^active/(?P<active_code>.*)/$', views.user_active, name="user_active"),  # 提取出active后的所有字符赋给active_code
]
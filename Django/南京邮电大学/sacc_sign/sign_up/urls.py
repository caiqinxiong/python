from django.conf.urls import url

from . import views

app_name = 'sign_up'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^new_team/$',views.new_team,name='new_team'),
    url(r'^my_team/$',views.my_team,name='my_team'),
    url(r'^delete_team/(?P<team_id>\d+)/$',views.delete_team,name='delete_team'),
    url(r'^edit_team/(?P<team_id>\d+)/$',views.edit_team,name='edit_team'),
    url(r'^add_team/$',views.add_team,name='add_team'),
    url(r'^quit_team/(?P<team_id>\d+)$',views.quit_team,name='quit_team'),
    url(r'^delete_member/(?P<member_id>\d+)$',views.delete_member,name='delete_member')
]


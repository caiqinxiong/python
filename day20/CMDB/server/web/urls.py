from django.conf.urls import url, include
from web import views

urlpatterns = [
    url(r'^server/list/', views.server,name='server'),
    url(r'^server/add/', views.server_add,name='server_add'),
    url(r'^server/edit/(\d+)/', views.server_edit,name='server_edit'),
]

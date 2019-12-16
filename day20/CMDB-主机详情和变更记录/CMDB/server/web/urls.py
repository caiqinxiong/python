from django.conf.urls import url, include
from web import views

urlpatterns = [

    url(r'^index/', views.index, name='index'),

    url(r'^business_unit/list/', views.business_unit, name='business_unit'),
    url(r'^business_unit/add/', views.business_unit_change, name='business_unit_add'),
    url(r'^business_unit/edit/(\d+)/', views.business_unit_change, name='business_unit_edit'),

    url(r'^server/list/', views.server, name='server'),
    url(r'^server/add/', views.server_add, name='server_add'),
    url(r'^server/edit/(\d+)/', views.server_edit, name='server_edit'),
    url(r'^server/detail/(\d+)/', views.server_detail, name='server_detail'),
    url(r'^server/record/(\d+)/', views.server_record, name='server_record'),
]

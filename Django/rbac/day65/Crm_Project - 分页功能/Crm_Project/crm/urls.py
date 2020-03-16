from django.conf.urls import url
from crm import views
urlpatterns = [
    url(r'^login/',views.login,name='login'),
    
    url(r'^reg/',views.reg,name='reg'),
    url(r'^index/',views.index,name='index'),

    url(r'^customer_list/',views.customer_list,name='customer_list'),



]

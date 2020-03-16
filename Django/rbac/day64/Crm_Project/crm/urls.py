from django.conf.urls import url
from crm import views
urlpatterns = [
    url(r'^login/',views.login,name='login'),
    url(r'^reg/',views.reg,name='reg'),
    url(r'^index/',views.index,name='index'),


]

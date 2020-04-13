from django.conf.urls import url
from app01 import views
urlpatterns = [
    url(r'^send/sms/', views.send_sms),
    url(r'^register/',views.register,name='register'),
]
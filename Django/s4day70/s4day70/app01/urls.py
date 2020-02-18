from django.conf.urls import url
from app01 import views
# 127.0.0.1:8000/app01/index.html
urlpatterns = [
    url(r'^index.html$', views.index),
]

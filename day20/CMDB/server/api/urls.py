from django.conf.urls import url, include
from api import views

urlpatterns = [
    # url(r'^asset/', views.asset),
    url(r'^asset/', views.Asset.as_view()),
]

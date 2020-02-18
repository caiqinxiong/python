"""mysite67 URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from app01 import views
from app01 import urls as app01_urls
from app02 import urls as app02_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^test/', views.test),
    # url(r'^test2/', views.test2),
    url(r'^upload/$', views.upload),


    url(r'^json997/$', views.json_test, name="json_test"),


    # url(r'^book/[0-9]{2,4}/$', views.book),
    # url(r'^book/([0-9]{2,4})/([a-zA-Z]{2})/$', views.book),

    # url(r'^book/(?P<year>[0-9]{2,4})/(?P<title>[a-zA-Z]{2})/$', views.book),

    url(r'^car/', include(app01_urls, namespace="car"),),
    url(r'^house/', include(app02_urls, namespace="house")),
]

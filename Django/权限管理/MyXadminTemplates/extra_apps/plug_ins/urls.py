from django.conf.urls import url

from .views import getJson, MenuOneXadminView, MenuTwoXadminView, MenuTheXadminView


urlpatterns = [
    url(r'^getJson/', getJson, name='getJson'),  # 获取数据

    url(r'^menuone/$', MenuOneXadminView.as_view(), name='menuone'),
    url(r'^menutwo/$', MenuTwoXadminView.as_view(), name='menutwo'),
    url(r'^menuthe/$', MenuTheXadminView.as_view(), name='menuthe'),
]

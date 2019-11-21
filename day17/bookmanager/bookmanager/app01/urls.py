from django.conf.urls import url
from app01 import views

urlpatterns = [
    # 出版社的展示
    # publisher/
    url(r'^publisher/$', views.publisher_list, name='publisher'),
    # 出版社的增加
    # url(r'^publisher/add/$', views.publisher_add, name='pub_add'),
    url(r'^publisher/add/$', views.PublisherAdd.as_view(), name='pub_add'),
    # url(r'^publisher/add/$', view, name='pub_add'),
    # 出版社的删除
    # url(r'^publisher_del/(?P<pk>\d+)/$', views.publisher_del, name='pub_del'),
    # 出版社的编辑
    url(r'^publisher_edit/$', views.publisher_edit),

    url(r'^book/$', views.book_list, name='book'),
    url(r'^book/add/$', views.BookAdd.as_view(), name='book_add'),
    url(r'^book/edit/(\d+)$', views.BookEdit.as_view(), name='book_edit'),
    # url(r'^book/del/(\d+)$', views.book_del, name='book_del'),
    url(r'^(\w+)/del/(\d+)/$', views.delete, name='del'),



    # # url(r'^home/$', views.home,name='home'),
    #
    # url(r'^get_data/$', views.get_data),

]

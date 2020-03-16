from django.conf.urls import url
from crm.views import auth,customer


urlpatterns = [
    url(r'^login/',auth.login,name='login'),
    
    url(r'^reg/',auth.reg,name='reg'),
    url(r'^index/',auth.index,name='index'),

    # 展示公户
    # url(r'^customer_list/',customer.customer_list,name='customer_list'),
    url(r'^customer_list/',customer.CustomerList.as_view(),name='customer_list'),

    # 展示私户
    # url(r'^my_customer/',customer.customer_list,name='my_customer'),
    url(r'^my_customer/',customer.CustomerList.as_view(),name='my_customer'),

    # # 添加客户
    # url(r'^customer_add/',customer.customer_add,name='customer_add'),
    # # 编辑客户
    # url(r'^customer_edit/(\d+)/',customer.customer_edit,name='customer_edit'),

    # 添加客户
    url(r'^customer_add/', customer.customer_change, name='customer_add'),
    # 编辑客户
    url(r'^customer_edit/(\d+)/', customer.customer_change, name='customer_edit'),



]

from django.conf.urls import url
from crm.views import auth,customer,consult,enrollment


urlpatterns = [
    url(r'^login/$',auth.login,name='login'),
    
    url(r'^reg/$',auth.reg,name='reg'),
    url(r'^index/$',auth.index,name='index'),

    # 展示公户
    # url(r'^customer_list/',customer.customer_list,name='customer_list'),
    url(r'^customer_list/$',customer.CustomerList.as_view(),name='customer_list'),

    # 展示私户
    # url(r'^my_customer/',customer.customer_list,name='my_customer'),
    url(r'^my_customer/$',customer.CustomerList.as_view(),name='my_customer'),

    # # 添加客户
    # url(r'^customer_add/',customer.customer_add,name='customer_add'),
    # # 编辑客户
    # url(r'^customer_edit/(\d+)/',customer.customer_edit,name='customer_edit'),

    # 添加客户
    url(r'^customer_add/$', customer.customer_change, name='customer_add'),
    # 编辑客户
    url(r'^customer_edit/(\d+)/$', customer.customer_change, name='customer_edit'),


    # 展示跟进 ConsultRecord
    url(r'^consult_list/$', consult.ConsultList.as_view(), name='consult_list'),
    # 展示某个客户的跟进
    url(r'^consult_list/(?P<customer_id>\d+)/$', consult.ConsultList.as_view(), name='one_consult_list'),

    # 添加跟进
    url(r'^consult_add/$', consult.consult_add, name='consult_add'),

    # 编辑跟进
    url(r'^consult_edit/(\d+)/$', consult.consult_edit, name='consult_edit'),


    # 展示报名表  Enrollment
    url(r'^enrollment_list/$', enrollment.EnrollmentList.as_view(), name='enrollment_list'),

    # 添加报名表
    url(r'^enrollment_add/(?P<customer_id>\d+)/$', enrollment.enrollment_change, name='enrollment_add'),

    # 编辑报名表
    url(r'^enrollment_edit/(?P<enrollment_id>\d+)/$', enrollment.enrollment_change, name='enrollment_edit'),

]

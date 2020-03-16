from django.conf.urls import url
from crm.views import auth, customer, consult, enrollment, teacher

urlpatterns = [
    url(r'^login/$', auth.login, name='login'),

    url(r'^reg/$', auth.reg, name='reg'),
    url(r'^index/$', auth.index, name='index'),

    # 展示公户
    # url(r'^customer_list/',customer.customer_list,name='customer_list'),
    url(r'^customer_list/$', customer.CustomerList.as_view(), name='customer_list'),

    # 展示私户
    # url(r'^my_customer/',customer.customer_list,name='my_customer'),
    url(r'^my_customer/$', customer.CustomerList.as_view(), name='my_customer'),

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

    # 展示班级  ClassList
    url(r'^class_list/$', teacher.ClassList.as_view(), name='class_list'),

    # 添加班级
    url(r'^class_add/$', teacher.class_change, name='class_add'),

    # 编辑班级
    url(r'^class_edit/(\d+)/$', teacher.class_change, name='class_edit'),

    # 展示课程记录  CourseRecord 某个班级的课程记录
    url(r'^course_record_list/(?P<class_id>\d+)/$', teacher.CourseRecordList.as_view(), name='course_record_list'),

    # 添加课程记录
    url(r'^course_record_add/(?P<class_id>\d+)/$', teacher.course_record_change, name='course_record_add'),

    # 编辑班级
    url(r'^course_record_edit/(?P<course_record_id>\d+)/$', teacher.course_record_change, name='course_record_edit'),

    # 展示学习记录
    url(r'^study_record_list/(?P<course_record_id>\d+)/$', teacher.study_record_list, name='study_record_list'),

]

from django.shortcuts import render,HttpResponse

from django.urls import reverse
# def index(request):
#     user_list = [
#         'n1','n1','n1'
#     ]
#     return render(request,'index.html',{'user_list': user_list})

# url(r'^edit/(\w+)/(\w+)/', views.edit),
# url(r'^edit/11/22/', views.edit),
# url(r'^edit/(?P<a2>\w+)/(?P<a1>\w+)/', views.edit),
# def edit(request,*args,**kwargs):
#     print(args,**kwargs)
#     return HttpResponse('...')
#
# def login(request):
#     return render(request,'login.html')

# 数据库相关操作
def index(request):
    # 增删改查
    from app01 import models
    # 新增
    # models.UserGroup.objects.create(title='销售部')
    # models.UserInfo.objects.create(user='root',password='pwd',age=18,ug_id=1)
    # 查找
    # group_list = models.UserGroup.objects.all()
    # group_list = models.UserGroup.objects.filter(id=1)
    # group_list = models.UserGroup.objects.filter(id__gt=1)
    # group_list = models.UserGroup.objects.filter(id__lt=1)

    # 删除
    # models.UserGroup.objects.filter(id=2).delete()

    # 更新
    models.UserGroup.objects.filter(id=2).update(title='公关部')

    # group_list QuerySet类型（列表）
    # QuerySet类型[obj,obj,obj]
    # print(group_list)
    # for row in group_list:
    #     print(row.id,row.title)
    # models.UserInfo.objects.all()


    group_list = models.UserGroup.objects.all()
    return render(request,'newindex.html',{"group_list": group_list})





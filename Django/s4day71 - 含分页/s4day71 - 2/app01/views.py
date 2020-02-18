from django.shortcuts import render,HttpResponse
from app01 import models
from django.core.paginator import Paginator,Page,PageNotAnInteger,EmptyPage
def test(request):
    # 创建数据
    # models.UserType.objects.create(title='普通用户')
    # models.UserType.objects.create(title='二逼用户')
    # models.UserType.objects.create(title='牛逼用户')

    # models.UserInfo.objects.create(name='方少伟',age=18,ut_id=1)
    # models.UserInfo.objects.create(name='由秦兵',age=18,ut_id=2)
    # models.UserInfo.objects.create(name='刘庚',age=18,ut_id=2)
    # models.UserInfo.objects.create(name='陈涛',age=18,ut_id=3)
    # models.UserInfo.objects.create(name='王者',age=18,ut_id=3)
    # models.UserInfo.objects.create(name='杨涵',age=18,ut_id=1)

    # 获取
    # QuerySet[obj,obj,obj]
    # result = models.UserInfo.objects.all()
    # for obj in result:
    #     print(obj.name,obj.age,obj.ut_id,obj.ut.title)

    # UserInfo，ut是FK字段 - 正向操作  PS: 一个用户只有一个用户类型
    # obj = models.UserInfo.objects.all().first()
    # print(obj.name,obj.age,obj.ut.title)

    # UserType, 表名小写_set.all()  - 反向操作   PS: 一个用户类型下可以有很多用户
    # obj = models.UserType.objects.all().first()
    # print('用户类型',obj.id,obj.title)
    # for row in obj.userinfo_set.all():
    #     print(row.name,row.age)

    # result = models.UserType.objects.all()
    # for item in result:
    #     print(item.title,item.userinfo_set.filter(name='xx'))

    # obj
    # [obj,obj,]

    # result = models.UserInfo.objects.all().values('id','name')
    # QuerySet[{'id':'xx','name':'xx'} ]
    # for row in result:
    #     print(row)

    # result = models.UserInfo.objects.all().values_list('id','name')
    # QuerySet[(1,'f'), ]
    # for row in result:
    #     print(row)

    # 数据获取多个数据时
    # 1. [obj,obj,obj,]
    # models.UserInfo.objects.all()
    # models.UserInfo.objects.filter(id__gt=1)
    # result = models.UserInfo.objects.all()
    # for item in result:
    #     print(item.name,item.ut.title)

    # 2. [{id:1,name:fd},{id:1,name:fd},{id:1,name:fd},]
    # models.UserInfo.objects.all().values('id','name')
    # models.UserInfo.objects.filter(id__gt=1).values('id','name')
    # 无法跨表
    # result = models.UserInfo.objects.all().values('id','name')
    # for item in result:
    #     print(item['id'],item['name'])
    # 夸表  __
    # result = models.UserInfo.objects.all().values('id','name',"ut__title")
    # for item in result:
    #     print(item['id'],item['name'],item['ut__title'])


    # 3. [(1,df),(2,'df')]
    # models.UserInfo.objects.all().values_list('id','name')
    # models.UserInfo.objects.filter(id__gt=1).values_list('id','name')
    # 无法跨表
    # result = models.UserInfo.objects.all().values_list('id','name')
    # for item in result:
    #     print(item[0],item[1])
    # 夸表  __
    # result = models.UserInfo.objects.all().values_list('id','name',"ut__title")
    # for item in result:
    #     print(item[0],item[1],item[2])







    return HttpResponse('...')

from django.views import View
class Login(View):
    """
    get     查
    post    创建
    put     更新
    delete  删除
    """
    def dispatch(self, request, *args, **kwargs):
        print('before')
        obj = super(Login,self).dispatch(request, *args, **kwargs)
        print('after')
        return obj

    def get(self,request):
        # return HttpResponse('Login.get')
        return render(request,'login.html')

    def post(self,request):
        print(request.POST.get('user'))
        return HttpResponse('Login.post')




def index(request):
    """
    分页
    :param request:
    :return:
    """
    # for i in range(300):
    #     name = "root" + str(i)
    #     models.UserInfo.objects.create(name=name,age=18,ut_id=1)


    current_page = request.GET.get('page')

    user_list = models.UserInfo.objects.all()
    paginator = Paginator(user_list,10)
    # per_page: 每页显示条目数量
    # count:    数据总个数
    # num_pages:总页数
    # page_range:总页数的索引范围，如: (1,10),(1,200)
    # page:     page对象
    try:
        posts = paginator.page(current_page)
    except PageNotAnInteger as e:
        posts = paginator.page(1)
    except EmptyPage as e:
        posts = paginator.page(1)
    # has_next              是否有下一页
    # next_page_number      下一页页码
    # has_previous          是否有上一页
    # previous_page_number  上一页页码
    # object_list           分页之后的数据列表
    # number                当前页
    # paginator             paginator对象
    return render(request,'index.html',{'posts':posts})

from utils.pager import PageInfo
def custom(request):
    # 表示用户当前想要访问的页码: 8

    all_count = models.UserInfo.objects.all().count()

    page_info = PageInfo(request.GET.get('page'),all_count,10,'/custom.html',11)
    user_list = models.UserInfo.objects.all()[page_info.start():page_info.end()]

    return render(request,'custom.html',{'user_list':user_list,'page_info':page_info})













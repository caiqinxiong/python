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


    # v = models.UserInfo.objects.values('id','name') # 6
    # v = models.UserInfo.objects.values('id','name','ut__title') # 6
    # select * from userinfo left join usertype

    # v1 = models.UserType.objects.values('id','title')
    # print(v1) # 4
    # v2 = models.UserType.objects.values('id','title','userinfo__name')
    # print(v2)
    # select  * from usertype left join userinfo

    # 排序
    # user_list = models.UserInfo.objects.all().order_by('-id','name')
    # print(user_list)

    # 分组
    from django.db.models import Count,Sum,Max,Min
    # v =models.UserInfo.objects.values('ut_id').annotate(xxxx=Count('id'))
    # print(v.query)
    # v =models.UserInfo.objects.values('ut_id').annotate(xxxx=Count('id')).filter(xxxx__gt=2)
    # print(v.query)
    # v =models.UserInfo.objects.filter(id__gt=2).values('ut_id').annotate(xxxx=Count('id')).filter(xxxx__gt=2)
    # print(v.query)
    # 过滤
    # models.UserInfo.objects.filter(id__gt=1)
    # models.UserInfo.objects.filter(id__lt=1)
    # models.UserInfo.objects.filter(id__lte=1)
    # models.UserInfo.objects.filter(id__gte=1)
    # models.UserInfo.objects.filter(id__in=[1,2,3])
    # models.UserInfo.objects.filter(id__range=[1,2])
    # models.UserInfo.objects.filter(name__startswith='xxxx')
    # models.UserInfo.objects.filter(name__contains='xxxx')
    # models.UserInfo.objects.exclude(id=1)

    # F,Q,extra
    # from django.db.models import F
    # models.UserInfo.objects.all().update(age=F("age")+1)

    # Q
    # models.UserInfo.objects.filter(id=1,name='root')

    # condition = {
    #     'id':1,
    #     'name': 'root'
    # }
    # models.UserInfo.objects.filter(**condition)
    # Q使用有两种方式：对象方式，方法方式*

    # from django.db.models import Q
    # models.UserInfo.objects.filter(Q(id__gt=1))
    # models.UserInfo.objects.filter(Q(id=8) | Q(id=2))
    # models.UserInfo.objects.filter(Q(id=8) & Q(id=2))

     # q1 = Q()
    # q1.connector = 'OR'
    # q1.children.append(('id__gt', 1))
    # q1.children.append(('id', 10))
    # q1.children.append(('id', 9))
    #
    #
    # q2 = Q()
    # q2.connector = 'OR'
    # q2.children.append(('c1', 1))
    # q2.children.append(('c1', 10))
    # q2.children.append(('c1', 9))
    #
    # q3 = Q()
    # q3.connector = 'AND'
    # q3.children.append(('id', 1))
    # q3.children.append(('id', 2))
    # q2.add(q3,'OR')
    #
    # con = Q()
    # con.add(q1, 'AND')
    # con.add(q2, 'AND')

    # condition_dict = {
    #     'k1':[1,2,3,4],
    #     'k2':[1,],
    # }
    # con = Q()
    # for k,v in condition_dict.items():
    #     q = Q()
    #     q.connector = 'OR'
    #     for i in v:
    #         q.children.append(('id', i))
    #     con.add(q,'AND')
    # models.UserInfo.objects.filter(con)
    #
    # q1 = Q()
    # q1.connector = 'OR'
    # q1.children.append(('id', 1))
    # q1.children.append(('id', 10))
    # q1.children.append(('id', 9))
    #
    #
    # q2 = Q()
    # q2.connector = 'OR'
    # q2.children.append(('c1', 1))
    # q2.children.append(('c1', 10))
    # q2.children.append(('c1', 9))
    #
    # q3 = Q()
    # q3.connector = 'AND'
    # q3.children.append(('id', 1))
    # q3.children.append(('id', 2))
    # q2.add(q3,'OR')
    #
    # con = Q()
    # con.add(q1, 'AND')
    # con.add(q2, 'AND')
    # (id=1 or id = 10 or id=9 or (id=1 and id=2)) and (c1=1 or c1=10 or c1=9)





    # """
    #     select
    #         id,
    #         name,
    #         (select count(1) from tb) as n
    #     from xb where ....
    # """
    #
    # v = models.UserInfo.objects.all().extra(
    #     select={
    #         'n':"select count(1) from app01_usertype where id=%s or id=%s",
    #         'm':"select count(1) from app01_usertype where id=%s or id=%s",
    #     },
    #     select_params=[1,2,3,4])
    # for obj in v:
    #     print(obj.name,obj.id,obj.n)

    # models.UserInfo.objects.extra(
    #     where=["id=1","name='alex'"]
    # )
    # models.UserInfo.objects.extra(
    #     where=["id=1 or id=%s ","name=%s"],
    #     params=[1,"alex"]
    # )

    # models.UserInfo.objects.extra(
    #     tables=['app01_usertype'],
    # )
    # """select * from app01_userinfo,app01_usertype"""


    # result = models.UserInfo.objects.filter(id__gt=1)
    # print(result.query)
    # result = models.UserInfo.objects.filter(id__gt=1).extra(
    #     where=['app01_userinfo.id < %s'],
    #     params=[100,],
    #     tables=['app01_usertype'],
    #     order_by=['-app01_userinfo.id'],
    #     select={'uid':1,'sw':"select count(1) from app01_userinfo"}
    # )
    # print(result.query)

    # v = models.UserInfo.objects.all().order_by('-id','name')
    # v = models.UserInfo.objects.all().order_by('-id','name').reverse()
    # v = models.UserInfo.objects.all().order_by('id','-name')
    # print(v)

    # v = models.UserInfo.objects.all()
    # [obj]
    # 10
    # 1
    # v = models.UserInfo.objects.all().only('id','name')
    # v = models.UserInfo.objects.all().defer('name')
    # # [obj]
    # for obj in v:
    #     # 10
    #     obj.id,obj.name
    # models.UserInfo.objects.values('id','name')
    # [{id,nam}]

    # models.UserInfo.objects.all().using('db2')

    # models.UserInfo.objects.all().filter().all().exclude().only().defer()

    # models.UserInfo.objects.none()
    # result = models.UserInfo.objects.aggregate(k=Count('ut_id', distinct=True), n=Count('id'))
    # print(result)

    # v = models.UserInfo.objects.all().first()
    # # models.UserInfo.objects.get(id=1)
    #
    # obj = models.UserType.objects.create(title='xxx')
    # obj = models.UserType.objects.create(**{'title': 'xxx'})
    # print(obj.id)
    #
    # obj = models.UserType(title='xxx')
    # obj.save()


    # objs = [
    #     models.UserInfo(name='r11'),
    # ]
    # models.UserInfo.objects.bulk_create(objs, 10)

    # obj, created = models.UserInfo.objects.get_or_create(
    #     username='root1',
    #     pwd='ff',
    #     defaults={'email': '1111111','u_id': 2, 't_id': 2})

    # models.UserInfo.objects.filter(id__in=[1,2,3])
    # models.UserInfo.objects.in_bulk([1,2,3])
    # name_map = {'first': 'first_name', 'last': 'last_name', 'bd': 'birth_date', 'pk': 'id'}
    # models.UserInfo.objects.raw('SELECT * FROM app01_usertype', translations=name_map)
    name_map = {'title': 'name'}
    v1 = models.UserInfo.objects.raw('SELECT id,title FROM app01_usertype',translations=name_map)
    for i in v1:
        print(i,type(i))

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













from django.shortcuts import render,redirect,HttpResponse
from app01 import models

# Create your views here.
def login(request):
    # print(request.method,type(request.method))
    if request.method == 'POST':
        # 获取用户提交的数据
        # print(request.POST,type(request.POST))
        user = request.POST.get('user')
        pwd = request.POST.get('password')
        # print(user,type(user))
        # print(pwd,type(pwd))
        # 校验
        if models.User.objects.filter(username=user,password=pwd):
            # 校验成功跳转
            return redirect('/publisher_list/')
        # 校验失败回复错误信息
        return render(request, 'html/login.html', {'error': '用户名或密码错误'})
    # 返回页面
    return render(request, 'html/login.html')

def index(request):
    # 业务逻辑
    return render(request, 'html/index.html')

def publisher_list(request):
    # 查询所有的出版社的对象
    all_publishers = models.Publisher.objects.all()
    # 返回一个页面
    return render(request, 'html/publisher_list.html', {'all_publishers': all_publishers})


def publisher_add(request):
    if request.method == 'POST':
        # 获取提交的数据
        pub_name = request.POST.get('pub_name')
        # 校验
        if not pub_name:
            return render(request, 'html/publisher_add.html', {'error': '名称不能为空'})
        # 插入数据库
        ret = models.Publisher.objects.create(name=pub_name)  # 返回新插入的对象
        print(ret, type(ret))
        # 跳转到展示页面
        return redirect('/publisher_list/')

    return render(request, 'html/publisher_add.html')


def publisher_del(request):
    # 获取提交的数据
    pk = request.GET.get('pk')
    # 删除对应的数据
    # models.Publisher.objects.get(pk=pk).delete()  # 单个对象删除
    models.Publisher.objects.filter(pk=pk).delete()  # 对象列表删除
    # 跳转到展示页面
    return redirect('/publisher_list/')


def publisher_edit(request):
    # 获取提交的数据
    pk = request.GET.get('pk')
    # 查找到要编辑的对象
    obj = models.Publisher.objects.get(pk=pk)

    if request.method == 'POST':
        # 获取新提交的数据
        pub_name = request.POST.get('pub_name')

        obj.name = pub_name  # 在内存中修改了属性
        obj.save()  # 向数据库提交更新

        # 跳转到展示页面
        return redirect('/publisher_list/')

    return render(request, 'html/publisher_edit.html', {'obj': obj})


def publisher_find(request):
    if request.method == 'POST':
        # 获取提交的数据
        pub_name = request.POST.get('pub_name')
        # 校验
        if not pub_name:
            return render(request, 'html/publisher_find.html', {'error': '名称不能为空！！'})
        find_publishers = models.Publisher.objects.filter(name=pub_name)
        if find_publishers:
            # 返回c查找信息
            return render(request, 'html/publisher_list.html', {'all_publishers': find_publishers})
        else:
           return HttpResponse( '<h1>没有找到相关信息！</h1>')

    return render(request, 'html/publisher_find.html')


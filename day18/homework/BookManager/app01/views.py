from django.shortcuts import render, redirect, reverse, HttpResponse
from app01 import models
from functools import wraps
import time
import json
from django.http.response import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator

def index(request):
    # 业务逻辑
    return render(request, 'index.html')

def login_status(func):
    def inner(request,*args,**kwargs):
        is_login = request.COOKIES.get('is_login')
        if not is_login:
            url = request.path_info # 获取URL信息
            return redirect("{}?return={}".format(reverse('login'),url))
        ret = func(request,*args,**kwargs)
        return ret
    return inner

def logout(request):
    ret = redirect(reverse('login'))
    # ret.delete_cookie('is_login')
    # request.session.pop('is_login')
    request.session.flush()

    return ret

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
            # 设置session
            request.session["user"] = user
            # request.session.set_expiry(3) # 设置session3秒过期，没生效，在settings里设置了
            return_url = request.GET.get('return')
            print(return_url)
            if return_url:
                response = redirect(return_url)
            else:
                response = redirect(reverse('publisher'))
            # 设置登录状态的cookie
            # response.set_cookie('is_login',True) # 可以任意自定义
            # 校验成功跳转
            return response
        # 校验失败回复错误信息
        return render(request, 'login.html', {'error': '用户名或密码错误'})
    # 返回页面
    return render(request, 'login.html')

def register(request):
    '''注册'''
    if request.method == 'POST':
        # 获取用户提交的数据
        # print(request.POST,type(request.POST))
        user = request.POST.get('user')
        pwd1 = request.POST.get('password')
        pwd2 = request.POST.get('password2')
        print(user,type(user))
        print(pwd1,type(pwd1))
        # 校验
        if not user or not pwd1 or not pwd2:
            return render(request, 'register.html', {'error': '带*号输入内容不能为空！'})
        elif models.User.objects.filter(username=user):
            return render(request,'register.html',{'error':'用户名已存在！'})
        elif pwd1 != pwd2:
            return render(request, 'register.html', {'error': '两次输入密码不一致！'})
        else:
            models.User.objects.create(username=user,password=pwd1)
            # return render(request, 'login.html')
            return redirect(reverse('publisher'))
    # 返回页面
    return render(request, 'register.html')


def get_data(request):
    ret = {'name': "alex", 'age': 84}  # 数字 字符串 列表  字典  None  布尔值
    ret = [1, 2, 3, 4]
    # return HttpResponse(json.dumps(ret))  #  Content-Type: text/html charset:utf-8
    return JsonResponse(ret, safe=False)  # Content-Type: application/json


def timer(func):
    @wraps(func)
    def inner(request, *args, **kwargs):
        print(request.path_info)
        print(request.get_full_path())
        # 执行之前
        start = time.time()
        ret = func(request, *args, **kwargs)
        print('{}函数执行的时间是:{}'.format(func.__name__, time.time() - start))
        # 执行之后
        return ret

    return inner


# Create your views here.
# 展示出版社
@timer  # publisher_list = timer(publisher_list)
# @login_status
def publisher_list(request, *args, **kwargs):
    # 查询所有的出版社的对象
    all_publishers = models.Publisher.objects.all()  # QuerySet [ 对象 ]
    if request.method == 'POST':
        search = request.POST.get('search')
        if not search:return HttpResponse('<h1>搜索内容不能为空！</h1>')
        all_publishers = models.Publisher.objects.filter(name__contains=search)
    print(args)
    print(kwargs)
    # url = reverse('app01:pub')
    # print(url,type(url))
    #
    # url = reverse('app01:pub_del',args=(2,))
    # print(url, type(url))
    #
    # url = reverse('app01:pub_del', kwargs={'pk':'100'})
    # print(url, type(url))
    # 返回一个页面
    return render(request, 'publisher_list.html', {'all_publishers': all_publishers})


def publisher_add(request):
    if request.method == 'POST':
        # 获取提交的数据
        pub_name = request.POST.get('pub_name')
        # 校验
        if not pub_name:
            return render(request, 'publisher_add.html', {'error': '名称不能为空'})
        # 插入数据库
        ret = models.Publisher.objects.create(name=pub_name)  # 返回新插入的对象
        print(ret, type(ret))
        # 跳转到展示页面
        return redirect('pub')

    return render(request, 'publisher_add.html')

# @method_decorator(timer,name='post')
@method_decorator(timer, name='dispatch')
class PublisherAdd(View):
    http_method_names = ['get', 'post']

    # @method_decorator(timer)
    # def dispatch(self, request, *args, **kwargs):
    #     #     ret = super().dispatch(request, *args, **kwargs)
    #     #     return ret

    # @method_decorator(timer)
    def get(self, request, *args, **kwargs):
        # 处理GET请求的逻辑
        print(self.request is request)
        print('get')
        return render(request, 'publisher_add.html')

    def post(self, request, *args, **kwargs):
        # 处理GET请求的逻辑
        # 获取提交的数据
        print('post')
        pub_name = request.POST.get('pub_name')
        # 校验
        if not pub_name:
            return render(request, 'publisher_add.html', {'error': '名称不能为空'})
        # 插入数据库
        ret = models.Publisher.objects.create(name=pub_name)  # 返回新插入的对象
        print(ret, type(ret))
        # 跳转到展示页面
        ret = HttpResponse('', status=302)
        # return redirect('pub')
        ret['Location'] = reverse('publisher')
        return ret


def publisher_del(request, pk):
    print(pk, type(pk))
    # 获取提交的数据
    # pk = request.GET.get('pk')
    # 删除对应的数据
    # models.Publisher.objects.get(pk=pk).delete()  # 单个对象删除   # get 不存在 或者 多个 就报错
    models.Publisher.objects.filter(pk=pk).delete()  # 对象列表删除
    # 跳转到展示页面
    return redirect(reverse('pub'))


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
        # return redirect(reverse('pub'))
        # 查询所有的出版社的对象
        all_publishers = models.Publisher.objects.all()  # QuerySet [ 对象 ]
        return render(request, 'publisher_list.html', {'all_publishers': all_publishers})

    return render(request, 'publisher_edit.html', {'obj': obj})

# @login_status
def book_list(request):
    all_books = models.Book.objects.all()  # [book_obj]
    if request.method == 'POST':
        search = request.POST.get('search')
        if not search:return HttpResponse('<h1>搜索内容不能为空！</h1>')
        all_books = models.Book.objects.filter(title__contains=search)
    for book in all_books:
        print(book.pk)
        print(book.title)
        print(book.pub, type(book.pub))  # book.外键  _>  所关联的对象
        print(book.pub_id)  # 从数据库中获取所关联的对象id

    return render(request, 'book.html', {'all_books': all_books})


class BookAdd(View):

    def get(self, request):
        # 查询所有的出版社
        all_pubs = models.Publisher.objects.all()
        return render(request, 'book_add.html', {'all_pubs': all_pubs})

    def post(self, request):
        # 获取参数
        title = request.POST.get('title')
        pub_id = request.POST.get('pub_id')
        # 插入数据
        # models.Book.objects.create(title=title,pub=models.Publisher.objects.get(pk=pub_id))
        models.Book.objects.create(title=title, pub_id=pub_id)
        # 重定向
        return redirect(reverse('book'))


class BookEdit(View):
    def get(self, request, pk):
        book_obj = models.Book.objects.get(pk=pk)
        all_pubs = models.Publisher.objects.all()
        return render(request, 'book_edit.html', {'book_obj': book_obj, 'all_pubs': all_pubs})

    def post(self, request, pk):
        # book_obj = models.Book.objects.get(pk=pk)
        # 新提交的数据
        title = request.POST.get('title')
        pub_id = request.POST.get('pub_id')
        # 修改
        # book_obj.title = title
        # # book_obj.pub = models.Publisher.objects.get(pk=pub_id)
        # book_obj.pub_id = pub_id
        # book_obj.save()
        # 编辑的方式
        models.Book.objects.filter(pk=pk).update(title=title, pub_id=pub_id)
        return redirect(reverse('book'))


def book_del(request, pk):
    book_obj = models.Book.objects.get(pk=pk)
    book_obj.delete()
    return redirect('book')


def delete(request, table, pk):
    model_class = getattr(models, table.capitalize())
    model_class.objects.get(pk=pk).delete()
    return redirect(reverse(table))

# @login_status
def author_list(request):
    all_authors = models.Author.objects.all()
    if request.method == 'POST':
        search = request.POST.get('search')
        if not search:return HttpResponse('<h1>搜索内容不能为空！</h1>')
        all_authors = models.Author.objects.filter(name__contains=search)
    for author in all_authors:
        print(author.pk)
        print(author.name)
        print(author.books, type(author.books))  # 关系管理对象
        print(author.books.all(), type(author.books.all()))  # 关联的所有的对象  [对象]
    return render(request, 'author.html', {'all_authors': all_authors})


def author_add(request):
    if request.method == 'POST':
        # 获取用户提交的数据
        author_name = request.POST.get('author_name')
        book_id = request.POST.getlist('book_id')
        # 插入数据
        author_obj = models.Author.objects.create(name=author_name) # 在作者表创建作者数据
        # 设置多对多的关系
        author_obj.books.set(book_id) # ['3', '4'] 在第三张表中创建多对多的关系
        return redirect(reverse('author'))

    all_books = models.Book.objects.all()
    return render(request, 'author_add.html', {'all_books': all_books})

def author_edit(request,pk):
    author_obj = models.Author.objects.get(pk=pk)

    if request.method == 'POST':
        author_name = request.POST.get('author_name')
        book_id = request.POST.getlist('book_id')
        author_obj.name = author_name
        author_obj.save()
        author_obj.books.set(book_id)
        return redirect('author')

    all_books = models.Book.objects.all()

    return render(request, 'author_edit.html', {'all_books':all_books,'author_obj': author_obj})



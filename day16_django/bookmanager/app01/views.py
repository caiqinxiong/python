from django.shortcuts import render, redirect, reverse,HttpResponse
from app01 import models
from functools import wraps
import time
import json
from django.http.response import JsonResponse

def get_data(request):
    ret = {'name':"alex",'age':84}  # 数字 字符串 列表  字典  None  布尔值
    ret = [1,2,3,4]
    # return HttpResponse(json.dumps(ret))  #  Content-Type: text/html charset:utf-8
    return JsonResponse(ret,safe=False)  # Content-Type: application/json



def timer(func):
    @wraps(func)
    def inner(request,*args, **kwargs):

        print(request.path_info)
        print(request.get_full_path())
        # 执行之前
        start = time.time()
        ret = func(request,*args, **kwargs)
        print('{}函数执行的时间是:{}'.format(func.__name__, time.time() - start))
        # 执行之后
        return ret

    return inner


# Create your views here.
# 展示出版社
@timer  # publisher_list = timer(publisher_list)
def publisher_list(request, *args, **kwargs):
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

    # 查询所有的出版社的对象
    all_publishers = models.Publisher.objects.all()  # QuerySet [ 对象 ]
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


from django.views import View

from django.utils.decorators import method_decorator

# @method_decorator(timer,name='post')
@method_decorator(timer,name='dispatch')
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
        ret = HttpResponse('',status=302)
        # return redirect('pub')
        ret['Location'] = reverse('pub')
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
        return redirect(reverse('pub'))

    return render(request, 'publisher_edit.html', {'obj': obj})

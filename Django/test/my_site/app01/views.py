from django.shortcuts import render,HttpResponse
from app01.models import *

# Create your views here.
def test_views(request):
    print('李小欣你好吗？')
    return HttpResponse('李小欣，你回去没有啊，都这么晚了！')

def index(request):
    #list=Account.objects.all()
    list=Article.objects.all()
    context={'booklist':list}
    return render(request,'app01/index.html',context)

def login_views(request):
#     html = '''
#     <form >
#     <input type="text" name="username"><br>
#     <input type="password" name="passwd"><br>
#     <input type="submit" value="登录">
# </form>
#     '''
#     return HttpResponse(html)
    return render(request,'app01/form.html')

def article_2003(request):
    return HttpResponse('静态路由！！')

def archive_name(request,name):
    return HttpResponse('动态路由，包括特殊字符的任意匹配！！%s' % name)

def archive(request,year,month):
    return HttpResponse('动态路由！%s-%s' % (year,month))

def archive3(request,year,month,slug):
    return HttpResponse('动态路由！%s-%s %s' % (year,month,slug))

def archive2(request,arg1,arg2):
    return HttpResponse('动态路由！%s-%s' % (arg1,arg2))
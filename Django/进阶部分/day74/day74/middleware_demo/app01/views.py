from django.shortcuts import render, HttpResponse, redirect

# Create your views here.


def index(request):
    print("这是app01里面的index视图函数...")
    # raise ValueError("sb")
    rep = HttpResponse("O98K")
    print("视图函数中的s10:", request.s10)
    # def render():
    #     print("我是index视图函数内部的render方法")
    #     return redirect("http://www.luffycity.com")
    #
    # rep.render = render
    return rep

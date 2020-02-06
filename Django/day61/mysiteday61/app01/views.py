from django.shortcuts import HttpResponse, render, redirect

from app01 import models
# Create your views here.
# 专门用来放函数


# 登录的函数
def login(request):
    error_msg = ""
    if request.method == "POST":  # 这里必须是大写的
        # 如果你是POST请求,我就取出提交的数据,做登录判断
        print(request.POST["email"])
        email = request.POST.get("email", None)
        pwd = request.POST.get("pwd", None)
        print(email, pwd)
        # 做是否登陆成功的判断
        if email == "alex@oldboyedu.com" and pwd == "alexdsb":
            # 登录成功
            # 回复一个特殊的响应,这个响应会让用户的浏览器请求指定的URL
            return redirect("http://www.luffycity.com")
        else:
            # 登录失败
            error_msg = "邮箱或密码错误"
    # 不是POST请求就走下面这一句
    return render(request, "login.html", {"error": error_msg})


# 展示所有的用户的函数
def user_list(request):
    # 去数据库中查询所有的用户
    # 利用ORM这个工具去查询数据库,不用自己去查询
    ret = models.UserInfo.objects.all()  # [UserInfo Object, UserInfo Object]
    print(ret[0].id, ret[0].name)
    # 打开user_list.html文件,
    return render(request, "user_list.html", {"user_list": ret})
    # return HttpResponse("别哭了!")


# 添加用户的函数
def add_user(request):
    if request.method == "POST":
        # 用户填写了新的用户名,并发送了POST请求过来
        new_name = request.POST.get("username", None)
        # 去数据库中新创建一条用户记录
        models.UserInfo.objects.create(name=new_name)
        # return HttpResponse("添加成功!")
        # 添加成功后直接跳转到用户列表页
        return redirect("/user_list/")

    # 第一个请求页面的时候,就返回一个页面,页面上有两个框让用户填写
    return render(request, "add_user.html")
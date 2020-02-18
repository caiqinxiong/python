from django.shortcuts import render, HttpResponse, redirect
from app01 import models

from django.urls import reverse

# Create your views here.


def delete(request, table_name, delete_id):
    print(table_name, delete_id)
    # 需要判断一下 表名和id值是否都是正经的数据

    # models.Book.objects.get(id=1).delete()
    # 从另外一个文件 根据字符串 反射具体的变量
    table_name = table_name.capitalize()
    if hasattr(models, table_name):
        # 如果能找到
        table_class = getattr(models, table_name)
        try:
            table_class.objects.get(id=delete_id).delete()
        except Exception as e:
            print(str(e))
            print("id值不存在！")
        return HttpResponse("表名:{} id:{}".format(table_name, delete_id))
    else:
        return HttpResponse("表不存在！")
    url = reverse("home", args=("baobao", ))
    return redirect("/home/")


def home(request, arg):
    return render(request, "home.html")

def test(request):
    print("首页的url是：", reverse("home", args=("house",)))
    print("index的url是：", reverse("index", kwargs={"name": "yimi"}))
    return render(request, "test.html")


def index(request, name):
    print(name)
    return HttpResponse("这是index页面！！！")
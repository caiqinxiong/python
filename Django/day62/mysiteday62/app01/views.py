from django.shortcuts import HttpResponse, render, redirect
from app01 import models
# Create your views here.


# 展示出版社列表
def publisher_list(request):
    # 去数据库查出所有的出版社,填充到HTML中,给用户返回
    ret = models.Publisher.objects.all().order_by("id")
    return render(request, "publisher_list.html", {"publisher_list": ret})


# 添加新的出版社
def add_publisher(request):
    error_msg = ""
    # 如果是POST请求,我就取到用户填写的数据
    if request.method == "POST":
        new_name = request.POST.get("publisher_name", None)
        if new_name:
            # 通过ORM去数据库里新建一条记录
            models.Publisher.objects.create(name=new_name)
            # 引导用户访问出版社列表页,查看是否添加成功  --> 跳转
            return redirect("/publisher_list/")
        else:
            error_msg = "出版社名字不能为空!"
    # 用户第一次来,我给他返回一个用来填写的HTML页面
    return render(request, "add_publisher.html", {"error": error_msg})


# 删除出版社的函数
def delete_publisher(request):
    print(request.GET)
    print("=" * 120)
    # 删除指定的数据
    # 1. 从GET请求的参数里面拿到将要删除的数据的ID值
    del_id = request.GET.get("id", None)  # 字典取值,娶不到默认为None
    # 如果能取到id值
    if del_id:
        # 去数据库删除当前id值的数据
        # 根据id值查找到数据
        del_obj = models.Publisher.objects.get(id=del_id)
        # 删除
        del_obj.delete()
        # 返回删除后的页面,跳转到出版社的列表页,查看删除是否成功
        return redirect("/publisher_list/")
    else:
        return HttpResponse("要删除的数据不存在!")


# 编辑出版社
def edit_publisher(request):
    # 用户修改完出版社的名字,点击提交按钮,给我发来新的出版社名字
    if request.method == "POST":
        print(request.POST)
        # 取新出版社名字
        edit_id = request.POST.get("id")
        new_name = request.POST.get("publisher_name")
        # 更新出版社
        # 根据id取到编辑的是哪个出版社
        edit_publisher = models.Publisher.objects.get(id=edit_id)
        edit_publisher.name = new_name
        edit_publisher.save()  # 把修改提交到数据库
        # 跳转出版社列表页,查看是否修改成功
        return redirect("/publisher_list/")
    # 从GET请求的URL中取到id参数
    edit_id = request.GET.get("id")
    if edit_id:
        # 获取到当前编辑的出版社对象
        publisher_obj = models.Publisher.objects.get(id=edit_id)
        return render(request, "edit_publisher.html", {"publisher": publisher_obj})
    else:
        return HttpResponse("编辑的出版社不存在!")


def test(request):
    print(request.GET)
    print(request.GET.get("id"))
    return HttpResponse("OK")

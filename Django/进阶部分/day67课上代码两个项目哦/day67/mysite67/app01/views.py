from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse

# Create your views here.


def test(request):
    data = ["第{:0>3}号技师".format(i) for i in range(1, 11)]
    return render(request, "test.html", {"results": data})


def test2(request):
    return render(request, "test2.html")


# 处理上传文件的函数
def upload(request):
    """
    保存上传文件前，数据需要存放在某个位置。默认当上传文件小于2.5M时，django会将上传文件的全部内容读进内存。从内存读取一次，写磁盘一次。
    但当上传文件很大时，django会把上传文件写到临时文件中，然后存放到系统临时文件夹中。
    :param request:
    :return:
    """
    if request.method == "POST":
        print(request.FILES)
        print(request.FILES["upload_file"].name)
        # 从请求的FILES中获取上传文件的文件名，file为页面上type=files类型input的name属性值
        filename = request.FILES["upload_file"].name
        # # 在项目目录下新建一个文件
        with open(filename, "wb") as f:
            # 从上传的文件对象中一点一点读
            for i in request.FILES["upload_file"].chunks():
                # 写入本地文件
                f.write(i)
        return HttpResponse("上传OK")

    else:
        return render(request, "upload.html")


def json_test(request):
    data = {"name": "小黑", "age": 18}
    data2 = [11, 22, 33, 44]
    # import json
    # data_str = json.dumps(data2)  # 把data序列化成json格式的字符串
    # return HttpResponse(data_str)

    from django.http import JsonResponse
    return JsonResponse(data2, safe=False)


# 位置参数
# def book(request, arg1, arg2):
#     print("arg1:", arg1)
#     print("arg2:", arg2)
#     return HttpResponse("口哥说一个~")


# 关键字参数
def book(request, year, title):
    print("year:", year, type(year))
    print("title:", title)
    return HttpResponse("口哥说一个~")


def home(request, age):
    print(age)
    # 传位置参数
    redirect_url = reverse("car:book", args=(2018, "sb"))
    # 传关键字参数
    # redirect_url = reverse("car:book", kwargs={"year": 2018, "title": "sb"})
    print(redirect_url)
    # return redirect(redirect_url)

    return render(request, "car/home.html")




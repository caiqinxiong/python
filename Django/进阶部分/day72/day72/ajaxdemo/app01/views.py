from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return render(request, "index.html")


def ajax_add(request):
    print(request.GET)
    print(request.GET.get("i1"))
    print(request.GET.get("i2"))

    i1 = int(request.GET.get("i1"))
    i2 = int(request.GET.get("i2"))
    # i1 = request.GET.get("i1")
    # i2 = request.GET.get("i2")
    #
    # i1 = int(i1)
    # i2 = int(i2)
    # print(i1, i2)
    # print("=" * 120)
    # ret = i1 + i2

    ret = i1 + i2
    return HttpResponse(ret)

def ajax_add3(request):
    print(request.POST)
    print("-" * 120)
    i1 = int(request.POST.get("i1"))
    i2 = int(request.POST.get("i2"))
    # i1 = request.GET.get("i1")
    # i2 = request.GET.get("i2")
    #
    # i1 = int(i1)
    # i2 = int(i2)
    # print(i1, i2)
    # print("=" * 120)
    # ret = i1 + i2

    ret = i1 + i2
    return HttpResponse(ret)


def test(request):
    # import time
    # time.sleep(5)
    url = "http://p7.yokacdn.com/pic/YOKA_HZP/2018-01-19/U10089P42TS1516351813_11903.jpg"
    # return HttpResponse(url)
    # return render(request, "index.html")
    return HttpResponse("http://www.luffycity.com")

from app01 import models
def persons(request):
    ret = models.Person.objects.all()

    # person_list = []
    # for i in ret:
    #     person_list.append({"name": i.name, "age": i.age})
    # print(person_list)
    # import json
    # s = json.dumps(person_list)
    # print(s)

    # from django.core import serializers
    # s = serializers.serialize("json", ret)
    # print(s)
    # return HttpResponse(s)

    return render(request, "sweetalert_demo.html", {"persons": ret})


def delete(request):
    import time
    time.sleep(3)
    del_id = request.POST.get("id")
    models.Person.objects.filter(id=del_id).delete()
    return HttpResponse("删除成功！")

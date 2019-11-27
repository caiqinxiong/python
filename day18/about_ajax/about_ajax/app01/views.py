from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    if request.method == 'POST':
        i1 = request.POST.get('i1')
        i2 = request.POST.get('i2')
        i3 = int(i1) + int(i2)
        return render(request, 'index.html', {'i1': i1, 'i2': i2, 'i3': i3})
    return render(request, 'index.html', )


# ajax 发送请求的js技术
# 特点 ： 异步  局部刷新  传输的数据量小
import time


def calc(request):
    l1 = request.POST.get('l1')
    l2 = request.POST.get('l2')
    time.sleep(3)
    return HttpResponse(int(l1) + int(l2))


from django.http.response import JsonResponse


def calc2(request):
    l1 = request.POST.get('l1')
    l2 = request.POST.get('l2')
    return JsonResponse({'status': 'ok', 'data': int(l1) + int(l2)})


import json

def test(request):
    print(request.POST)

    # ret = request.POST.getlist('hobby[]')
    # print(ret,type(ret))

    ret = request.POST.get('hobby')
    ret = json.loads(ret)
    print(ret,type(ret))

    return JsonResponse({'status': 'ok', })


def file_upload(request):

    if request.method == 'POST':
        f1 = request.FILES.get('f1')
        with open(f1.name,'wb') as f:
            for i in f1.chunks():
                f.write(i)

    return render(request,'file_upload.html')
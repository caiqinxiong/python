from django.shortcuts import render

# Create your views here.
import queue
from django.shortcuts import render,HttpResponse
from django.http import JsonResponse

QUEUE_DICT = {}


def home(request):
    name = request.GET.get('name')
    QUEUE_DICT[name] = queue.Queue()
    return  render(request,'home.html',{'name':name})

def send_massage(request):
    msg = request.POST.get('msg')
    print(msg)
    for q in QUEUE_DICT.values():
        q.put(msg)

    return HttpResponse('发送成功！')


def get_massage(request):
    name = request.GET.get('name')
    q = QUEUE_DICT[name]
    result = {'status':True,'data':None}
    try:
        data = q.get(timeout=10)
        result['data'] = data
    except queue.Empty as e:
        result['status'] = False

    return JsonResponse(result)



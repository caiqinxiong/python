from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
import queue
import json

QUEUE_DICT = {}

def home(request):
    name = request.GET.get('name')
    QUEUE_DICT[name] = queue.Queue()
    return render(request,'home.html',{'name':name})

def send_message(request):
    """
    接收客户端端浏览器发送的消息
    :param request:
    :return:
    """
    msg = request.POST.get('msg')
    for q in QUEUE_DICT.values():
        q.put(msg)

    return HttpResponse('发送成功')

def get_message(request):
    """
    浏览器获取消息
    :param request:
    :return:
    """
    name = request.GET.get('name')
    q = QUEUE_DICT[name]

    result = {'status':True,"data":None}
    try:
        data = q.get(timeout=10)
        result['data'] = data
    except queue.Empty as e:
        result['status'] = False

    # return HttpResponse(json.dumps(result))
    return JsonResponse(result)





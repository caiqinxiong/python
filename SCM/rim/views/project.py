from django.shortcuts import render

# Create your views here.
import json
from django.shortcuts import render,redirect,HttpResponse,reverse
from django.http import JsonResponse
from rim import models
from rim.forms.task import TasktModelForm

def index(request):
    '''发布信息首页'''

    return render(request, 'index.html')


def project_list(request):
    '''项目信息'''
    project_info = models.Project.objects.all()

    return render(request, 'project_list.html', {'project_info':project_info})

def add_project(request):
    '''添加项目'''
    ret = {'status': True, 'msg': None}
    pname = request.POST.get('pname')
    kname = request.POST.get('kname')
    if pname and kname:
        models.Project.objects.create(pname=pname,kname=kname)
        return HttpResponse('ok')
    else:
        return HttpResponse('填写信息不能为空！')

def edit_project(request):
    '''编辑项目'''
    ret = {'status': True, 'message': None}
    try:
        pid = request.POST.get('pid')
        pname = request.POST.get('pname')
        kname = request.POST.get('kname')
        if pname and kname:
            obj = models.Project.objects.get(pid=pid)
            obj.pname = pname
            obj.kname = kname
            obj.save()
        else:
            ret['status'] = False
            ret['message'] = "编辑信息不能为空"
    except Exception as e:
        ret['status'] = False
        ret['message'] = "处理异常"

    return HttpResponse(json.dumps(ret))

def del_project(request,pk):
    '''删除项目'''
    models.Project.objects.filter(pid=pk).delete()
    return JsonResponse({"status": True})

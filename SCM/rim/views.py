from django.shortcuts import render

# Create your views here.
import json
from django.shortcuts import render,redirect,HttpResponse,reverse
from django.http import JsonResponse
from rim import models

def index(request):
    '''发布信息首页'''

    return render(request,'index.html')


def project_list(request):
    '''项目信息'''
    project_info = models.Project.objects.all()

    return render(request,'project_list.html',{'project_info':project_info})

def add_project(request):
    '''添加项目'''
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
        obj = models.Project.objects.get(pid=pid)
        obj.pname = pname
        obj.kname = kname
        obj.save()
    except Exception as e:
        ret['status'] = False
        ret['message'] = "处理异常"

    return HttpResponse(json.dumps(ret))

def del_project(request,pk):
    '''删除项目'''
    models.Project.objects.filter(pid=pk).delete()
    return JsonResponse({"status": True})

def task_list(request,project_id):
    # project_object = models.Project.objects.filter(pid=project_id).first()
    task_list = models.ReleaseInfo.objects.filter(project_id=project_id).all()
    return render(request,'task_list.html',{'task_list':task_list,"project_id":project_id})

def task_add(request,project_id):
    if request.method == 'POST':
        taskname = request.POST.get('taskname')
        svnversion = request.POST.get('svnversion')
        branch = request.POST.get('branch')
        versionname = request.POST.get('versionname')
        versioncode = request.POST.get('versioncode')
        build_cmd = request.POST.get('build_cmd')
        release_info = request.POST.get('release_info')
        issue = request.POST.get('issue')
        models.ReleaseInfo.objects.create(taskname=taskname,svnversion=svnversion,project_id=project_id,
                                          branch=branch,versioncode=versioncode,versionname=versionname,
                                          build_cmd=build_cmd,release_info=release_info,issue=issue)
        return redirect(reverse('task_list' ,kwargs={'project_id':project_id}))
    project_object = models.Project.objects.filter(pid=project_id).first()
    return render(request,'add_release_info.html',{'project_object':project_object})

def task_edit(request,project_id):
    release_object = models.ReleaseInfo.objects.filter(id=project_id).first()
    if request.method == 'POST':
        taskname = request.POST.get('taskname')
        svnversion = request.POST.get('svnversion')
        branch = request.POST.get('branch')
        versionname = request.POST.get('versionname')
        versioncode = request.POST.get('versioncode')
        build_cmd = request.POST.get('build_cmd')
        release_info = request.POST.get('release_info')
        issue = request.POST.get('issue')
        models.ReleaseInfo.objects.filter(id=project_id).update(taskname=taskname,svnversion=svnversion,
                                          branch=branch,versioncode=versioncode,versionname=versionname,
                                          build_cmd=build_cmd,release_info=release_info,issue=issue)
        return redirect(reverse('task_list' ,kwargs={'project_id':release_object.project_id}))
    relase_object = models.ReleaseInfo.objects.filter(id=project_id).first()
    return render(request,'edit_release_info.html',{'project_id':project_id,'relase_object':relase_object})

def task_del(request,project_id):
    '''删除发布信息'''
    release_obj = models.ReleaseInfo.objects.filter(id=project_id)
    project_id = release_obj.first().project_id
    release_obj.delete()
    return redirect(reverse('task_list' ,kwargs={'project_id':project_id}))


def release_info(request,project_id):
    '''发布信息'''
    release_object = models.ReleaseInfo.objects.filter(id=project_id).first()
    return render(request,'release_list.html',{'release_object':release_object})
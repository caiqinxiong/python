from django.shortcuts import HttpResponse,render,redirect
from django.http import JsonResponse
from web import models
from web.forms.task import TaskModelForm
from django.urls import reverse

def task_list(request,project_id):
    project_object = models.Project.objects.filter(id=project_id).first()
    task_list = models.DeployTask.objects.filter(project_id=project_id).all()
    return render(request,'task_list.html',{'task_list':task_list,"project_object":project_object})

def task_add(request,project_id):
    project_object = models.Project.objects.filter(id=project_id).first()

    if request.method == 'GET':
        form = TaskModelForm(project_object)
        return render(request,'task_form.html',{'form':form,'project_object':project_object})

    form = TaskModelForm(project_object,data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('task_list',kwargs={'project_id':project_id}))
    return render(request, 'task_form.html', {'form': form,'project_object':project_object})


def hook_template(request,tid):
    hook_template_object = models.HookTemplate.objects.filter(id=tid).first()
    return JsonResponse({'status':True,'content':hook_template_object.content})

def deploy(request,task_id):
    task_object = models.DeployTask.objects.filter(id=task_id).first()
    return render(request,'deploy.html',{'task_object':task_object})
from django.shortcuts import render

# Create your views here.
import json
from django.shortcuts import render,redirect,HttpResponse,reverse
from django.http import JsonResponse
from rim import models
from rim.forms.task import TasktModelForm
from utils.pager import PageInfo

def task_list(request,pk):
    '''发布信息列表'''
    search = request.POST.get('search')
    if search:
        release_obj = models.ReleaseInfo.objects.filter(taskname__contains=search).all()
        return render(request, 'task_list.html',{'task_list':release_obj, "project_id":pk})
    else:
        release_obj = models.ReleaseInfo.objects.filter(project_id=pk).all()
        all_count = release_obj.count() # 获取所有数据行数
        page_info = PageInfo(request.GET.get('page'), all_count, per_page=20, base_url='/rim/task/list/%s' % pk, show_page=11) # 添加分页展示功能
        task_list = release_obj.order_by('-id')[page_info.start():page_info.end()] # 将查找到的数据按id反向排序，只展示某个区间的数据
        return render(request, 'task_list.html', {'task_list':task_list, "project_id":pk, 'page_info':page_info})

def task_add(request,pk):
    '''添加发布信息'''
    if request.method == 'GET':
        form = TasktModelForm(initial={'project': pk})
        return render(request, 'form.html', {'form': form})
    # 接收用户提交的数据并进行表单验证
    form = TasktModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('task_list' ,kwargs={'pk':pk}))
    else:
        return render(request, 'form.html', {'form':form})

def task_edit(request,pk):
    '''编辑发布信息'''
    project_obj = models.ReleaseInfo.objects.filter(id=pk).first()
    if request.method == 'GET':
        form = TasktModelForm(instance=project_obj)
        return render(request, 'form.html', {'form': form})
    # 接收用户提交的数据并进行表单验证
    form = TasktModelForm(data=request.POST,instance=project_obj)
    if form.is_valid():
        form.save()
        return redirect(reverse('task_list', kwargs={'pk': project_obj.project_id}))
    else:
        return render(request, 'form.html', {'form': form})

def task_del(request,pk):
    '''删除发布信息'''
    release_obj = models.ReleaseInfo.objects.filter(id=pk)
    # project_id = release_obj.first().project_id
    release_obj.delete()
    return JsonResponse({"status": True})
    # return redirect(reverse('task_list' ,kwargs={'project_id':project_id}))

def release_info(request,pk):
    '''发布信息'''
    release_object = models.ReleaseInfo.objects.filter(id=pk).first()
    return render(request, 'release_list.html', {'release_object':release_object})


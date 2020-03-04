from django.shortcuts import render

# Create your views here.
import json
from django.shortcuts import render,redirect,HttpResponse,reverse
from django.http import JsonResponse
from rim import models
from rim.forms.group import GroupModelForm


def group_list(request):
    '''组信息'''
    search = request.POST.get('search')
    if search:
        group_info = models.Group.objects.filter(pname__contains=search).all()
    else:
        group_info = models.Group.objects.all()
    return render(request, 'group_list.html', {'group_info':group_info})

def add_group_ajax(request):
    '''添加组'''
    ret = {'status': True, 'message': None}
    try:
        gname = request.POST.get('gname')
        if gname:
            models.Group.objects.create(gname=gname)
            print('ok')
        else:
            ret['status'] = False
            ret['message']='填写信息不能为空！'
    except Exception as e:
        ret['status'] = False
        ret['message'] = "处理异常"
    return HttpResponse(json.dumps(ret))

def add_group(request):
    '''添加组'''
    if request.method == 'GET':
        form = GroupModelForm()
        return render(request, 'form.html', {'form': form})
    # 接收用户提交的数据并进行表单验证
    form = GroupModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('group_list')
    else:
        return render(request,'form.html',{'form':form})



def edit_group_ajax(request):
    '''编辑组'''
    ret = {'status': True, 'message': None}
    try:
        id = request.POST.get('id')
        gname = request.POST.get('gname')
        if gname:
            obj = models.Group.objects.get(id=id)
            obj.gname = gname
            obj.save()
        else:
            ret['status'] = False
            ret['message'] = "编辑信息不能为空!!"
    except Exception as e:
        ret['status'] = False
        ret['message'] = "用户组已存在！"

    return HttpResponse(json.dumps(ret))

def edit_group(request,pk):
    '''编辑组'''
    group_obj = models.Group.objects.filter(id=pk).first()
    if request.method == 'GET':
        form = GroupModelForm(instance=group_obj)
        return render(request, 'form.html', {'form': form})
    form = GroupModelForm(data=request.POST,instance=group_obj)
    if form.is_valid():
        form.save()
        return redirect('group_list')
    else:
        return render(request, 'form.html', {'form': form})

def del_group(request,pk):
    '''删除组'''
    models.Group.objects.filter(id=pk).delete()
    return JsonResponse({"status": True})

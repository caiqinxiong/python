from django.shortcuts import render,HttpResponse
from web.forms.file import FolderModelForm,FileModelForm
from django.http import JsonResponse
from web import models
from utils.tencent.cos import delete_file,delete_file_list, credential
from django.forms import model_to_dict
from django.views.decorators.csrf import csrf_exempt
import json
from django.urls import reverse
import requests


def file(request,project_id):
    parent_object = None
    folder_id = request.GET.get('folder', '')
    if folder_id.isdecimal():
        parent_object = models.FileRepository.objects.filter(id=int(folder_id), file_type=2,
                                                             project=request.tracer.project).first()

    if request.method == 'GET':

        breadcrumb_list = []
        parent = parent_object
        while parent:
            breadcrumb_list.insert(0,model_to_dict(parent,['id','name']))
            parent = parent.parent

        queryset = models.FileRepository.objects.filter(project=request.tracer.project)
        if parent_object:
            file_object_list = queryset.filter(parent=parent_object).order_by('-file_type')
        else:
            file_object_list = queryset.filter(parent__isnull=True).order_by('-file_type')
        form = FolderModelForm(request, parent_object)
        context = {
            'form': form,
            'file_object_list': file_object_list,
            'breadcrumb_list': breadcrumb_list,
            'folder_object': parent_object,
        }
        return render(request,'file.html',context)

    fid = request.POST.get('fid','')
    edit_object = None
    if fid.isdecimal():
        edit_object = models.FileRepository.objects.filter(id=int(fid),file_type=2,project=request.tracer.project).first()
    if edit_object:
        form = FolderModelForm(request,parent_object,data=request.POST,instance=edit_object)
    else:
        form = FolderModelForm(request,parent_object,data=request.POST)
    # form = FolderModelForm(request, parent_object, data=request.POST)
    if form.is_valid():
        form.instance.project = request.tracer.project
        form.instance.file_type = 2
        form.instance.update_user = request.tracer.user
        form.instance.parent = parent_object
        form.save()
        return JsonResponse({'status':True, })
    return JsonResponse({'status':False, 'error':form.errors})


def file_delete(request,project_id):
    fid = request.GET.get('fid')
    delete_object = models.FileRepository.objects.filter(id=fid,project=request.tracer.project).first()
    if delete_object.file_type == 1:
        #删除文件   database  cos  free space
        request.tracer.project.use_space -= delete_object.file_size
        request.tracer.project.save()
        #cos中删除文件
        delete_file(request.tracer.project.bucket,request.tracer.project.region,delete_object.key)
        delete_object.delete()
        return JsonResponse({'status': True})

    total_size = 0
    folder_list = [delete_object,]
    key_list = []
    for folder in folder_list:
        child_list = models.FileRepository.objects.filter(project=request.tracer.project,parent=folder).order_by('-file_type')
        for child in child_list:
            if child.file_type == 2:
                folder_list.append(child_list)
            else:
                total_size += child.file_size

                key_list.append({"Key": child.key})

    if key_list:
        delete_file_list(request.tracer.project.bucket, request.tracer.project.region,key_list)
    if total_size:
        request.tracer.project.use_space -= delete_object.file_size
        request.tracer.project.save()

    delete_object.delete()
    return JsonResponse({'status': True})


@csrf_exempt
def cos_credential(request,project_id):

    per_file_limit = request.tracer.price_policy.each_file_size * 1024 * 1024
    total_file_limit = request.tracer.price_policy.project_space * 1024 * 1024 * 1024

    total_size = 0
    file_list = json.loads(request.body.decode('utf-8'))

    for item in file_list:
        if item['size'] > per_file_limit:
            msg = "单文件超出限制(最大{}M), 文件: {}".format(request.tracer.price_policy.each_file_size,item['name'])
            return JsonResponse({'status':False, 'error': msg})
        total_size += item['size']

    #和总容量进行比较
    if request.tracer.project.use_space + total_size > total_file_limit:
        return JsonResponse({'status': False, 'error':"容量超过限制,请升级套餐"})

    data_dict = credential(request.tracer.project.bucket, request.tracer.project.region)
    return JsonResponse({'status':True, 'data':data_dict})


@csrf_exempt
def file_post(request, project_id):
    #将上传成功的数据写入数据库
    #根据ETag校验
    """
    name: fileName,
    key:key,
    size: fileSize,
    parent: CURRENT_FOLDER_ID,
    etag: data.ETag,
    file_path: data.Location,
    :param request:
    :param project_id:
    :return:
    """
    # print(request.POST)
    form = FileModelForm(request,data=request.POST)
    if form.is_valid():
        data_dict = form.cleaned_data
        data_dict.pop('etag')
        data_dict.update({'project': request.tracer.project, 'file_type':1, 'update_user': request.tracer.user})
        instance = models.FileRepository.objects.create(**data_dict)
        #项目使用空间更新
        request.tracer.project.use_space += data_dict['file_size']
        request.tracer.project.save()

        result = {
            'id': instance.id,
            'name' : instance.name,
            'file_size': instance.file_size,
            # 'file_type' : instance.get_file_type_display(),
            'username': instance.update_user.username,
            'datetime': instance.update_datetime,
            'download_url': reverse('file_download', kwargs={"project_id": project_id, 'file_id': instance.id})
        }
        return JsonResponse({'status': True, 'data':result})

        # form.instance.file_type = 1
        # form.update_user = request.tracer.user
        # instance = form.save() #添加成功之后,获取到新添加的对象

    return JsonResponse({'status': True, 'data':'文件错误'})

def file_download(request,project_id,file_id):
    # COS 获取内容 网络文件获取
    file_object = models.FileRepository.objects.filter(id=file_id,project_id=project_id).first()
    res = requests.get(file_object.file_path)
    data = res.content
    response = HttpResponse(data)
    #设置响应头
    response['Content-Disposition'] = f"attachment; filename={file_object.name}"
    return response














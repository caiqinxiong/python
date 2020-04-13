from django.shortcuts import render,redirect,HttpResponse
from web.forms.project import ProjectModelForm
from django.http import JsonResponse
from web import models
from utils.tencent.cos import create_bucket
import time

def project_list(request):
    if request.method == 'GET':
        form = ProjectModelForm(request)
        #myproject
        # my_project_objs = models.Project.objects.filter(creator=request.tracer.user)
        #
        # my_star_objs = models.ProjectUser.objects.filter(user=request.tracer.user,star=True)
        #
        # all_occupy = models.ProjectUser.objects.filter(user=request.tracer.user)

        project_dict = {'star': [],'my':[],'join':[]}
        my_project_list = models.Project.objects.filter(creator=request.tracer.user)
        for row in my_project_list:
            if row.star:
                project_dict['star'].append({"value": row, 'type': 'my'})
            else:
                project_dict['my'].append(row)
        join_project_list = models.ProjectUser.objects.filter(user=request.tracer.user)
        for item in join_project_list:
            if item.star:
                project_dict['star'].append({"value":item.project,'type':'join'})
            else:
                project_dict['join'].append(item.project)
        return render(request, 'project_list.html',{'form':form,'project_dict':project_dict})
    form = ProjectModelForm(request,data=request.POST)
    if form.is_valid():
        #"手机号+时间戳+1301483313"
        bucket = "{}-{}-1301483313".format(request.tracer.user.mobile_phone,str(int(time.time())))
        region = 'ap-chengdu'
        create_bucket(bucket,region)
        form.instance.bucket = bucket
        form.instance.region = region
        form.instance.creator = request.tracer.user
        instance = form.save()

        #项目初始化问题类型
        issues_type_object_list = []
        for item in models.IssuesType.PROJECT_INIT_LIST:
            issues_type_object_list.append(models.IssuesType(project=instance,title=item))
        models.IssuesType.objects.bulk_create(issues_type_object_list)
        return JsonResponse({'status':True})

    return JsonResponse({'status':False, 'error':form.errors})


def project_star(request,project_type,project_id):
    if project_type == 'my':
        models.Project.objects.filter(id=project_id, creator=request.tracer.user).update(star=True)
        return redirect('project_list')
    if project_type == 'join':
        models.ProjectUser.objects.filter(project_id=project_id,user=request.tracer.user).update(star=True)
        return redirect('project_list')
    return HttpResponse('请求错误')


def project_unstar(request,project_type,project_id):
    if project_type == 'my':
        models.Project.objects.filter(id=project_id, creator=request.tracer.user).update(star=False)
        return redirect('project_list')
    if project_type == 'join':
        models.ProjectUser.objects.filter(project_id=project_id,user=request.tracer.user).update(star=False)
        return redirect('project_list')
    return HttpResponse('请求错误')



def test(request):
    return render(request,'layout/manage.html')
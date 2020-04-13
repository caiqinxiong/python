from django.shortcuts import render
from django.db.models import Count
from web import models
import collections
import datetime
from django.http import JsonResponse
import time

def dashboard(request,project_id):

    #数据处理
    status_dict = collections.OrderedDict()
    for key,text in models.Issues.status_choices:
        status_dict[key] = {'text':text,'count':0}
    issues_data = models.Issues.objects.filter(project_id=project_id).values('status').annotate(ct=Count('id'))
    for item in issues_data:
        status_dict[item['status']]['count'] = item['ct']

    #项目成员
    user_list = models.ProjectUser.objects.filter(project_id=project_id).values('user_id','user__username')
    # 显示最近前10个动态(指派不为空)
    top_ten = models.Issues.objects.filter(project_id=project_id, assign__isnull=False).order_by('-id')[0:10]
    context = {
        'status_dict': status_dict,
        'user_list': user_list,
        'top_ten_object': top_ten,
    }

    return render(request,'dashboard.html',context)


def issues_chart(request, project_id):

    today = datetime.datetime.now().date()
    date_dict = collections.OrderedDict()
    for i in range(0, 30):
        date = today - datetime.timedelta(days=i)
        date_dict[date.strftime("%Y-%m-%d")] = [time.mktime(date.timetuple()) * 1000, 0]

    result = models.Issues.objects.filter(project_id=project_id,
                                          create_datetime__gte=today - datetime.timedelta(days=30)).extra(
        select={'ctime': "strftime('%%Y-%%m-%%d',web_issues.create_datetime)"}).values('ctime').annotate(ct=Count('id'))
    """
    {
        2020-03-21:[111,0],
        2020-03-22:[222,0],
        ......
    }
    """

    for item in result:
        date_dict[item['ctime']][1] = item['ct']

    return JsonResponse({'status': True, 'data': list(date_dict.values())})
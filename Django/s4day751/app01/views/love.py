from django.shortcuts import render,HttpResponse,redirect
from app01 import models

def index(request):
    if not request.session.get('user_info'):
        return redirect('/login.html')
    else:

        # 男：女生列表
        # 女：男生
        gender = request.session.get('user_info').get('gender')
        if gender == '1':
            user_list = models.Girl.objects.all()
        else:
            user_list = models.Boy.objects.all()
        return render(request,'index.html',{'user_list':user_list})

def others(request):
    """
    获取与当前用户有关系的异性
    :param request:
    :return:
    """
    current_user_id = request.session.get('user_info').get('user_id')
    gender = request.session.get('user_info').get('gender')
    if gender == '1':
        user_list = models.B2G.objects.filter(b_id=current_user_id).values('g__nickname')
    else:
        user_list = models.B2G.objects.filter(g_id=current_user_id).values('b__nickname')
    return render(request,'others.html',{'user_list':user_list})








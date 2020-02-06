from django.shortcuts import render,HttpResponse,redirect
from app01 import models
def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        user = request.POST.get('username')
        pwd = request.POST.get('password')
        gender = request.POST.get('gender')
        rmb = request.POST.get('rmb')
        # 性别判断
        if gender == "1":
            obj = models.Boy.objects.filter(username=user,password=pwd).first()
        else:
            obj = models.Girl.objects.filter(username=user,password=pwd).first()
        if not obj:
            # 未登录
            return render(request,'login.html',{'msg': '用户名或密码错误'})
        else:
            # request.session['user_id'] = obj.id
            # request.session['gender'] = gender
            # request.session['username'] = user
            request.session['user_info'] = {'user_id':obj.id,'gender':gender,'username':user,'nickname':obj.nickname}
            return redirect('/index.html')

def logout(request):
    if request.session.get('user_info'):
        request.session.clear()
        # request.session.delete(request.session.session_key)
    return redirect('/login.html')

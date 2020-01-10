from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.db import connection
from web import models

def msyql_connnec(sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    return result
def server_list(request):
    # queryset = models.Server.objects.all()
    sql = 'select * from web_server'
    reslut=msyql_connnec(sql)
    return render(request,'server_list.html',{'result':reslut})

# 为了做表单验证,引入ModelForm的功能
# 1. 自动生成HTML标签
# 2. 表单验证
# from django.forms import ModelForm
#
# class ServerModelForm(ModelForm):
#
#     exclude_bootstrap = []
#
#     class Meta:
#         model = models.Server
#         fields = "__all__"
#
#     def __init__(self,*args,**kwargs):
#         # 执行父类的 __init__
#         super().__init__(*args,**kwargs)
#
#         # 自定义功能,为字段添加bootstrap样式
#         for k,field in self.fields.items():
#             if k in self.exclude_bootstrap:
#                 continue
#             field.widget.attrs['class'] = 'form-control'

def server_add(request):
    if request.method == 'GET':
        # form = ServerModelForm()
        # return render(request, 'form.html', {'form': form})
        return render(request, 'form1.html')
    # 接收用户提交的数据并进行表单验证
    # form = ServerModelForm(data=request.POST)
    # if form.is_valid():
        # 验证通过: 保存到数据库
        # form.save()
        # 跳转到服务器列表页面: /server/list/
    if request.method == 'POST':
        hostname=request.POST.get('hostname')

        if hostname:
            sql = "insert into web_server(hostname) values ('{}')".format(hostname)
            msyql_connnec(sql)
            return redirect('server_list')
        else:
            return render(request,'form1.html')

def server_edit(request,pk):
    # server_object = models.Server.objects.filter(id=pk).first()
    sql = "select * from web_server where id={}".format(pk)
    result=msyql_connnec(sql)
    # print(result)
    if request.method == 'GET':
        # form = ServerModelForm(instance=server_object)
        return render(request, 'form1.html', {'result': result})
    if request.method == 'POST':
        hostname=request.POST.get('hostname')

        if hostname:
            sql = "update web_server set hostname='{}' where id={}".format(hostname,pk)
            msyql_connnec(sql)
            return redirect('server_list')
        else:
            return render(request, 'form1.html')
    # form = ServerModelForm(data=request.POST,instance=server_object)
    # if form.is_valid():
    #     form.save()
    #     return redirect('server_list')
    # else:
    #     return render(request, 'form.html', {'form': form})

def server_del(request,pk):
    # models.Server.objects.filter(id=pk).delete()
    sql = "delete from web_server where id={}".format(pk)
    msyql_connnec(sql)
    return JsonResponse({"status":True})
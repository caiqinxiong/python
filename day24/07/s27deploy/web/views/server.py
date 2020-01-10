from django.shortcuts import render,redirect
from django.http import JsonResponse
from web import models
from web.forms.server import ServerModelForm

def server_list(request):
    queryset = models.Server.objects.all()
    return render(request,'server_list.html',{'queryset':queryset})

def server_add(request):
    if request.method == 'GET':
        form = ServerModelForm()
        return render(request, 'form.html', {'form': form})
    # 接收用户提交的数据并进行表单验证
    form = ServerModelForm(data=request.POST)
    if form.is_valid():
        # 验证通过: 保存到数据库
        form.save()
        # 跳转到服务器列表页面: /server/list/
        return redirect('server_list')
    else:
        return render(request,'form.html',{'form':form})

def server_edit(request,pk):
    server_object = models.Server.objects.filter(id=pk).first()
    if request.method == 'GET':
        form = ServerModelForm(instance=server_object)
        return render(request, 'form.html', {'form': form})

    form = ServerModelForm(data=request.POST,instance=server_object)
    if form.is_valid():
        form.save()
        return redirect('server_list')
    else:
        return render(request, 'form.html', {'form': form})

def server_del(request,pk):
    models.Server.objects.filter(id=pk).delete()
    return JsonResponse({"status":True})
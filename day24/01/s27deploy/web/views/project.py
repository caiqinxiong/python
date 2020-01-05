from django.shortcuts import render,redirect
from django.http import JsonResponse
from web import models
def project_list(request):
    queryset = models.Project.objects.all()
    return render(request,'project_list.html',{'queryset':queryset})

# 为了做表单验证,引入ModelForm的功能
# 1. 自动生成HTML标签
# 2. 表单验证
from django.forms import ModelForm

class ProjectModelForm(ModelForm):

    exclude_bootstrap = []

    class Meta:
        model = models.Project
        fields = "__all__"

    def __init__(self,*args,**kwargs):
        # 执行父类的 __init__
        super().__init__(*args,**kwargs)

        # 自定义功能,为字段添加bootstrap样式
        for k,field in self.fields.items():
            if k in self.exclude_bootstrap:
                continue
            field.widget.attrs['class'] = 'form-control'

def project_add(request):
    if request.method == 'GET':
        form = ProjectModelForm()
        return render(request, 'project_form.html', {'form': form})
    # 接收用户提交的数据并进行表单验证
    form = ProjectModelForm(data=request.POST)
    if form.is_valid():
        # 验证通过: 保存到数据库
        form.save()
        # 跳转到服务器列表页面: /server/list/
        return redirect('project_list')
    else:
        return render(request,'project_form.html',{'form':form})

def project_edit(request,pk):
    server_object = models.Project.objects.filter(id=pk).first()
    if request.method == 'GET':
        form = ProjectModelForm(instance=server_object)
        return render(request, 'project_form.html', {'form': form})

    form = ProjectModelForm(data=request.POST,instance=server_object)
    if form.is_valid():
        form.save()
        return redirect('project_list')
    else:
        return render(request, 'project_form.html', {'form': form})

def project_del(request,pk):
    models.Project.objects.filter(id=pk).delete()
    return JsonResponse({"status":True})
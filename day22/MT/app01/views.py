from django.shortcuts import render, redirect, HttpResponse
from app01 import models
# Create your views here.


def index(request):
    """   """
    obj = models.Project.objects.all()
    return render(request, 'index.html', {"project_obj": obj})






from django.forms import ModelForm
from django.forms import widgets as wid
class ProjectModelForm(ModelForm):
    class Meta:
        model = models.Project
        fields = "__all__"
        labels = {
            "project_name": "项目名称",
            "project_desc": "项目描述",
        }
        error_messages = {
            "project_name": {"required": "不能为空"},
            "project_desc": {"required": "不能为空"}
        }
        widgets = {
            "project_name": wid.TextInput(attrs={"class": "form-control"}),
            "project_desc": wid.Textarea(attrs={"class": "form-control"})
        }

def add_project(request):
    """  添加项目记录 """
    if request.method == "POST":
        form_obj = ProjectModelForm(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            return redirect('/index/')
        else:
            return render(request, 'add_project.html', {"form": form_obj})
    else:
        form_obj = ProjectModelForm()
        return render(request, 'add_project.html', {"form": form_obj})

def edit_project(request, pk):
    """ 修改项目 """
    project_obj = models.Project.objects.filter(pk=pk).first()
    if request.method == 'POST':
        form_obj = ProjectModelForm(request.POST,instance=project_obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect('/index/')
        else:
            return render(request, 'edit_project.html', {"form": form_obj})
    else:
        form_obj = ProjectModelForm(instance=project_obj)
        return render(request, 'edit_project.html', {"form": form_obj})



# --------------------- 用例相关,以下 ---------------------

class CaseModelForm(ModelForm):
    class Meta:
        model = models.Case
        # fields = "__all__"
        exclude = ['case_execute_status']  # 排除字段
        labels = {
            "case_project": "所属项目",
            "case_name": "用例名称",
            "case_desc": "用例描述",
            "case_expect": "用例期望值",
            "case_url": "请求URL",
            "case_method": "请求类型",
            "case_params": "请求参数",

        }
        error_messages = {
            "case_project": {"required": "不能为空"},
            "case_name": {"required": "不能为空"},
            "case_desc": {"required": "不能为空"},
            "case_expect": {"required": "不能为空"},
            "case_url": {"required": "不能为空"},
            "case_method": {"required": "不能为空"},
            "case_params": {"required": "不能为空"},
        }
        widgets = {
            "case_project": wid.Select(attrs={"class": "form-control"}),
            "case_name": wid.TextInput(attrs={"class": "form-control"}),
            "case_desc": wid.Textarea(attrs={"class": "form-control"}),
            "case_expect": wid.TextInput(attrs={"class": "form-control"}),
            "case_url": wid.TextInput(attrs={"class": "form-control"}),
            "case_method": wid.TextInput(attrs={"class": "form-control"}),
            "case_params": wid.TextInput(attrs={"class": "form-control"}),

        }
def case_list(request,pk):
    """  项目下的用例列表,pk是用例所属项目的pk """
    # 找到指定项目下的所有用例
    case_list_obj = models.Case.objects.filter(case_project_id=pk)
    print(case_list_obj)
    return render(request, 'case_list.html', {"case_list_obj": case_list_obj})


def add_case(request, pk):
    """ 添加用例, 所属项目的pk """
    if request.method == 'POST':
        form_obj = CaseModelForm(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            return redirect('/case_list/{}'.format(pk))
        else:
            return render(request, 'add_case.html', {"form": form_obj})
    else:
        form_obj = CaseModelForm()
        return render(request, 'add_case.html', {"form": form_obj})

def edit_case(request, pk):
    """ 修改用例, pk是用例的pk"""
    case_obj = models.Case.objects.filter(pk=pk).first()
    if request.method == "POST":
        form_obj = CaseModelForm(request.POST, instance=case_obj)
        if form_obj.is_valid():
            form_obj.save()
            # 查找用例所属项目的pk
            obj = models.Project.objects.filter(case__id=pk).first()
            return redirect('/case_list/{}'.format(obj.pk))
        else:
            return render(request, 'edit_case.html', {"form": form_obj})
    else:  # get请求
        form_obj = CaseModelForm(instance=case_obj)
        return render(request, 'edit_case.html', {"form": form_obj})


import xlrd
from django.db import transaction
def add_case_all(request, pk):
    """ 批量从excel表中添加用例
     1. 返回一个上传文件的页面
     2. 点击上传文件,
     3. 后台获取到上传的文件
     4. 校验
     5. 循环写入到数据库
     """
    if request.method == "POST":
        # 获取普通的post请求的input数据
        # print(request.POST.get('a2'))
        try:
            if transaction.atomic():   # 事务
                # 获取form表单上传的文件
                file_name = request.FILES.get('a1')
                # if file_name.split('.')[-1] in ['xls', 'xlsx']:   # 或者判断后缀名
                book = xlrd.open_workbook(file_contents=file_name.read())
                sheet = book.sheet_by_index(0)
                # print(sheet.nrows)
                for row  in range(1, sheet.nrows):
                    print(sheet.row_values(row))
                    models.Case.objects.create(
                        case_project_id=pk,
                        case_name="用例名称",
                        case_desc=sheet.row_values(row)[0],
                        case_url=sheet.row_values(row)[1],
                        case_method=sheet.row_values(row)[2],
                        case_params=sheet.row_values(row)[3],
                        case_expect=sheet.row_values(row)[4],
                    )
                return redirect('/case_list/{}'.format(pk))
        except Exception as e:
            print(e)
            return render(request, 'add_case_all.html', {"error": "只能上传 xls 或 xlsx 类型的excel表"})
    else:
        return render(request, 'add_case_all.html', {"error": ""})


from util.case import run
from django.http import FileResponse
def execute(request):
    """ 执行用例 """
    if request.method == "POST":
        pk_list = request.POST.getlist("pk_list")  # ['5', '6']
        if pk_list:
            case_list = models.Case.objects.filter(pk__in=pk_list)
            file_path = run(case_list)
            print(11111, file_path)
            # print(pk_list, case_list)
            # 将HTML文件发送给前端,下载

            file = open(file_path, 'rb')
            response = FileResponse(file)
            response['Content-Type'] = 'application/octet-stream'
            response['Content-Disposition'] = 'attachment;filename="report.html"'
            return response
        else:
            pass
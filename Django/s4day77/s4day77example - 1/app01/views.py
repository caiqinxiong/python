from django.shortcuts import render,redirect
from app01 import models
from django.forms import Form
from django.forms import fields
from django.forms import widgets



class ClassForm(Form):
    title = fields.RegexField('全栈\d+')

def class_list(request):
    cls_list = models.Classes.objects.all()
    return render(request,'class_list.html',{'cls_list':cls_list})

def add_class(request):
    if request.method == "GET":
        obj = ClassForm()
        return render(request,'add_class.html',{'obj': obj})
    else:
        obj = ClassForm(request.POST)
        if obj.is_valid():
            # obj.cleaned_data # 字典
            # 数据库创建一条数据
            # print(obj.cleaned_data)
            # models.Classes.objects.create(title=obj.cleaned_data['tt'])

            models.Classes.objects.create(**obj.cleaned_data)
            return redirect('/class_list/')
        return render(request,'add_class.html',{'obj': obj})

def edit_class(request,nid):
    if request.method == "GET":
        row = models.Classes.objects.filter(id=nid).first()
        # 让页面显示初始值
        # obj = ClassForm(data={'title': 'asdfasdfasdfas'})
        obj = ClassForm(initial={'title': row.title})
        return render(request,'edit_class.html',{'nid': nid,'obj':obj})
    else:
        obj = ClassForm(request.POST)
        if obj.is_valid():
            models.Classes.objects.filter(id=nid).update(**obj.cleaned_data)
            return redirect('/class_list/')
        return render(request,'edit_class.html',{'nid': nid,'obj':obj})



class StudentForm(Form):
    name = fields.CharField(
        min_length=2,
        max_length=6,
        widget=widgets.TextInput(attrs={'class': 'form-control'})
    )
    email = fields.EmailField(widget=widgets.TextInput(attrs={'class': 'form-control'}))
    age = fields.IntegerField(min_value=18,max_value=25,widget=widgets.TextInput(attrs={'class': 'form-control'}))
    cls_id = fields.IntegerField(
        # widget=widgets.Select(choices=[(1,'上海'),(2,'北京')])
        widget=widgets.Select(choices=models.Classes.objects.values_list('id','title'),attrs={'class': 'form-control'})
    )


def student_list(request):

    stu_list = models.Student.objects.all()
    return render(request,'student_list.html',{'stu_list':stu_list})

def add_student(request):
    if request.method == "GET":
        obj = StudentForm()
        return render(request,'add_student.html',{'obj':obj})
    else:
        obj = StudentForm(request.POST)
        if obj.is_valid():
            models.Student.objects.create(**obj.cleaned_data)
            return redirect('/student_list/')
        return render(request,'add_student.html',{'obj':obj})



def edit_student(request,nid):
    if request.method == "GET":
        row = models.Student.objects.filter(id=nid).values('name','email','age','cls_id').first()
        obj = StudentForm(initial=row)
        return render(request,'edit_student.html',{'nid':nid,'obj': obj})
    else:
        obj = StudentForm(request.POST)
        if obj.is_valid():
            models.Student.objects.filter(id=nid).update(**obj.cleaned_data)
            return redirect('/student_list/')
        return render(request,'edit_student.html',{'nid':nid,'obj': obj})










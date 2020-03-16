from django.shortcuts import render, redirect, reverse, HttpResponse
from crm import models
from crm.froms import CustomerForm


# 展示客户列表
def customer_list(request):

    if request.path_info == reverse('customer_list'):

        all_customer = models.Customer.objects.filter(consultant__isnull=True)
    else:
        all_customer = models.Customer.objects.filter(consultant=request.user_obj)


    return render(request, 'customer_list.html', {'all_customer': all_customer})


# 添加客户
def customer_add(request):
    # 不包含数据的form
    form_obj = CustomerForm()

    if request.method == 'POST':
        # 包含用户提交数据的form
        form_obj = CustomerForm(request.POST)
        # 对数据进行校验
        if form_obj.is_valid():
            form_obj.save()  # 创建对象
            # 跳转到展示页面
            return redirect(reverse('customer_list'))

    return render(request, 'customer_add.html', {'form_obj': form_obj})


# 编辑客户
def customer_edit(request, edit_id):
    obj = models.Customer.objects.filter(pk=edit_id).first()

    # 处理POST
    if request.method == 'POST':
        # 包含提交的数据 原始数据
        form_obj = CustomerForm(request.POST, instance=obj)
        if form_obj.is_valid():
            form_obj.save()  # 保存修改
            # 跳转到展示页面
            return redirect(reverse('customer_list'))
    else:
        # 包含原始数据的form表单
        form_obj = CustomerForm(instance=obj)

    return render(request, 'customer_edit.html', {'form_obj': form_obj})

from django.template.response import TemplateResponse


def customer_change(request, edit_id=None):
    obj = models.Customer.objects.filter(pk=edit_id).first()

    # 处理POST
    if request.method == 'POST':
        # 包含提交的数据 原始数据
        form_obj = CustomerForm(request.POST, instance=obj)
        if form_obj.is_valid():
            form_obj.save()
            # 跳转到展示页面
            return redirect(reverse('customer_list'))
    else:
        form_obj = CustomerForm(instance=obj)

    title = '编辑客户' if edit_id else '添加客户'

    obj = HttpResponse('xxx')


    return render(request, 'customer_change.html', {'title': title, 'form_obj': form_obj})


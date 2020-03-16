from django.shortcuts import render, redirect, reverse, HttpResponse
from crm import models
from crm.froms import CustomerForm
from utils.pagination import Pagination


# 展示客户列表
def customer_list(request):
    if request.path_info == reverse('customer_list'):

        all_customer = models.Customer.objects.filter(consultant__isnull=True)
    else:
        all_customer = models.Customer.objects.filter(consultant=request.user_obj)

    page = Pagination(request.GET.get('page', 1), all_customer.count(), )

    return render(request, 'customer_list.html', {
        'all_customer': all_customer[page.start:page.end],
        'page_html': page.page_html
    })


# 展示客户列表 CBV
from django.views import View


class CustomerList(View):

    def get(self, request, *args, **kwargs):
        if request.path_info == reverse('customer_list'):

            all_customer = models.Customer.objects.filter(consultant__isnull=True)
        else:
            all_customer = models.Customer.objects.filter(consultant=request.user_obj)

        page = Pagination(request.GET.get('page', 1), all_customer.count(), )

        return render(request, 'customer_list.html', {
            'all_customer': all_customer[page.start:page.end],
            'page_html': page.page_html
        })

    def post(self, request, *args, **kwargs):

        action = request.POST.get('action')  # multi_apply  multi_pub

        # 判断是否有相应的操作
        if hasattr(self, action):
            # 有 获取并且执行
            func = getattr(self, action)
            print(func)
            func()
        else:
            return HttpResponse('非法操作')

        return self.get(request, *args, **kwargs)

    def multi_apply(self, ):
        ids = self.request.POST.getlist('ids')
        # 把提交的客户的ID 都变成当前用户的私户

        # 方式一  查询的客户
        # models.Customer.objects.filter(pk__in=ids).update(consultant=self.request.user_obj)
        # models.Customer.objects.filter(pk__in=ids).update(consultant_id=self.request.session.get('pk'))

        # 方式二 查用户
        self.request.user_obj.customers.add(*models.Customer.objects.filter(pk__in=ids))

    def multi_pub(self):
        ids = self.request.POST.getlist('ids')
        # 把提交的客户的ID

        # 方式一  查询的客户
        models.Customer.objects.filter(pk__in=ids).update(consultant=None)

        # 方式二 查用户
        # self.request.user_obj.customers.remove(*models.Customer.objects.filter(pk__in=ids))


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

from django.shortcuts import render, redirect, reverse, HttpResponse
from crm import models
from crm.froms import ConsultForm
from utils.pagination import Pagination
from django.views import View
from django.db.models import Q


class ConsultList(View):

    def get(self, request, *args, **kwargs):

        q = self.search([])

        customer_id = kwargs.get('customer_id')

        if customer_id:
            # 某个客户的所有跟进
            all_consult = models.ConsultRecord.objects.filter(q,customer_id=customer_id,consultant=request.user_obj, delete_status=False).order_by('-date')
        else:
            # 当前销售的所有客户的跟进
            all_consult = models.ConsultRecord.objects.filter(q, consultant=request.user_obj, delete_status=False).order_by('-date')

        page = Pagination(request.GET.get('page', 1), all_consult.count(), request.GET.copy(), 2)

        return render(request, 'consult_list.html', {
            'all_consult': all_consult[page.start:page.end],
            'page_html': page.page_html
        })

    def post(self, request, *args, **kwargs):

        action = request.POST.get('action')  # multi_apply  multi_pub

        # 判断是否有相应的操作
        if hasattr(self, action):
            # 有 获取并且执行
            func = getattr(self, action)
            func()
        else:
            return HttpResponse('非法操作')

        return self.get(request, *args, **kwargs)

    def search(self, field_list):
        query = self.request.GET.get('query', '')

        # Q(Q(qq__contains=query) | Q(name__contains=query)),
        q = Q()
        q.connector = 'OR'
        # q.children.append(Q(qq__contains=query))
        # q.children.append(Q(name__contains=query))

        for field in field_list:
            # q.children.append(Q(qq__contains=query))

            if field == 'sex':
                if query == '男':
                    sex = 'male'
                elif query == '女':
                    sex = 'female'
                else:
                    sex = ''
                q.children.append(Q(sex=sex))

            q.children.append(Q(('{}__contains'.format(field), query)))

        return q


# 添加跟进
def consult_add(request):
    obj = models.ConsultRecord(consultant=request.user_obj)
    # obj.save()   # 新增
    form_obj = ConsultForm(instance=obj)

    if request.method == 'POST':
        form_obj = ConsultForm(request.POST, instance=obj)
        if form_obj.is_valid():
            form_obj.save()
            next = request.GET.get('next')
            return redirect(next)

    return render(request, 'consult_add.html', {"form_obj": form_obj})


# 编辑跟进
def consult_edit(request, edit_id):
    obj = models.ConsultRecord.objects.filter(pk=edit_id).first()
    form_obj = ConsultForm(instance=obj)

    if request.method == 'POST':
        form_obj = ConsultForm(request.POST, instance=obj)
        if form_obj.is_valid():
            form_obj.save()

            return redirect(reverse('consult_list'))

    return render(request, 'consult_edit.html', {"form_obj": form_obj})

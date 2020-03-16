from django.shortcuts import render, redirect, reverse, HttpResponse
from crm import models
from crm.froms import EnrollmentForm
from utils.pagination import Pagination
from django.views import View
from django.db.models import Q


class EnrollmentList(View):

    def get(self, request, *args, **kwargs):

        q = self.search([])

        all_enrollment = models.Enrollment.objects.filter(q, customer__in=request.user_obj.customers.all())

        page = Pagination(request.GET.get('page', 1), all_enrollment.count(), request.GET.copy(), 2)

        return render(request, 'enrollment_list.html', {
            'all_enrollment': all_enrollment[page.start:page.end],
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


def enrollment_change(request, customer_id=None, enrollment_id=None):
    # obj = models.Enrollment(customer_id=customer_id)
    #
    # obj = models.Enrollment.objects.filter(pk=enrollment_id)

    obj = models.Enrollment(customer_id=customer_id) if customer_id else models.Enrollment.objects.filter(
        pk=enrollment_id).first()
    title = '新增报名' if customer_id else '编辑报名'
    form_obj = EnrollmentForm(instance=obj)
    if request.method == 'POST':

        form_obj = EnrollmentForm(request.POST, instance=obj)
        if form_obj.is_valid():
            form_obj.save()
            next = request.GET.get('next')
            return redirect(next)

    return render(request, 'form.html', {'form_obj': form_obj, "title": title})

from django.shortcuts import render, redirect, reverse
from rbac import models
from rbac.forms import RoleForm, MenuForm
from django.db.models import Q


# Create your views here.
def role_list(request):
    all_role = models.Role.objects.all()
    return render(request, 'rbac/role_list.html', {'all_role': all_role})


def role_change(request, edit_id=None):
    obj = models.Role.objects.filter(pk=edit_id).first()

    form_obj = RoleForm(instance=obj)
    if request.method == 'POST':
        form_obj = RoleForm(request.POST, instance=obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse('rbac:role_list'))

    return render(request, 'rbac/form.html', {'form_obj': form_obj})


def role_del(request, del_id):
    models.Role.objects.filter(pk=del_id).delete()
    return redirect(reverse('rbac:role_list'))


def menu_list(request):
    all_menus = models.Menu.objects.all()

    mid = request.GET.get('mid')
    if mid:
        all_permission = models.Permission.objects.filter(Q(parent__menu_id=mid) | Q(menu_id=mid)).values('id',
                                                                                                          'parent_id',
                                                                                                          'title',
                                                                                                          'url', 'name',
                                                                                                          'menu__title')
    else:
        all_permission = models.Permission.objects.all().values('id', 'parent_id', 'title', 'url', 'name',
                                                                'menu__title')

    permission_dict = {}

    for i in all_permission:
        if not i.get('parent_id'):
            i['children'] = []
            permission_dict[i['id']] = i

    for i in all_permission:
        pid = i.get('parent_id')
        if pid:
            permission_dict[pid]['children'].append(i)
    print(permission_dict)

    return render(request, 'rbac/menu_list.html',
                  {'mid': mid,'all_menus': all_menus, 'all_permission': permission_dict.values()})


def menu_change(request, edit_id=None):
    obj = models.Menu.objects.filter(pk=edit_id).first()

    form_obj = MenuForm(instance=obj)
    if request.method == 'POST':
        form_obj = MenuForm(request.POST, instance=obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse('rbac:menu_list'))

    return render(request, 'rbac/form.html', {'form_obj': form_obj})


def delete(request, table, del_id):
    table_class = getattr(models, table.capitalize())
    table_class.objects.filter(pk=del_id).delete()
    return redirect(reverse('rbac:{}_list'.format(table)))

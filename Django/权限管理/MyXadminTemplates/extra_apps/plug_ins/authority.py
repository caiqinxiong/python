from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import Permission


def menu_filter(request):
    user = request.user
    menus = ModelBackend().get_all_permissions(user_obj=user)
    can_menus = {
        'menus': [],
    }

    for menu in menus:
        if str(menu).split('.')[0] == 'plug_ins':
            menu = Permission.objects.get(codename=str(menu).split('.')[-1])
            if menu.codename.split('_')[0] == 'view':
                can_menus['menus'].append({
                    'id': menu.codename.split('view_')[-1],
                    'url': '/xadmin/ta/%s/' % menu.codename.split('view_')[-1].replace('menu', '')
                })
    return can_menus

from django.conf import settings


def init_permission(request, obj):
    # 认证成功 保存权限信息

    # ORM获取到权限信息 去除权限为空的权限  去重
    permission_query = obj.roles.filter(permissions__url__isnull=False).values('permissions__url',
                                                                               'permissions__title',
                                                                               'permissions__icon',
                                                                               'permissions__is_menu',
                                                                               ).distinct()
    # 权限的列表
    permission_list = []

    # 菜单的列表
    menu_list = []

    for i in permission_query:
        # 把权限的信息放入permission_list
        permission_list.append({'url': i['permissions__url']})

        # 把是菜单的权限的信息放入menu_list
        if i['permissions__is_menu']:
            menu_list.append({'url': i['permissions__url'],
                              'title': i['permissions__title'],
                              'icon': i['permissions__icon'],
                              })

    request.session[settings.PERMISSION_SESSION_KEY] = permission_list  # json的序列化
    request.session[settings.MENU_SESSION_KEY] = menu_list
    request.session['is_login'] = True

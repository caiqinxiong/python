from django.conf import settings


def init_permission(request, obj):
    # 认证成功 保存权限信息

    # ORM获取到权限信息 去除权限为空的权限  去重
    permission_query = obj.roles.filter(permissions__url__isnull=False).values('permissions__url',
                                                                               'permissions__title',
                                                                               'permissions__menu__title',
                                                                               'permissions__menu__icon',
                                                                               'permissions__menu__wight',
                                                                               'permissions__menu_id',
                                                                               'permissions__id',
                                                                               'permissions__parent_id',
                                                                               'permissions__parent__name',
                                                                               'permissions__name',
                                                                               ).distinct()

    print(permission_query)

    # 权限的字典
    permission_dict = {}

    # 菜单的字典
    menu_dict = {}

    for i in permission_query:
        # 把权限的信息放入permission_list
        permission_dict[i['permissions__name']] = {'url': i['permissions__url'],
                                                   'id': i['permissions__id'],
                                                   'pid': i['permissions__parent_id'],
                                                   'pname': i['permissions__parent__name'],
                                                   'title': i['permissions__title'],
                                                   }
        menu_id = i.get('permissions__menu_id')

        if not menu_id:
            continue

        menu_dict.setdefault(menu_id, {
            'title': i['permissions__menu__title'],
            'icon': i['permissions__menu__icon'],
            'wight': i['permissions__menu__wight'],
            'children': [

            ]
        })

        menu_dict[menu_id]['children'].append(
            {'id': i['permissions__id'], 'title': i['permissions__title'], 'url': i['permissions__url']})

    request.session[settings.PERMISSION_SESSION_KEY] = permission_dict  # json的序列化
    request.session[settings.MENU_SESSION_KEY] = menu_dict
    request.session['is_login'] = True



    print(permission_dict)

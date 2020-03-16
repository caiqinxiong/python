data = [{
    'permissions__url': '/customer/list/',
    'permissions__title': '展示客户',
    'permissions__menu__title': '客户管理',
    'permissions__menu__icon': 'fa-user-o',
    'permissions__menu_id': 1
}, {
    'permissions__url': '/customer/add/',
    'permissions__title': '添加用户',
    'permissions__menu__title': None,
    'permissions__menu__icon': None,
    'permissions__menu_id': None
}, {
    'permissions__url': '/customer/edit/(\\d+)/',
    'permissions__title': '编辑用户',
    'permissions__menu__title': None,
    'permissions__menu__icon': None,
    'permissions__menu_id': None
}, {
    'permissions__url': '/customer/del/(\\d+)/',
    'permissions__title': '删除用户',
    'permissions__menu__title': None,
    'permissions__menu__icon': None,
    'permissions__menu_id': None
}, {
    'permissions__url': '/payment/list/',
    'permissions__title': '缴费列表',
    'permissions__menu__title': '财务管理',
    'permissions__menu__icon': 'fa-usd',
    'permissions__menu_id': 2
}, {
    'permissions__url': '/oder/list/',
    'permissions__title': '账单列表',
    'permissions__menu__title': '财务管理',
    'permissions__menu__icon': 'fa-usd',
    'permissions__menu_id': 2
},

    {
        'permissions__url': '/payment/add/',
        'permissions__title': '添加缴费',
        'permissions__menu__title': None,
        'permissions__menu__icon': None,
        'permissions__menu_id': None
    }, {
        'permissions__url': '/payment/edit/(\\d+)/',
        'permissions__title': '编辑缴费',
        'permissions__menu__title': None,
        'permissions__menu__icon': None,
        'permissions__menu_id': None
    }, {
        'permissions__url': '/payment/del/(\\d+)/',
        'permissions__title': '删除缴费',
        'permissions__menu__title': None,
        'permissions__menu__icon': None,
        'permissions__menu_id': None
    }]

"""
{
    2: {
        'title': '财务管理',
        'icon': 'fa-usd',
        'wight': 10,
        'children': [
            {'title': '缴费列表', 'url': '/payment/list/'}
            {'title': '账单列表', 'url': '/oder/list/'}
        ]

    },
    1: {
        'title': '客户管理',
        'icon': 'fa-usd',
        'wight': 100,
        'children': [
            {'title': '缴费列表', 'url': '/payment/list/'}
        ]

    },

}
"""
ret = {}

for i in data:
    menu_id = i.get('permissions__menu_id')

    if not menu_id:
        continue

    ret.setdefault(menu_id, {
        'title': i['permissions__menu__title'],
        'icon': i['permissions__menu__icon'],
        'children': [
        ]
    })

    ret[menu_id]['children'].append({'title': i['permissions__title'], 'url': i['permissions__url']})

print(ret)

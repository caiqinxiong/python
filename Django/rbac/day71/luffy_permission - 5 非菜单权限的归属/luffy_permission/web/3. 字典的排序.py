from collections import OrderedDict

dic = OrderedDict()
dic[3] = 3
dic[1] = 1
dic[2] = 2

menu_dict = {
    2: {
        'title': '财务管理',
        'icon': 'fa-usd',
        'wight': 10,
        'children': [
            {'title': '缴费列表', 'url': '/payment/list/'},
            {'title': '账单列表', 'url': '/oder/list/'}
        ]

    },
    1: {
        'title': '客户管理',
        'icon': 'fa-usd',
        'wight': 1,
        'children': [
            {'title': '缴费列表', 'url': '/payment/list/'},
        ]

    },

}

ret = sorted(menu_dict, key=lambda x: menu_dict[x]['wight'], reverse=True)
print(ret)

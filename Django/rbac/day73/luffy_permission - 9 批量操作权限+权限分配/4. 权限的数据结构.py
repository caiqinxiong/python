data = [{'url': '/customer/list/', 'id': 1, 'pid': None, 'title': '展示客户'},
        {'url': '/customer/add/', 'id': 2, 'pid': 1, 'title': '添加用户'},
        {'url': '/customer/edit/(\\d+)/', 'id': 3, 'pid': 1, 'title': '编辑用户'},
        {'url': '/customer/del/(\\d+)/', 'id': 4, 'pid': 1, 'title': '删除用户'},
        {'url': '/payment/list/', 'id': 5, 'pid': None, 'title': '缴费列表'},
        {'url': '/payment/add/', 'id': 6, 'pid': 5, 'title': '添加缴费'},
        {'url': '/payment/edit/(\\d+)/', 'id': 7, 'pid': 5, 'title': '编辑缴费'},
        {'url': '/payment/del/(\\d+)/', 'id': 8, 'pid': 5, 'title': '删除缴费'}
        ]

data = {

    1: {'url': '/customer/list/', 'id': 1, 'pid': None, 'title': '展示客户'},
    2: {'url': '/customer/add/', 'id': 2, 'pid': 1, 'title': '添加用户'},
    3: {'url': '/customer/edit/(\\d+)/', 'id': 3, 'pid': 1, 'title': '编辑用户'},
    4: {'url': '/customer/del/(\\d+)/', 'id': 4, 'pid': 1, 'title': '删除用户'},
    5: {'url': '/payment/list/', 'id': 5, 'pid': None, 'title': '缴费列表'},
    6: {'url': '/payment/add/', 'id': 6, 'pid': 5, 'title': '添加缴费'},
    7: {'url': '/payment/edit/(\\d+)/', 'id': 7, 'pid': 5, 'title': '编辑缴费'},
    8: {'url': '/payment/del/(\\d+)/', 'id': 8, 'pid': 5, 'title': '删除缴费'}

}

import json

ret = json.dumps(data)
print(ret)

ret = json.loads(ret)
print(ret)

data = {
    'customer_list': {'url': '/customer/list/', 'id': 1, 'pid': None, 'pname': None, 'title': '展示客户'},
    'customer_add': {'url': '/customer/add/', 'id': 2, 'pid': 1, 'pname': 'customer_list', 'title': '添加用户'},
    'customer_edit': {'url': '/customer/edit/(\\d+)/', 'id': 3, 'pid': 1, 'pname': 'customer_list',
                      'title': '编辑用户'},
    'customer_del': {'url': '/customer/del/(\\d+)/', 'id': 4, 'pid': 1, 'pname': 'customer_list', 'title': '删除用户'},
    'payment_list': {'url': '/payment/list/', 'id': 5, 'pid': None, 'pname': None, 'title': '缴费列表'},
    'payment_add': {'url': '/payment/add/', 'id': 6, 'pid': 5, 'pname': 'payment_list', 'title': '添加缴费'},
    'payment_edit': {'url': '/payment/edit/(\\d+)/', 'id': 7, 'pid': 5, 'pname': 'payment_list', 'title': '编辑缴费'},
    'payment_del': {'url': '/payment/del/(\\d+)/', 'id': 8, 'pid': 5, 'pname': 'payment_list', 'title': '删除缴费'}
}

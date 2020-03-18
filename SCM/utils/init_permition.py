# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
#2020/3/9 10:58
from django.conf import settings
def init_permission(obj,request):
    """
    初始化权限信息，获取权限信息并放置到session中。
    :param obj:
    :param request:
    :return:
    """
    # 获取相关权限
    permission_url_list = obj.group_set.filter(permission__url__isnull=False).values('permission__title',
                                                                                     "permission__name",
                                                                                     'permission__url',
                                                                                     ).distinct()

    url_list = []  # 转换为list才能写入session，并去重
    for i in permission_url_list:
        if i not in url_list: url_list.append(i)
    request.session['permission_url_list'] = url_list  # 将权限信息写入session，不支持直接写入对象

    return url_list

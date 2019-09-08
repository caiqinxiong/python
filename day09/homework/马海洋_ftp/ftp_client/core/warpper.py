#!/usr/bin/env python
# coding=UTF-8
'''
@Author: 马海阳
@CreateFileDate: 2019-08-31 00:09:50
'''
from functools import wraps


def format_wrapper(func):
    '''格式整理装饰器'''
    @wraps(func)
    def inner(*args, **kwargs):
        str_num = '%s%s%s\n' % ('=' * 50, func.__doc__, '=' * 50)
        print(str_num)
        ret = func(*args, *kwargs)
        print('\n' + '=' * int(len(str_num) + 5), '\n')
        return ret
    return inner



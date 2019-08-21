# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/8/21 14:19
class Course(object):
    '''课程类'''

    def __init__(self, name, price, period, teacher):
        self.name = name
        self.price = price
        self.period = period
        self.teacher = teacher
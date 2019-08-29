# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/8/28 10:34

class Course:
    def __init__(self,name,price,period):
        self.name = '*'* 25 + '\n课程名称：' + name
        self.price = '课程价格：' + price
        self.period = '课程周期：' + period


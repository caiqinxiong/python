# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/8/21 15:39
class User(object):
    '''用户类，作为学生和讲师的父类，应用公共属性'''
    def __init__(self, username, password, age, sex, phone):
        self.username = username
        self.password = password
        self.age = age
        self.sex = sex
        self.phone = phone
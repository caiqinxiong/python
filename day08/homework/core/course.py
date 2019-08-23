# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/8/21 14:19
class Course(object):
    '''课程类'''

    def __init__(self, name, teacher, price, period):
        self.name = name
        self.teacher = teacher
        self.price = price
        self.period = period


class Classroom(object):
    '''班级类'''

    def __init__(self, classroom, course, teacher={'讲师信息：':None}, student={'学生信息：':[]}):
        self.classroom = classroom  # 班级名称
        self.course = course  # 所教课程
        self.teacher = teacher  # 授课讲师
        self.student = student  # 学生列表



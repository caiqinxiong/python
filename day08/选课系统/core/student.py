# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/8/28 10:33
from core.common import Common as cn
from core.log import Log as log
from conf import settings as ss

class Student:
    opt_lst = [('查看可选课程', 'showCourse'), ('选择课程', 'chooseCourse'),('查看已选课程','showSelectedCourse'),('退出','quit')]

    def __init__(self,name):
        self.name = name
        self.courses = []

    def showCourse(self):
        '''查看可选课程'''
        log.debug('*'*25 + '\n' + self.name+'可选的课程有：')
        stu = list(cn.readInfo(ss.choose_course_file(self.name)))
        for k,v in cn.readInfo(ss.course_file):
            for s,t in stu:
                if k == s:break
            else:
                for s, t in v.__dict__.items():log.debug(t)
        log.info(self.name+'查看了可选课程！')

    def chooseCourse(self):
        '''选择课程'''
        flag = True
        while flag:
            name = input('请选择课程：').strip()
            for s, t in cn.readInfo(ss.choose_course_file(self.name)): # 已经选过的课程就不能重复选择了。
                if name == s:
                    log.warning('您已经选过%s课程！请重新选择：' % name)
                    break
            else:
                for k,v in cn.readInfo(ss.course_file):
                    if name == k:
                        cn.writeInfo(ss.choose_course_file(self.name),name,v)
                        content = self.name + '选择课程%s成功！' % name
                        log.debug(content)
                        log.info(content)
                        flag = False
                        break
                else:
                    log.warning('选择的%s课程不存在哦！请重新选择：' % name)

    def showSelectedCourse(self):
        '''查看已选课程'''
        log.info(self.name+'查看了已选课程信息！')
        [log.debug(t) for k,v in cn.readInfo(ss.choose_course_file(self.name)) for s,t in v.__dict__.items()]


    def quit(self):
        print('谢谢使用！')
        exit(-1)


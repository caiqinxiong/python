# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/8/28 10:34
import os
from core.common import Common as cn
from core.log import Log as log
from core import course as cs
from conf import settings as ss

class Manager:
    opt_lst = [('创建学生', 'createStudent'), ('创建课程', 'createCourse'), ('查看所有学生', 'showStudents'),
               ('查看所有课程', 'showCourse'),('查看学生所选课程', 'showStudentCourse'), ('退出', 'quit')]

    def __init__(self, name):
        self.name = name

    def __createInfo(self,file,kind):
        '''创建信息'''
        while True:
            name = input('请输入%s名称：' % kind).strip()
            for k, v in cn.readInfo(file):
                if k == name:
                    log.warning('%s%s已存在！' % (name,kind))
                    break
            else:
                if kind == '课程':
                    pric = input('请输入课程价格：').strip()
                    period = input('请输入课程周期：').strip()
                    c = cs.Course(name, pric, period)
                    cn.writeInfo(ss.course_file, name, c)
                else:
                    __password = cn.changeHashlib(input('请输入密码：').strip())
                    cn.writeInfo(ss.student_file, name, (name, __password, 'Student'))
                conten = self.name + '创建%s%s成功！' % (name,kind)
                log.debug(conten)
                log.info(conten)
                break

    def createCourse(self):
        '''创建课程'''
        self.__createInfo(ss.course_file,'课程')

    def createStudent(self):
        '''创建学生账号'''
        self.__createInfo(ss.student_file,'学生')

    def showStudents(self):
        '''查看所有学生'''
        log.debug('*' * 25 + '\n所有的学生信息如下：\n' + '*' * 25)
        for k, v in cn.readInfo(ss.student_file):
            if v[-1] == 'Student': log.debug(k)
        log.info(self.name + '查看了所有学生信息！')

    def printInfo(self, file):
        '''打印信息，利用列表推导式打印'''
        [log.debug(t) for k, v in cn.readInfo(file) for s, t in v.__dict__.items()]

    def showCourse(self):
        '''查看所有课程'''
        log.debug('*' * 25 + '\n所有课程信息如下：')
        self.printInfo(ss.course_file)
        log.info(self.name + '查看了所有课程信息！')

    def showStudentCourse(self):
        '''查看学生所选择的课程'''
        log.info(self.name + '查看了所有学生选择的课程信息！')
        dir_path = os.path.join(ss.db_path, 'choose_course')
        for name in os.listdir(dir_path):
            log.debug('*' * 25 + '\n%s选择的课程如下：' % name)
            file_name = os.path.join(dir_path, name, 'choose_course_info')
            self.printInfo(file_name)

    def quit(self):
        log.debug('谢谢使用！')
        exit(-1)




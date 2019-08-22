# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/8/21 15:33
import os
import time
from conf import settings as ss
from core.certification import Certification as cc
from core import course as cs
from core import human as hm
from core import admin as ad


class Teacher(object):
    '''讲师类'''

    def __init__(self, username, password, age, sex, phone):
        hm.Human.__init__(self,username, password, age, sex, phone)


    def view_classroom(self):
        '''查看所教班级'''
        flag = False
        for file_name in os.listdir(ss.classroom_path):
            ret = list(cc().read_information(os.path.join(ss.classroom_path,file_name)))
            for i in ret:
                if self.username in i:
                    print('%s所教的班级信息如下：\n%s\n%s' % (self.username,ret[0][-1],ret[1][-1]))
                    flag = True
        if not flag: print('%s还未分配任何班级哦，请联系管理员指定。' % self.username)



    def view_classroom_student(self):
        '''查看班级中的学生'''
        flag = False
        for file_name in os.listdir(ss.classroom_path):
            ret = list(cc().read_information(os.path.join(ss.classroom_path,file_name)))
            for i in ret:
                if self.username in i:
                    print('%s所教的班级中的学生信息如下：' % (self.username))
                    print('%s教室共有%s名学生:\n%s' % (ret[0][-1].split('：')[-1],len(ret[-1][-1]),ret[-1][-1]))
                    flag = True
        if not flag: print('%s还未分配任何班级哦，请联系管理员指定。' % self.username)


    def teacher_view(self):
        '''讲师界面'''
        while True:
            print('*' * 25 + '\n1、查看所有课程\n2、查看所教班级\n3、查看班级中的学生\n4、退出\n' + '*' * 25)
            choose = input('请选择：').strip()
            if '1' == choose: # 查看所有课程
                ad.Admin.view_all_courses(self) # 直接调用管理员的查看所有课程函数即可
            elif '2' == choose: # 查看所教班级
                self.view_classroom()
            elif '3' == choose: # 查看班级中的学生
                self.view_classroom_student()
            elif '4' == choose:
                print('谢谢使用！')
                exit(-1)
            else:
                print('输入有误，请重新输入！')
            print('5秒后自动跳转回主页面！')
            time.sleep(5)

if __name__ == '__main__':
    Teacher('alex','pwd','age','sex','phone').student_view()
# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/8/21 15:33
import os
import time
from conf import settings as ss
from core.certification import Certification as cc
from core import course as cs
from core import user as us
from core import manager as ad
from core.log import Log as log


class Teacher(us.User): # 继承父类
    '''讲师类'''

    def __init__(self, username, password, age, sex, phone):
        us.User.__init__(self,username, password, age, sex, phone)


    def classroom_info(self,kind):
        '''班级信息'''
        flag = True
        for file_name in os.listdir(ss.classroom_path):
            ret = list(cc().read_information(os.path.join(ss.classroom_path,file_name)))
            if self.username == ret[2][-1]['讲师信息：']:
                if kind == '讲师':
                    log.debug('%s所教的班级信息如下：\n%s\n%s' % (self.username,ret[0][-1],ret[1][-1]))
                else:
                    log.debug('%s所教的班级中的学生信息如下：' % (self.username))
                    log.debug('%s教室共有%s名学生:\n%s' % (ret[0][-1].split('：')[-1],len(ret[-1][-1]['学生信息：']),ret[-1][-1]['学生信息：']))
                flag = False
        if flag: log.warning('%s还未分配任何班级哦，请联系管理员指定。' % self.username)


    def view_classroom(self):
        '''查看所教班级'''
        self.classroom_info('讲师')


    def view_classroom_student(self):
        '''查看班级中的学生'''
        self.classroom_info('学生')


    def teacher_view(self):
        '''讲师界面'''
        while True:
            print('*' * 25 + '\n1、查看所有课程\n2、查看所教班级\n3、查看班级中的学生\n4、退出\n' + '*' * 25)
            choose = input('请选择：').strip()
            if '1' == choose: # 查看所有课程
                ad.Manager.view_all_courses(self) # 直接调用管理员的查看所有课程函数即可
                log.info(self.username+'查看所有课程!')
            elif '2' == choose: # 查看所教班级
                self.view_classroom()
                log.info(self.username+'查看了所教班级信息！')
            elif '3' == choose: # 查看班级中的学生
                self.view_classroom_student()
                log.info(self.username+'查看了TA所教班级中的学生！')
            elif '4' == choose:
                print('谢谢使用！')
                exit(-1)
            else:
                print('输入有误，请重新输入！')
            print('3秒后自动跳转回主页面！')
            time.sleep(3)

if __name__ == '__main__':
    Teacher('Eva_J','pwd','age','sex','phone').teacher_view()
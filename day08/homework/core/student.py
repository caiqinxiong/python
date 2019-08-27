# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/8/21 10:36
import os
import time
from conf import settings as ss
from core import certification as cc
from core import course as cs
from core import user as us
from core.log import Log as log


class Students(us.User): # 继承父类
    '''学生类'''

    def __init__(self, username, password, age, sex, phone):
        us.User.__init__(self, username, password, age, sex, phone)

    def view_optional_courses(self):
        '''查看可选课程'''
        if not os.path.exists(ss.course_file): return log.warning('课程文件不存在，还未有可选课程哦！')
        print('*' * 25 + '\n\033[31;1m所有可选课程信息如下：\033[0m')
        stu = list(cc.Certification().read_information(ss.choose_course_file(self.username)))
        ret = cc.Certification().read_information(ss.course_file)
        for k, v in ret:
            for s, t in stu: # 只展示该学生未选的课程，已经选过的课就不能再选啦。
                if t == v: break
            else:
                log.debug(v)


    def choose_course(self):
        '''选择课程'''
        print('请输入选择课程名称：')
        flag = True
        while flag:
            choose = input().strip()
            ret = cc.Certification().read_information(ss.choose_course_file(self.username))
            for k, v in ret: # 已经选过的课程就不能重复选择了。
                if choose in v:
                    log.warning('您已经选过%s课程！请重新选择：' % choose)
                    break
            else:
                ret = cc.Certification().read_information(ss.course_file)
                for k, v in ret: # 从剩下的可选课程中选择。
                    if '课程名称' in v and choose in v:
                        name = v # 将选择的课程信息都写入到该学生的选课文件中。
                        price = ret.__next__()[-1]
                        period = ret.__next__()[-1]
                        teacher = ret.__next__()[-1]
                        print("*" * 25 + '\n\033[31;1m选择课程成功！详情如下：\033[0m\n%s\n%s\n%s\n%s' % (name, price, period, teacher))
                        log.info(self.username+'选择%s课程成功！' % choose)
                        c = cs.Course(name, price, period, teacher)  # 将课程信息传入课程类
                        cc.Certification().written_information(ss.choose_course_file(self.username),c)  # 将课程类写入文件
                        flag = False
                        break
                else:
                    log.warning('选择的%s课程不存在哦！请重新选择：' % choose)


    def view_selected_courses(self):
        '''查看所选课程'''
        if not os.path.exists(ss.choose_course_file(self.username)): return log.warning('您还未选择任何课程哦！')
        print('*' * 25 + '\n\033[31;1m%s所选课程信息如下：\033[0m' % self.username)
        ret = cc.Certification().read_information(ss.choose_course_file(self.username))
        for k, v in ret:print(v) # 打印课程信息


    def student_view(self):
        '''学生界面'''
        while True:
            print('*' * 25 + '\n1、查看可选课程\n2、选择课程\n3、查看已选课程\n4、退出\n' + '*' * 25)
            choose = input('请选择：').strip()
            if '1' == choose: # 查看可选课程
                self.view_optional_courses()
                log.info(self.username+'查看了可选的课程！')
            elif '2' == choose: # 选择课程
                self.choose_course()
            elif '3' == choose: # 查看已选课程
                self.view_selected_courses()
                log.info(self.username+'查看了已选的课程！')
            elif '4' == choose:
                print('谢谢使用！')
                exit(-1)
            else:
                print('输入有误，请重新输入！')
            print('3秒后自动跳转回主页面！')
            time.sleep(3)

if __name__ == '__main__':
    Students('caiqinxiong','pwd','age','sex','phone').student_view()
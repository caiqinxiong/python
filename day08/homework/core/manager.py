# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/8/21 14:20
import os
import sys
import time
from conf import settings as ss
from core.certification import Certification as cc
from core import student as st
from core import teacher as tc
from core import user as us
from core import course as cs
from core.log import Log as log

class Manager(object):
    '''管理员类'''

    def __init__(self, name):
        self.name = name

    def __create_account(self,file,kind):
        '''创建账号，私有方法，只有管理员才能创建。'''
        while True:
            username = '*' * 25 + '\n姓名：' + input('please input the username:').strip()
            ret = cc().read_information(file)
            for k, v in ret: # 校验账号是否已存在
                if username in v:
                    log.warning('%s%s账号已存在！！' % (username.split('：')[-1], kind))
                    break
            else:
                __password = '密码：' + cc.change_hashlib(input('please input the  password:').strip()) # 将输入的密码转换成密文存储
                age = '年龄：' + input('please input the age:').strip()
                sex = '性别：' + input('please input the sex:').strip()
                phone = '手机号码：' + input('please input the phone number:').strip()
                print("*" * 25 + '\n\033[31;1m%s账号创建成功！详细信息如下：\033[0m\n%s\n%s\n%s\n%s' % (kind, username, age, sex, phone))
                log.info(self.name+'创建'+username.split('：')[-1]+kind+'账号成功！')
                u = us.User(username, __password, age, sex, phone)
                cc().written_information(file, u)  # 将实例化对象写入文件
                break

    def create_student_account(self):
        '''创建学生账号'''
        print('请添加学生信息！')
        self.__create_account(ss.student_file, '学生')


    def create_teacher_account(self):
        '''创建讲师账号'''
        print('请添加讲师信息！')
        self.__create_account(ss.teacher_file, '讲师')


    def view_accout_info(self,file, kind):
        '''查看账号信息'''
        if not os.path.exists(file):return log.error('%s文件不存在，还未添加任何%s账号！' % (file,kind))
        ret = cc().read_information(file)
        print('*' * 25 + '\n\033[31;1m所有%s信息如下：\033[0m' % kind)
        for k, v in ret:log.debug(v) # 打印账号信息


    def view_all_students(self):
        '''查看所有学生'''
        self.view_accout_info(ss.student_file, '学生')


    def view_all_teachers(self):
        '''查看所有讲师信息'''
        self.view_accout_info(ss.teacher_file, '讲师')


    def create_course(self):
        '''创建课程'''
        print('请添加课程信息！')
        flag = True
        while flag:
            name = '*' * 25 + '\n课程名称：' + input('please input the course`s name:').strip()
            ret = cc().read_information(ss.course_file)
            for k, v in ret: # 校验课程是否已存在，避免重复创建课程。
                if name in v:
                    log.error('%s课程已存在！！' % name.split('：')[-1])
                    break
            else:
                teacher = '授课老师：' + input('please input the teacher`s name:').strip()
                ret = cc().read_information(ss.teacher_file)
                for k,v in ret: # 校验讲师信息是否存在，否则先添加讲师信息。
                    if teacher.split('：')[-1] in v:
                        price = '课程价格：' + input('please input the course`s price:').strip()
                        period = '课程周期：' + input('please input the period:').strip()
                        print("*" * 25 + '\n\033[31;1m创建课程成功！信息如下：\033[0m\n%s\n%s\n%s\n%s' % (name, teacher, price, period))
                        log.info(self.name+'创建'+name.split('：')[-1]+'课程成功！')
                        c = cs.Course(name, teacher, price, period)  # 将课程信息传入课程类
                        cc().written_information(ss.course_file, c)  # 将课程类写入文件
                        flag = False
                        break
                else:
                    log.warning('授课老师%s不存在！' % teacher.split('：'[-1])[-1])


    def view_all_courses(self):
        '''查看所有课程'''
        if not os.path.exists(ss.course_file): return log.warning('课程文件不存在，还未添加任何课程哦！')
        print('*' * 25 + '\n\033[31;1m所有课程信息如下：\033[0m')
        ret = cc().read_information(ss.course_file)
        for k, v in ret:log.debug(v) # 打印所有课程信息


    def view_all_selected_courses(self):
        '''查看所有学生的选课情况'''
        flag = True
        for file_name in os.listdir(ss.choose_course_path): # 获取所有的学生选课信息文件
            if 'choose_course_info' in file_name:
                print('*' * 25 + '\n\033[31;1m%s所选课程信息如下：\033[0m' % file_name.split('_')[0])
                ret = cc().read_information(ss.choose_course_file(file_name.split('_')[0]))
                for k, v in ret:log.debug(v) # 打印所选课程信息
                flag = False
        if flag: log.warning('还未有学生选择任何课程哦！')


    def create_classroom(self):
        '''创建班级'''
        print('请添加班级信息！')
        while True:
            classroom = input('请输入教室名称(如：101)：').strip()
            if os.path.exists(ss.classroom_file(classroom)):
                log.warning('%s教室已存在！！' % classroom)
            else:
                classcourse = '班级课程：' + input('请输入班级课程名称：').strip()
                classroom = '*'*25 + '\n教室名称：' + classroom
                print('添加班级信息成功！详细信息如下：\n%s\n%s\n讲师信息：None\n学生信息：[]' % (classroom,classcourse))
                log.info(self.name+'创建%s教室信息成功！' % classroom.split('：')[-1])
                c = cs.Classroom(classroom,classcourse) # 只传入教室和课程名称，学生和讲师使用默认值，等管理员单独指定。
                cc().written_information(ss.classroom_file(classroom.split('：')[-1]), c)  # 将班级信息写入文件
                break


    def view_classroom_info(self):
        '''查看教室信息'''
        flag = True
        for file_name in os.listdir(ss.classroom_path):
            ret = cc().read_information(os.path.join(ss.classroom_path,file_name))
            for k,v in ret:log.debug(v)
            flag = False
        if flag:log.warning('还未创建任何教室信息哦！')


    def __specified_classroom(self,file,kind):
        '''指定班级，私有方法，只有管理员才能指定。'''
        if not os.path.exists(file): return log.warning('还未添加任何%s账号信息，请先添加！' % kind)
        dir = os.listdir(ss.classroom_path)
        if not dir:return log.warning('还未添加任何教室信息，请先添加！') # 目录为空
        flag = True
        while flag:
            name = input('请输入%s姓名：' % kind).strip()
            teacher = cc().read_information(file)
            for s,t in teacher:
                if '姓名' in t and  name in t:
                    flag = False
                    classroom = input('请输入教室名称(如：101)：').strip()
                    for file_name in dir:
                        if  classroom in file_name:
                            ret = cc().read_information(ss.classroom_file(classroom))
                            class_name = ret.__next__()[-1] # 装饰器逐个取值
                            course_name = ret.__next__()[-1]
                            teacher_name = ret.__next__()[-1]
                            student_list = ret.__next__()[-1]
                            if kind == '讲师':
                                teacher_name['讲师信息：'] = name # 指定讲师，一个班只有一个讲师
                                conten = '%s成功将%s讲师分配到%s教室！' % (self.name,name,classroom)
                            else:
                                if name in student_list['学生信息：']: # 一个班里不能重复添加学生信息
                                    log.warning('%s已经在%s教室里了哦！' % (name,classroom))
                                    break
                                else:
                                    student_list['学生信息：'].append(name) #指定学生，一个班可以有多个学生
                                    conten = '%s成功将%s同学分配到%s教室！' % (self.name,name,classroom)
                            log.debug(conten)
                            c = cs.Classroom(class_name, course_name,teacher_name,student_list)
                            cc().written_information(ss.classroom_file(classroom), c, mode='wb')  # 将班级信息覆盖写入文件
                            log.info(conten)
                            break
                    else:
                        log.warning('%s教室不存在！！' % classroom.split('：')[-1])
                        break
            if flag:log.warning('%s%s不存在！' % (name,kind))


    def classroom_teacher(self):
        '''为讲师指定班级'''
        self.__specified_classroom(ss.teacher_file,'讲师')


    def classroom_student(self):
        '''为学生指定班级'''
        self.__specified_classroom(ss.student_file,'学生')


    def quit(self):
        '''退出程序'''
        print('\033[31;1m谢谢使用！\033[0m')
        exit(-1)


    def admin_view(self):
        '''管理员界面'''
        opt_list = [('创建学生账号','create_student_account'),('查看所有学生信息','view_all_students'),('为学生指定班级','classroom_student'),
                        ('创建讲师','create_teacher_account'),('查看所有讲师信息','view_all_teachers'),('为讲师指定班级','classroom_teacher'),
                        ('创建课程','create_course'),('查看所有课程','view_all_courses'),('查看所有学生的选课情况','view_all_selected_courses'),
                        ('创建班级','create_classroom'),('查看教室信息','view_classroom_info'),('退出','quit')]
        while True:
            print('*' * 25)
            for index,opt in enumerate(opt_list,1):print(index,opt[0]) # 打印操作列表信息
            try:
                num = int(input( '*' * 25 + '\n请输入您要选择的操作序号:'))
                if hasattr(Manager(self.name),opt_list[num-1][1]):getattr(Manager(self.name),opt_list[num-1][1])() # 反射
            except ValueError as e:
                log.error('%s不是效数字！！' % e)
            except IndexError as e:
                log.error('%s\n请输入1-12的有效数字！！' % e)
            print('3秒后自动跳转回主页面！')
            time.sleep(3)


if __name__ == '__main__':
    Manager('admin').admin_view()


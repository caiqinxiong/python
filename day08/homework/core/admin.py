# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/8/21 14:20
import os
import time
from conf import settings as ss
from core import certification as cc
from core import student as st
from core import course as cs

class Admin(object):
    '''管理员类'''

    def __init__(self, name):
        self.name = name

    def create_student_account(self):
        '''创建学生账号'''
        while True:
            username = '*' * 25 + '\n姓名：' + input('please input the student`s username:').strip()
            ret = cc.Certification().read_information(ss.student_file)
            for k, v in ret: # 校验账号是否已存在
                if username in v:
                    print('\033[31;1m%s学生账号已存在！！\033[0m' % username.split('：')[-1])
                    break
            else:
                password = '密码：' + input('please input the student`s password:').strip()
                age = '年龄：' + input('please input the age:').strip()
                sex = '性别：' + input('please input the sex:').strip()
                phone = '手机号码：' + input('please input the phone number:').strip()
                print("*" * 25 + '\n\033[31;1m学生账号创建成功！详细信息如下：\033[0m\n%s\n%s\n%s\n%s' % (username, age, sex, phone))
                s = st.Students(username, password, age, sex, phone) # 将信息传入学生类
                cc.Certification().written_information(ss.student_file, s)  # 将学生类写入文件
                break

    def view_all_students(self):
        '''查看所有学生'''
        if not os.path.exists(ss.student_file): return print('还未添加任何学生账号哦！')
        print('*' * 25 + '\n\033[31;1m所有学生信息如下：\033[0m')
        ret = cc.Certification().read_information(ss.student_file)
        for k, v in ret:print(v) # 打印学生账号信息


    def create_course(self):
        '''创建课程'''
        while True:
            name = '*' * 25 + '\n课程名称：' + input('please input the course`s name:').strip()
            ret = cc.Certification().read_information(ss.course_file)
            for k, v in ret: # 校验课程是否已存在，避免重复创建课程。
                if name in v:
                    print('\033[31;1m%s课程已存在！！\033[0m' % name.split('：')[-1])
                    break
            else:
                price = '课程价格：' + input('please input the course`s price:').strip()
                period = '课程周期：' + input('please input the period:').strip()
                teacher = '授课老师：' + input('please input the teacher`s name:').strip()
                print("*" * 25 + '\n\033[31;1m创建课程成功！信息如下：\033[0m\n%s\n%s\n%s\n%s' % (name, price, period, teacher))
                c = cs.Course(name, price, period, teacher)  # 将课程信息传入课程类
                cc.Certification().written_information(ss.course_file, c)  # 将课程类写入文件
                break

    def view_all_courses(self):
        '''查看所有课程'''
        if not os.path.exists(ss.course_file): return print('还未添加任何课程哦！')
        print('*' * 25 + '\n\033[31;1m所有课程信息如下：\033[0m')
        ret = cc.Certification().read_information(ss.course_file)
        for k, v in ret:print(v) # 打印所有课程信息

    def view_all_selected_courses(self):
        '''查看所有学生的选课情况'''
        flag = True
        for file_name in os.listdir(ss.db_path): # 获取所有的学生选课信息文件
            if 'choose_course_info' in file_name:
                print('*' * 25 + '\n\033[31;1m%s所选课程信息如下：\033[0m' % file_name.split('_')[0])
                ret = cc.Certification().read_information(ss.choose_course_file(file_name.split('_')[0]))
                for k, v in ret:print(v) # 打印所选课程信息
                flag = False
        if flag: print('还未有学生选择任何课程哦！')


    def admin_view(self):
        '''管理员界面'''
        while True:
            print('*' * 25 + '\n1、创建学生账号\n2、查看所有学生信息\n3、创建课程\n4、查看所有课程\n5、查看所有学生的选课情况\n6、退出\n' + '*' * 25)
            choose = input('请选择：').strip()
            if '1' == choose:  # 创建学生账号
                self.create_student_account()
            elif '2' == choose:  # 查看所有学生信息
                self.view_all_students()
            elif '3' == choose:  # 创建课程
                self.create_course()
            elif '4' == choose:  # 查看所有课程
                self.view_all_courses()
            elif '5' == choose:  # 查看所有学生的选课情况
                self.view_all_selected_courses()
            elif '6' == choose:
                print('谢谢使用！')
                exit(-1)
            else:
                print('输入有误，请重新输入！')
            print('5秒后自动跳转回主页面！')
            time.sleep(5)


if __name__ == '__main__':
    Admin('admin').admin_view()
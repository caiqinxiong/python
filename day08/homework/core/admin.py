# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/8/21 14:20
import os
import time
from conf import settings as ss
from core.certification import Certification as cc
from core import student as st
from core import teacher as tc
from core import human as hm
from core import course as cs

class Admin(object):
    '''管理员类'''

    def __init__(self, name):
        self.name = name

    def create_account(self,file,kind):
        '''创建账号'''
        while True:
            username = '*' * 25 + '\n姓名：' + input('please input the username:').strip()
            ret = cc().read_information(file)
            for k, v in ret: # 校验账号是否已存在
                if username in v:
                    print('\033[31;1m%s%s账号已存在！！\033[0m' % (username.split('：')[-1], kind))
                    break
            else:
                password = '密码：' + cc().change_hashlib(input('please input the  password:').strip()) # 将输入的密码转换成密文存储
                age = '年龄：' + input('please input the age:').strip()
                sex = '性别：' + input('please input the sex:').strip()
                phone = '手机号码：' + input('please input the phone number:').strip()
                print("*" * 25 + '\n\033[31;1m%s账号创建成功！详细信息如下：\033[0m\n%s\n%s\n%s\n%s' % (kind, username, age, sex, phone))
                h = hm.Human(username, password, age, sex, phone)
                cc().written_information(file, h)  # 将实例化对象写入文件
                break

    def create_student_account(self):
        '''创建学生账号'''
        self.create_account(ss.student_file, '学生')


    def create_teacher_account(self):
        '''创建讲师账号'''
        self.create_account(ss.teacher_file, '讲师')


    def view_accout_info(self,file, kind):
        '''查看账号信息'''
        if not os.path.exists(file):return print('还未添加任何%s账号哦！' % kind)
        ret = cc().read_information(file)
        print('*' * 25 + '\n\033[31;1m所有%s信息如下：\033[0m' % kind)
        for k, v in ret:print(v) # 打印账号信息


    def view_all_students(self):
        '''查看所有学生'''
        self.view_accout_info(ss.student_file, '学生')


    def view_all_teachers(self):
        '''查看所有讲师信息'''
        self.view_accout_info(ss.teacher_file, '讲师')


    def create_course(self):
        '''创建课程'''
        flag = True
        while flag:
            name = '*' * 25 + '\n课程名称：' + input('please input the course`s name:').strip()
            ret = cc().read_information(ss.course_file)
            for k, v in ret: # 校验课程是否已存在，避免重复创建课程。
                if name in v:
                    print('\033[31;1m%s课程已存在！！\033[0m' % name.split('：')[-1])
                    break
            else:
                teacher = '授课老师：' + input('please input the teacher`s name:').strip()
                ret = cc().read_information(ss.teacher_file)
                for k,v in ret: # 校验讲师信息是否存在，否则先添加讲师信息。
                    if teacher.split('：')[-1] in v:
                        price = '课程价格：' + input('please input the course`s price:').strip()
                        period = '课程周期：' + input('please input the period:').strip()
                        print("*" * 25 + '\n\033[31;1m创建课程成功！信息如下：\033[0m\n%s\n%s\n%s\n%s' % (name, teacher, price, period))
                        c = cs.Course(name, teacher, price, period)  # 将课程信息传入课程类
                        cc().written_information(ss.course_file, c)  # 将课程类写入文件
                        flag = False
                        break
                else:
                    print('\n\033[31;1m授课老师不存在！\033[0m')


    def view_all_courses(self):
        '''查看所有课程'''
        if not os.path.exists(ss.course_file): return print('还未添加任何课程哦！')
        print('*' * 25 + '\n\033[31;1m所有课程信息如下：\033[0m')
        ret = cc().read_information(ss.course_file)
        for k, v in ret:print(v) # 打印所有课程信息


    def view_all_selected_courses(self):
        '''查看所有学生的选课情况'''
        flag = True
        for file_name in os.listdir(ss.choose_course_path): # 获取所有的学生选课信息文件
            if 'choose_course_info' in file_name:
                print('*' * 25 + '\n\033[31;1m%s所选课程信息如下：\033[0m' % file_name.split('_')[0])
                ret = cc().read_information(ss.choose_course_file(file_name.split('_')[0]))
                for k, v in ret:print(v) # 打印所选课程信息
                flag = False
        if flag: print('还未有学生选择任何课程哦！')


    def create_classroom(self):
        '''创建班级'''
        while True:
            classroom = input('请输入教室名称(如：101)：').strip()
            if os.path.exists(ss.classroom_file(classroom)):
                print('\033[31;1m%s教室已存在！！\033[0m' % classroom)
            else:
                classcourse = '班级课程：' + input('请输入班级课程名称：').strip()
                classroom = '*'*25 + '\n教室名称：' + classroom
                print('添加班级信息成功！详细信息如下：\n%s\n%s\n讲师信息：None\n学生信息：[]' % (classroom,classcourse))
                c = cs.Classroom(classroom,classcourse) # 只传入教室和课程名称，学生和讲师使用默认值，等管理员单独指定。
                cc().written_information(ss.classroom_file(classroom.split('：')[-1]), c)  # 将班级信息写入文件
                break


    def view_classroom_info(self):
        '''查看教室信息'''
        flag = True
        for file_name in os.listdir(ss.classroom_path):
            ret = cc().read_information(os.path.join(ss.classroom_path,file_name))
            for k,v in ret:print(v)
            flag = False
        if flag:print('还未创建任何教室信息哦！')


    def specified_classroom(self,file,kind):
        '''指定班级'''
        if not os.path.exists(file): return print('还未添加任何%s账号信息，请先添加！' % kind)
        dir = os.listdir(ss.classroom_path)
        if not dir:return print('还未添加任何教室信息，请先添加！') # 目录为空
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
                                print('\033[31;1m成功将%s讲师分配到%s教室！\033[0m' % (name,classroom))
                            else:
                                if name in student_list['学生信息：']: # 一个班里不能重复添加学生信息
                                    print('\033[31;1m%s已经在%s教室里了哦！\033[0m' % (name,classroom))
                                    break
                                else:
                                    student_list['学生信息：'].append(name) #指定学生，一个班可以有多个学生
                                    print('\033[31;1m成功将%s同学分配到%s教室！\033[0m' % (name,classroom))
                            c = cs.Classroom(class_name, course_name,teacher_name,student_list)
                            cc().written_information(ss.classroom_file(classroom), c, mode='wb')  # 将班级信息覆盖写入文件
                            break
                    else:
                        print('\033[31;1m%s教室不存在！！\033[0m' % classroom.split('：')[-1])
                        break
            if flag:print('%s%s不存在！' % (name,kind))


    def classroom_teacher(self):
        '''为讲师指定班级'''
        self.specified_classroom(ss.teacher_file,'讲师')


    def classroom_student(self):
        '''为学生指定班级'''
        self.specified_classroom(ss.student_file,'学生')


    def admin_view(self):
        '''管理员界面'''
        while True:
            print('*' * 25 + '\n1、创建学生账号\n2、查看所有学生信息\n3、创建课程\n4、查看所有课程\n5、查看所有学生的选课情况\n6、创建讲师')
            print('7、为讲师指定班级\n8、创建班级\n9、为学生指定班级\n10、查看所有讲师信息\n11、查看教室信息\n12、退出\n' + '*' * 25)
            choose = input('请选择：').strip()
            if '1' == choose:  # 创建学生账号
                print('请添加学生信息！')
                self.create_student_account()
            elif '2' == choose:  # 查看所有学生信息
                self.view_all_students()
            elif '3' == choose:  # 创建课程
                print('请添加课程信息！')
                self.create_course()
            elif '4' == choose:  # 查看所有课程
                self.view_all_courses()
            elif '5' == choose:  # 查看所有学生的选课情况
                self.view_all_selected_courses()
            elif '6' == choose: # 创建讲师
                print('请添加讲师信息！')
                self.create_teacher_account()
            elif '7' == choose: # 为讲师指定班级
                self.classroom_teacher()
            elif '8' == choose: # 创建班级
                print('请添加班级信息！')
                self.create_classroom()
            elif '9' == choose: # 为学生指定班级
                self.classroom_student()
            elif '10' == choose: # 查看所有讲师信息
                self.view_all_teachers()
            elif '11' == choose: #查看教室信息
                self.view_classroom_info()
            elif '12' == choose:
                print('谢谢使用！')
                exit(-1)
            else:
                print('输入有误，请重新输入！')
            print('5秒后自动跳转回主页面！')
            time.sleep(5)


if __name__ == '__main__':
    Admin('admin').admin_view()


# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/8/19 10:12
import pickle
import os
import time


class Certification(object):
    '''登录认证类'''

    def __init__(self):
        pass

    def written_information(self, file_name, content):
        '''写入信息'''
        with open('%s' % file_name, mode='ab') as f:
            pickle.dump(content, f)


    def read_information(self, file_name):
        '''读取信息'''
        with open('%s' % file_name, mode='rb') as f:
            while True:
                try:
                    r = pickle.load(f)
                    # print(r.__dict__)
                    print('~' * 25)
                    for k, v in r.__dict__.items():
                        yield k, v
                except EOFError:
                    break

    def login(self):
        '''登录验证'''
        for i in range(3):
            user = input('请输入登录名 :').strip()
            if 'admin' == user.lower():
                passwd = input('请输入管理员密码 :').strip()
                if 'admin' == passwd:
                    print('登录成功！欢迎你，%s管理员！' % user)
                    return user
                else:
                    print('管理员密码校验失败！')
                    continue
            ret = Certification().read_information('db/student_info.txt')
            for k, v in ret:
                if 'username' == k and user == v.split('：')[-1].strip():
                    passwd = input('请输入密码 :').strip()
                    if passwd == ret.__next__()[-1].split('：')[-1].strip():
                        print('登录成功！欢迎你，%s同学！' % user)
                        return user, passwd, ret.__next__()[-1], ret.__next__()[-1], ret.__next__()[-1]
                    else:
                        print('密码校验失败！')
            else:
                print('账号不存在！')
        else:
            print('您的3次尝试机会已用完，谢谢使用！')
            return False


class Course(object):
    '''课程类'''

    def __init__(self, name, price, period, teacher):
        self.name = name
        self.price = price
        self.period = period
        self.teacher = teacher


class Students(object):
    '''学生类'''

    def __init__(self, username, password, age, sex, phone):
        self.username = username
        self.password = password
        self.age = age
        self.sex = sex
        self.phone = phone

    def view_optional_courses(self):
        '''查看可选课程'''
        # Admin('admin').view_all_courses()
        print('~' * 25)
        print('\033[31;1m所有可选课程信息如下：\033[0m')
        ret = Certification().read_information('db/course_info.txt')
        for k, v in ret:
            print(v)
        print('~' * 25)

    def choose_course(self):
        '''选择课程'''
        print('请输入选择课程名称：')
        flag = True
        while flag:
            choose = input().strip()
            ret = Certification().read_information('db/course_info.txt')
            for k, v in ret:
                if '课程名称' in v and choose in v:
                    name = v
                    price = ret.__next__()[-1]
                    period = ret.__next__()[-1]
                    teacher = ret.__next__()[-1]
                    print('选择课程成功！详情如下：\n%s\n%s\n%s\n%s' % (name, price, period, teacher))
                    c = Course(name, price, period, teacher)  # 将课程信息传入课程类
                    Certification().written_information('db/%s_choose_course_info.txt' % self.username, c)  # 将课程类写入文件
                    flag = False
                    break
            else:
                print('选择的课程不存在哦！请重新选择：')

    def view_selected_courses(self):
        '''查看所选课程'''
        print('~' * 25)
        print('\033[31;1m%s所选课程信息如下：\033[0m' % self.username)
        ret = Certification().read_information('db/%s_choose_course_info.txt' % self.username)
        for k, v in ret:
            print(v)
        print('~' * 25)

    def student_view(self):
        '''学生界面'''
        while True:
            print('*' * 25)
            print('1、查看可选课程')
            print('2、选择课程')
            print('3、查看已选课程')
            print('4、退出')
            print('*' * 25)
            choose = input('请选择：').strip()
            if '1' == choose:
                self.view_optional_courses()
            elif '2' == choose:
                self.choose_course()
            elif '3' == choose:
                try:
                    self.view_selected_courses()
                except:
                    print('\033[31;1m你还没有选择任何课程哦！\033[0m')
            elif '4' == choose:
                print('谢谢使用！')
                exit(-1)
            else:
                print('输入有误，请重新输入！')
            print('5秒后自动跳转回主页面！')
            time.sleep(5)


class Admin(object):
    '''管理员类'''

    def __init__(self, name):
        self.name = name


    def create_student_account(self):
        '''创建学生账号'''
        username = '姓名：' + input('please input the student`s username:').strip()
        password = '密码：' + input('please input the student`s password:').strip()
        age = '年龄：' + input('please input the age:').strip()
        sex = '性别：' + input('please input the sex:').strip()
        phone = '手机号码：' + input('please input the phone number:').strip()
        print('\033[31;1m学生账号创建成功！详细信息如下：\033[0m\n%s\n%s\n%s\n%s' % (username, age, sex, phone))
        s = Students(username, password, age, sex, phone)
        Certification().written_information('db/student_info.txt', s)  # 将学生类写入文件


    def view_all_students(self):
        '''查看所有学生'''
        print('~' * 25)
        print('\033[31;1m所有学生信息如下：\033[0m')
        ret = Certification().read_information('db/student_info.txt')
        for k, v in ret:
            print(v)
        print('~' * 25)

    def create_course(self):
        '''创建课程'''
        name = '课程名称：' + input('please input the course name:').strip()
        price = '课程价格：' + input('please input the course`s price:').strip()
        period = '课程周期：' + input('please input the period:').strip()
        teacher = '授课老师：' + input('please input the teacher`s name:').strip()
        print('\033[31;1m创建课程成功！信息如下：\033[0m\n%s\n%s\n%s\n%s' % (name, price, period, teacher))
        c = Course(name, price, period, teacher)  # 将课程信息传入课程类
        Certification().written_information('db/course_info.txt', c)  # 将课程类写入文件


    def view_all_courses(self):
        '''查看所有课程'''
        print('~' * 25)
        print('\033[31;1m所有课程信息如下：\033[0m')
        ret = Certification().read_information('db/course_info.txt')
        for k, v in ret:
            print(v)
        print('~' * 25)


    def view_all_selected_courses(self):
        '''查看所有学生的选课情况'''
        work_path = os.getcwd()
        path = os.path.join(work_path, 'db')
        for file_name in os.listdir(path):
            if 'choose_course_info' in file_name:
                print('~' * 25)
                print('\033[31;1m%s所选课程信息如下：\033[0m' % file_name.split('_')[0])
                ret = Certification().read_information('db/%s' % file_name)
                for k, v in ret:
                    print(v)
                print('~' * 25)

    def admin_view(self):
        '''管理员界面'''
        while True:
            print('*' * 25)
            print('1、创建学生账号')
            print('2、查看所有学生信息')
            print('3、创建课程')
            print('4、查看所有课程')
            print('5、查看所有学生的选课情况')
            print('6、退出')
            print('*' * 25)
            choose = input('请选择：').strip()
            if '1' == choose:
                self.create_student_account()
            elif '2' == choose:
                self.view_all_students()
            elif '3' == choose:
                self.create_course()
            elif '4' == choose:
                self.view_all_courses()
            elif '5' == choose:
                self.view_all_selected_courses()
            elif '6' == choose:
                print('谢谢使用！')
                exit(-1)
            else:
                print('输入有误，请重新输入！')
            print('5秒后自动跳转回主页面！')
            time.sleep(5)


if __name__ == '__main__':
    '''
    管理员账号：admin
    管理员密码：admin
    '''
    print('欢迎来到luffy选课系统！')
    ret = Certification().login()
    if 'admin' == ret:
        a = Admin(ret)
        a.admin_view()
    elif ret:
        s = Students(ret[0], ret[1], ret[2], ret[3], ret[4])
        s.student_view()


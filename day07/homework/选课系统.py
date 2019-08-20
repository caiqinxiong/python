# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/8/19 10:12
import pickle
import os
import time
work_path = os.getcwd() # 获取当时工作目录绝对路径
db_path = os.path.join(work_path, 'db') # 数据存储路径


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
        try:
            with open('%s' % file_name, mode='rb') as f:
                while True:
                    try:
                        r = pickle.load(f)
                        for k, v in r.__dict__.items():
                            yield k, v  # 以迭代器方式返回，节省内存使用
                    except EOFError:break
        except:return ("", "")


    def login(self):
        '''登录验证'''
        for i in range(3):  # 3次机会
            user = input('请输入登录名 :').strip()
            if user in admin_dict:  # 优先校验管理员账号，管理员账号总会比普通账号少嘛。
                passwd = input('请输入管理员密码 :').strip()
                if admin_dict[user] == passwd:
                    print("*" * 25 + '\n登录成功！%s管理员！' % user)
                    return user
                else:
                    print('管理员密码校验失败！')
                    continue
            ret = Certification().read_information('db/student_info.txt')  # 读取学生账号信息文件，返回迭代器
            for k, v in ret:
                if 'username' == k and user == v.split('：')[-1].strip():
                    passwd = input('请输入密码 :').strip()
                    if passwd == ret.__next__()[-1].split('：')[-1].strip():
                        print("*" * 25 + '\n登录成功！%s同学！' % user)
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
        if not os.path.exists(db_path + '/course_info.txt'): return print('还未有可选课程哦！')
        print('*' * 25 + '\n\033[31;1m所有可选课程信息如下：\033[0m')
        stu = list(Certification().read_information('db/%s_choose_course_info.txt' % self.username))
        ret = Certification().read_information('db/course_info.txt')
        for k, v in ret:
            for s, t in stu: # 只展示该学生未选的课程，已经选过的课就不能再选啦。
                if t == v: break
            else:
                print(v)


    def choose_course(self):
        '''选择课程'''
        print('请输入选择课程名称：')
        flag = True
        while flag:
            choose = input().strip()
            ret = Certification().read_information('db/%s_choose_course_info.txt' % self.username)
            for k, v in ret: # 已经选过的课程就不能重复选择了。
                if choose in v:
                    print('您已经选过\033[31;1m%s\033[0m课程！请重新选择：' % choose)
                    break
            else:
                ret = Certification().read_information('db/course_info.txt')
                for k, v in ret: # 从剩下的可选课程中选择。
                    if '课程名称' in v and choose in v:
                        name = v # 将选择的课程信息都写入到该学生的选课文件中。
                        price = ret.__next__()[-1]
                        period = ret.__next__()[-1]
                        teacher = ret.__next__()[-1]
                        print("*" * 25 + '\n\033[31;1m选择课程成功！详情如下：\033[0m\n%s\n%s\n%s\n%s' % (name, price, period, teacher))
                        c = Course(name, price, period, teacher)  # 将课程信息传入课程类
                        Certification().written_information('db/%s_choose_course_info.txt' % self.username,c)  # 将课程类写入文件
                        flag = False
                        break
                else:
                    print('选择的课程不存在哦！请重新选择：')


    def view_selected_courses(self):
        '''查看所选课程'''
        if not os.path.exists(db_path + '/%s_choose_course_info.txt' % self.username): return print('您还未选择任何课程哦！')
        print('*' * 25 + '\n\033[31;1m%s所选课程信息如下：\033[0m' % self.username)
        ret = Certification().read_information('db/%s_choose_course_info.txt' % self.username)
        for k, v in ret:print(v) # 打印课程信息


    def student_view(self):
        '''学生界面'''
        while True:
            print('*' * 25 + '\n1、查看可选课程\n2、选择课程\n3、查看已选课程\n4、退出\n' + '*' * 25)
            choose = input('请选择：').strip()
            if '1' == choose: # 查看可选课程
                self.view_optional_courses()
            elif '2' == choose: # 选择课程
                self.choose_course()
            elif '3' == choose: # 查看已选课程
                self.view_selected_courses()
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
        while True:
            username = '*' * 25 + '\n姓名：' + input('please input the student`s username:').strip()
            ret = Certification().read_information('db/student_info.txt')
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
                s = Students(username, password, age, sex, phone) # 将信息传入学生类
                Certification().written_information('db/student_info.txt', s)  # 将学生类写入文件
                break

    def view_all_students(self):
        '''查看所有学生'''
        if not os.path.exists(db_path + '/student_info.txt'): return print('还未添加任何学生账号哦！')
        print('*' * 25 + '\n\033[31;1m所有学生信息如下：\033[0m')
        ret = Certification().read_information('db/student_info.txt')
        for k, v in ret:print(v) # 打印学生账号信息


    def create_course(self):
        '''创建课程'''
        while True:
            name = '*' * 25 + '\n课程名称：' + input('please input the course`s name:').strip()
            ret = Certification().read_information('db/course_info.txt')
            for k, v in ret: # 校验课程是否已存在，避免重复创建课程。
                if name in v:
                    print('\033[31;1m%s课程已存在！！\033[0m' % name.split('：')[-1])
                    break
            else:
                price = '课程价格：' + input('please input the course`s price:').strip()
                period = '课程周期：' + input('please input the period:').strip()
                teacher = '授课老师：' + input('please input the teacher`s name:').strip()
                print("*" * 25 + '\n\033[31;1m创建课程成功！信息如下：\033[0m\n%s\n%s\n%s\n%s' % (name, price, period, teacher))
                c = Course(name, price, period, teacher)  # 将课程信息传入课程类
                Certification().written_information('db/course_info.txt', c)  # 将课程类写入文件
                break

    def view_all_courses(self):
        '''查看所有课程'''
        if not os.path.exists(db_path + '/course_info.txt'): return print('还未添加任何课程哦！')
        print('*' * 25 + '\n\033[31;1m所有课程信息如下：\033[0m')
        ret = Certification().read_information('db/course_info.txt')
        for k, v in ret:print(v) # 打印所有课程信息

    def view_all_selected_courses(self):
        '''查看所有学生的选课情况'''
        flag = True
        for file_name in os.listdir(db_path): # 获取所有的学生选课信息文件
            if 'choose_course_info' in file_name:
                print('*' * 25 + '\n\033[31;1m%s所选课程信息如下：\033[0m' % file_name.split('_')[0])
                ret = Certification().read_information('db/%s' % file_name)
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
    admin_dict = {'admin': 'admin', 'xiaoqiang': '123'}
    print("#" * 25 + '\n欢迎来到luffycity选课系统！\n' + "#" * 25)
    ret = Certification().login() # 登录校验
    if ret in admin_dict:
        a = Admin(ret)
        a.admin_view() # 管理员视图
    elif ret:
        s = Students(ret[0], ret[1], ret[2], ret[3], ret[4])
        s.student_view() # 学生视图


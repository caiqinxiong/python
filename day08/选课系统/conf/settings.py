# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/8/28 10:37
import os
import time

# 当前文件工作目录绝对路径
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# 数据存储路径
db_path = os.path.join(BASE_DIR, 'db')
if not os.path.exists(db_path):os.makedirs(db_path)

# 学生账号信息文件
student_file = r'%s/student_info' % db_path

# 课程信息文件
course_file = r'%s/course_info' % db_path

# 学生选课信息存储路径
def choose_course_path(name):
    path = os.path.join(db_path,'choose_course',name)
    if not os.path.exists(path):os.makedirs(path)
    return path

# 学生选课信息文件，函数：传入学生姓名。
choose_course_file = lambda name: r'%s/choose_course_info' % (choose_course_path(name))

# 日志文件路径
log_path = os.path.join(BASE_DIR,'log')
if not os.path.exists(log_path):os.makedirs(log_path)
log_file = r'%s/%s-log' % (log_path,time.strftime('%Y-%m-%d', time.localtime(time.time())))
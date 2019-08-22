# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/8/21 10:40
import os
# 管理员账号密码信息
admin_dict = {'admin': 'admin', 'xiaoqiang': '123'}

# 当前文件工作目录绝对路径
work_path = os.getcwd()

# 数据存储路径
db_path = os.path.join(work_path, '../db')
if not os.path.exists(db_path):os.makedirs(db_path)

# 学生账号信息文件
student_file = r'%s/student_info' % db_path

# 讲师账号信息文件
teacher_file = r'%s/teacher_info' % db_path

# 课程信息文件
course_file = r'%s/course_info' % db_path

# 学生选课信息文件，函数：传入学生姓名。
choose_course_path = os.path.join(db_path,'choose_course')
if not os.path.exists(choose_course_path):os.makedirs(choose_course_path)
choose_course_file = lambda name: r'%s/%s_choose_course_info' % (choose_course_path,name)

# 班级信息文件
classroom_path = os.path.join(db_path,'classroom')
if not os.path.exists(classroom_path):os.makedirs(classroom_path)
classroom_file = lambda  classname:r'%s/%s_classroom_info' % (classroom_path,classname)

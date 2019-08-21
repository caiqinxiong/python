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
# 学生账号信息文件
student_file = r'%s/student_info.txt' % db_path
# 课程信息文件
course_file = r'%s/course_info.txt' % db_path
# 学生选课信息文件，函数：传入学生姓名。
choose_course_file = lambda name: r'%s/%s_choose_course_info.txt' % (db_path,name)


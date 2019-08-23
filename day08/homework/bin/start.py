# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/8/21 14:25
import os
import sys
# 项目工作目录绝对路径
#BASE_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = os.path.dirname(os.getcwd())
sys.path.append(BASE_DIR) # 先添加当前工作路径，导入自定义模块时才能生效
from conf import settings as ss
from core import student as st
from core import teacher as tc
from core import certification as cc
from core import admin as ad

if __name__ == '__main__':
    print("#" * 25 + '\n欢迎来到luffycity选课系统！\n' + "#" * 25)
    ret = cc.Certification().login() # 登录校验，返回用户信息
    if ret in ss.admin_dict:
        ad.Admin(ret).admin_view() # 管理员视图
    elif ret:
        if ret[-1] == 'student':
            s = st.Students(ret[0], ret[1], ret[2], ret[3], ret[4])
            s.student_view() # 学生视图
        elif ret[-1] == 'teacher':
            t = tc.Teacher(ret[0], ret[1], ret[2], ret[3], ret[4])
            t.teacher_view() # 讲师视图

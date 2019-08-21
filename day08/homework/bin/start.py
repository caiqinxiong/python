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
from core import certification as cc
from core import admin as ad
if __name__ == '__main__':
    print("#" * 25 + '\n欢迎来到luffycity选课系统！\n' + "#" * 25)
    ret = cc.Certification().login() # 登录校验
    if ret in ss.admin_dict:
        a = ad.Admin(ret)
        a.admin_view() # 管理员视图
    elif ret:
        s = st.Students(ret[0], ret[1], ret[2], ret[3], ret[4])
        s.student_view() # 学生视图

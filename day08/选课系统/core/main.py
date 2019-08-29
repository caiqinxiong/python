# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/8/28 10:11
import sys
import time
from core.common import Common as cn
from core.log import Log as log
from conf import settings as ss
from core import student
from core import manager


def main():
    '''主逻辑函数'''
    log.debug('*' * 25 + '\n欢迎来到LuffyCity选课系统！\n' + '*' * 25)
    username = input('请输入用户名： ').strip()
    password = cn.changeHashlib(input('请输入密码：').strip())
    flag = False
    ident = None
    for k, v in cn.readInfo(ss.student_file):
        if username == k and password == v[1]:
            ident = v[-1]
            content = '%s用户%s登录成功！' % (ident, username)
            log.debug(content)
            log.info(content)
            flag = True
            break
    else:
        log.warning('%s用户登录失败！' % username)

    if flag:  # flag为真表示登录成功
        cls = getattr(sys.modules['core.%s' % ident.lower()], ident)
        obj = cls(username)
        while True:
            for index, opt in enumerate(cls.opt_lst, 1): print('\033[35;1m%s、%s\033[0m' % (index, opt[0]))
            try:
                num = int(input('请选择要操作的序号:'))
                getattr(obj, cls.opt_lst[num - 1][1])()
            except ValueError as e:
                log.error('%s不是效数字！！' % e)
            except IndexError as e:
                log.error('%s\n请输入有效数字！！' % e)
            log.debug('*' * 25 + '\n3秒后自动跳转回主页面！')
            time.sleep(3)

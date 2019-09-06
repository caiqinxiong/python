# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/9/2 15:20
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
from core.ftp_client import FtpClient as fc
from core.log import Log as log
from core.auth import Auth as at

def main():
    '''主逻辑'''
    head = '*' * 20 + '\n欢迎来到FTP系统！\n' + '*' * 20
    print('\033[35;1m%s\033[0m' % head)
    opt_list = [('登录','login'),('注册','register'),('退出','quit')]
    while True:
       for index,opt in enumerate(opt_list,1):print('\033[35;1m%s、%s\033[0m' % (index, opt[0])) # 打印操作列表信息
       try:
           num = int(input( '请输入您要选择的操作序号:'))
           if hasattr(at(),opt_list[num-1][1]):return getattr(at(),opt_list[num-1][1])() # 反射
       except ValueError as e:
           log.error('%s不是效数字！！' % e)
       except IndexError as e:
           log.error('%s\n请输入1-12的有效数字！！' % e)

if __name__ == '__main__':
    ret = main()
    if ret:fc(ret).clientView()



# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/9/2 15:25

import os,sys,json
from conf import settings as ss
class Users(object):
    '''
    用户类
    '''
    def __init__(self,username):
        self.username = username
        self.user_file = ss.USER_FILE + "\\%s.json"%(self.username)
        #print(self.user_file)
        self.users_read = self.read_users()

    def read_users(self):
        '''
        读取用户文件信息函数
        1、判断用户文件是否存在（用户是否存在）
        2、遍历用户json文件中内容
        3、返回遍历内容
        :return:
        '''
        if os.path.exists(self.user_file):
            with open(self.user_file, 'r') as f:
                user_read = eval(f.read())
                return user_read

    def get_user(self):
        '''
        1、判断服务端传过来的用户名参数是否与文件中用户名参数
        2、异常处理：用户名与用户文件参数类型不一直
        :return:
        '''
        #print('in the User_get_user:',user)
        try:
            if self.users_read["username"] == self.username:
                return self.users_read
        except TypeError as e:
            pass

    def update_status_close(self):
        '''
        修改用户登录状态函数
        0-未登录
        1-已登录
        无法重复登录
        :return:
        '''
        with open(self.user_file,'r') as f:
            fr = f.read()
            fd = eval(fr)

        with open(self.user_file,'w') as fw:
            res = fr.replace(str(fd['status']),str(1))
            fw.write(res)

    def update_status_open(self):
        '''
                修改用户登录状态函数
                0-未登录
                1-已登录
                无法重复登录
                :return:
                '''
        with open(self.user_file, 'r') as f:
            fr = f.read()
            fd = eval(fr)

        with open(self.user_file, 'w') as fw:
            res = fr.replace(str(fd['status']), str(0))
            fw.write(res)

    def update_disk_quota(self,new_disk_quota):
        '''
        更改用户磁盘配额函数
        :param new_disk_quota:接收客户端新磁盘配额参数
        :return:
        '''
        with open(self.user_file,'r') as f:
            fr = f.read()
            fd = eval(fr)

        with open(self.user_file,'w') as fw:
            res = fr.replace(str(fd["disk_quota"]),str(new_disk_quota))
            fw.write(res)

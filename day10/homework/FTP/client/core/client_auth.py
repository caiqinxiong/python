# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/9/2 10:33
import json
from core.log import Log as log
from core.client_common import Common as cn

class ClinetAuth:
    '''客户端认证类'''

    def __init__(self,conn):
        self.conn = conn
        self.auth_dict = {}

    def __auth(self,operate):
        '''身份认证'''
        for i in range(3):# 3次登录
            name = input('请输入用户名：').strip()
            password = input('请输入密码：').strip() # 为了安全起见，发送明文到服务器再加密，避免破解加密算法。
            if 'login' == operate:
                self.auth_dict = {'operate':'login','name':name,'password':password}
            elif 'register' == operate:
                password2 = input('请再次输入密码：').strip()
                if password == password2:
                    self.auth_dict = {'operate':'register','name':name,'password':password}
                else:
                    log.debug('两次输入密码不一致！')
                    continue
            cn.mySend(self.conn,self.auth_dict,True) # 将用户信息发送给服务器校验
            self.auth_dict = cn.myRecv(self.conn,True) # 接收服务器校验完成的结果
            log.readAndWrite(self.auth_dict['msg'])
            if self.auth_dict['flag']:break # 登录或注册成功了
        return self.auth_dict

    def login(self):
        '''登录'''
        return self.__auth('login')

    def register(self):
        '''注册'''
        return self.__auth('register')

    def quit(self):
        log.debug('谢谢使用！')
        cn.mySend(self.conn,b'exit')
        self.conn.close()
        exit(-1)

    def main(self):
        '''主逻辑'''
        head = '*' * 20 + '\n欢迎来到FTP系统！\n' + '*' * 20
        print('\033[35;1m%s\033[0m' % head)
        opt_list = [('登录','login'),('注册','register'),('退出','quit')]
        while True:
           for index,opt in enumerate(opt_list,1):print('\033[35;1m%s、%s\033[0m' % (index, opt[0])) # 打印操作列表信息
           try:
               num = int(input( '请输入您要选择的操作序号:'))
               if hasattr(self,opt_list[num-1][1]):return getattr(self,opt_list[num-1][1])() # 反射
           except ValueError as e:
               log.error('%s不是效数字！！' % e)
           except IndexError as e:
               log.error('%s\n请输入1-3的有效数字！！' % e)


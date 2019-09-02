# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/9/2 10:33
import os
import hashlib
from conf import settings as ss
from core.log import Log as log

class Auth:
    '''身份验证类'''

    def __init__(self):
        pass

    @staticmethod
    def writeInfo(file,content):
        '''写入信息'''
        with open(file,mode='a',encoding='utf-8') as f:
           f.write(content)

    @staticmethod
    def readInfo(file):
        '''读取信息'''
        if not os.path.exists(file):return False
        with open(file,mode='r',encoding='utf-8') as f:
            for line in f:
                usr, pwd = line.strip().split('|')
                yield usr, pwd

    @staticmethod
    def changeMD5(content,name):
        '''MD5加密'''
        md5 = hashlib.md5(('MD5加盐，加上用户%s' % name).encode('utf-8'))
        md5.update(content.encode('utf-8'))
        ret = md5.hexdigest()
        return ret


    def login(self):
        '''登录'''
        for i in range(3):
            name = input('请输入用户名：').strip()
            password = Auth.changeMD5(input('请输入密码：').strip(),name)
            for n,p in Auth.readInfo(ss.USER_FILE):
                if name == n and password == p:
                    log.readAndWrite('%s登录成功！')
                    return True
            else:
                log.readAndWrite('%s登录失败！')
        return False


    def register(self):
        '''注册'''
        for i in range(3):
            name = input('请输入用户名：').strip()
            for n,p in Auth.readInfo(ss.USER_FILE):
                if name == n:
                    log.warning('%s用户已存在！' % name)
                    break
            else:
                password = Auth.changeMD5(input('请输入密码：').strip(),name)
                content = name + '|' + password + '\n'
                Auth.writeInfo(ss.USER_FILE,content)
                log.readAndWrite('%s用户注册成功！' % name)
                return True
        return False

Auth().register()
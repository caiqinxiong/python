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
        if not os.path.exists(ss.USER_FILE):return
        with open(file,mode='r',encoding='utf-8') as f:
            for line in f:
                usr, pwd, quota= line.strip().split('|')
                yield usr, pwd, quota

    @staticmethod
    def changeMD5(content,name):
        '''MD5加密'''
        md5 = hashlib.md5(('MD5加盐，加上用户%s' % name).encode('utf-8'))
        md5.update(content.encode('utf-8'))
        return md5.hexdigest()

    def __auth(self,kind):
        '''身份认证'''
        for i in range(3):
            name = input('请输入用户名：').strip()
            password = Auth.changeMD5(input('请输入密码：').strip(),name)
            for n,p,q in Auth.readInfo(ss.USER_FILE):
                if kind == '登录' and name == n and password == p:
                    log.readAndWrite('%s%s成功！' %(name,kind))
                    return name
                elif kind == '注册' and name == n:
                    log.warning('%s用户已存在，请重新注册！' % name)
                    break
            else:
                if kind == '注册':
                    content = name + '|' + password + '|' + ss.QUOTA + '\n'
                    Auth.writeInfo(ss.USER_FILE,content)
                    log.readAndWrite('%s%s成功！' %(name,kind))
                    return name
            log.debug('%s%s失败！' % (name,kind))
        return False


    def login(self):
        '''登录'''
        return self.__auth('登录')

    def register(self):
        '''注册'''
        return self.__auth('注册')



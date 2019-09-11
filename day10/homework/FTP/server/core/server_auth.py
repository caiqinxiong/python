# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/9/2 10:33
import os
import hashlib
import json
from conf import settings as ss
from core.log import Log as log

class ServerAuth:
    '''服务器认证类'''

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


    @classmethod
    def auth(cls,opt_dict):
        '''身份认证'''
        opt_dict['password'] = cls.changeMD5(opt_dict['password'],opt_dict['name']) # 将密码转换成密文
        for n,p,q in cls.readInfo(ss.USER_FILE):
            if opt_dict['operate'] == 'login' and opt_dict['name'] == n and opt_dict['password'] == p:
                opt_dict['flag'] = True
                opt_dict['msg'] = '%s登录成功！' % opt_dict['name']
                break
            elif opt_dict['operate'] == 'register' and opt_dict['name'] == n:
                opt_dict['flag'] = False
                opt_dict['msg'] = '%s用户已存在，请重新注册！' % opt_dict['name']
                break
        else:
            if opt_dict['operate'] == 'register':
                content = opt_dict['name'] + '|' + opt_dict['password'] + '|' + ss.QUOTA + '\n'
                cls.writeInfo(ss.USER_FILE,content)
                opt_dict['flag'] = True
                opt_dict['msg'] = '%s注册成功！' % opt_dict['name']
            elif opt_dict['operate'] == 'login':
                opt_dict['flag'] = False
                opt_dict['msg'] = '%s登录失败！' % opt_dict['name']
        log.readAndWrite(opt_dict['msg'])
        opt_dict = json.dumps(opt_dict).encode('utf-8') # 将字典转换为字符串，再转换为二进制
        return opt_dict # 返回二进制的字典





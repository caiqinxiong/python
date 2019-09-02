# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/9/2 10:33
import os
import hashlib
import json
from conf import settings as ss
from core.log import Log as log

class Auth:
    '''身份验证类'''

    def __init__(self):
        pass

    @staticmethod
    def writeInfo(file,content):
        '''写入信息'''
        with open(ss.USER_FILE, mode='w', encoding='utf-8') as f :
            return json.dump(content , f , ensure_ascii=False, indent="\t")

    @staticmethod
    def readInfo(file):
        '''读取信息'''
        if not os.path.exists(file):return [('','','')]
        with open(ss.USER_FILE, mode='r', encoding="utf-8") as f:
                return json.load(f)


    @staticmethod
    def changeMD5(content,name):
        '''MD5加密'''
        md5 = hashlib.md5(('MD5加盐，加上用户%s' % name).encode('utf-8'))
        md5.update(content.encode('utf-8'))
        ret = md5.hexdigest()
        return ret


    def __auth(self,kind):
        '''身份认证'''
        for i in range(3):
            name = input('请输入用户名：').strip()
            password = Auth.changeMD5(input('请输入密码：').strip(),name)
            users_list = Auth.readInfo(ss.USER_FILE)
            # print(users_list)
            for user in users_list:
                print(user)
                if kind == '登录' and name == user[0] and password == user[1]:
                    log.readAndWrite('%s%s成功！' %(name,kind))
                    return True
                elif kind == '注册':
                    if name == user[0]:
                        log.warning('%s用户已存在，请重新注册！' % name)
                        break
                    users_list.append((name, password, ss.QUOTA))
                    print(users_list)
                    Auth.writeInfo(ss.USER_FILE,users_list)
                    log.readAndWrite('%s%s成功！' %(name,kind))
                    return True
            else:
                log.debug('%s%s失败！' % (name,kind))
        return False


    def login(self):
        '''登录'''
        self.__auth('登录')

    def register(self):
        '''注册'''
        self.__auth('注册')

    def main(self):
        '''主逻辑'''
        log.debug('*' * 20 + '\n欢迎来到FTP系统！\n' + '*' * 20 + '\n1、登录\n2、注册\nq、退出\n'  + '*' * 20 )
        while True:
            num = input('请选择：')
            if '1' == num:
                self.login()
                break
            elif '2' == num:
                self.register()
                break
            elif 'Q' == num.upper():
                log.debug('谢谢使用！')
                exit(-1)
            else:
                log.debug('输入有误，请重新输入！')

Auth().register()
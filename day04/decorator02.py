# -*- coding:utf-8 -*-
# Author:caiqinxiong
user = 'cai'
passwd = 'cai'
def auth(auth_type):
    def out_wraper(func):
        def wraper(*args,**kwargs):
           if auth_type == 'local':
                username = input('username:').strip()
                password = input('password:').strip()
                if username == user and password == passwd:
                    print('\033[32;1muser has passed authentication!\033[0m')
                    res = func(*args,**kwargs)
                    #print('####################')
                    return res
                else:
                    exit('\033[31Ivalid username or password!\033[0m')
           elif auth_type == 'ldap':
               print('@@@@@@@@@@不会ladp，不再输入密码验证@@@@@@@@@@@@')
        return wraper
    return out_wraper
def index():
    print('welcome to index page!')

@auth(auth_type='local')
def home():
    print('welcome to home page!')

@auth(auth_type='ldap')
def bbs():
    print('welcome to bbs page!')

index()
home()
bbs()
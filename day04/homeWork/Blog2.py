# -*- coding:utf-8 -*-
# caiqinxiong 
# 2019/7/29 下午11:01
from functools import wraps
import time
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
dict_info = {'login_status': False, 'username': None}


def get_user(file):
    with open(file, mode='r', encoding='utf-8') as f:
        for line in f:
            usr, pwd = line.strip().split('|')
            yield usr, pwd


def login(func):
    @wraps(func)
    def inner(*args, **kwargs):
        if dict_info['login_status'] == True:
            ret = func(*args, **kwargs)
            return ret
        else:
            for i in range(3):
                user = input('username :')
                passwd = input('password :')
                for usr, pwd in get_user('userinfo'):
                    if usr == user and pwd == passwd:
                        print('登录成功')
                        dict_info['login_status'] = True
                        dict_info['username'] = user
                        ret = func(*args, **kwargs)
                        return ret
                else:
                    print('账号或密码错误！')
            else:
                print('尝试登录次数已用完！')
                exit(-1)

    return inner


def log(func):
    @wraps(func)
    def inner(*args, **kwargs):
        ret = func(*args, **kwargs)
        DATE = time.strftime('%Y-%m-%d %H:%M:%S')
        with open(r'access.log', mode='a', encoding='utf-8') as f:
            log_conten = '用户[%s]在%s执行了%s函数\n' % (args[0], DATE, func.__name__)
            # print(log_conten)
            f.write(log_conten)
        return ret

    return inner
@login
@log
def articlePage(username):
    '''文章页面'''
    print('欢迎%s用户访问\033[31;1m文章\033[0m页面!' % username)
    return
@login
@log
def diaryPage(username):
    '''日记页面'''
    print('欢迎%s用户访问\033[31;1m日记\033[0m页面!' % username)
    return
@login
@log
def commentPage(username):
    '''评论页面'''
    print('欢迎%s用户访问\033[31;1m评论\033[0m页面!' % username)
    return

@login
@log
def collectionPage(username):
    '''收藏页面'''
    print('欢迎%s用户访问\033[31;1m收藏\033[0m页面!' % username)
    return


def menu():
    '''主菜单'''
    print('#' * 20)
    print('''欢迎来到博客园首页
1、登录博客园
2、注册新用户
3、文章页面
4、日记页面
5、评论页面
6、收藏页面
7、注销
8、退出程序''')
    print('#' * 20)
    while True:
        choise = input('请选择:').strip()
        if '1' == choise:
            @login
            def loginBlog():
                pass
            loginBlog()
        elif '2' == choise:
            pass
            #register(users)
        elif '3' == choise:
            articlePage(dict_info['username'])
        elif '4' == choise:
            diaryPage(dict_info['username'])
        elif '5' == choise:
            commentPage(dict_info['username'])
        elif '6' == choise:
            collectionPage(dict_info['username'])
        elif '7' == choise:
            print(''.center(15, '*'))
            print('注销成功，已退出登录！')
            dict_info['login_status'] = False
        elif '8' == choise:
            print('谢谢使用！')
            exit(-1)
        else:
            print('输入有误，请重新输入！')


if __name__ == '__main__':
    menu()

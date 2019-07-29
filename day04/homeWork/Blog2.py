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
            print('您已登录啦！')
            ret = func(*args, **kwargs)
            return ret
        else:
            for i in range(3):
                user = input('请输入登录名 :')
                passwd = input('请输入密码 :')
                for usr, pwd in get_user('userinfo'):
                    if usr == user and pwd == passwd:
                        print('#' * 20)
                        print('登录成功')
                        dict_info['login_status'] = True
                        dict_info['username'] = user
                        ret = func(*args, **kwargs)
                        return ret
                else:
                    print('账号或密码错误！')
            else:
                print('您的3次尝试机会已用完，是否注册新用户？Y/N')
                while True:
                    choise = input().strip().upper()
                    if 'Y' == choise:
                        register()
                        break
                    elif 'N' == choise:
                        print('谢谢使用！')
                        exit(-1)
                    else:
                        print('输入有误！')

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
def loginBlog():
    return printMenu()


def register():
    '''注册'''
    for i in range(3):
        user = input('请输入注册名 :')
        for usr, pwd in get_user('userinfo'):
            if usr != user:
                passwd = input('请输入密码 :')
                print('账户\033[42;1m%s\033[0m注册成功！' % user)
                dict_info['login_status'] = True
                dict_info['username'] = user
                with open('userinfo', mode='a', encoding='utf-8') as f:
                    f.write(user+'|'+passwd+'\n')
                printMenu()
        else:
            print('用户名已存在！')
    else:
        print('尝试次数已用完！')
        exit(-1)
@login
@log
def articlePage(username):
    '''文章页面'''
    print('欢迎%s用户访问\033[31;1m文章\033[0m页面!' % username)
    return printMenu()


@login
@log
def diaryPage(username):
    '''日记页面'''
    print('欢迎%s用户访问\033[31;1m日记\033[0m页面!' % username)
    return printMenu()


@login
@log
def commentPage(username):
    '''评论页面'''
    print('欢迎%s用户访问\033[31;1m评论\033[0m页面!' % username)
    return printMenu()


@login
@log
def collectionPage(username):
    '''收藏页面'''
    print('欢迎%s用户访问\033[31;1m收藏\033[0m页面!' % username)
    return printMenu()

def printMenu():
    '''打印主菜单'''
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

def menu():
    '''主菜单'''
    while True:
        choise = input('请选择:').strip()
        if '1' == choise:
            loginBlog()
        elif '2' == choise:
            register()
        elif '3' == choise:
            articlePage(dict_info['username'])
        elif '4' == choise:
            diaryPage(dict_info['username'])
        elif '5' == choise:
            commentPage(dict_info['username'])
        elif '6' == choise:
            collectionPage(dict_info['username'])
        elif '7' == choise:
            print('#' * 20)
            print('注销成功，已退出登录！')
            dict_info['login_status'] = False
            printMenu()
        elif '8' == choise:
            print('谢谢使用！')
            exit(-1)
        else:
            print('输入有误，请重新输入！')


if __name__ == '__main__':
    printMenu()
    menu()

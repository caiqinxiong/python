# -*- coding:utf-8 -*-
# caiqinxiong 
# 2019/7/28 下午8:34
from functools import wraps
import time
import json
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)


def getUser():
    '''获取账户信息'''
    try:
        with open(r'register.txt', mode="r", encoding="utf-8") as f:
            users = json.load(f)
            # print(users)
    except:
        print('have no users inof!')
        users = {}
    return users


def setUser(users):
    '''写入用户信息'''
    with open(r'register.txt', mode='w') as f:
        json.dump(users, f, indent="\t")
        # print(users)


def checkUser(users, username):
    '''检查用户是否存在'''
    if username in users:
        return True
    return False


def checkPassword(users, username, password):
    '''校验密码是否正确'''
    if password == users[username]:
        return True
    else:
        return False


def login(users, login_status):
    '''登录'''
    if login_status:
        return login_status
    i = 3
    while i > 0:
        i -= 1
        username = input('请输入用户名：')
        if checkUser(users, username):
            j = 3
            while j > 0:
                j -= 1
                password = input('请输入密码：')
                if checkPassword(users, username, password):
                    print('登录成功！')
                    printPage(username)
                else:
                    print('密码输入有误！')
                    if j == 0:
                        print('登录失败，谢谢使用！')
                        exit(-1)
                    else:
                        print('你还有%s次尝试机会！' % j)
        else:
            print('用户名不存在！')
            if i != 0:
                print('你还有%s次尝试机会！' % i)
            else:
                print('您的尝试机会已用完，是否注册新用户？Y/N')
                while True:
                    choise = input().strip().upper()
                    if 'Y' == choise:
                        register(users)
                        break
                    elif 'N' == choise:
                        print('谢谢使用！')
                        exit(-1)
                    else:
                        print('输入有误！')


def register(users):
    '''注册 '''
    i = 3
    while i > 0:
        i -= 1
        username = input('请输入注册的用户名：')
        if checkUser(users, username):
            print('用户名已存在！')
            if i != 0:
                print('请重新输入，你还有%s次尝试机会！' % i)
            else:
                print('您的尝试次数已用完！')
        else:
            j = 3
            while j > 0:
                j -= 1
                password1 = input('请输入密码：')
                password2 = input('请再次输入密码：')
                if password1 == password2:
                    print('账户\033[42;1m%s\033[0m注册成功！' % username)
                    users[username] = password1
                    setUser(users)
                    users = getUser()
                    return menu(users, username, login_status=True)
                else:
                    print('两次输入密码不一致！')
                    if j == 0:
                        print('操作过于频繁，请5分钟后再次尝试！')
                        time.sleep(300)
                    else:
                        print('你还有%s次尝试机会！' % j)


def log(func):
    @wraps(func)
    def inner(*args, **kwargs):
        ret = func(*args, **kwargs)
        # DATE = time.strftime('%Y-%m-%d %H:%M:%S')
        cc = time.localtime(time.time())
        DATE = str(cc.tm_year) + '年' + str(cc.tm_mon) + '月' + str(cc.tm_mday) + '日'
        with open(r'access.log', mode='a', encoding='utf-8') as f:
            log_conten = '用户[%s]在%s执行了%s函数\n' % (args[0], DATE, func.__name__)
            # print(log_conten)
            f.write(log_conten)
        return ret

    return inner


@log
def articlePage(username, login_status):
    '''文章页面'''
    print('欢迎%s用户访问\033[31;1m文章\033[0m页面!' % username)
    return


@log
def diaryPage(username, login_status):
    '''日记页面'''
    print('欢迎%s用户访问\033[31;1m日记\033[0m页面!' % username)
    return


@log
def commentPage(username, login_status):
    '''评论页面'''
    print('欢迎%s用户访问\033[31;1m评论\033[0m页面!' % username)
    return


@log
def collectionPage(username, login_status):
    '''收藏页面'''
    print('欢迎%s用户访问\033[31;1m收藏\033[0m页面!' % username)
    return


def turnBack(username, login_status):
    '''返回上级菜单'''
    print(''.center(15, '*'))
    print("1、返回上级")
    print("2、退出")
    print(''.center(15, '*'))
    while True:
        choise = input("请选择：")
        if choise == '1':
            menu(users, username, login_status)
            break
        elif choise == '2':
            print("谢谢使用！")
            exit(-1)
        else:
            print("输入有误，请重新输入！")


def printPage(username):
    '''打印访问页面'''
    print('#' * 20)
    print('3、文章页面')
    print('4、日记页面')
    print('5、评论页面')
    print('6、收藏页面')
    print('#' * 20)
    while True:
        choise = input('请选择：').strip()
        if '3' == choise or '4' == choise or '5' == choise or '6' == choise:
            return accessPage(username, choise, login_status=True)
        else:
            print('输入有误！')


def accessPage(username, choise, login_status):
    '''访问页面逻辑控制'''
    if '3' == choise:
        articlePage(username, login_status)
    elif '4' == choise:
        diaryPage(username, login_status)
    elif '5' == choise:
        commentPage(username, login_status)
    elif '6' == choise:
        collectionPage(username, login_status)
    else:
        print('输入有误！，请重新输入！')

    return turnBack(username, login_status)


def menu(users, username='', login_status=False):
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
            if login_status:
                print('用户已登录，请重新选择！')
            else:
                login(users, login_status)
        elif '2' == choise:
            register(users)
        elif '3' == choise or '4' == choise or '5' == choise or '6' == choise:
            if login_status:
                accessPage(username, choise, login_status)
            else:
                print('请登录后访问！')
                login(users, login_status)
        elif '7' == choise:
            print(''.center(15, '*'))
            print('注销成功，已退出登录！')
            login_status = False
            turnBack(username, login_status)
        elif '8' == choise:
            print('谢谢使用！')
            exit(-1)
        else:
            print('输入有误，请重新输入！')


if __name__ == '__main__':
    users = getUser()
    menu(users)

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
        with open(r'userinfo.txt', mode="r", encoding="utf-8") as f:
            users = json.load(f)
            # print(users)
    except:
        print('have no users inof!')
        users = {}
    return users


def setUser(users):
    '''重新写入账户信息'''
    with open(r'userinfo.txt', mode='w') as f:
        json.dump(users, f, indent="\t")
        # print(users)


def checkUser(users, username):
    '''检查用户是否存在'''
    for userID in users.keys():
        if username == users[userID]['username']:
            # print('账户名已存在！')
            return True
    return False


def loggin(user_info):
    '''
    登录
    :param user_info: 
    :return: 
    '''

    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            i = 3
            while i > 0:
                i -= 1
                username = input('请输入用户名：')
                if username in user_info:
                    j = 3
                    while j > 0:
                        j -= 1
                        password = input('请输入密码：')
                        if password == user_info[username]:
                            ret = func(*args, **kwargs)
                            return ret
                        else:
                            print('密码输入有误！')
                            if j == 0:
                                print('您的尝试机会已用完，账号已锁定，请10分钟后重新尝试！')
                                time.sleep(600)
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
                                register(user_info)
                                break
                            elif 'N' == choise:
                                print('谢谢使用！')
                                exit(-1)
                            else:
                                print('输入有误！')

        return inner

    return wrapper


def register(user_info):
    '''
    注册
    :param user_info: 
    :return: 
    '''
    i = 3
    while i > 0:
        i -= 1
        username = input('请输入用户名：')
        if username in user_info:
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
                    print('注册成功,是否登录？Y/N')
                    user_info[username] = password1
                    f = open('userinfo.txt', 'a')
                    f.write(username + '|' + password1 + '\n')
                    f.close()
                    while True:
                        choise = input().strip().upper()
                        if 'Y' == choise:
                            loggin(user_info)
                            break
                        elif 'N' == choise:
                            print('谢谢使用！')
                            exit(-1)
                        else:
                            print('输入有误！')

                else:
                    print('两次输入密码不一致！')
                    if j == 0:
                        print('操作过于频繁，谢谢使用！')
                        exit(-1)
                    else:
                        print('你还有%s次尝试机会！' % j)


def turnBack():
    '''返回上级菜单'''
    print(''.center(15, '*'))
    print("1、返回上级")
    print("2、退出")
    print(''.center(15, '*'))
    while True:
        choise = input("请选择：")
        if choise == '1':
            menu()
        elif choise == '2':
            print("谢谢使用！")
            exit(-1)
        else:
            print("输入有误，请重新输入！")


def menu():
    '''
    主菜单
    :return: 
    '''
    print('''
欢迎来到博客园首页
1、登录博客园
2、注册新用户
3、文章页面
4、日记页面
5、评论页面
6、收藏页面
7、注销
8、退出程序
    ''')
    while True:
        choise = input().strip()
        if '1' == choise:
            pass
        elif '2' == choise:
            pass
        elif '3' == choise:
            pass
        elif '4' == choise:
            pass
        elif '5' == choise:
            pass
        elif '6' == choise:
            pass
        elif '7' == choise:
            pass
        elif '8' == choise:
            print('谢谢使用！')
            exit(-1)
        else:
            print('输入有误，请重新输入！')


if __name__ == '__main__':
    users = getUser()
    turnBack()

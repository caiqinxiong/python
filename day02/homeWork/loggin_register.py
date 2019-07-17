# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong'
# 2019/7/17 22:30
# 用户信息
user_info = {'caiqinxiong': 'cai', 'lixiaoxin': '123'}


def loggin(user_info):
    '''登录'''
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
                    print('welcom to old boy!!!')
                    exit(-1)
                else:
                    print('密码输入有误！')
                    if j == 0:
                        print('您的尝试机会已用完，账号已锁定，请10分钟后重新尝试！')
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
                        register(user_info)
                        break
                    elif 'N' == choise:
                        print('谢谢使用！')
                        exit(-1)
                    else:
                        print('输入有误！')



def register(user_info):
    '''注册'''
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


def menu():
    '''首页'''
    print('欢迎登录oldBoy官网！')
    print('1、登录')
    print('2、注册')
    while True:
        choise = input('请选择：').strip()
        if '1' == choise:
            loggin(user_info)
            break
        elif '2' == choise:
            register(user_info)
            break
        else:
            print('输入有误！')


if __name__ == '__main__':
    menu()

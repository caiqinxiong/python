#!/usr/bin/python
# coding:utf-8
# CreateTime: 2019-08-02

import time


# 记录是否退出
flag = True
# 记录登录状态和用户名
status_dic = {
    'user': '',
    'status': False,
}


def wapper(funcname):
    # @wraps(funcname)
    def inner(*args, **kwargs):
        if status_dic['status']:
            ret = funcname(*args, **kwargs)
            return ret
        else:
            print('访问此页面，您需要先登录')
            if login():
                ret = funcname(*args, **kwargs)
                return ret

    return inner

def log(funcname):
    '''每次进入子页面前，记录登录日志'''
    # @wraps(funcname)
    def inner(*args, **kwargs):
        now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        with open('log_func.txt','a',encoding='utf-8') as f:
            f.write("用户:%s 在 %s 执行了 %s函数\n"%(status_dic['user'], now_time, funcname.__name__))
        ret = funcname(*args, **kwargs)
        return ret
    return inner

def login(*args, **kwargs):
    '''登录函数,三次登录
    status_dic['user']：记录登录的用户
    status_dic['status']： 记录登录状态
    '''
    print('欢迎进入登录界面')
    count = 0
    while count < 3:
        with open('register', mode='r', encoding='utf-8') as f:
            input_usr = input('用户名:').strip()
            input_pwd = input('密码:').strip()
            for line in f:
                if line:
                    usr, pwd = line.strip().split('|')
                    if input_usr == usr and input_pwd == pwd:
                        print('登录成功')
                        status_dic['user'] = usr  # 登录完成记录登录的用户名
                        status_dic['status'] = True
                        return True
        count += 1

def register(*args, **kwargs):
    ''' 注册功能，如果成功注册，则改变登录状态是已完成'''
    while True:
        input_usr = input('请输入要注册的用户名(b退出):').strip()
        if input_usr.upper() == 'B':
            return
        f  = open('register', mode='r', encoding='utf-8')
        for line in f:
            if line:
                usr, pwd = line.strip().split('|')
                if input_usr in usr:
                    print('用户名已存在，请重新输入')
                    f.close()
                    break
        else:
            f.close()
            input_pwd = input('请输入要注册的密码:').strip()
            with open('register', mode='a', encoding='utf-8') as f:
                f.write('%s|%s\n'%(input_usr,input_pwd))
            print('恭喜您注册成功，已自动登录')
            status_dic['user'] = input_usr
            status_dic['status'] = True
            return True



@wapper
@log
def article():
    '''文章页面'''
    print('欢迎%s用户访问文章页面'%status_dic['user'])


@wapper
@log
def diary():
    '''日记页面'''
    print('欢迎%s用户访问日记页面'%status_dic['user'])


@wapper
@log
def comments():
    '''评论页面'''
    print('欢迎%s用户访问评论页面'%status_dic['user'])


@wapper
@log
def collection():
    '''收藏页面'''
    print('欢迎%s用户访问收藏页面'%status_dic['user'])

def login_out():
    '''注销'''
    status_dic['user'] = None
    status_dic['status'] = False
    print('注销成功')

def Quit():
    '''退出'''
    global flag
    flag = False
    return flag

menu_dic = {
    1: login,
    2: register,
    3: article,
    4: diary,
    5: comments,
    6: collection,
    7: login_out,
    8: Quit
}

while flag:
    print("欢迎来到博客园首页\n1:请登录\n2:请注册\n3:文章页面\n4:日记页面\n5:评论页面\n6:收藏页面\n7:注销\n8:退出程序")
    choice = input('请选择菜单:').strip()
    if choice.isdigit():
        choice = int(choice)
        if choice in menu_dic:
            menu_dic[choice]()
        else:
            print('输入指令不正确')
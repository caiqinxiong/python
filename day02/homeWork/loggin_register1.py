# -*- coding: utf-8 -*-

def getUser():
    '''获取用户名信息'''
    user_list = []
    try:
        f = open('user.txt', 'r',encoding='utf-8')
        users = f.readlines()
        for user in users:
            user_list.append(user.split())
    except:
        print("用户信息文件未存在！")
        user_list = []
    return dict(user_list)


def login():
    '''登录'''
    user = getUser()
    name = input("please input your name:")
    if name in user:
        for j in range (1,4):
            password = input("please input your pass:")
            if password == user[name]:
                print('登录成功！！！')
                return True

            else:
                print ("password error!!!")
                num = 3 - j
                print ("you have %d change!" % num )

    else:
        print ("用户名 %s 不存在!!" % name)
        reg = input('''请选择：
    重新尝试 输入 1
    注册新用户 输入 2
    退出 输入其他任意字符\n''')
        if reg == '2':
            register()
        elif reg == "1":
            login()
        else:
            print('goodbye!!')

    return False



def register():
    '''注册'''
    user = getUser()
    for i in range(3):
        name = input("please input your name:")
        if name in user:
            print("用户名已存在！！")
            continue
        passwd1 = input("please input your password!")
        passwd2 = input("please input your password again!")
        if passwd1 == passwd2:
            print("注册成功! ")
            f = open('user.txt','a')
            f.write(name + ' ' + passwd1 + '\n')
            f.close()
            break
        else:
            print("输入的密码不一致，请重新输入！")
    else:
        print("操作过于频繁，请稍后再试！")


if __name__ == '__main__':
    print('欢迎登录XXX系统！')
    login()
# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong'
# 2019/7/9 17:22
my_name = 'caiqinxiong'
my_password = 'cai'
i = 2
while i >= 0:
    username = input('请输入用户名：')
    if username == my_name:
        j = 2
        while j >= 0:
            password = input('请输入密码：')
            if password == my_password:
                print('welcom!!')
                exit(-1)
            else:
                print('密码输入有误！')
                if j == 0:
                    print('账号已锁定，请10分钟后重新尝试！')
                    break
                else:
                    print('你还有%s次尝试机会！' % j)
            j -= 1

    else:
        print('账号输入有误！')
        if i != 0:
            print('你还有%s次尝试机会！' % i)
        else:
            print('账号已锁定，请10分钟后重新尝试！')
    i -= 1
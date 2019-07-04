# -*- coding:utf-8 -*-
# Author:caiqinxiong
import getpass

__users = []
__lock_users = []

#按行读取用户名，并存入list中
with open('users.txt', 'r') as u:
    for line in u.readlines():
        __users = line.strip().split('\t')
        print ("users:",__users)
u.close()
p = open('password.txt','r')
for line in p.readlines():
    __password = line.strip().split('\t')
    #print(__password)
p.close()

with open('lock_user.txt', 'r') as u:
    for line in u.readlines():
        __lock_users = line.strip().split('\t')
        print ("lock_users:",__lock_users)
u.close()

username = input("please input username:")
if not username in  __lock_users:
    if username in __users:
        for i in range(3):
            #password = getpass.getpass("please input password:")
            password = input("please input password:")
            if __password[__password.index(username)] == password:
                print("welcome to login!")
                break
            else:
                print("password input error,please try again!\n")
            if i == 2:
                l = open('lock_user.txt','a+')
                l.write(username + '\t')
                l.close()
    else:
        print("username is not exist!")
else:

    print("username was already locked,Please contact with the administrator！")


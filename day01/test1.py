# -*- coding:utf-8 -*-
# Author:caiqinxiong

import getpass

'''
print "Hello World!!"
name = "caiqinxiong"
name2 = name
name = "cai"
print name ,name2
'''
#name = raw_input("aa:")
#print name
#print ("哈哈")
#print("哈哈哈哈")
__username = "caiqinxiong"
__password = "cai"
username = input("yourname:")
password = getpass.getpass("password:")
print(username,password )
if __username == username and __password == password:
    print("Welcome user {name} login...".format(name=username))
else:
    print("username or password error!!")
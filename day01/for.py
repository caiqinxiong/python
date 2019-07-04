# -*- coding:utf-8 -*-
# Author:caiqinxiong

for i in range(5,10,2):#打印5到10，跳2个打印
    print (i)

for i in range(10):
    print("#")
    for j in range(10):
        if i > 5:
            continue
        print("@")
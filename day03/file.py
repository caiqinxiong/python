# -*- coding:utf-8 -*-
# Author:caiqinxiong
#date = open("shooping_list.txt").read()
#print(date)
f = open('shooping_list.txt','r')
for i in range(5):
    print(f.readline())
#当前光标位置
print(f.tell())
#将光标移动到0
print(f.seek(0))
print(f.tell())

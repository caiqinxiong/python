# -*- coding:utf-8 -*-
# caiqinxiong 
# 2019/7/7 下午2:28
'''
cout = 1
while True:
    print(''.center(cout,'*'))
    cout +=1
    if cout > 5:
        break
cout = 4
while True:
    print(''.center(cout,'*'))
    cout -=1
    if cout == 0:
        break
'''
i = 1
while True:
    print(''.center(i,'*'))
    i +=1
    if i > 5:
        j = 4
        while True:
            print(''.center(j, '*'))
            j -=1
            if j == 0:
                exit(-1)

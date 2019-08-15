# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/8/12 14:57
import os
import time
def chengeChar(path):
    '''处理乱码'''
    print(path)
    file_name = os.path.split(path)[-1]
    file_path = os.path.split(path)[0]
    print('@'*20)
    print(file_name)
    print('@'*20)
    try:
        new_name = file_name.encode('cp437').decode('gbk')
    except:
        new_name = file_name.encode('utf-8').decode('utf-8')
    print('#'*20)
    print(new_name)
    print('#'*20)
    # time.sleep(2)
    path2 = os.path.join(file_path,new_name)
    try:
        os.renames(path, path2)
    except:
        print('error')
    return path2

def main(path):
    '''遍历所有文件'''
    if os.path.isfile(path):
        chengeChar(path)
    elif os.path.isdir(path):
        for i in os.listdir(path):
            file_path = os.path.join(path, i)
            chengeChar(file_path)
            main(file_path)
    else:
        print('the path is not exist!')


if __name__ == '__main__':
    path = r'C:\Users\ES-IT-PC-193\Desktop\aa\A'
    main(path)



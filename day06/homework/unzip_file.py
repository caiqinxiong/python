# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/8/13 14:57
import zipfile
import rarfile
import time
import os
import chardet

def chengeChar_old(path):
    '''处理乱码'''
    print(3333333333333333333)
    print(path)
    if not os.path.exists(path):
        return path
    # time.sleep(5)
    # encode = chardet.detect(path)
    # str_encode = encode['encoding']
    # print(str_encode)
    try:
        path2 = path.encode('cp437').decode('gbk')
    except:
        path2 = path.encode('utf-8').decode('utf-8')
    print(path2)
    os.renames(path, path2)
    return path2

def chengeChar(path):
    '''处理乱码'''
    file_name = os.path.split(path)[-1]
    file_path = os.path.split(path)[0]
    # if not os.path.exists(path):
    #     return path
    # time.sleep(5)
    # encode = chardet.detect(path)
    # str_encode = encode['encoding']
    # print(str_encode)
    try:
        new_name = file_name.encode('cp437').decode('gbk')
    except:
        new_name = file_name.encode('utf-8').decode('utf-8')
    # time.sleep(2)
    path2 = os.path.join(file_path,new_name)
    try:
        os.renames(path, path2)
    except:
        print('error')
    return path2

def unzip_file(path):
    '''解压zip包'''
    path = chengeChar(path)
    if os.path.exists(path):
        if path.endswith('.zip'):
            print(111111111111111)
            z = zipfile.ZipFile(path, 'r')
            unzip_path = os.path.split(path)[0]
            z.extractall(path=unzip_path)
            zip_list = z.namelist() # 返回解压后的所有文件夹和文件
            for zip_file in zip_list:
                path = os.path.join(unzip_path,zip_file)
                # path = chengeChar(path)
                if os.path.exists(path):unzip_file(path)
            z.close()
        elif os.path.isdir(path):
            print(2222222222222222)
            for file_name in os.listdir(path):
                path = os.path.join(path, file_name)
                # path = chengeChar(path)
                if os.path.exists(path):unzip_file(path)
        else:
            print(path)
    else:
        print('the path is not exist!!!')

if __name__ == '__main__':
    zip_path = r'C:\Users\ES-IT-PC-193\Desktop\aa\A.zip'
    # zip_path = r'C:\Users\ES-IT-PC-193\Desktop\aa\蔡亲雄_day06_homework.zip'
    unzip_file(zip_path)




# zip_path = r'C:\Users\ES-IT-PC-193\Desktop\homework.rar'
#
# z = rarfile.RarFile(zip_path)
# z.extractall(path=r'C:\Users\ES-IT-PC-193\Desktop')
# z.close()
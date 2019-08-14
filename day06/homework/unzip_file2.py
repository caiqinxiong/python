# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/8/13 14:57
import zipfile
import rarfile
import os
import sys
import shutil

def unzip_file(path):
    '''解压zip包'''
    if os.path.exists(path):
        if path.endswith('.zip'):
            print(111111111)
            z = zipfile.ZipFile(path, 'r')
            unzip_path = os.path.split(path)[0]
            z.extractall(path=unzip_path)
            zip_list = z.namelist() # 返回解压后的所有文件夹和文件
            print(len(zip_list))
            print(zip_list)
            for zip_file in zip_list:
                print(zip_file)
                print(zip_file.encode('utf-8'))
                try:
                    zip_file2 = zip_file.encode('cp437').decode('gbk')
                except:
                    zip_file2 = zip_file.encode('utf-8').decode('utf-8')
                print(zip_file2)
                print(os.path.join(unzip_path,zip_file))
                print(os.path.join(unzip_path,zip_file2))
                old_path = os.path.join(unzip_path,zip_file)
                new_path = os.path.join(unzip_path,zip_file2)
                if os.path.exists(old_path):
                    try:
                        os.renames(old_path, new_path)
                    except:
                        print('文件已存在！',old_path)
                        if os.path.isdir(old_path):
                            shutil.rmtree(old_path)
                        else:
                            os.remove(old_path)

                    unzip_file(new_path)
            z.close()
        elif os.path.isdir(path):
            print(2222222)
            for file_name in os.listdir(path):
                unzip_file(os.path.join(path, file_name))
    else:
        print('the path is not exist!!!')


if __name__ == '__main__':
    zip_path = r'C:\Users\ES-IT-PC-193\Desktop\aa\A.zip'
    zip_path = r'C:\Users\ES-IT-PC-193\Desktop\aa\蔡亲雄_day06_homework.zip'
    unzip_file(zip_path)




# zip_path = r'C:\Users\ES-IT-PC-193\Desktop\homework.rar'
#
# z = rarfile.RarFile(zip_path)
# z.extractall(path=r'C:\Users\ES-IT-PC-193\Desktop')
# z.close()
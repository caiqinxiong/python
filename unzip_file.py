# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/8/13 14:57
import zipfile
import rarfile
import os
import sys


def chengeChar(path):
    '''处理乱码'''
    if not os.path.exists(path): return path
    path = path.rstrip('/').rstrip('\\')  # 去除路径最右边的/
    file_name = os.path.split(path)[-1]  # 获取最后一段字符，准备转换
    file_path = os.path.split(path)[0]  # 获取前面的路径，为rename做准备
    try:  # 将最后一段有乱码的字符串转换，尝试过整个路径转换，不生效，估计是无法获取整个路径的编码格式吧。
        new_name = file_name.encode('cp437').decode('gbk')
    except:  # 先转换成Unicode再转换回gbk或utf-8
        new_name = file_name.encode('utf-8').decode('utf-8')
    path2 = os.path.join(file_path, new_name)  # 将转换完成的字符串组合成新的路径
    try:
        os.renames(path, path2)  # 重命名文件
    except:
        print('renames error！！')
    return path2


def del_zip(path):
    '''删除解压出来的zip包'''
    path = chengeChar(path)
    if path.endswith('.zip') or path.endswith('.rar'):
        os.remove(path)
    elif os.path.isdir(path):
        for i in os.listdir(path):
            file_path = os.path.join(path, i)
            del_zip(file_path)  # 递归调用，先把所有的文件删除


def unzip_file(z, unzip_path):
    '''解压zip包'''
    z.extractall(path=unzip_path)
    zip_list = z.namelist()  # 返回解压后的所有文件夹和文件list
    z.close()
    for zip_file in zip_list:
        path = os.path.join(unzip_path, zip_file)
        if os.path.exists(path): main(path)


def main(path):
    '''主逻辑函数'''
    path = chengeChar(path)
    if os.path.exists(path):
        unzip_path = os.path.splitext(path)[0]  # 解压至当前目录
        if path.endswith('.zip') and zipfile.is_zipfile(path):
            z = zipfile.ZipFile(path, 'r')
            unzip_file(z, unzip_path)
        elif path.endswith('.rar'):
            r = rarfile.RarFile(path)
            unzip_file(r, unzip_path)
        elif os.path.isdir(path):
            for file_name in os.listdir(path):
                path = os.path.join(path, file_name)
                if os.path.exists(path): main(path)
        else:
            print(path)
    else:
        print('the path is not exist!!!')
        print(path)


if __name__ == '__main__':
    #zip_path = r'C:\Users\ES-IT-PC-193\Desktop\aa\HighLevel\HighLevel'
    zip_path = r'/Users/caiqinxiong/Desktop/HighLevel.zip'
    # zip_path = sys.argv[1]  # 接收传入的路径参数
    if os.path.isdir(zip_path):
        for file_name in os.listdir(zip_path):
            path = os.path.join(zip_path, file_name)
            main(path)
    else:
        main(zip_path)
    if zipfile.is_zipfile(zip_path):  # 删除解压出来的压缩包
        del_zip(os.path.splitext(zip_path)[0]) # 以后缀名切割

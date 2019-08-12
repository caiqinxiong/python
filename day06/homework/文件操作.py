# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/8/12 15:37
'''
# 3.sys.argv 和os模块 完成一个大作业
# 完成文件的copy: 从dir1 到dir2的copy
# 文件\文件夹的size
# 移动文件: 从dir1 到dir2
# 重命名文件/文件夹
# python xxx.py copy F:\python自动化27期\day6 F:\python自动化27期\day5
# python xxx.py size F:\python自动化27期\day6\cc.txt
# python xxx.py size F:\python自动化27期\day6
# python xxx.py move F:\python自动化27期\day6\cc.txt F:\python自动化27期\day5\cc.txt
# python xxx.py rename F:\python自动化27期\day6\cc1.txt F:\python自动化27期\day5\cc2.txt
'''

import os
import sys
import shutil
import argparse


def parseArgs(sys_args=sys.argv):
    '''处理命令行参数传入'''
    # 校验传入参数，多传或少传时报错！
    type = (lambda x: len(x) != 1 and x[1] or 'help')(sys_args)
    parser = argparse.ArgumentParser(epilog='')
    parser.add_argument('type', help='copy, move, size, del')
    if type.count('copy') or type.count('move'):
        parser.add_argument('path1', help='输入源路径！')
        parser.add_argument('path2', help='输入目的路径！')
    elif type.count('size') or type.count('del'):
        parser.add_argument('path', help='输入路径！')
    else:
        parser.add_argument('**', help='**')
        parser.description = u'Type error, with -h show help'
    args = parser.parse_args()
    return type, args, parser


def read_file(path1, path2):
    '''读写文件'''
    # 1、利用文件的打开重新写入的方式复制
    with open(path1, mode='r', encoding='utf-8') as f1, open(path2, mode='w') as f2:
        for line in f1:
            if line.strip():
                f2.write(line)
    # 2、利用shutil模块的copyfile直接进行复制
    # shutil.copyfile(path1,path2)
    # 3、利用os.system模块或os.popen模块实现


def copy_file(path1, path2):
    '''复制文件'''
    if os.path.isfile(path1):
        if not os.path.exists(os.path.split(path2)[0]):
            os.makedirs(os.path.split(path2)[0])
        read_file(path1, path2)
    elif os.path.isdir(path1):
        if not os.path.exists(path2):
            os.makedirs(path2)
        elif os.listdir(path2):
            print('%s\n目录已存在,且不为空！' % path2)
            return False
        for i in os.listdir(path1):
            file_path1 = os.path.join(path1, i)
            file_path2 = os.path.join(path2, i)
            copy_file(file_path1, file_path2)
    else:
        print('the path is not exist!')
        return False
    return True


def del_file(path):
    '''删除文件'''
    if os.path.isfile(path):
        os.remove(path)
    elif os.path.isdir(path):
        for i in os.listdir(path):
            file_path = os.path.join(path, i)
            del_file(file_path)  # 递归调用，先把所有的文件删除
            if os.path.isdir(file_path): os.removedirs(file_path)  # 再删除所有的空子目录
    else:
        print('the path is not exist!')


def move_file(path1, path2):
    '''剪切文件'''
    # 移动文件就是先复制后删除，直接调用复制函数和删除函数即可
    if copy_file(path1, path2):
        del_file(path1)
        if os.path.exists(path1): os.rmdir(path1)


def get_size(path):
    '''获取目录大小'''
    if os.path.isdir(path):
        sum_size, dirs = 0, [path]
        while dirs:
            path = dirs.pop()
            dir_lst = os.listdir(path)
            for name in dir_lst:
                file_path = os.path.join(path, name)
                if os.path.isfile(file_path):
                    sum_size += os.path.getsize(file_path)
                else:
                    dirs.append(file_path)
        return sum_size
    elif os.path.isfile(path):
        return os.path.getsize(path)
    else:
        print('the path is not exist!')


def main():
    '''主逻辑'''
    # 1. 分析获取参数
    type, args, parser = parseArgs()
    # 2. 根据获取的参数运行相应的方法
    if type == 'copy':
        copy_file(args.path1, args.path2)
    elif type == 'move':
        move_file(args.path1, args.path2)
    elif type == 'size':
        get_size(args.path)
    elif type == 'del':
        del_file(args.path)
    else:
        print(parser.parse_args('-h'))

if __name__ == '__main__':
    main()
    # path1 = r'E:\python_test\python\day06\day6\dir5'
    # path2 = r'E:\python_test\python\day06\day6\dir3'
    # # copy_file(path1,path2)
    # move_file(path1, path2)
    # # os.renames(path1,path2)

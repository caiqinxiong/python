# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/8/12 14:57
'''
# 1.给你一个非空文件夹,要求你删掉这个文件夹
# 进阶需求,这个非空文件夹下还有其他非空文件夹,并且不知道有多少层
'''
import os
def del_dir(path):
    '''删除非空文件夹'''
    if os.path.isfile(path):
        os.remove(path)
    elif os.path.isdir(path):
        for i in os.listdir(path):
            file_path = os.path.join(path, i)
            del_dir(file_path) # 递归调用，先把所有的文件删除
            if os.path.isdir(file_path):os.removedirs(file_path) # 再删除所有的空子目录
    else:
        print('the path is not exist!')


if __name__ == '__main__':
    path = r'E:\python_test\python\day06\day6\dir1'
    #1、利用os模块递归删除
    del_dir(path)
    if os.path.exists(path):os.rmdir(path) # 删除最后一层空目录


    #2、利用shutil模块直接删除非空文件夹
    # import shutil
    # if os.path.isdir(path):
    #     shutil.rmtree(path)

    #3、直接调用os.system模块或os.popen模块直接shell命令删除
    # import sys
    # if 'win' in sys.platform:
    #     os.system('rd /s /q %s' % path)
    #     #os.popen('rd /s /q %s' % path)
    # else:
    #     os.system('rm -rf %s' % path)
    #     #os.popen('rm -rf %s' % path)


# -*- coding:utf-8 -*-
# Author:caiqinxiong
import os,multiprocessing
def info(title):
    print(title)
    print('module_name:',__name__)
    print('parent process:',os.getppid())
    print('my process:',os.getpid())
    print('\n')

def fun(name):
    info('\033[31;1mcalled from child process function  \033[0m')
    print('hello', name)

if __name__ == '__main__':
    info('\033[32;1mmain process line\033[0m')
    m = multiprocessing.Process(target=fun,args=('lixiaoxin',))
    m.start()
    m.join()

# -*- coding:utf-8 -*-
# Author:caiqinxiong
from  multiprocessing import Process, Pool
import time,os

def Foo(i):
    time.sleep(1)
    print('in the process:',os.getpid())
    return i + 100


def Bar(arg):
    print('-->exec done:', arg,os.getpid())

if __name__ == '__main__':
    pool = Pool(5) # 进程池，允许进程池同时放入5个进程
    print('主进程：',os.getpid())
    for i in range(10):
        pool.apply_async(func=Foo, args=(i,), callback=Bar) #callback=回调，Foo（子进程）执行完才回调Bar（主进程），应用场景：备份1000台机器mysql子进程要连接1000次，主进程就只连接1次就行
        # pool.apply(func=Foo, args=(i,)) # 串行
        # pool.apply_async(func=Foo, args=(i,)) # 并行

    print('end')
    pool.close() # 必须先close才join，要不就报错
    pool.join()  # 进程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭。
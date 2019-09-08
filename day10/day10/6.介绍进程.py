# 进程是计算机中资源分配的最小单位
# 所有的计算机中的内存资源 文件资源 程序代码

# 进程可以被操作系统调度\CPU执行
# 一个进程在创建的时候 必须创建大量的资源内存资源 文件资源 程序代码
# 一个进程在结束的时候 必须被销毁
# 谁来销毁这个进程呢?
    # 一个进程总是被他的父进程销毁掉
# 进程与进程之间有一个父子关系
    # 父进程要负责销毁子进程
# 你在你写的python代码中开启的所有进程都是子进程
# 而你写的这个程序本身是这些子进程的父进程
# import os
# import time
# from multiprocessing import Process
#
# def func(参数1,参数2):
#     print('一个子进程',os.getpid(),参数1,参数2)
#     time.sleep(1)
#
# if __name__ == '__main__':   # 当本文件被导入的时候不执行if条件中的代码
#     p = Process(target=func,args=(1,2))
#     p.start()
#     p.join()   # 阻塞 等待子进程执行完毕
#     print('子进程执行完啦')

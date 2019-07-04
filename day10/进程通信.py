# -*- coding:utf-8 -*-
# Author:caiqinxiong
from multiprocessing import Process,Queue # 进程里的Queue，不是线程里的queue
#import queue,threading
def fun(q):
    q.put('hi,lixiaoxin!')

if __name__ == '__main__':
    q = Queue()
    #q = queue.Queue()
    #p = threading.Thread(target=fun,args=(q,)) # 线程间通信
    p = Process(target=fun,args=(q,)) #进程间通信
    p.start()
    print(q.get())
    #p.join()

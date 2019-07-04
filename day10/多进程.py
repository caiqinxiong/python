# -*- coding:utf-8 -*-
# Author:caiqinxiong
import multiprocessing
import threading
import time
start_time = time.time()
m_list=[]

def thread_run():
    print(threading.get_ident())
    #print()

def run(name):
    time.sleep(2)
    print('hei,',name)
    t = threading.Thread(target=thread_run,)
    t.start()

if __name__ == '__main__':
    for i in range(10):
        m = multiprocessing.Process(target=run,args=('lixiaoxin%s' % i,))
        m.start()
        m_list.append(m)
    for m in m_list:
        m.join()

    print('use time:',time.time()-start_time)
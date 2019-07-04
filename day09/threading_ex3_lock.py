# -*- coding:utf-8 -*-
# Author:caiqinxiong
import threading,time

num = 0
lock = threading.Lock()
def run(n):
    #lock.acquire() # 申请锁
    global num
#    num += 1
    time.sleep(0.8) # 加sleep计算结果就不一样了，先加和后加结果还不一样
    num += 1
    #lock.release() # 释放锁
start_time = time.time()
t_jobs = [] # 存线程实例

# 先循环创建50个线程
for i in range(50):
    #print(i)
    t = threading.Thread(target=run,args=('t-%s'% i,))
    #t.setDaemon(True) # 将该线程设置为守护进程，必须在start（）前,主线程结束，守护进程也随之结束，sleep(2)以及下面到语句不执行了。
    t.start() # 启动线程
    t_jobs.append(t) # 为了不阻塞后面都线程启动，不在这里join，先加到list里

# 等待50个线程都执行完了计算时间
# for t in t_jobs:
#     t.join()

print("!!!!!!all threads has finished!!!!!",threading.current_thread(),threading.active_count()) # 主线程， 计算一共有几个线程
print('use time',time.time()-start_time)
print('num:',num)
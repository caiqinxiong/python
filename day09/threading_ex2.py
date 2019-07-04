# -*- coding:utf-8 -*-
# Author:caiqinxiong
import threading,time

class MyThreading(threading.Thread):
    def __init__(self,n,sleep_time):
        super(MyThreading,self).__init__()
        self.n = n
        self.sleep_tiime = sleep_time
    def run(self):
        print('run task:',self.n)
        time.sleep(self.sleep_tiime)
        print("task done",self.n)

t1 = MyThreading('t1',2)
t2 = MyThreading('t2',4)
t1.start()
#t1.join() #相当于wait（）等待t1执行完才执行下一个指令
t2.start()
t1.join()# 加这里没有用，程序执行完默认就有一个
print("等待join执行完成")

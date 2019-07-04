# -*- coding:utf-8 -*-
# Author:caiqinxiong
import threading,time

def run(n):
    print('task:',n)
    time.sleep(2)

# 并行
t1 = threading.Thread(target=run,args=('task1',)) # 参数里面是元组
t2 = threading.Thread(target=run,args=('task2',))
t1.start()
t2.start()
# 串行
run('t1')
run('t2')
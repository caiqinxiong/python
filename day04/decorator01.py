# -*- coding:utf-8 -*-
# Author:caiqinxiong
import time
def timer(func):
    def deco(*args,**kwargs):
        start_time = time.time()
        res = func(*args,**kwargs)
        stop_time = time.time()
        print('the func run time is %s'%(stop_time-start_time))
        return res
    return deco
@timer #func01=timer(func01)
def func01():
    time.sleep(1)
    print('in the func01!')
@timer #func02=timer(func02)
def func02(name):
    time.sleep(2)
    print('in the func02!',name)
    return 'haha'

#func01=timer(func01)
func01()
#func02=timer(func02)
func02('caiqinxiong')
print(func02('cai'))
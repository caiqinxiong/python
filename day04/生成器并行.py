# -*- coding:utf-8 -*-
# Author:caiqinxiong

# 单线程下的并行效果,协程
import  time
# 消费者
def consumer(name):
    print('%s准备吃包子了！' % name)
    while True:
        baozi = yield
        print('包子[%s]来了，被[%s]吃了！' % (baozi,name))
'''
c = consumer('lixiaoxin')
c.__next__()#只是唤醒yield
b1 = '新肉虾仁'
c.send(b1)#只是唤醒yield，并给它传值
c.__next__()
'''

# 生产者
def product(name):
    c = consumer(name)
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    print('caiqinxiong要开始准备包子啦！')
    for i in range(10):
        time.sleep(0.5)
        print("做了一个包子，分两半！")
        c.send(i)
        c2.send(i)

product('lixiaoxin')




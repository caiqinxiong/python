# -*- coding:utf-8 -*-
# caiqinxiong 
# 2019/12/29 上午10:09
import queue

q = queue.Queue()

q.put('aa')
q.put('bb')
v1 = q.get()
v2 = q.get()
print(v1)
print(v2)

# v3 = q.get(timeout=5)
# print(v3)

l = []

def func():
    l.append('1')
    print(len(l))
    func()

func()

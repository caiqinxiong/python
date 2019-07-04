# -*- coding:utf-8 -*-
# Author:caiqinxiong
import queue # python2里是Queue

#q = queue.Queue(maxsize=10)
q = queue.LifoQueue(maxsize=10)

q.put(1)
q.put(2)
q.put(3)
print(q.get())
print(q.get())
print(q.get())
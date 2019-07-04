# -*- coding:utf-8 -*-
# Author:caiqinxiong

class Dog:
    '''狗类'''
    def __init__(self,name):
        self.name = name

    def bulk(self):
        print('%s:汪汪汪！！'% self.name)

d1 = Dog('大黄')
d2 = Dog('小白')
d3 = Dog('小灰')

d1.bulk()
d2.bulk()
d3.bulk()

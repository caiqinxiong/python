# -*- coding:utf-8 -*-
# Author:caiqinxiong
class Dog(object):

    def __init__(self,name):
        self.name = name
    #例子，台湾跟大陆
    @staticmethod #静态方法后，名义上还是属于该类，基本跟该类就没有什么关系类了（例子，os.system,os.mkdir,工具包组合）
    def eat(self,food):
        #print("%s is eating %s" % (self.name,food))
        print("%s is eating %s" % (self,food))#跟类没有关系类，相当于需要传人两个参数

d = Dog('大黄')
#d.eat('骨头')
d.eat('大黄','骨头')

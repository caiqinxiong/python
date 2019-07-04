# -*- coding:utf-8 -*-
# Author:caiqinxiong
class Dog(object):
    name = 'xiaoxin'
    def __init__(self,name):
        self.name = name

    #@staticmethod #静态方法后，名义上还是属于该类，基本跟该类就没有什么关系类了
    @classmethod #只能访问类变量，不能访问实例变量 （例子，类变量为国籍时，不可修改）
    def eat(self,food):
        print("%s is eating %s" % (self.name,food))

d = Dog('大黄')
d.eat('骨头')


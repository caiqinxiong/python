# -*- coding:utf-8 -*-
# Author:caiqinxiong
class Dog(object):
    name = 'xiaoxin'
    def __init__(self,name):
        self.name = name
        self.__food = None
    #@staticmethod #静态方法后，名义上还是属于该类，基本跟该类就没有什么关系类了
    #@classmethod #只能访问类变量，不能访问实例变量
    @property #属性方法，把一个方法变成一个静态属性,可以赋值了,作业，对用户来说，不需要关注更多
    def eat(self):
        print("%s is eating %s" % (self.name,self.__food))

    @eat.setter
    def eat(self,food):
        print('set food is :',food)
        self.__food = food

    @eat.deleter
    def eat(self):
        del self.__food
        print("删除了food")

d = Dog('大黄')
#d.eat('骨头')
d.eat
d.eat = '包子'
d.eat
del d.eat
#d.eat


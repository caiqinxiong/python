# -*- coding:utf-8 -*-
# Author:caiqinxiong

def func(self):
    print("my name is %s , I am %s years old!" % (self.name,self.age))

def __init__(self,name,age):
    self.name = name
    self.age = age

Foo = type('Foo',(object,),{'talk':func,'__init__':__init__}) #一切皆对象，type是Foo的父类，（object，）新式类，元组

f = Foo('caiqinxiong',29)
f.talk()
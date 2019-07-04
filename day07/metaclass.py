# -*- coding:utf-8 -*-
# Author:caiqinxiong
#自定义元类
class MyType(type):
    def __init__(self,*args,**kwargs):
        print("Mytype __init__",*args,**kwargs)

    def __call__(self, *args, **kwargs):
        print("Mytype __call__", *args, **kwargs)
        obj = self.__new__(self)
        print("obj ",obj,*args, **kwargs)
        print(self)
        self.__init__(obj,*args, **kwargs)
        return obj

    def __new__(cls, *args, **kwargs):
        print("Mytype __new__",*args,**kwargs)
        return type.__new__(cls, *args, **kwargs)

print('here...')
class Foo(object,metaclass=MyType):
    def __init__(self,name):
        self.name = name

        print("Foo __init__")

    def __new__(cls, *args, **kwargs): # 用来实例化对象的，调用__inti__来实例化，平时不要写这个方法。
        print("Foo __new__",cls, *args, **kwargs)
        return object.__new__(cls) # 继承父亲的__new__方法

f = Foo("Alex")
print("f",f)
print("fname",f.name)


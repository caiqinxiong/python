# -*- coding:utf-8 -*-
# Author:caiqinxiong

# 在类外面定义一个方法
def bulk(self):
    print('%s is yelling....'% self.name)

class Dog(object):
    def __init__(self,name):
        self.name = name
    def eat(self,food):
        print("%s is eating %s...." % (self.name,food))

d = Dog('dahuang')
choice = input('>>：').strip()

# print(hasattr(d,choice)) # 判断d对象里是否有choice方法。
# print(getattr(d,choice)) # 根据字符串去获取d对象里的对应方法的内存地址
# getattr(d,choice)()# 加上括号，调用
if hasattr(d,choice):
    #delattr(d,choice)
    setattr(d,choice,"lixiaoxin") # 动态的设置变量,给对象添加新的属性
    #func = getattr(d,choice)
    #func('gutou')
else:
    setattr(d,choice,bulk) # 动态的设置方法，将bulk方法变成d类的属性，并改名为talk
    d.talk(d)

print(d.name)
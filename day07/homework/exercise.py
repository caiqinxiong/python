# -*- coding:utf-8 -*-
# caiqinxiong 
# 2019/8/18 上午9:26
import json
# lst = ['caiqinxiong','lixiaoxin']
# with open('name.txt',mode='w',encoding='utf-8') as f:
#     json.dump(lst,f)

# with open('name.txt',mode='r',encoding='utf-8') as f:
#     ret = json.load(f)
#     print(ret)


# lst = ['蔡亲雄','李小欣']
# s = json.dumps(lst,ensure_ascii=False) # 取消ascii的形式存储
# with open('name.txt','w',encoding='utf-8') as f:
#     f.write(s)

import pickle # 二进制的方式
#
# class Persion(object):
#     '''人物类'''
#     def __init__(self,name,hp,ad,sex,job):
#         self.name = name
#         self.hp = hp
#         self.ad = ad
#         self.sex = sex
#         self.job = job
#
#     def attack(self,dog):
#         dog.hp -= self.ad
#         print('%s打了%s，%s掉了%s血量！' % (self.name,dog.name,dog.name,self.ad))
#
#
# class Dog(object):
#     '''狗类'''
#     def __init__(self,name,kind,hp,ad):
#         self.name = name
#         self.kind = kind
#         self.hp = hp
#         self.ad = ad
#
#     def bite(self,persion):
#         persion.hp -= self.ad
#         print('%s咬了%s，%s掉了%s血量！' % (self.name,persion.name,persion.name,self.ad))
#
# p1 = Persion('alex',500,100,'man','IT')
# p2 = Persion('wusir',1000,200,'boy','IT')
#
# d1 = Dog('旺财','拉布拉多',500,300)
# d2 = Dog('大黄','哈士奇',800,100)
#
# p1.attack(d1)
# d1.bite(p1)
# p2.attack(d2)
# d2.bite(p2)
#
# class Circular(object):
#     from math import pi
#     #pi = pi
#     def __init__(self,r):
#         self.r = r
#
#     def perimeter(self):
#         ret = 2*Circular.pi*self.r
#         return ret
#
#     def area(self):
#         ret = Circular.pi*self.r**2
#         return ret
#
# c = Circular(10)
# ret = c.area()
# ret2 = c.perimeter()
# print(ret)
# print(ret2)

# class CoutAgr(object):
#     cout = 0
#     def __init__(self):
#         CoutAgr.cout +=1
#
# alex = CoutAgr()
# print(alex.cout)
# wusir = CoutAgr()
# print(CoutAgr.cout)

# from math import pi
# class Circular(object):
#     '''计算圆环'''
#     def __init__(self,r1,r2):
#         self.r1 = r1
#         self.r2 = r2
#
#     def perimeter(self):
#         return 2*pi*(self.r1 + self.r2)
#
#     def area(self):
#         return pi*self.r1**2 - pi*self.r2**2
#
#
# c = Circular(20,10)
# print(c.perimeter())
# print(c.area())

# class Students(object):
#     def __init__(self,name,age,sex,phone,couerse):
#         self.name = name
#         self.age = age
#         self.sex = sex
#         self.phone = phone
#         self.course = couerse
#
#
# class Course(object):
#     def __init__(self,cname,period,price):
#         self.cname = cname
#         self.period = period
#         self.price = price
#
#
# c1 = Course('python','6 moth',19800)
# s1 = Students('蔡亲雄','19','male','1326994274893',c1)
# print(s1.course.price)

# ret = json.dumps('蔡亲雄')
# print(ret)
# ret = json.dumps('蔡亲雄',ensure_ascii=False)
# print(ret)

class Parent(object):
    x = 1
class Child1(Parent):
    pass
class Child2(Parent):
    pass

print(Parent.x,Child1.x,Child2.x)
Child1.x = 2
print(Parent.x,Child1.x,Child2.x)
Parent.x = 3
print(Parent.x,Child1.x,Child2.x)
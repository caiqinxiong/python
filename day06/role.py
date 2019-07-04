# -*- coding:utf-8 -*-
# Author:caiqinxiong

class Role:

    n = 123 # 类变量，大家共用的属性，节省开销
    name = '我是类name'
    _list = []
    def __init__(self, name, role, weapon, life_value=100, money=15000):
        # 构造函数
        # 在实例化时做一些类的初始化工作
        self.name = name # 实例变量（静态属性），作用域，实例本身
        self.role = role
        self.weapon = weapon
        self.life_value = life_value
        self.money = money

    def shot(self): #类方法，功能，动态属性
        print("shooting...")

    def got_shot(self):
        print("ah...,I got shot...")

    def buy_gun(self, gun_name):
        print("just bought %s" % gun_name)


r1 = Role('Alex', 'police', 'AK47') # 生成一个角色，一个实例，一个对象
r1.naem = 'lixiaoxin' # 属性修改
r1.bullet = True # 新增属性
print(r1.weapon)
del r1.weapon # 删除属性
#print(r1.weapon)

r1.n = '改类变量' #相当于给r1新增属性，跟r2无关

r2 = Role('Jack', 'terrorist', 'B22') # 生成一个角色

r1.shot()
r2.buy_gun('机关枪')
print(Role.n)
print(r1.n,r1.name ,r1.bullet) #先找实例本身的变量，没有再从类里找
print(r2.n,r2.name )

Role.n = 'ABC' # 修改类变量， r1还是先找自己的属性
print(r1.n,r2.n)
# list共用一个内存变量
r1._list.append('aaaa')
r2._list.append('bbbb')
print(Role._list,r1._list,r2._list)
# -*- coding:utf-8 -*-
# Author:caiqinxiong

def func01(x,y):
    print('x:',x)
    print('y:',y)

x=1
y=2
func01(1,2)#与型参一一对应
func01(y=y,x=x)# 与型参位置无关，给指定型参赋值

#、func01(x=2,3)
#func01(2,x=3)#已经把2给x了，又把3给x，报错

func01(2,y=3)#给指定参数赋值必须放在后面（关键参数不能写在位置参数前面）

print('-----------------------------------------')
#默认参数（用途：默认安装路径，mysql端口号：3306）
def func02(x,y=2):
    print('x:', x)
    print('y:', y)

func02(1)
func02(1,3)

print('-----------------------------------------')
#型参不固定（放到元组里）
def func03(*args):
    print('args:', args)
func03(1)
func03(1,2,3)
func03(*[1,2,3])
func03([1,2,3])

print('-----------------------------------------')
#型参不固定（放到元组里）
def func04(x,*args):#把第一个实参给x，剩下的给元组
    print('x:',x)
    print('args:', args)
func04(1)
func04(1,2,3)
func04(*[1,2,3])
func04([1,2,3])

print('-----------------------------------------')
#字典模式（两个*）
def func05(**kwargs):
    print('kwargs:', kwargs)
    print(kwargs['name'])

func05(name='caiqinxiong',age=28,sex='man')
func05(**{'name':'lixiaoxin','age':30})

print('-----------------------------------------')
#字典模式扩展功能
def func06(name,**kwargs):
    print('name:',name)
    print('kwargs:', kwargs)

func06('cai')
#func06('cai','xin')只有一个位置参数，所以不能传俩
func06('cai',age=28,sex='M')


print('-----------------------------------------')
#字典模式默认值组合
def func07(name,age=28,**kwargs):
    print('name:',name)
    print('age:',age)
    print('kwargs:', kwargs)

func07('cai',sex='M',hobby='sport')
func07('cai',18,sex='M',hobby='sport')
func07('cai',age=18,sex='M',hobby='sport')
func07('cai',sex='M',hobby='sport',age=30)


print('-----------------------------------------')
#各种组合，*args接收N个位置参数，**kwargs接收N个关键字参数转换成字典的模式
def func08(name,age=28,*args,**kwargs):
    print('name:',name)
    print('age:',age)
    print('args:',args)
    print('kwargs:', kwargs)

#func08('cai',age=18,'aa','bb',sex='M',hobby='sport')位置参数不能写在关键参数后面
func08('cai',18,'aa','bb',sex='M',hobby='sport')

def fun01():
    #time.sleep(3)
    print('in the test01!')

fun01()
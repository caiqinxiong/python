# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/7/30 10:15
#1，老师给课上讲的
def add(n,i):                     #普通求和函数
    return n + i
def test():                       #生成器函数
    for i in range(4):
        yield i
g=test()                          #获取生成器对象，后面的操作都指向这个对象，这和直接执行fun()函数销效果是不一样的
for n in [1,10]:                  #因为前面已经定义了生成器g,这个for循环的代码块等于是重新定义了变量g,
    g=(add(n,i) for i in g)       #重新定义的这个变量g也是一个生成器，使用推导式定义的生成器
print(list(g))                    #list自带for方法，所以list(g)会一次性把上面列表生成器的值拿完

#2，生成器例子
import  time
# 消费者
def consumer(name):  #生成器函数，处于监听状态
    print('%s准备吃包子了！' % name)
    while True:
        baozi = yield
        print('包子[%s]来了，被[%s]吃了！' % (baozi,name))

# 生产者
def product(name):
    c = consumer(name)
    c2 = consumer('xiaoqiang')
    c.__next__()  #只是唤醒yield
    c2.__next__()
    print('caiqinxiong要开始准备包子啦！')
    for i in range(10):
        time.sleep(0.5)
        print("做了一个包子，分两半！")
        c.send(i)  #只是唤醒yield，并给它传值
        c2.send(i)

product('lixiaoxin')
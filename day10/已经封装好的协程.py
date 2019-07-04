# -*- coding:utf-8 -*-
# Author:caiqinxiong
# -*- coding:utf-8 -*-
# greenlet是一个用C实现的协程模块，相比与python自带的yield，它可以使你在任意函数之间随意切换，而不需把这个函数先声明为generator
# 感觉确实用着比generator还简单了呢，但好像还没有解决一个问题，就是遇到IO操作，自动切换，对不对？
from greenlet import greenlet

def test1():
    print(12)
    gr2.switch()
    print(34)
    gr2.switch()


def test2():
    print(56)
    gr1.switch()
    print(78)


gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()
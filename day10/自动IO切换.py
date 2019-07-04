# -*- coding:utf-8 -*-
# Author:caiqinxiong
'''
Gevent 是一个第三方库，可以轻松通过gevent实现并发同步或异步编程，
在gevent中用到的主要模式是Greenlet, 它是以C扩展模块形式接入Python的轻量级协程。
Greenlet全部运行在主程序操作系统进程的内部，但它们被协作式地调度
'''
import gevent

def func1():
    print('\033[31;1mruning in func1...\033[0m')
    gevent.sleep(2)
    print('\033[31;1mback func1\033[0m')


def func2():
    print('\033[32;1mruning in func2...\033[0m')
    gevent.sleep(1)
    print('\033[32;1mback func2\033[0m')


def func3():
    print('\033[33;1mruning in func3...\033[0m')
    gevent.sleep(0)
    print('\033[33;1mback func3\033[0m')

gevent.joinall([
    gevent.spawn(func1),
    gevent.spawn(func2),
    gevent.spawn(func3),
])
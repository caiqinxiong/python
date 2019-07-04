# -*- coding:utf-8 -*-
# Author:caiqinxiong
'''
1、把一个函数名当作实参传给另外一个函数
2、返回值中包含函数名
'''
#高阶函数，实参传入的是函数
def add(a,b,f):
    return f(a)+f(b)

res = add(3,-6,abs)#abs是一个求绝对值的内置函数

print(res)
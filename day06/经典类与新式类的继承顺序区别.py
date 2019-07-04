# -*- coding:utf-8 -*-
# Author:caiqinxiong

#class A(object):新式类，不管是在python2还是python3，都按广度优先查找
class A: # 经典类，python2里按"深度优先"查找，python3里按"广度优先"查找
    def __init__(self):
        print("A")

class B(A):
    pass
    # def __init__(self):
    #     print("B")

class C(A):
    def __init__(self):
        print("C")

class D(B,C):
    pass
    # def __init__(self):
    #     print("D")

obj = D()
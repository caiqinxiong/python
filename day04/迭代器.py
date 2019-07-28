# -*- coding:utf-8 -*-
# Author:caiqinxiong
# 可以直接用于for循环的对象统称为可以迭代对象：Iterable，（str,[],{}等都是可以直接作用于for循环的，Iterable返回True or false）
# 可以被next()函数调用，并不断返回不断返回下一个值的对象称为迭代器：Iterator

from collections import Iterable
print(isinstance([],Iterable))
print(isinstance({},Iterable))
print(isinstance('abc',Iterable))
print(isinstance((x for x in range(10)),Iterable))
print(isinstance(123,Iterable))

# 迭代器只做一件事，节省内存空间，文件操作
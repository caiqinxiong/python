# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/7/25 15:18
'''
斐波那契数列指的是1、1、2、3、5、8、13、21、···这样一个数列,我们可以发现它后面的一个数是前两个数之和
递归实现n个斐波那契数列：
'''
# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
# print('20个斐波那契数列为：')
# for i in range(1,21):
#     print(fibonacci(i),end=' ')

'''
利用递归求解n的阶乘：
'''
def func(n):
    if n == 1:
        return 1
    else:
        return n * func(n - 1)
for i in range(1, 10):
    print('%s！的阶乘为：%s'% (i,func(i)))

'''
利用递归来求解 汉诺塔
'''
# def Hanoi(n, a, b, c):
#     if(n == 1):
#         print(a,"-->",c)
#         return
#     Hanoi(n-1, a, c, b)
#     Hanoi(1, a, b, c)
#     Hanoi(n-1, b, a, c)
#     # print('~'*10)
#
# Hanoi(5, "A", "B", "C")

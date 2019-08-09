# -*- coding:utf-8 -*-
# caiqinxiong 
# 2019/8/4 上午10:16
from functools import wraps
# def outer(func):
#     @wraps(func)
#     def inner(*args,**kwargs):
#         print('start')
#         res = func(*args,**kwargs)
#         print('end')
#         return res
#     return inner
#
# @outer
# def home():
#     print('in the home!')
#     return True
#
# @outer
# def shop_car():
#     print('in the shop_car')
#     return True
# @outer
# def shop():
#     print('in the shop')

#     return True
#
# home()
# shop_car()
# shop()
#
# def wahaha(n):
#     print(n)
#     n+=1
#     wahaha(n)
# wahaha(1)
# lis =[1,2,3,4,[5,6,7,8,[6,3,2,1]]]
# sum_num = 0
#
# def sum_(lis):
#     global sum_num
#     for i in lis:
#         if type(i) is list:
#             sum_(i)
#         else:
#             sum_num += i
# sum_(lis)
# print(sum_num)
#
# l =[1,2,3,4,[5,6,7,8,[6,3,2,1]]]
# n = []
# def sum_l(l):
#     for i in l:
#         if type(i) is list:
#             sum_l(i)
#         else:
#             n.append(i)
#     return sum(n)
#
# ret = sum_l(l)
# print(ret)
#
# lis =[1,2,3,4,[5,6,7,8,[6,3,2,1]]]
#
# def sum_(lis):
#     sum_num = 0
#     for i in lis:
#         if type(i) is list:
#             ret = sum_(i)
#             sum_num = ret +sum_num
#             return sum_num
#         else:
#             sum_num += i
#     return sum_num
# sum_(lis)
# print(sum_num)
#
# def func(n):
#     if n>1:
#         return n*func(n-1)
#     else:
#         return n
# ret = func(10)
# print(ret)

# s = '1+2+3'
# res = eval(s) # 执行代码，有返回值
# print(res)
# res = exec(s) # 执行代码，没有返回值
# print(res)

# l = [2,3,5,10,15,16,18,22,26,30,32,35,41,42,43,55,56,66,67,69,72,76,82,83,88]
#
# def func(l,aim):
#     mid = (len(l)-1)//2
#     if l:
#         if aim > l[mid]:
#             func(l[mid+1:],aim)
#         elif aim < l[mid]:
#             func(l[:mid],aim)
#         elif aim == l[mid]:
#             print("bingo",mid)
#     else:
#         print('找不到')
# func(l,66)
# func(l,2)

# print(('-' or '+') in '9+2*3')
# print(('-' or '+') in '9-2*3')
# print(type('-' or '+'))
# s = ('-' or '+')
# s2 = ('+' or "-")
# print(s)
# print(s2)
#
#
# print(type('1' or '2'))
# s = ('1' or '2')
# s2 = ('2' or "1")
# print(s)
# print(s2)
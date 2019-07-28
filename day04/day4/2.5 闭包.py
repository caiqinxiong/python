# 闭包 :如果一个内部的函数引用了外部函数的变量,那么这个内部函数就是一个闭包函数
# def wahaha():
#     name = 'alex'
#     def a():
#         # '''一旦内层函数引用了外层函数的变量,a就是一个闭包函数'''
#         print('in func a',name)  # 闭包函数
#     return a
#
# a = wahaha()
# print(a())

# def func1():
#     a = 1
#     b = 2
#     def inner():  # inner中没有用到a,b所以不是闭包
#         print(1,2)

# def func2():
# #     a = 1
# #     b = 2
# #     def inner(a,b):  # inner中虽然用到a,b,但用到的是自己的参数a,b,而不是外部的变量,所以不是闭包
# #         print(a,b)

# def func2():
#     a = 1
#     b = 2
#     def inner():  # 是闭包
#         print(a,b)
#
# def func2(a,b):
#     def inner():  # 是闭包
#         print(a,b)
#
# a = 1
# b = 2
# def func2():
#     def inner():  # 不是闭包
#         print(a,b)

# 闭包有什么用?
from urllib import request   # url模块

# ret = request.urlopen('https://www.cnblogs.com/Eva-J/p/7277026.html')
# print(ret.read().decode('utf-8'))

# def get_source_html(url):
#     dic = {}
#     def get_url():
#         if url in dic:
#             return dic[url]
#         else:
#             ret = request.urlopen(url)
#             dic[url] = ret
#             return ret.read().decode('utf-8')
#     return get_url
# get_url = get_source_html('https://www.cnblogs.com/Eva-J/p/7277026.html')
# print(get_url())
# print(get_url())
# print(get_url())
# print(get_url())
# print(get_url())
# print(get_url())









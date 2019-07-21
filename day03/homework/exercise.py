# -*- coding:utf-8 -*-
# caiqinxiong 
# 2019/7/21 上午10:48
# import copy
# a = [1,2,3]
# # b = a
# b = copy.copy(a)
# a.append(1)
# a[0] = 8
# print(a)
# print(b)
# dic = {}
# f = open(r'userinfo',
#      mode='r',encoding='utf-8')
# # print(f.read())
# print(f.tell()) # 获取指针位置
# print(f.readline())
# print(f.seek(5)) # 指针定位
# print(f.tell())
# # 比较常用的第一种读方式
# for line in f:
#      line = line.strip()
#      if line:# 把空行也给去掉
#           #print(line)
#           dic[line.split('|')[0]] = [line.split('|')[1] ,line.split('|')[2]]
# print(dic)
# f.close()

# with open(r'userinfo',mode='r',encoding='utf-8') as f:
#      for line in f:
#           line = line.strip()
#           if line:
#                print(line)
# a = 1
# b = 2
# c = 3
#
# def func():
#     ret =  a * b / c
#     print(ret)
# func()

# def sum(a,b):
#      return  a+b
# ret = sum(1,3)
# print(ret)

# def func(a,b):
#      if a > b:
#           return a
#      else:
#           return b
# print(func(2,5))
# 列表 、元组 、字符串、字典。求两个类型的长度比，返回数据长度更长的类型
# def mylen(seq):
#     i = 0
#     for j in seq:
#         i += 1
#     return i
#
# def compare(agr1,agr2):
#      if mylen(agr1) > mylen(agr2):
#           return agr1
#      else:
#           return  agr2
#
# ret = compare([1,2,4],'fajdhkdfa')
# print(ret)
#
# a = 1
# def func():
#      global a # 尽量少用，一旦修改了全局变量，其他函数调用到它到时候，值也是会改变的
#      a = a+1
#      #print(a)
#      return a
# print(func())
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
#################################分割线##########################################################################

'''
1、任一个英文的纯文本文件，统计其中的每个单词出现的个数，注意是每个单词。。
'''
# import collections
# with open('test.txt','r') as fp:
#     str1=fp.read().split(' ')
# b = collections.Counter(str1)
# with open('result.txt','w') as result_file:
#     for key,value in b.items():
#         result_file.write(key+':'+str(value)+'\n')

'''
2、写函数，计算传入数字参数的和。（动态传参）
'''
# def cout(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum
# print(cout(1,2,3,4,5))

'''
3、写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量修改操作
'''
# import os
# def modifyFile(fileName,old,new):
#     try:
#         with open(fileName,mode='r',encoding='utf-8') as f1, open("%s.bak" % fileName,mode='w',encoding='utf-8') as f2:
#             for line in f1:
#                 line = line.strip()
#                 if old in line:
#                     line = line.replace(old,new)
#                 f2.write(line+'\n')
#         os.remove(fileName)
#         os.rename("%s.bak" % fileName,fileName)
#     except:
#         print('have no file!')
#
# modifyFile('userinfo','alex','wusir')
# modifyFile('userinfo','10','20')

'''
4、写函数，检查用户传入的对象（字符串、列表、元组）的每一个元素是否含有空内容。
'''
# def checkEmptyContent(args):
#     if isinstance(args,str):
#         for a in args:
#             if a.isspace():
#                 print('有空内容！')
#                 break
#         else:
#             print('无空内容！')
#     else:
#         for i in args:
#             if i =='':
#                 print('有空元素！')
#                 break
#         else:
#             print('无空元素！')
# checkEmptyContent('1232   43243')
# checkEmptyContent('123243243')
# checkEmptyContent(['a','','c'])
# checkEmptyContent(('a','b','c'))

'''
5、写函数，检查传入字典的每一个value的长度,如果大于2，
那么仅保留前两个长度的内容（对value的值进行截断），
并将新内容返回给调用者，注意传入的数据可以是字符、list、dict
'''
# def checkLen(args):
#     if isinstance(args,dict):
#         for k,v in args.items():
#             #print(k,v)
#             if len(v)>2:
#                 args[k] = v[:2]
#     elif isinstance(args,list):
#         for i in args:
#             if len(i)>2:
#                 args[args.index(i)] = i[:2]
#     else:
#         if len(args)>2:
#             args = args[:2]
#     return args
#
# args = checkLen('aabbcc')
# print(args)
# args = checkLen(['11111','22','333'])
# print(args)
# args = checkLen({'k1':'1','k2':'222','k3':'33333333'})
# print(args)

'''
6、写函数，返回一个扑克牌列表，里面有52项，每一项是一个元组
　　例如：[(‘红心’，2),(‘草花’，2), …(‘黑桃A’)]
'''
# def poker():
#     poker_list = []
#     for i in ['红心','草花','梅花','黑桃']:
#         for j in range(1,13):
#             poker_list.append((i,j))
#         else:
#             poker_list.append((i,'A'))
#     print(poker_list)
# poker()

'''
7、写函数，传入n个数，返回字典{‘max’:最大值,’min’:最小值}
　　例如:minmax(2,5,7,8,4)
　　返回:{‘max’:8,’min’:2}
'''
# def maxMin(*args):
#     dic = {}
#     dic['max'] = max(args)
#     dic['min'] = min(args)
#     print(dic)
#     return dic
# maxMin(2,5,7,8,4)

'''
8、写函数，专门计算图形的面积
其中嵌套函数，计算圆的面积，正方形的面积和长方形的面积
调用函数area(‘圆形’,圆半径) 返回圆的面积
调用函数area(‘正方形’,边长) 返回正方形的面积
调用函数area(‘长方形’,长，宽) 返回长方形的面积
'''

# def area(*args):
#     def rectangularArea(l,w):
#         '''计算长方形面积'''
#         area = l*w
#         return area
#
#     def squareArea(l):
#         '''计算正方形面积'''
#         area = l*l
#         return area
#
#     def circularArea(r):
#         '''计算圆形面积'''
#         area = 3.14*r*r
#         return area
#     area = 0
#     if args[0] == '长方形':
#         area = rectangularArea(args[1],args[2])
#     elif args[0] == '正方形':
#         area = squareArea(args[1])
#     elif args[0] == '圆形':
#         area = circularArea(args[1])
#     else:
#         print('暂时无该图形的计算！')
#     print('%s的面积为:%s' % (args[0],area))
#     return area
#
# area('圆形',2)
# area('正方形',4)
# area('长方形',2,4)

'''
9、写函数，传入一个参数n，返回n的阶乘
　　例如:cal(7)
　　返回计算7*6*5*4*3*2*1的结果
'''
# def cal(n):
#     if n == 1:
#         return 1
#     else:
#         return n * cal(n - 1)
# print('7*6*5*4*3*2*1的结果为：',cal(7))

'''
10、如下，每个小字典的name对应股票名字，shares对应多少股，price对应股票的价格

portfolio = [
{‘name’: ‘IBM’, ‘shares’: 100, ‘price’: 91.1},
{‘name’: ‘AAPL’, ‘shares’: 50, ‘price’: 543.22},
{‘name’: ‘FB’, ‘shares’: 200, ‘price’: 21.09},
{‘name’: ‘HPQ’, ‘shares’: 35, ‘price’: 31.75},
{‘name’: ‘YHOO’, ‘shares’: 45, ‘price’: 16.35},
{‘name’: ‘ACME’, ‘shares’: 75, ‘price’: 115.65}
]
通过哪个内置函数可以计算购买每支股票的总价
用filter过滤出，单价大于100的股票有哪些
'''
portfolio = [
{'name': 'IBM', 'shares': 100, 'price': 91.1},
{'name': 'AAPL', 'shares': 50, 'price': 543.22},
{'name': 'FB', 'shares': 200, 'price': 21.09},
{'name': 'HPQ', 'shares': 35, 'price': 31.75},
{'name': 'YHOO', 'shares': 45, 'price': 16.35},
{'name': 'ACME', 'shares': 75, 'price': 115.65}
]
# 通过哪个内置函数可以计算购买每支股票的总价
ret = map(lambda dic : {dic['name']:round(dic['shares']*dic['price'],2)},portfolio)
print(list(ret))
# 用filter过滤出，单价大于100的股票有哪些
ret = filter(lambda dic:True if dic['price'] > 100 else False,portfolio)
print(list(ret))

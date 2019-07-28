# -*- coding:utf-8 -*-
# caiqinxiong 
# 2019/7/28 上午10:43

# # 监听
# def listen():
#     with open(r'operate.log',mode='r',encoding='utf-8') as f:
#         while True:
#             conten = f.readline().strip()
#             if 'error' in conten:
#                 yield conten
#
# for conten in listen():
#     print(conten)
#
# # 操作监听的文件
# def wite_file():
#     f = open(r'operate.log',mode='a',encoding='utf-8')
#     inp = input()
#     f.write(inp)
#     f.close()
#
# wite_file()

# # 利用生成器来提高读取效率
# def get_user():
#     with open(r'userinfo', mode='r',encoding='utf-8') as f:
#         for line in f:
#             user,pwd = line.strip().split('|')
#             yield user,pwd

# lst = [i for i in range(1,31) if i % 3 == 0]
# print(lst)
#
# lst = [i**2 for i in range(1,31) if i % 3 == 0]
# # print(lst)
#
# def add(n,i):
#     return n+i
#
# def test():
#     for i in range(4):
#         yield i
#
# g=test()
# for n in [1,10]:
#     g=(add(n,i) for i in g)
# #
# print(list(g))

# def demo():
#     for i in range(4):
#         yield i

# g = demo()
#
# g1=(i for i in g)
# print(list(g1))
# print(list(g))
# # g2=(i for i in g1)
#
# # print(list(g1))
# # print(list(g2))

#
# fun1 = lambda a,b: a if a> b else b
# ret = fun1(1,3)
# print(ret)
#
#
# func2 = lambda a:'偶数' if a % 2 == 0 else '奇数'
#
# print(func2(2))




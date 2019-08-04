# 自己调用自己
# 最大的递归深度 1000次  RecursionError
from sys import setrecursionlimit
# def wahaha():
#     print('wahaha')
#     wahaha()
#     print('结束')
#
# wahaha()
# 函数的调用过程中 内存情况

# 递归函数-解决嵌套的列表操作
# lst = ['a1','a2',['a11','a22',['b11','b22',['ccc','ddd']]]]
# def look_up(lst):  # ['a1','a2',['a11','a22',['b11','b22',['ccc','ddd']]]]
#     for i in lst:
#         if type(i) is list:  # ['a11','a22',['b11','b22',['ccc','ddd']]]
#             look_up(i)       # lst(['a11','a22',['b11','b22',['ccc','ddd']]])
#         else:
#             print(i)   # 'a1'   'a2'
# look_up(lst)

# l1 =[1,[90,80.2],4,[5,6,7,8,[6,3,2]]] # 求列表中所有元素的和
# # 先写函数
# # 然后写循环
# # 考虑一层循环中的求和
# # 考虑每个数据的数据类型
# sum_n = 0
# def rec_sum(lst):
#     global sum_n
#     for n in lst:
#         if type(n) is list:
#             rec_sum(n)
#         elif type(n) is int or  type(n) is float:
#             sum_n += n
# rec_sum(l1)
# print(sum_n)

# l1 =[1,[90,80.2],4,[5,6,7,8,[6,3,2]]] # 求列表中所有元素的和
# def rec_sum(lst):
#     sum_n = 0
#     for n in lst:
#         if type(n) is list:
#             ret = rec_sum(n)
#             sum_n += ret
#         elif type(n) is int or  type(n) is float:
#             sum_n += n
#     return sum_n
# ret1= rec_sum(l1)   # [1,[90,80.2],4,[[6,3,2],5]]
# print(ret1)
# ret2= rec_sum([1,2,[3,[4,5]]])   # [1,[90,80.2],4,[[6,3,2],5]]
# print(ret2)

# 阶乘 用递归实现
# 8! = 8*7*6*5*4*3*2*1
# def fn(n):  # n=3
#     if n>1:
#         return n * fn(n-1)
#     else:
#         return n
# ret = fn(10)
# print(ret)

# l = [3,5,7,9,13,27,32,45,66,88,102]
# 列表有序 求某一个元素的位置
# 32值在哪儿








# -*- coding:utf-8 -*-
# caiqinxiong 
# 2019/8/11 上午9:32
# print(max(1,2,5,3,7,10))
# print(max([1,2,5,3,7,10])) #list也一样，因为max接收的是*args
# dic = {'a':100,'b':10}
# print(max(dic)) # 字典按key进行比较
# print(max(dic,key=lambda k:dic[k])) # 自定义按值来比较
#
# lst = [[10,2],[3,40],[1,9]]
# print(max(lst,key=lambda k:sum(k))) # 求lst里和最大的值sum(k)求每一项的和
#
# ret = sorted([1,3,3,6,4,2,3,7,8,9])
# print(ret)
#
# ret = sorted([10,373,332,62,44,26,37,74,8,9],key=lambda i:i % 10) # 只求个位数,负数求余数需要注意，-1%10=9
# print(ret)
#
# ret = filter(lambda n:n>10,[1,5,10,19]) # 参选，过滤，返回原数据
# print(ret)
# for i in ret:
#     print(i)
#
# # map 也是一个返回值为迭代器的函数,将每一项元素进行加工，并返回加工后的值
# lst = [1,2,3,4,5,6,7,8,9,10]
# ret = map(lambda n:n*2,lst)
# print(ret)
# for o in ret:
#     print(o)

# import re
# ret = re.search('(?:<num1>\d)(?:<num1>)','a1,b22,c345')
# print(ret)

#
# import os
# def get_file_size(path,size = 0):
#     '''计算一个目录下所有文件大小'''
#     if os.path.isdir(path):
#         file_list = os.listdir(path)
#         for i in file_list:
#             file_path = os.path.join(path,i)
#             size += int(os.path.getsize(file_path))
#     return size
#
# if __name__ == '__main__':
#     path1 = r'/Users/caiqinxiong/PycharmProjects/python/day06/homework'
#     ret = get_file_size(path1)
#     print('目录%s下的所有文件大小为：%s' % (path1,ret))
#
# #################################方法一################################################
# size = 0
# def get_all_size(path):
#     '''计算目录下所有文件大小，包括下面的文件夹'''
#     global size
#     file_list = os.listdir(path)
#     for i in file_list:
#         file_path = os.path.join(path, i)
#         #print(file_path)
#         if not os.path.isdir(file_path):
#             size += int(os.path.getsize(file_path))
#         else:
#             get_all_size(file_path)
#     return size
#
# if __name__ == '__main__':
#     path2 = r'/Users/caiqinxiong/PycharmProjects/python/day06'
#     ret = get_all_size(path2)
#     print('目录%s下的所有文件大小为：%s' % (path2, ret))
#
#     #os.system('du -sh %s' % path2)
#
# ##################################方法二###############################################
#
# def get_all_size(path,size):
#     '''计算目录下所有文件大小，包括下面的文件夹'''
#     file_list = os.listdir(path)
#     for i in file_list:
#         file_path = os.path.join(path, i)
#         #print(file_path)
#         if not os.path.isdir(file_path):
#             dic['size'] += int(os.path.getsize(file_path))
#         else:
#             get_all_size(file_path, dic['size'])
#     return  dic['size']
#
# if __name__ == '__main__':
#     dic = {'size' : 0,'path' : r'/Users/caiqinxiong/PycharmProjects/python/day06'}
#     ret = get_all_size(dic['path'],dic['size'])
#     print('目录%s下的所有文件大小为：%s' % (dic['path'], ret))
#
#     os.system('du -sh %s' % dic['path'])
#
#
# def get_size(path):
#     sum_size = 0
#     li_dir = os.listdir(path)
#     li_dir = map(lambda n: os.path.join(path, n), li_dir)
#     for i in li_dir:
#         if os.path.isdir(i):
#             sum_size += get_size(i)
#         if os.path.isfile(i):
#             sum_size += os.path.getsize(i)
#     return sum_size
#
#
# path = r'/Users/caiqinxiong/PycharmProjects/python/day06'
# print(get_size(path))
#
#
# import os
#
# def file_size(path):
#     size = 0
#     if os.path.isdir(path):
#         for d in os.listdir(path):
#             new_path = os.path.join(path, d)
#             ret = file_size(new_path)
#             size += ret
#     else:
#         size += os.path.getsize(path)
#     return size
#
#
# path = r'/Users/caiqinxiong/PycharmProjects/python/day06'
# ret = file_size(path)
# print(ret)

import time

# print(time.time())
# ret = time.localtime()
# print(ret)
# print(ret[1])

# print(time.strftime('%Y-%d-01 00:00:00'))
import sys
# print(sys.modules)
print(sys.path)
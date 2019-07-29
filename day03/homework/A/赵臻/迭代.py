#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time : 2019/7/25 0025 11:31
@Author : 赵臻
@File : 迭代.py
@Software: PyCharm
'''

# 有一个无序的序列list_c = [37, 99, 73, 48, 47, 40, 40, 25, 99, 51], 请先排序并打印输出
# 分别尝试插入[20，40，41，100]到序列中合适的位置，保证其有序

list_c = [37, 99, 73, 48, 47, 40, 40, 25, 99, 51,99]
list_s = [20, 40, 41, 100]

# 首先进行排序
order_list = sorted(list_c)
# 浅复制，保留原来数据
ret = order_list[:]

def insert_sort(ret, num):
    # 索引起点
    low = 0
    # 索引终点
    high = len(ret)
    # 起点索引大于或等于列表最后一个元素的索引，条件无法进入
    while low < high:
        # 取列表中间点的索引
        mid = (low + high) // 2
        #  条件判断，如果待插入列表的值小于有序列表对应mid索引的值，就向左查询
        if num < ret[mid]:
            # 同时确认这个中间点mid索引就是ret列表的high最高索引
            high = mid
        # 如果待插入列表的值大于有序列表对应mid索引的值，就向右查询，求中点
        else:
            # 同时确认这个中间点mid索引就是ret列表的开始索引low的值
            low = mid + 1
    # 这个开始索引low就是最终计算出来的待插入索引的位置low，所以返回low
    return low
# 循环去取待插入列表的元素
for num in list_s:
    # 调用上面的函数取出插入元素索引值
    index = insert_sort(ret, num)
    # 就地插入对应索引的值到列表ret中
    ret.insert(index, num)
# 打印插入元素后的列表
print(ret)
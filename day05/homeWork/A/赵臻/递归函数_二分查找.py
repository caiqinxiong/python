#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File  :  递归函数_二分查找.py
@Time  :  2019/08/05 16:06:09
@Author:  赵臻 
'''

def binary_search(num_list,value):
    num_list=sorted(num_list)
    left = 0
    right = len(num_list)
    while left <= right:
        mid = (right+left)//2
        if num_list[mid] > value:
            right = mid - 1
        elif num_list[mid] < value:
            left = mid + 1
        else:
            return '{} <----> 元素\033[031m{}\033[0m在列表中的下标为：\033[031m{}\033[0m'.format(num_list,value,mid)
    return '元素\033[031m%s\033[0m不存在指定列表中'%value

num_list = [12,23,67,34,56,77,87,99,120,16,2,9]
ret = binary_search(num_list,77)
print(ret)


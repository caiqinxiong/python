# -*- coding:utf-8 -*-
# Author:caiqinxiong
#集合主要用于关系测试
#集合，去重，无序的
list_1 = [1,2,4,1,3,4,5,6,7,8,6,9]
list_1 = set(list_1)
print(list_1,'\n',type(list_1))

list_2 = set([1,4,6,3,9,12,34])
print(list_2)
#交集
print("交集")
print(list_1.intersection(list_2))
print(list_1 & list_2)
#并集
print('并集')
print(list_1.union(list_2))
print(list_1 | list_2)
#差集
print(list_1.difference(list_2))
print(list_1 - list_2)
print(list_2.difference(list_1))
print(list_2 - list_1)

#子集
print(list_1.issubset(list_2))
print(list_1.issubset(list_1))
#父集
print(list_1.issuperset(list_2))
#对称差集，把公共部分去掉
print("对称差集，把公共部分去掉")
print(list_1.symmetric_difference(list_2))
print(list_1 ^ list_2)
print("########################")
#没有交集时返回true
list_3 = set([1,3,5])
list_4 = set([2,4,6])
print(list_3.isdisjoint(list_4))
list_4 = set([1,2,4,6])
print(list_3.isdisjoint(list_4))

print(list_3.add(999))
print(list_3)
list_3.update([888,777,999])
print(list_3)
print(len(list_3))
#去重的，只有删除一个
list_3.remove(999)
print(list_3)
#随机删除一个
print(list_3.pop())
#remove的没有的话程序报错，discard不报错
print(list_3.discard(999))
print(list_3)


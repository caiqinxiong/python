# -*- coding:utf-8 -*-
# Author:caiqinxiong

aa = [1,2,3]
print(aa)
print(aa[2])
#列表中可以做运算或其他操作
bb = [i*3 for i in range(10)]
print(bb)
len(bb)
print("###################")
print(bb[3])#列表把所有数据都加入到内存了，直接打印第四个元素时，已经准备好
print("###################")


a = []
for i in range(10):
    a.append(i*3)
print(a)

#生成器,bb里存里生成的列表(访问的时候才生成数据，在百万级数据的时候，性能就出来了）
bb = (i*3 for i in range(10))
print(bb )
for i in bb:
    print(i)

print("###################")
print(bb[3]) #生成器是用到了才生成，要一个一个生成，直接打印第四个元素时，没有准备好（还没生成）
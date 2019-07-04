# -*- coding:utf-8 -*-
# Author:caiqinxiong
#接列表生成器
#生成器，只有被调用都时候才会生成相应都数据
#只有一个next方法
#生成器,bb里存里生成的列表(访问的时候才生成数据，在百万级数据的时候，性能就出来了）
bb = (i*3 for i in range(10))
print(bb )
#for i in bb:
#    print(i)
#只记住了当前位置，只能往后一个，不能往前（为了节省内存空间）
print(bb.__next__())
print(bb.__next__())
print(bb.__next__())

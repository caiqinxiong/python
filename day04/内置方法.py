# -*- coding:utf-8 -*-
# Author:caiqinxiong
#all()方法，元素全为真时，返回真
print(all([0,-1,2,5,7]))
print(all([1,-1,2,5,7]))
#any()任意一个为真，返回真
print(any([0,0,0,1]))
print(any([0,0,0]))
print(any([]))
#bin()十进制转二进制
print(bin(255))
print(bin(2))
print(bin(4))
a=bytes('abcdefg',encoding='utf-8')#不可修改
b=bytearray('abcdefg',encoding='utf-8')#可修改
print(a.capitalize(), a)
print(b)
print(b[0])
b[0]=100
print(b)
print('#转八进制')
print(oct(16))
print(oct(15))
print('转16进制')
print(hex(15))

#判断是否可被调用
print(callable([1,2,3]))
def haha():pass
print(callable(haha))

print(chr(100))
print(chr(97))

print(dir(dict))
print(dir(str))
#divmod()返回商和余数
print(divmod(5,2)) #5／2
print(divmod(5,1))#5／1
print(divmod(10,5))#5／1


print("######################")
#过滤出你想要的数据
res = filter(lambda n:n>5,range(10))
for i in res:
    print(i)

print("######################")
#map将数据进行处理
res = map(lambda n:n*2,range(5)) # [i*2 for i in range(5)]
for i in res:
    print(i)
print(res)
print([i*2 for i in range(5)])
print("######################")
#求0～9的和,   reduce
import functools
res = functools.reduce(lambda x,y:x+y,range(10))
res2 = functools.reduce(lambda x,y:x*y,range(1,10))#10!,10的阶乘
print(res)
print(res2 )
print("######################")

a = {1:23,4:21,-4:89 ,99:71}
print(a)
print(sorted(a.items()))#按key来排序，得到list
print(sorted(a.items(),key=lambda x:x[1]))#按值来排序
print("######################")
a=[1,2,3,4,5,6,7,8 ]
b=['a','b','c','d']
for i in  (a,b):
    print(i)
print("######################")
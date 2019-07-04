# -*- coding:utf-8 -*-
# Author:caiqinxiong
# 生成器
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a,b = b,a+b
        n = n+1
    return 'done'

#fib(10)
print("#############")
def fib2(max):
    a=0
    b=1
    for i in range(max):
        #print(b)
        yield b
        #a=b
        #b=a+b
        a, b = b, a + b  #相当于元组 t = (a,a+b), a=t[0],b=t[1]
f=fib2(10)
print(f.__next__())
print(f.__next__())
print("############### ")
for i in f:
    print(i)

g=fib(6)
while True:
    try:
        x = next(g)
        print('g:',x)
    except StopIteration as e:
        print('hahahahahaha', e.value)
        break
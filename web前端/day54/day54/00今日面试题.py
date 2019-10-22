"""
问:执行完下面的代码后,  l,m的内容分别是什么?
"""

def func(m):
    for k,v in m.items():
        m[k+2] = v+2

m = {1: 2, 3: 4}
l = m  # 浅拷贝
from copy import deepcopy
l2 = deepcopy(m)
l[9] = 10
l2[90] = 100
# func(l)
m[7] = 8

# 1. 在Python中遍历字典的时候能不能对字典本身做涉及键(key)的操作
# 2. 深浅拷贝的理解

print("l:", l)
print("l2:", l2)
print("m:", m)


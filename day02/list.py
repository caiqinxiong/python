# -*- coding:utf-8 -*-
# Author:caiqinxiong
import copy
__list = ['cai','li','zhang','wang']
print(__list)
print(__list[3])
print(__list[1:3])
#等于2<3
print(__list[2:3])
print(__list[2:])
print(__list[-3:-1])
print(__list[:2])
print(__list[0:2])
__list.append('xin')
print(__list)
__list.insert(2,"xiao")
print(__list)
#在当前索引处插入
__list.insert(__list.index("xiao"),'xin')
print(__list)
#只删除找到的第一个
__list.remove('xin')
print(__list)
del __list[-1]
print(__list)
print(__list.pop())
print(__list)
print(__list.insert(__list.index("zhang"),'xin'))
print(__list)
print(__list.count('cai'))
#__list.clear()
__list.reverse()
print(__list)
print(__list.sort())
print(__list)
__list.extend([["caiqinxiong","lixiaoxin"]])
print(__list)
#浅复制
#name2 = copy.copy(name)
name = __list.copy()
print(name)
__list[-2] = '张'
__list[-1][0] = 'CAIQINXIONG'
print(__list)
print(name)
#修改name，__list也会改变，指向同一块内存地址
name[-1][0] = 'caiqinxiong_cai'
print(__list)
print(name)
#等号赋值也不行
name2 = name
print(name2)
name[-1][0] = '哈哈哈'
print(name)
print(name2)
#深复制
name3 = copy.deepcopy(name)
name[-1][0] = '呵呵'
print(name)
print(name3)
#隔2个打印
print(name[::2])




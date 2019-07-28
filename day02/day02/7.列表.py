# 数据结构
# 列表list
# lst = ['张晗','胡日查','老王','周老板','小强']


# print(lst)
# 索引-下标  通过索引(下标)取值
# print(lst[0])
# print(lst[1])
# print(lst[2])
# print(lst[3])
# print(lst[4])
# print(lst[5]) # 报错 IndexError: list index out of range
# print(lst[-1])
# print(lst[-2])
# print(lst[-3])
# print(lst[-4])
# print(lst[-5])



# 切片 [1~3)
# print(lst[:])
# print(lst[:2])
# print(lst[2:])
# print(lst[1:3])
# print(lst[-3:-1:1])   # start:end:step
# print(lst[-3:-1:1])
# print(lst[-1:-3:-1])
# print(lst[::-1])
# print(lst[::2])
# print(lst[1::3])

# lst = ['张晗','胡日查','老王','周老板','小强']
# lst2 = lst[:]
# print(lst == lst2)
# print(id(lst))
# print(id(lst2))
# 列表的拷贝
# lst3 = lst.copy()
# print(lst)
# print(lst2)
# print(lst3)

# 列表的增 删 改 查
# 增
# append
# insert
lst = [1,2,3,4,5,6,7,8,9,'alex','老王',True,12.334]
# l = lst.append('贡金敏')
# print(lst)
# lst.insert(0,'胡日查')
# print(lst)
# lst.insert(10,'周老板')
# print(lst)

# lst.remove(8)
# print(lst)

# n = lst.pop()
# print(n)
# print(lst)
# n = lst.pop()
# print(n)
# print(lst)
# lst.clear()
# print(lst)
# del lst[8]
# print(lst)


# 改
# lst = [1,2,3,4,5,6,7,8,9,'alex','老王',True,12.334]
# a = 'alexsb'
# lst[9] = a
# print(lst)
# lst[8] = 7+5

# 写一个列表，描述一个人
# [姓名,密码,年龄]
# l2 = []
# name = input('name :')
# l2.append(name)
# pwd = input('password :')
# l2.append(pwd)
# age = input('age :')
# l2.append(age)
# print(l2)

# l = ['王剑', '6666', '20']
# l2 = ['周老板', '123456', '50']
# lst = []
# lst.append(l)
# lst.append(l2)
# print(lst)

# 修改王剑的年龄 --> 22
# lwang = lst[0]
# lwang[2] = 22
# print(lwang)
# print(lst)
#
# lst[0][2] = 22
# print(lwang)
# print(lst)

# 浅拷贝
# l = ['alex',123,True,['王剑', '6666', '20'],['周老板', '123456', '50']]
# l2 = l[:]
# l3 = l.copy()

# l2.append('hello,world')
# print(l)
# print(l2)
# print(l3)

# l2[3].append('hello kitty')
# print(l)
# print(l2)
# print(l3)

# import copy
# l2 = copy.deepcopy(l)
# l2[3].append('hello kitty')
# print(l)
# print(l2)
# lst = [1,2,3]
# l = ['alex',123,True]
# l2 = ['alex',123,True]
# l[2] = False
# print(l)
# print(l2)
#
# lst = [1,2,3]
# l = ['alex',123,True,lst]
# l2 = ['alex',123,True,lst]
# lst.append(4)
# print(l)
# print(l2)

# l = ['wusir','alex','alex']
# print(l.index('alex'))
# print('alex' in l)
# print('alex2' in l)
# print('alex2' not in l)
# print('alex' not in l)

# 练习题
    # 循环5次
    # 输入用户的名字，如果名字之前存在了，就提示已经存在
    # 如果这个名字之前未存在，把这个名字添加到列表中
    # 最后打印列表

# n = 0
# l = []
# while n<5:
#     name = input('username :')
#     if name in l:
#         print('您输入的用户名%s已经存在'%name)
#     else:
#         l.append(name)
#         n += 1    # 只有当用户输入5个不重复的用户名程序才结束
# print(l)


# n = 0
# l = []
# while n<5:
#     name = input('username :')
#     if name in l:
#         print('您输入的用户名%s已经存在'%name)
#     else:
#         l.append(name)
#     n += 1    # 只要用户输入5个用户名，不管重复与否程序都结束
# print(l)

# l = [3,2,5,7,1,9,10]
# l.sort()
# print(l)
















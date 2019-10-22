# 可变对象不能做关键字参数

# def foo(arg, li=[]):
#     li.append(arg)
#     return li
#
# list1 = foo(21)
# list2 = foo(21, [1,])
# list3 = foo(28)
#
# print(list1)
# print(list2)
# print(list3)

# li.append()没有返回值
def foo(arg, li=[]):
    return li.append(arg)

list1 = foo(21)
list2 = foo(21, [1,])
list3 = foo(28)

print(list1)
print(list2)
print(list3)

# list5 = [11, 22, 33, 44, 55]
# print(list5[10:])


# 打乱列表的顺序
# import random
# random.shuffle(list5)
# print(list5)

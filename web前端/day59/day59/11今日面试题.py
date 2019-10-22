list1 = [11, [22, 3], [4, ], [55, 66], 8, [9, [7, [12, [34, [26]]]]]]
# 去除多余嵌套的列表,得到[11, 22, 3, 4, 55, 66, 8]

# 小剥皮
# [11, [22, 3]]
# [11, [22, [3, 4]]
def func(x):
    return [a for b in x for a in func(b)] if isinstance(x, list) else [x]

def f(x):
    ret = []
    for b in x:
        if isinstance(b, list):
            for a in f(b):
                ret.append(a)
        else:
            ret.append(b)
    return ret

list2 = [11, 22, [33, 44], [55, [66, 77]], [88, [99, [100, [200, [300]]]]]]
ret = f(list2)
print(ret)
ret2 = func(list2)
print(ret2)




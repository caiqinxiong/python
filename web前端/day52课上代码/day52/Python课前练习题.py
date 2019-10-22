# 复习Python中的匿名函数

# ("a", "b")和("c", "d"),  用lambda表达式 --> [{"a": "c"}, {"b": "d"}]


t1 = ("a", "b")
t2 = ("c", "d")

def foo(t1, t2):
    return [{t1[0]: t2[0]}, {t1[1]: t2[1]}]

f = lambda a, b:[{a[0]: b[0]}, {a[1]: b[1]}]
ret = f(t1,t2)
print(ret)






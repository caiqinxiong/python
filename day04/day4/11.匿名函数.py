# 如果一个函数中的功能非常小,只有一句代码
# 这个时候我们就可以把这个函数创建成一个匿名函数

# lambda表达式 == 匿名函数
# def func1(a,b):
#     return a+b
# ret = func1(1,2)
# print(ret)
# lambda 参数:返回值
# func2 = lambda a,b : a+b
# ret = func2(3,4)
# print(ret)

# print(func1.__name__)
# print(func2.__name__)


# lambda表达式 a,b两个值,求比较大的值
# lambda表达式 a为参数,求a的奇\偶性
# lambda表达式 a为参数,求a的绝对值

# func1 = lambda a,b : a if a>b else b
# ret = func1(10,2)
# print(ret)

# func2 = lambda a : '偶数' if a%2 == 0 else '奇数'
# ret = func2(11)
# print(ret)

# func3 = lambda a:a if a>0 else -a
# ret = func3(-2)
# print(ret)
# ret = func3(6)
# print(ret)

# func = lambda :2+3+4
# ret = func()
# print(ret)
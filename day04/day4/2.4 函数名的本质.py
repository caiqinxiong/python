def a():
    print('in a func')

# a()
# print(a)  # <function a at 0x00000000039C41E0>
# b = a
# print(b)
# b()
# 并不是只有函数名()才能调用一个函数
# 只要是函数的地址对应的变量都可以通过()调用函数
# l = [a]
# print(l[0])
# l[0]()
# 实际上函数的名字可以被赋值,也可以作为一个容器类型的元素,可以作为函数的参数,可以做返回值
# 变量怎么使用,函数的名字都可以怎么用
# def a():
#     '''可以作为函数的参数'''
#     print('in a func')
# def wahaha(f):
#     f()
# wahaha(a)

# def wahaha():
#     '''函数名可以作为返回值'''
#     def a():
#         print('in func a')
#     return a
#
# funca = wahaha()
# funca()
# 命名空间 名称空间 —— namespace
    # 内置命名空间 ：print() input() len() open()
    # 全局命名空间 ：定义在函数外部的所有变量
    # 局部命名空间 ：定义在函数内部的所有变量
# 作用域
    # 全局和局部 ：内置命名空间、全局命名空间
    # 局部作用域 ：内置命名空间、全局命名空间、局部命名空间

# 程序启动的一瞬间做了什么事儿？
# print() input() len() open() 函数
    # 为什么程序一启动这些名字就都可以用了

# 函数的嵌套调用
# def func2():
#     print('hello')
#     return True
#
# def func1():
#     print('start')
#     r = func2()
#     print('end')
#     return r
#
# ret = func1()
# print(ret)

# 函数修改全局变量
# a = 1
# def func():
#     # 在局部如果想要查看a的值是可以看的
#     # 如果想要引用a的值也是可以的
#     # 但是不能直接在函数内部修改全局空间中的值
#     b = a+1
#     print(b)
# func()
# print(a)

# global关键字可以修改全局变量的值，但是容易造成代码的安全隐患
# a = 1
# def func():
#     global a
#     a += 1
#     print(a)
# func()
# print(a)

# a = 1
# def func():
#     return a+1
# a = func()
# print(a)

# 高阶函数
# def outer():
#     def inner():
#         print('inner')
#     inner()
#     print('outer')
#
# outer()

# f = 1
# def outer():
#     f =2
#     def inner():
#         nonlocal f
#         f = f+1
#         print('inner',f)
#     inner()
#     print('outer',f)
# print('全局',1)
#
# outer()













# 函数名的本质: 第一类对象
    # 可以做参数 可以返回值 可以做容器类型的元素 可以赋值
# def aaa():
#     print('in aaa')
# print(aaa)

# bbb = aaa
# bbb() # ==aaa()
# l = [aaa]
# l[0]()
# dic = {'a':aaa}
# dic['a']()

# def wahaha(a):
#     print(a)
#     a()
# wahaha(aaa)

# def wahaha():
#     return aaa  # 在局部可以使用全局的名字
# b = wahaha()
# print(b)
# b()

# 闭包
# 在函数内部引用了外部函数的变量
# def outer(a):
#     def inner():
#         print(a)

# 装饰器 :框架中用到.
# 1.别人写好的你会用 2.你现在不会写根本不影响你写代码\写项目 3.如果你能写一些简单的就先写着,以后做资深开的时候都用得上
# def outer(func):
#     def inner(*args,**kwargs):
#         ret = func(*args,**kwargs)
#         return ret
#     return inner

# django框架里 提供了一个login装饰器
# def index():
#     pass
#
# @login
# def shop_car():
#     pass
#
# @login
# def add_to_car():
#     pass
#
# def show_goods():
#     pass
# 场景 有一个功能,是你知道会用到的,但是你不知道程序员在哪个地方会用到,搞成一个装饰器,把使用权交给程序员
# 程序员在设计程序的阶段,想往哪儿添加,直接在这个函数上加上装饰器就行了.

# def outer(func):
#     def inner(*args,**kwargs):
#         if 'shop' in func.__name__:
#             with open('wrapper.log','a',encoding='utf-8') as f:
#                 f.write('%s 被执行了\n'%func.__name__)
#         else:
#             print('%s 被执行了\n'%func.__name__)
#         ret = func(*args,**kwargs)   # func = index
#         return ret
#     return inner
#
# @outer
# def home():
#     print('我是index函数')
#     return True
#
# @outer
# def index():
#     print('我是index函数')
#     return True
#
# @outer
# def shopp_car():
#     print('我是index函数')
#     return True
#
# @outer
# def shop():
#     print('我是index函数')
#     return True

# 如果被装饰的函数是shop相关的函数,就把这个函数的执行行为记录在文件中,其余的函数执行行为打印在屏幕上
# shopp_car()
# index()
# shop()

# 迭代器
    # 可迭代(iterable)的: __iter__方法的是可迭代的
    # 迭代器 :  __iter__和__nect__是迭代器

    # 可迭代的: 可以被for循环的(列表\字典\元组\集合\字符串)
        # 如果是可迭代,而不是迭代器,那么可以被for循环多次
# lst = [1,2,3,4]
# for i in lst:
#     print(i)
# print('-->',i)
# for i in lst:
#     print(i)
    # 迭代器: 通过执行 可迭代.__iter__ 总是能够把一个可迭代对象 变成迭代器(f文件句柄)
        # 如果变成迭代器,那么数据只能被for循环一次
        # 不取值的时候数据不存在 -- 节省内存
# lst = [1,2,3,4]
# lst_iterator = lst.__iter__()
# for i in lst_iterator:
#     print(i)
# for i in lst_iterator:
#     print(i)
# 生成器
    # 生成器函数

# def file_opt():
#     with open('egg_lst', encoding='utf-8') as f:
#         for line in f:
#             lst = line.strip().split('|')
#             yield lst
#
# username = input('用户名 :')
# password = input('密  码 :')
# 生成器 = file_opt()
# for l in 生成器:
#     if l[1] == username and l[2] == password:
#         print('登录成功')
#         break
    # 生成器表达式
        # g = (i的操作 for i in 可迭代类型 if i的条件)
        # 列表推导式
            # lst = [i的操作 for i in 可迭代类型 if i的条件]
# 三元运算 : 结果 = 条件为真的结果 if 条件 else 条件为假的结果
# 匿名函数
    # func = lambda 参数1,参数2 : 返回的值

# 以下代码的输出是什么？请给出答案并解释。  [6,6,6,6] 在执行m(2)的时候,里面的for循环已经结束了,这个时候i = 3
# def multipliers():
#     return [lambda x:i*x for i in range(4)]
# print([m(2) for m in multipliers()])
# 请修改multipliers的定义来产生期望的结果。--> [0,2,4,6]

# def multipliers2():
#     lst = []
#     i = 0
#     def func(x):
#         return i*x
#     lst.append(func)  # [<function multipliers2.<locals>.func]
#     i = 1
#     def func(x):
#         return i * x
#     lst.append(func) # [<function multipliers2.<locals>.func,<function multipliers2.<locals>.func]
#     i = 2
#     def func(x):
#         return i * x
#     lst.append(func)  # [<function multipliers2.<locals>.func,<function multipliers2.<locals>.func,<function multipliers2.<locals>.func]
#     i = 3
#     def func(x):
#         return i * x
#     lst.append(func)
#     # [<function multipliers2.<locals>.func,<function multipliers2.<locals>.func,<function multipliers2.<locals>.func,<function multipliers2.<locals>.func]
#     return lst
#
# l = multipliers2()
# print(l)
# print(l[0](2))

# def func_o():
#     a = 1
#     def func():
#         print(a)
#     a = 2
#     a = 3
#     return func
#
# func =func_o()
# func()


# 要想产生预期的[0,2,4,6]应该怎么改
# def multipliers2():
#     i = 0
#     def func(x):
#         return i*x
#     yield func
#     i = 1
#     def func(x):
#         return i * x
#     yield func
#     i = 2
#     def func(x):
#         return i * x
#     yield func
#     i = 3
#     def func(x):
#         return i * x
#     yield func
#
# l = multipliers2()
# func = l.__next__()
# print(func(2))
# func = l.__next__()
# print(func(2))

#
# def multipliers2():
#     for i in  range(4):
#         func = lambda x:i*x
#         yield func
#
# l = multipliers2()
# func = l.__next__()
# print(func(2))
# func = l.__next__()
# print(func(2))
# func = l.__next__()
# print(func(2))
# func = l.__next__()
# print(func(2))

# def multipliers2():
#     return (lambda x:i*x for i in  range(4))
# ret = [func(2) for func in multipliers2()]
# print(ret)

# 小练习
iter = [1,2,3,4,5].__iter__()
iter2 = ['a','b','c'].__iter__()
for i in iter:
    print('-->',i)
    for j in iter2:
        print(i,j)
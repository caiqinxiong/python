# -*- coding:utf-8 -*-
# caiqinxiong 
# 2019/7/28 上午10:43

# # 监听
# def listen():
# with open(r'operate.log',mode='r',encoding='utf-8') as f:
#         while True:
#             conten = f.readline().strip()
#             if 'error' in conten:
#                 yield conten
#
# for conten in listen():
#     print(conten)
#
# # 操作监听的文件
# def wite_file():
#     f = open(r'operate.log',mode='a',encoding='utf-8')
#     inp = input()
#     f.write(inp)
#     f.close()
#
# wite_file()

# # 利用生成器来提高读取效率
# def get_user():
#     with open(r'userinfo', mode='r',encoding='utf-8') as f:
#         for line in f:
#             user,pwd = line.strip().split('|')
#             yield user,pwd

# lst = [i for i in range(1,31) if i % 3 == 0]
# print(lst)
#
# lst = [i**2 for i in range(1,31) if i % 3 == 0]
# # print(lst)
#
# def add(n,i):
#     return n+i
#
# def test():
#     for i in range(4):
#         yield i
#
# g=test()
# for n in [1,10]:
#     g=(add(n,i) for i in g)
# #
# print(list(g))

# def demo():
#     for i in range(4):
#         yield i

# g = demo()
#
# g1=(i for i in g)
# print(list(g1))
# print(list(g))
# # g2=(i for i in g1)
#
# # print(list(g1))
# # print(list(g2))

#
# fun1 = lambda a,b: a if a> b else b
# ret = fun1(1,3)
# print(ret)
#
#
# func2 = lambda a:'偶数' if a % 2 == 0 else '奇数'
#
# print(func2(2))


'''
1、整理装饰器的形成过程，背诵装饰器的固定格式
'''

# 装饰器的固定格式

# def 装饰器的名字(func):
#     def inner(*args,**kwargs):
#         '''在执行被装饰的函数之前要做的事儿'''
#         '''判断是否登录'''
#         ret = func(*args,**kwargs)
#         '''在执行被装饰的函数之后要做的事儿'''
#         '''写log'''
#         return ret
#     return inner
#
# @装饰器的名字
# def wahaha():
#     pass
#
# wahaha()

'''
2、编写装饰器,在每次执行被装饰函数之前打印一句’每次执行被装饰函数之前都得先经过这里,这里根据需求添加代码’
'''

# def warrper(func):
#     def inner(*args,**kwargs):
#         print('每次执行被装饰函数之前都得先经过这里,这里根据需求添加代码')
#         ret = func(*args,**kwargs)
#         return ret
#     return inner
#
# @warrper
# def func():
#     print('in the func')
# func()

'''
3、编写装饰器,在每次执行被装饰函数之后打印一句’每次执行完被装饰函数之后都得先经过这里,这里根据需求添加代码’
'''
# def warrper(func):
#     def inner(*args,**kwargs):
#         ret = func(*args,**kwargs)
#         print('每次执行完被装饰函数之后都得先经过这里,这里根据需求添加代码')
#         return ret
#     return inner
#
# @warrper
# def func():
#     print('in the func')
# func()
'''
4、编写装饰器,在每次执行被装饰函数之前让用户输入用户名,密码,给用户三次机会,登录成功之后,才能访问该函数.
'''
# # 用户信息
# user_info = {'caiqinxiong': 'cai', 'lixiaoxin': '123'}
# def loggin(user_info):
#     '''登录'''
#     def warrper(func):
#         def inner(*args,**kwargs):
#             i = 3
#             while i > 0:
#                 i -= 1
#                 username = input('请输入用户名：')
#                 if username in user_info:
#                     j = 3
#                     while j > 0:
#                         j -= 1
#                         password = input('请输入密码：')
#                         if password == user_info[username]:
#                             ret = func(*args,**kwargs)
#                             return ret
#                         else:
#                             print('密码输入有误！')
#                             if j == 0:
#                                 print('您的尝试机会已用完，账号已锁定，请10分钟后重新尝试！')
#                                 exit(-1)
#                             else:
#                                 print('你还有%s次尝试机会！' % j)
#
#
#                 else:
#                     print('用户名不存在！')
#                     if i != 0:
#                         print('你还有%s次尝试机会！' % i)
#                     else:
#                         print('您的尝试机会已用完!')
#                         exit(-1)
#         return inner
#     return warrper
#
# @loggin(user_info)
# def func():
#     print('wlcome to oldBoy!')
#
# func()

'''
5、编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件,只支持单用户的账号密码,给用户三次机会），要求登录成功一次，后续的函数都无需再输入用户名和密码
'''
# FLAG = False
# def get_user(file):
#     with open(file,mode = 'r',encoding='utf-8') as f:
#         for line in f:
#             usr,pwd = line.strip().split('|')
#             yield usr,pwd
#
# def login(func):
#     def inner(*args,**kwargs):
#         global FLAG  # 将FLAG变量设置成全局变量
#         if FLAG:
#             ret = func(*args, **kwargs)
#             return ret
#         else:
#             for i in range(3):
#                 user = input('username :')
#                 passwd = input('password :')
#                 for usr,pwd in get_user('userinfo'):
#                     if usr == user and pwd == passwd:
#                         print('登录成功')
#                         FLAG = True
#                         ret = func(*args,**kwargs)
#                         return ret
#                 else:
#                     print('账号或密码错误！')
#             else:
#                 print('登录失败')
#     return inner
#
# @login
# def func1():
#     print('in the func1')
#
# @login
# def func2():
#     print('in the func2')
# func1()
# func2()

'''
6、编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件,可支持多账号密码），要求登录成功一次（给三次机会），后续的函数都无需再输入用户名和密码。
'''
'''
7、给每个函数写一个记录日志的功能，
功能要求：每一次调用函数之前，要将函数名称，时间节点记录到log的日志中。
所需模块：
import time
struct_time = time.localtime()
print(time.strftime("%Y-%m-%d %H:%M:%S",struct_time))
'''
# from functools import wraps
# import time
# def log(func):
#     @wraps(func)
#     def inner(*args, **kwargs):
#         ret = func(*args, **kwargs)
#         DATE = time.strftime('%Y-%m-%d %H:%M:%S')
#         with open(r'access.log', mode='a', encoding='utf-8') as f:
#             log_conten = '用户[%s]在%s执行了%s函数\n' % (args[0], DATE, func.__name__)
#             # print(log_conten)
#             f.write(log_conten)
#         return ret
#
#     return inner
#
# @log
# def func1():
#     print('in the func1')
#
# @log
# def func2():
#     print('in the func2')
#
# func1()
# func2()


'''
8、lambda是什么？试着把简单的需求写成lambda函数。
'''
# lambda 是匿名函数
# lambda表达式 a,b两个值,求比较大的值
# lambda表达式 a为参数,求a的奇\偶性
# lambda表达式 a为参数,求a的绝对值

# func1 = lambda a,b : a if a>b else b
# ret = func1(10,2)
# print(ret)
#
# func2 = lambda a : '偶数' if a%2 == 0 else '奇数'
# ret = func2(5)
# print(ret)
#
# func3 = lambda a:a if a>0 else -a
# ret = func3(-5)
# print(ret)
# ret = func3(10)
# print(ret)
#
# func = lambda :2+3+4+5
# ret = func()
# print(ret)

# def func():
#     def func1():
#         print('in the func1')
#     return func1
# f = func()
# f()
#
# def wahaha():
#     pass
#
# def login(func):
#     def inner(*args,**kwargs):
#         print('start')
#         ret = func(*args,**kwargs)
#         print('end')
#         return ret
#     return inner
# f = login(wahaha)
# f()

# from functools import wraps
# def wapper(func):
#     @wraps(func)
#     def inner(*args,**kwargs):
#         print(func.__name__)
#         ret = func(*args,**kwargs)
#         return ret
#     return inner
#
# @wapper
# def now():
#     print("2013-12-25")
#
# now()
'''
2. 列表推导式和生成器表达式 [i % 2 for i in range(10)] 和 (i % 2 for i in range(10)) 输出结果分别是什么？
'''
# # [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
# # 生成器的内存地址
# print([i % 2 for i in range(10)])
# print((i % 2 for i in range(10)))

'''
def multipliers():
    return [lambda x: i * x for i in range(4)]
print([m(2) for m in multipliers()])
'''
# def multipliers():
#     return [lambda x: i * x for i in range(4)] # lambda 参数 x：返回值 i * x for i in range(4) # 返回4个内存地址
# print([m(2) for m in multipliers()])
#
# for i in [lambda x: i * x for i in range(4)]: # 生成器被取值时，i最后都等于3了。
#     print(i(3))
#
# print((lambda a,b:a+b)(1,2))
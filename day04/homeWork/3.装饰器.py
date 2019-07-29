import time  # 时间模块
# 别人写好的一些功能,放在一个模块里
# 和时间相关的功能,就放在了time模块

# 格林威治时间 - 19700101 08:00:00 北京
# 格林威治时间 - 19700101 00:00:00 伦敦
# def timmer(funcname):   # funcname就是"func的内存地址"
#     def inner(*args,**kwargs):
#         # (1000000,20)  ()
#         start = time.time()
#         ret = funcname(*args,**kwargs)
#         print(time.time() - start)
#         return ret
#     return inner
#
# @timmer    # func = timmer(func) func = inner的内存地址
# def func(n,m):
#     print(n,m)
#     sum_num = 0
#     for i in range(n):
#         sum_num += i
#     return sum_num
#
# @timmer  # func2 = timmer(func2) # func2 = inner的内存地址
# def func2():
#     sum_num = 0
#     for i in range(10000000):
#         sum_num += i
#     return sum_num
# #
# # timmer(func)
# # timmer(func2)
#
# # 函数是写好的功能
# # 使用别人写的函数
# # timmer(func)
# # 你的代码有1000处都用到了我写的func
# # 把func改成timmer(func)改1000次
#
# # 如果可以在不改变使用者的调用方式的情况下,能够添加上计算时间的这个功能 就好了
# ret = func(100000,20)     # 想调用func,实际调的inner
# ret2 = func2()
# print(ret,ret2)

# 什么情况下用
    # 在已经写好发版的程序的基础上,需要对一个函数执行前后增加功能的时候
        # 开放封闭原则
                # 开放 ：对扩展是开放的
                # 封闭 ：对修改时封闭
    # 有的时候也会写好一些装饰器,加在需要装饰的函数上面
        # login  django框架里也这么用
        # log


# def login():
#     pass
#
# @login     # 判断用户的登录状况
# def 联系():
#     pass
#
# @login
# def 管理():
#     pass
#
# @login
# def 新随笔():
#     pass

# 论坛程序
# def log():
#     pass
#
# @log
# def 发布帖子():
#     pass
#
# @log
# def 评论():
#     pass


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

import time
from functools  import wraps

# 把这个函数看明白了,然后把原本打印在屏幕上的内容写到operate.log文件里,做成一个日志文件
def wrapper(func):
    @wraps(func)
    def inner(*args,**kwargs):
        ret = func(*args,**kwargs)
        t = time.strftime('%Y-%m-%d %H:%M:%S')
        log_conten = '在%s[%s]执行了%s函数' % (t, args[0], func.__name__)
        print(log_conten)
        with open('operate.log',mode='a',encoding='utf-8') as f:
            f.write(log_conten+'\n')

        return ret
    return inner

@wrapper
def login(name):
    print('%s登录啦'%name)

@wrapper
def register(name):
    print('%s注册啦'%name)
# print([register.__name__])

login('caiqinxiong')
register('alex')


print(register.__name__)









# 带参数的装饰器
# flask框架中 路由里用到了带参数的装饰器
# import time
# flag = False
# def timmer(flag):   # flag = True
#     def outer(func): # func = wahaha
#         def inner(*args,**kwargs):
#             if flag:
#                 start = time.time()
#                 ret = func(*args,**kwargs)
#                 print(time.time() - start)
#             else:
#                 ret = func(*args, **kwargs)
#             return ret
#         return inner
#     return outer
#
# @timmer(flag) # @outer = wahaha=outer(wahaha)
# def wahaha():
#     print('in wahaha')
#
# @timmer(flag)
# def wahaha1():
#     print('in wahaha1')
#
# @timmer(flag)
# def wahaha2():
#     print('in wahaha2')
#
# @timmer(flag)
# def wahaha3():
#     print('in wahaha3')
#
# wahaha1()
# wahaha2()
# wahaha3()
# wahaha()
from functools import wraps
import time
def log(filename):
    def wrapper(func):
        @wraps(func)
        def inner(*args,**kwargs):
            ret = func(*args,**kwargs)
            t = time.strftime('%Y-%m-%d %H:%M:%S')
            with open(filename,mode= 'a',encoding='utf-8') as f:
                f.write('在%s[%s]执行了%s函数\n'%(t,args[0],func.__name__))
            return ret
        return inner
    return wrapper

@log('login.log')
def login(name):
    print('%s登录啦'%name)

@log('register.log')
def register(name):
    print('%s注册啦'%name)

# print([register.__name__])
login('alex')
register('alex')
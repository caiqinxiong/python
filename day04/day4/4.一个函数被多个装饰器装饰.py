# def wrapper1(func):   # func = inner2
#     def inner1(*args,**kwargs):
#         print('before inner1')
#         ret = func(*args,**kwargs)
#         print('after inner1')
#         return ret
#     return inner1
#
# def wrapper2(func):    # func = wahaha
#     def inner2(*args,**kwargs):
#         print('before inner2')
#         ret = func(*args,**kwargs)
#         print('after inner2')
#         return ret
#     return inner2
#
# @wrapper1   # wahaha = wrapper1(inner2) = inner1
# @wrapper2   # wahaha = wrapper2(wahaha) = inner2
# def wahaha():
#     print('WAHAHA')
#
# wahaha()   # inner1


# timmer装饰器 计算被装饰的函数的执行时间
# login装饰器 检测被装饰的函数是不是登录,如果没有登录要先登录才能使用这个函数
# timmer装饰器永远紧贴着被装饰的函数
# login装饰器 可以任意的排列
# logger装饰器 可以任意的排列














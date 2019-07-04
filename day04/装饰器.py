# -*- coding:utf-8 -*-
# Author:caiqinxiong
#装饰器：本质是函数（装饰其他函数，就是为其他函数添加附加功能）
'''
原则：1.不能修改被装饰的函数源代码
     2.不能修改被装饰的函数调用方式
实现装饰器知识储备：
    1.函数既是"变量"
    2.高阶函数
    3.嵌套函数
    高阶函数+嵌套函数===》装饰器
'''
import  time

#装饰器
def timer(func):
    def warpper(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        stop_time = time.time()
        print('the function run time is %s'% (stop_time-start_time))
    return warpper
#装饰器用法
@timer

#普通函数
def fun01():
    time.sleep(3)
    print('in the test01!')

fun01()
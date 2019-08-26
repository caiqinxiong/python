# 凡是数据类型 都会或多或少带有一些 双下方法
#  __xxxx__ 魔术方法 内置方法
# 调用的时候总是不好好调用

# 'abc'.split('b')  # 正经调用str类型的split方法
# ret = 'abc'.__add__('efg')
# print(ret)
# print('abc' + 'edf')

# __str__
class Course:
    course_lst = []
    def __init__(self,name,period,price):
        self.name = name
        self.period = period
        self.price = price
    def __str__(self):
        return '%s,%s,%s'%(self.name,self.period,self.price)
# python = Course('python','6 months',19800)
# linux = Course('linux','5 months',17800)
# Course.course_lst = [python,linux]
# for course in Course.course_lst:
#     print(course)  # 打印一个对象总是打印内存地址,这个数据对我们来说没有用
    # 打印这个对象的时候查看这个对象的相关信息
    # print(obj) 打印一个对象 总是调用obj.__str__(),打印的是这个方法的返回值

# __new__
# class A(object):
#     def __new__(cls, *args, **kwargs): # 构造方法 开辟空间 构造对象的方法
#         obj  = object.__new__(cls)
#         return obj
#
#     def __init__(self):       # 初始化方法
#         print('init : ',self)
#         self.name = 'alex'

# 1.创建一块空间 : __new__
# 2.调用init
# A()

# 算法导论 - 微观
# 23个设计模式 - 宏观

# java语言

# 单例模式 - 只创建一个实例
# class A:
#     pass
#
# a1 = A()
# a2 = A()
# print(a1)
# print(a2)

class Singleton:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            obj = object.__new__(cls)
            cls.__instance = obj
        return cls.__instance

    def __init__(self,name):
        self.name = name

obj1 = Singleton('alex')
obj2 = Singleton('wusir')
print(obj1.name,obj2.name)

# 什么是单例模式?
# 怎么实现
    # 用new实现
    # new做什么用 在什么时候执行








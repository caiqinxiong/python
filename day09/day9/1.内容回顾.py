# 多继承 :一个类有多个父亲
    # 查找变量遵循mro算法
    # super :查找mro算法中的下一个类
# 多态 : 在python中处处是多态
# 封装 : 属性和方法的私有化 : 只能在类的内部调用
#     # 不能继承也不能在类的外部使用
#     # A.__私有变量
# 静态方法\类方法\属性方法  *****
    # 类方法 classmethod   *****
        # 默认接收cls参数,表示当前所在的类
        # 调用的时候 类名\对象名都可以调用
# class Student:
#     course = ['python','linux']
#     def __init__(self,name):
#         self.name = name
#     @classmethod
#     def show_courses(cls):
#         # 在这个方法中没有用到对象空间中存储的内容
#         print('可选择的课程有:',cls.course)
# Student.show_courses()
# alex = Student('alex')
# alex.show_courses()

    # 静态方法  ****
# class Student:
#     course = ['python','linux']
#     @staticmethod
#     def quit():
#         exit()
# obj = Student()
# Student.quit()
# obj.quit()
    # 属性方法  ***
        # 圆形面积 周长 年龄
# class House:
#     def __init__(self,length,width):
#         self.len = length
#         self.wid = width
#     @property
#     def area(self):
#         return self.wid *self.len
#
# house = House(10,10)
# print(house.area)

# 反射       *****
    # 通过字符串使用变量(包括 类 函数 方法 各种变量)
# class Manager:
#     pass
# import sys
# Man= getattr(sys.modules[__name__],'Manager')
# print(Man is Manager)

# def login():pass
# def register():pass
# import sys
# func1= getattr(sys.modules[__name__],'login')
# func2= getattr(sys.modules[__name__],'register')
# print(func1,func2)

# 模块的导入 *****
# import 模块名    # 模块名以小写开头 符合变量的命名规范
# 模块名.变量名

# from 模块名 import 变量名,函数名
# from 模块名 import 变量名 as 新名字,函数名
# from 模块名 import *
# 直接使用变量名就可以了

# 包的导入
# import 包.包.包.模块名 as 新名字
    # 新名字.变量名
# from 包.包.包 import 模块名
    # 模块名.变量名

# sys.path 模块导入是从path列表中找到路径,从路径下导入模块
    # 如果我们要导入的模块在path的路径下都没找到,那么就会报错

# 开发规范   *****
    # 后来拆了文件
        # 重新写入一遍数据
        # 读数据
# from 项目名称.core import student
# stu = student.Student()

# 日志模块   *****
# logging模块
# import logging
# from logging import handlers
# handlers.RotatingFileHandler
# handlers.TimedRotatingFileHandler
# sh = logging.StreamHandler()
# fn = logging.FileHandler(filename='xxx.log',encoding='utf-8')
# logging.basicConfig(
#     format= '',
#     datefmt= '',
#     level=logging.INFO,
#     handlers=[sh,fn]
# )


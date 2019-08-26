# 什么是反射
# 如果有一个变量名 是字符串数据类型的 你能获取到这个变量的值么?
# class Student:
#     def __init__(self):
#         self.name = 'alex'
#         self.age = 80
#         self.gender = 'male'
#
#     def show_info(self):
#         print('%s,%s'%(self.name,self.age))
# stu = Student()
# content = input('>>>')
# if hasattr(stu,content):
#     name = getattr(stu,content)   # stu.show_info  name=showinfo的地址
#     if callable(name):
#         name()
#     else:
#         print(name)
# if content == 'name':
#     print(stu.name)
# elif content == 'age':
#     print(stu.age)
# elif content == 'gender':
#     print(stu.gender)

# 对象的反射
    # hasattr(对象,'属性名') 判断对象是否有这个属性,有返回True
    # getattr(对象,'属性名') 返回对象中属性名对应的值
# 反射属性
    # val = getattr(对象,'属性名')
        # val就是属性的值
# 反射方法
    # val = getattr('对象','方法名')
        # val就是方法的地址
        # val() ==> 调用方法

# 类的反射
# class A:
#     role = 'China'
# print(getattr(A,'role'))  # 用类获取类的变量

# 模块的反射
# import time
# print(time.time())
# print(getattr(time,'time')())

# 反射
    # a.b ===== getattr(a,'b')

# name = 'alex'
# age = 84
# def func(*args):
#     print('wahaha')
# class Student:pass


# import sys
# print(getattr(sys.modules[__name__],'name'))
# print(getattr(sys.modules[__name__],'age'))
# getattr(sys.modules[__name__],'func')(1,2,3)
# print(getattr(sys.modules[__name__],'Student'))












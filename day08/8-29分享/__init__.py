# class A:
#     name = 'alex'
#
# print(A.name)
# print(getattr(A,'name'))   # 反射

class Student:pass
class Manager:pass

ident = 'Student'
# 通过字符串数据类型的ident值获取到对应的类
import sys
cls = getattr(sys.modules[__name__],ident)
print(cls)

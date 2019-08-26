# class Student:
#     def __init__(self,name):
#         self.name = name
#     @staticmethod     # 生命login方法是一个静态方法 ,不必传任何默认的参数
#     def login(flag):
#         print('登录程序',flag)
#         username = input('>>>')
#         stu = Student(username)
#         return stu
# # 要想调用login 必须现有对象
# # 要想创建对象 必须用户先输入名字
# # 得调用登录之后才开始input
#
# # 不必实例化就可以调用的login方法 不需要传递对象作为参数,就定义这个方法为静态方法
# obj = Student.login(flag = True)  # 用类名可以直接调用这个方法了
# print(obj.__dict__)

# class Manager:
#     def __init__(self,name):
#         self.name = name
#     @classmethod     # 装饰当前这个方法为一个类方法,默认传参数cls,表示当前所在的类名
#     def login(cls):
#         username = input('>>>')
#         stu = cls(username)
#         return stu
#
# obj = Manager.login()  # 用类名可以直接调用这个方法了
# print(obj.__dict__)


# class A:
#     def func(self):  pass  # 实例方法 self作为默认参数,需要用对象来调用
#
#     @classmethod
#     def func1(cls):  pass  # 类方法 cls作为默认参数,可以用类名来调用
#
#     @staticmethod
#     def func1():  pass  # 静态方法方法 没有默认参数,可以用用类名来调用
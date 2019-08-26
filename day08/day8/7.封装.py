# 三大特定 : 继承 封装 多态
# 封装
# 人狗大战
    # 规范的创建对象
        # 创建的所有人的属性名都能一致
        # 把所有的方法装进一个角色中
# 广义上的封装 : 把方法和变量都封装在类中
              # 在类的外部就不能直接调用了
# 狭义上的封装 : 在类的外部干脆不能调用了

# class Student:
#     def __init__(self,name):
#         self.__name = name  # 把name这个属性私有化了
#     def get_name(self):
#         return self.__name
#     def set_name(self,value):
#         if type(value) is str:
#             self.__name = value
#
# 老王 = Student('老王')
# print(老王.get_name())
# 老王.set_name(1010101010100010)
# print(老王.get_name())
# print(老王.__name)


# class Person:
#     def __init__(self,username,password):
#         self.username = username
#         self.__password = password
#
# p = Person('alex','alex3714')
# print(p.username)

# class A:
#     __val = []
#     def __init__(self):
#         print(A.__val)
#
# A()
# print(A.__val)

# class A:
#     def func(self):
#         self.__aaa()
#     def __aaa(self):
#         print('aaa')

# a = A()
# a.func()

# 在类的内部 ,实例变量(对象属性)可以变成私有的,类变量可以变成私有的,实例方法也可以变成私有的
# 一旦变成私有的就只能在类的内部使用,而不能在类的外部使用了

# 私有化到底是怎么做到的 :只是在类内部使用的时候对名字进行了包装 变成了_类名xxxx
# class B:
#     __abc = 123  # _类名xxxx
#     print(__abc) # 使用 都会由这个类进行一个变形 _类名xxxx
# print(B.__dict__)
# print(B.__abc)

# 私有的变量不能被继承
# class A:
#     def __func(self):   # _A__func
#         print('in A')
#
# class B(A):
#     def wahaha(self):
#         self.__func()   # _B__func
#
# b = B()
# b.wahaha()

# 毕业练习题
# class A:
#     def __init__(self):
#         self.__func()    # self._A__func
#     def __func(self):   # _A__func
#         print('in A')
#
# class B(A):
#     def __func(self):   # _B__func
#         print('in B')
#
# b = B()

# 在哪个类中调用方法,就在这个私有方法之前加上这个类中的变形
# 和self本身是谁的对象都没有关系









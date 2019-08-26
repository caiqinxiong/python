# 在python中处处是多态
# def func(int a,int b,int c):
#     pass
# java是比较严谨的,所有在传递参数的时候必须指定参数的类型才可以

# class User:pass
# class Student(User):pass
# class Manager(User):pass
#
# def change_pwd(person):
#     pass
# 希望指定的类型 既能够保证 学生对象能传进来  管理员也能传进来

# print(type('123'))
# alex = Manager()
# print(type(alex))
# 周老板 = Student()
# print(type(周老板))

# User这个类可以表现出多种状态 :学生的状态  管理员的状态
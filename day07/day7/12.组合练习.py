# 学生 : 姓名 性别 年龄 所学习的课程
# class Student:
#     def __init__(self,name,sex,age,course):
#         self.name = name
#         self.sex = sex
#         self.age = age
#         self.course = course
# class Course:
#     def __init__(self,cname,period,price):
#         self.name = cname
#         self.period = period
#         self.price = price
#
# php = Course('php','5 months',18000)
# python = Course('python','6 months',19800)
# go = Course('go','5 months',8999)
# tang = Student('汤青松','不详',80,python)
# print(python.price)
# print(tang.course.price)

# wang = Student('老王','不详',80,'php')
# tang.course = python
# wang.course = python
#
# print(tang.course.price)
# print(wang.course.price)
# python.price = 21800
# print(tang.course.price)
# print(wang.course.price)


# class Student:
#     def __init__(self,name,sex,age,course_price,course_period,course_name):
#         self.name = name
#         self.sex = sex
#         self.age = age
#         self.course_price = course_price
#         self.course_period = course_period
#         self.course_name = course_name
#
# tang = Student('汤青松','不详',80,19800,'5 months','python')
# wang = Student('老王','不详',80,19800,'5 months','python')
# print(tang.course_name)
# print(wang.course_name)
# wang.course_price = 21800
# tang.course_price = 21800

# class A:
#     def __init__(self,name):
#         self.name = name
#
# a = A('alex Li')
# a是对象,是A的对象
# a.name # 是对象a的属性
# a.name是个字符串'alex Li'
# 'alex Li'是str的对象
# 'alex Li'.split(' ')
# a.name.split(' ')
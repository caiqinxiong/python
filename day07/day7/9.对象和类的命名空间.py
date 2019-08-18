# class A:
#     静态变量 = '值'
#     def __init__(self,属性):
#         self.属性名 = 属性
#
#     def show(self):
#         print('展示一下所有的属性')
#
# a = A('参数')   # 对象a\
# print(a.静态变量) # 对象可以引用类的命名空间中的内容 包括方法和静态变量

# 类的命名空间中
    # 静态变量
    # 方法
# 对象的命名空间中
    # 对象指针
    # 实例变量/对象的属性

# class Person:
#     sum = 0   # 全家人的工资总和为0
#     def __init__(self):
#         self.salary = 1000
#
# # 一家人
# father = Person()
# mother = Person()
# mother.age = 18
# print(mother.age)
# # print(mother.sum)
# # print(mother.salary)
# Person.sum += mother.salary    # 用对象修改静态变量只要用到赋值,相当于在自己的空间中新建
# print('-->',mother.sum)
# print('person -->',Person.sum)
#
# Person.sum += father.salary
# print('-->',father.sum)
# print('-->',mother.sum)
# print('person -->',Person.sum)


# 例题:
# 写一个类 ,统计一共实例化了多少个变量?
# class Person:
#     count = 0
#     def __init__(self):
#         Person.count +=1
#
# alex = Person()
# print(alex.count,Person.count)
# wusir = Person()
# print(alex.count)
# print(wusir.count)
# print(Person.count)  # 2


# class A:
#     num = 0
#     def __init__(self):
#         self.num += 1
#
# a1 = A()
# a2 = A()
# a3 = A()
# print(A.num)   # 0
# print(a1.num,a2.num,a3.num)  # 1


# class A:
#     lst = []
#     def __init__(self):
#         self.lst.append(1)
#
# a1 = A()
# a2 = A()
# a3 = A()
# print(A.lst)
# print(a1.lst)
# print(a2.lst)
# print(a3.lst)

# class A:
#     lst = []
#     def __init__(self):
#         self.lst = [1]
#
# a1 = A()
# a2 = A()
# a3 = A()
# print(A.lst)
# print(a1.lst)
# print(a2.lst)
# print(a3.lst)

# class A:
#     lst = [0]
#     def __init__(self):
#         self.lst[0] += 1
#
# a1 = A()   # [1]
# print(A.lst)
# a2 = A()   # [2]
# print(A.lst)
# a3 = A()   # [3]
# print(A.lst)
# print(a1.lst)
# print(a2.lst)
# print(a3.lst)

# 操作静态变量的时候
# 如果是查看用类或者对象都可以
# 如果是修改 只用类名进行修改
# 不要在对象的空间中创建一个和类变量同名的实例变量

# class Student:
#     '''
#     这是一个学生类,描述了学生的选课和查看分数的行为
#     '''
#     def __init__(self,id,name,sex,phone):
#         self.id = id
#         self.name = name
#         self.sex = sex
#         self.phone = phone
#         self.course_lst = []
#
#     def choose_course(self):
#         print('选择课程')
#
#     def show_score(self):
#         print('查看分数')
#
# print(Student.__dict__)   # __dict__ 内置的属性 可以查看类或者对象的命名空间中存储了什么
# 老王 = Student(1,'老王','male','110119120999')
# print(老王.__dict__)
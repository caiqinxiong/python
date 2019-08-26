# class Student:
#     def __init__(self,name,birth):
#         self.name = name
#         self.birth = birth
#
#     @property     # 将一个方法伪装成属性
#     def age(self):
#         import time
#         return time.localtime().tm_year - self.birth
# alex = Student('alex',1930)
# print(alex.age)   # 名词

class Circle:
    def __init__(self,r):
        self.r = r

    @property
    def area(self):
        return 3.14*self.r**2

    @property
    def perimeter(self):
        return 2*3.14*self.r

c = Circle(10)
print(c.area)
print(c.perimeter)
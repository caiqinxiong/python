# 圆形类
# 属性 :半径
# 内部提供两个方法
# 计算周长 2πr
# 计算面积 πr**2
from math import pi
class Circle:
    def __init__(self,r):
        self.r = r
    def area(self):
        return self.r**2*pi
    def perimeter(self):
        return 2*self.r*pi

c1 = Circle(10)
c2 = Circle(20)
# print(c1.area())
# c1.r = 20
# print(c1.area())
# print(c2.area() - c1.area())
# 在哪里计算周长和面积?
# 返回值还是print?
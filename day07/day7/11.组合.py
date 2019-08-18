from math import pi
class Circle:
    def __init__(self,r):
        self.r = r
    def area(self):
        return self.r**2*pi
    def perimeter(self):
        return 2*self.r*pi

# 圆环类型
    # 属性 :大圆半径 小圆半径
    # 实现计算面积
    # 计算周长
class Ring:
    def __init__(self,outer_r,inner_r):
        c1 = Circle(outer_r)
        c2 = Circle(inner_r)
        self.outer = c1    # 如果一个属性和一个对象联系在一起 组合
        self.inner = c2
    def area(self):
        return self.outer.area() - self.inner.area()
    def perimeter(self):
        return self.outer.perimeter() + self.inner.perimeter()
# r1 = Ring(10,5)
# print(r1.area())
# print(r1.perimeter())


# class Ring:
#     def __init__(self,outer_r,inner_r):
#         self.outer_r = outer_r
#         self.inner_r = inner_r
#     def area(self):
#         o_area = self.outer_r**2 * 3.14
#         i_area = self.inner_r**2 * 3.14
#         return o_area - i_area
#     def perimeter(self):
#         return self.outer_r*2*3.14 + self.inner_r*2*3.14










class A:
    pass
    def func(self):
        print('in A')

class C(A):
    pass
    # def func(self):
    #     print('in C')

class B(A):
    pass
    # def func(self):
    #     print('in B')

class D(B):
    pass
    # def func(self):
    #     print('in D')
class E(C):
    pass
    # def func(self):
    #     print('in E')

class F(D,E):
    pass
    # def func(self):
    #     print('in F')
# f = F()
# f.func()
print(F.mro())  # 查看多继承中的继承顺序
# 顺序 遵循C3算法

# 重新认识super
# class D:
#     def func(self):print('D')
# class C(D):
#     def func(self):
#         super().func()
#         print('C')
# class B(D):
#     def func(self):
#         super().func()
#         print('B')
# class A(B,C):
#     def func(self):
#         super().func()
#         print('A')

# a = A()
# a.func()

# b = B()
# b.func()


# 在单继承中 super的作用就是找父类
# 在多继承中 super是找mro顺序的下一个类







# object
# 有很多__xxx__方法
# init方法也在object类中

# object类
# 在python3.x的所有类都是object的子类
# 所以对于一些内置的方法会写在object类中
# 如果子类不定义,在调用的时候最终会调用object类中的方法
# 就不会让程序出现不必要的错误了
# __init__方法就是其中的一个例子

# 所有继承了object类的类 ---- 新式类
# 在python2中 不继承object类的都是 经典类

# class A(object):
#     pass    # 新式类

# class A:
#     pass   # 经典类 :在多继承中遵循深度优先
             # 经典类中没有super和mro方法

# 把面向对象的基础知识掌握之后才来深入的了解复杂的继承关系

# 所有的py3中 的类都继承object 是新式类
# 在继承中 遵循 广度优先的 C3算法
# 也可以使用mro来查看继承顺序
# super这个方法 可以帮助我们查找到mro顺序中的下一个类





# class  Fruits:
#     discount = 0.8  # 折扣  # 类变量 静态变量
#     def __init__(self,name,price):  # 实例方法 初始化方法
#         self.name = name    # 实例变量 属性
#         self.pri = price
#         self.price = Fruits.discount * self.pri
#     def attack(self):pass   # 自定义实例方法
#     def bite(self):pass     # 自定义实例方法
# apple = Fruits('苹果',5)
# banana = Fruits('香蕉',7)
# 栗子 = Fruits('栗子',4)
# 李子 = Fruits('李子',10)
# pear = Fruits('梨',2)
# print(apple.price)
# print(李子.price)
# print(apple.pri * Fruits.discount)
# print(pear.pri * Fruits.discount)

# 类名一共有三个作用:
    # 可以调用类中的变量 Fruits.discount
    # 实例化创建一个对象 Fruits('苹果',5)
    # 调用一个方法(现在不常用):类名.方法名()

# 对象名
    # 查看对象的属性 对象名.属性
    # 调用对象的方法 对象名.方法名()

# 类和对象和实例和实例化
    # 什么是类 ? Dog Person Fruits
    # 什么是对象 ? alex 二饼 旺财 苹果 李子
    # 什么是实例 ? 对象就是实例
    # 实例化 是一个动词 类创造实例的过程叫做实例化
        # 对象 = 类名() 实例化

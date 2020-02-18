"""
反射
由字符串反向找 变量、函数、类
"""

import sys


class Person(object):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print("{} 在吃 {}".format(self.name, food))

    def dream(self):
        print("{} 在做白日梦！".format(self.name))


s = "person"

# 字符串首字母大写
s = s.capitalize()
print(s, type(s))

# 打印下当前可用的变量
print(locals()["s"])
print(locals().get("s"))

# # 反射
if hasattr(sys.modules[__name__], s):
    print("找到了")
    the_class = getattr(sys.modules[__name__], s)

    print(the_class)
    obj = the_class(name="赵导")
    obj.eat("炒饼")


# s(name="赵导")

print("=" * 120)


def f():
    a = 1
    b = 2
    c = 3
    print(locals())

f()





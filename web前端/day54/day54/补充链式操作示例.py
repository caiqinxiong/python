"""
Python模拟链式操作示例
"""

class Foo(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def wang(self):
        print("旺旺~")
        return self

    def run(self):
        print("哒哒~哒哒~")
        return self

f = Foo("二哥", 9000)
# 链式操作
f.wang().run()

# f2 = f.wang()
# f2.run()
f.run()

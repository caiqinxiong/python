""""""

"""
class Foo(object):
    def __enter__(self):
        print('进入')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('出去')

with Foo() as f1:
    print(1,f1)
    print(2)
"""

class Context:
    def __enter__(self):
        return self

    def __exit__(self, *args,**kwargs):
        pass

    def do_something(self):
        pass

with Context() as ctx:
    ctx.do_something()

# 请在Context类中添加代码完成该类的实现.







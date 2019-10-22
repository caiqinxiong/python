"""
装饰器
"""
from functools import wraps

# 装饰器
def func(f):
    @wraps(f)  # 修复装饰器带来的副作用
    def inner(*args, **kwargs):
        print("小强，老地方见！")
        f(*args, **kwargs)
        print("小强，物美价廉！")
    return inner


@func
def foo(name):
    """
    这个函数是个测试装饰器的函数
    :param name: 接收一个字符串类型的值
    :return: 打印一句话
    """
    print("hello", name)


if __name__ == '__main__':
    foo("小强")
    print(foo.__doc__)


# 进阶知识点：
# 1. 带参数的装饰器
# 2.多个装饰器装饰同一个函数的时候，执行顺序
# 3.带返回值的装饰器
# 4. 装饰类的装饰器
# https://q1mi.github.io/PythonBlog/post/advanced_decorator/
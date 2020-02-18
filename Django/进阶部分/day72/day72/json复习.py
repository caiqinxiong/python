"""
复习python中json模块的基本使用
"""

import json

s = '{"name":"xiaohei","age": 18}'
# 把字符串反序列化成Python中的数据类型
ret = json.loads(s)
print(ret, type(ret))

# 把字典序列化成Python中的字符串
ret2 = json.dumps(ret)
print(ret2, type(ret2))


class Person(object):
    def __init__(self, name):
        self.name = name


p1 = Person("口哥")

# def foo(a,b):
#     sss = "我是函数中的变量"
#     print("a+b=", a+b)
#
# foo(11,22)
# print(sss)


# def func():
#     print(s)
#     s = "小强"
# func()

# l1 = [11, 22, 33]
# l2 = list([11, 22, 33])  # 相当于实例化一个列表对象
# print(l1, l2)


s = '{"name": "xiaoqiang", "age": 38}'
import json
ret = json.loads(s)
print(ret)

# 这是单行注释
dict1 = {"name": "little strong", "age": 18}  # 行内注释

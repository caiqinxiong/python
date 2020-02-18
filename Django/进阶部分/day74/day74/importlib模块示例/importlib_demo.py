# from xx import oo

# print(oo.NAME)
# p = oo.Person("赵导")
# p.dream()



s = "xx.oo"

# m, n = s.split(".")
# from m import n
#
# p = n.Person("赵导")
# p.dream()

import importlib

# 根据字符串导入模块
# 通畅用来导入包下面的模块
o = importlib.import_module("xx.oo")
s2 = "Person"

# 由字符串找函数、方法、类  利用 反射
the_class = getattr(o, "Person")
p2 = the_class("小黑")
p2.dream()


# print(o.NAME)
# p = o.Person("赵导")
# p.dream()

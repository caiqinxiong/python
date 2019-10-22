"""
有一个列表[11, 2, 3, 3, 7, 9, 11, 2, 3],去重并且保持原来的顺序.
"""

l1 = [11, 2, 3, 3, 7, 9, 11, 2, 3]
ret = list(set(l1))
print(ret)
ret.sort(key=l1.index)  # 按值在l1中的索引进行排序
print(ret)

l2 = [
    {"name": "alex", "age": 36},
    {"name": "GoldBoss", "age": 30},
    {"name": "xiaoyima", "age": 18}
]
# 课后作业
l2.sort(key=lambda x: x["age"])
print(l2)

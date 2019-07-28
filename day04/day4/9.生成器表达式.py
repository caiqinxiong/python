# 生成器表达式
# 列表推导式的[] 换成() 就变成了生成器表达式了

# lst= [i*2 for i in range(5)]
# print(lst) # lst中的所有元素已经在内存里了

# gen = (i*2 for i in range(5))
# print(gen) # gen里什么也没有

# print('-->',gen.__next__())
# print(list(gen))
# for i in gen:
#     print(i)

# 迭代器 是一个可以被for循环的节省内存的类型
# 生成器 是程序员能够自己写的迭代器
    # 生成器函数 yield
        #  g = 生成器函数()
    # 生成器表达式
        # g = (表达式)
        # 列表推导式和生成器表达式所使用的的 "表达式是相同的"
# 所有的生成器都符合迭代器的特点
    # 1.一个一个的取值，而不是一次性把所有数据都创建出来,迭代器中的数据不取不创建
    # 2.只能按照顺序取，不能跳过也不能回头
    # 3.一个迭代器中的数据只能从头到尾取一次
# 从迭代器中取值的三种方式
    # 1.gen.__next__
    # 2.for n in gen:pass
    # 3.list(gen)

# 简单的for循环生成新列表 -->列表推导式联系起来
# 只要用到列表推导式 --> 把列表推导式转成生成器表达式
# 生成器函数 --> 处理文件

# 面试题一 : 生成器函数 + 生成器表达式
# def demo():
#     for i in range(4):
#         yield i
#
# g=demo()
#
# g1=(i for i in g)
# g2=(i for i in g1)
#
# print(list(g1))
# print(list(g2))
# 生成器中的值只能从头到尾取一次

# 面试题二:重点内容 : 生成器 + for循环
    # for循环一定要拆
# def add(n,i):
#     return n+i
#
# def test():
#     for i in range(4):
#         yield i
#
# g=test()
# for n in [1,10]:
#     g=(add(n,i) for i in g)
#
# print(list(g))

# 课后作业
    # 都去找一道生成器相关的面试题,并且解释清楚
# 需要一个从1-1000000的数字序列
# python2.7 range(100000000) 真的在内存中生成100000000个数
        #   xrange(100000000)并不是在执行的时候生成100000000个数
# python3.x range(100000000) 并不是在执行的时候生成100000000个数

# ran = range(0,5)
# print(ran)
# 找这个ran拿衣服了
# ran变成一个迭代器
# iterator = ran.__iter__()
# print(iterator)
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())
# 迭代器：
    # 1.一个一个的取值，而不是一次性把所有数据都创建出来,迭代器中的数据不取不创建
    # 2.只能按照顺序取，不能跳过也不能回头
    # 3.一个迭代器中的数据只能从头到尾取一次
# 可迭代器协议: 如果一个数据类型中有 iter方法 ,那么这个数据类型就是可迭代类型
# 迭代器协议:如果一个数据类型中有iter和next方法,那么这个数据类型就是一个迭代器类型
# print('__iter__' in dir(123))
# print('__iter__' in dir(123.43))

# 只是可迭代类型而不是迭代器
    # print('__iter__' in dir('abc'))
    # print('__iter__' in dir([1,2,3]))
    # print('__iter__' in dir({1,2,3}))
    # print('__iter__' in dir((1,2,3)))
    # print('__iter__' in dir({1:3}))
    # print('__iter__' in dir(range(10)))
# 文件操作符是一个迭代器
#     f = open(r'F:\python自动化27期\day4\test',encoding='utf-8')
#     print('__iter__' in dir(f))
#     f.close()

# 迭代器的特点:节省内存空间
# 除了文件操作符以外你见过的所有内容都不是迭代器类型
# 都只是可迭代类型
# 可迭代类型是可以通过某些方法转换成迭代器的

# 可迭代类型.__iter__方法可以把可迭代类型转换成迭代器
# l = [1,2,3,4,5,6]
# iter = l.__iter__()
# print(iter.__next__())
# print(iter.__next__())
# print(iter.__next__())
# print(iter.__next__())
# print(iter.__next__())
# print(iter.__next__())
# print(iter.__next__())

# l = [1,2,3,4,5,6]
# iter = l.__iter__()
# while True:
#     try:
#         print(iter.__next__())
#     except StopIteration:
#         break

# 所有能被for循环的至少是一个可迭代类型
# 今后如果我说xxx是一个迭代器,知道这个xxx并不是直接存储了内容,而是需要for循环才能获取每一个值

def make_cloth_simple(n):
    '''
    生成器函数,没有return 只有yield
    :param n:
    :return:
    '''
    print('做第一件衣服')
    yield 1    # 暂停键
    print('做第二件衣服')
    yield 2
    print('做第三件衣服')
    yield 3

ret = make_cloth_simple(1000000)
print(ret)   # generator 生成器 生成器的本质就是一个迭代器
# print(ret.__next__())
# print(ret.__next__())
# print(ret.__next__())
for i in ret:
    print(i)


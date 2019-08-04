# ord，chr，repr
# print(ord('a'))
# print(chr(97))

# repr 打印某个变量的值的时候 更便于区分类型
# print(repr('123'))
# print(repr(123))
# print(123)
# print('123')

# 列表的方法 永远是 lst.xxx(),xxx方法是专门属于list数据类型,
# 这个时候所有的修改都是针对这个列表lst本身的
# l = [1,2,3,4,5]
# l.reverse()   # lst.reverse lst反转 lst本身发生改变
# print(l)

# 内置函数不是作用在某一个类型上的,而是接收参数返回结果
# 这种情况下,翻转列表为了能够更节省空间,所以返回的是迭代器而不是新的列表
# ret = reversed(l)  # l本身不变
# print(l)
# print(ret)   # 迭代器iterator
# for i in ret:
#     print(i)

# filter 也是一个返回值为迭代器的函数
# lst = [1,2,3,4,5,6,7,8,9,10]
# for n in lst:
#     if n%3 == 0:
#         print(n)
# ret = filter(lambda n:n%3 == 0,lst)   # 生成器函数返回的是一个迭代器
# for i in ret:
#     print('i:',i)

# map 也是一个返回值为迭代器的函数
# lst = [1,2,3,4,5,6,7,8,9,10]
# ret = map(lambda n:n*2,lst)
# print(ret)
# for o in ret:
#     print(o)

# enumerate 枚举函数 enumerate(iterable,1)
# with open('goods_lst',encoding='utf-8') as f:
#     for num,line in enumerate(f,1):
#         print(num,line.strip().split('|'))

# zip 拉链方法
# a = [1,2,3,4]
# b = ['a','b','c','d']
# ret = zip(a,b)
# for i in ret:
#     print(i)

# lst =['换手率','涨跌幅']
# lst2 = [25,10]
# ret = zip(lst,lst2)
# print(list(ret))

# lst0 =[1,2]
# lst1 =['换手率','涨跌幅']
# lst2 = [25,10]
# ret = zip(lst0,lst1,lst2)
# for i in ret:
#     print(i)

# 练习题
# 现有两个元组(('a'),('b')),(('c'),('d'))，
# 请使用python中匿名函数生成列表[{'a':'c'},{'b':'d'}]
# tup1 = (('a'),('b'))
# tup2 = (('c'),('d'))
# ret= zip(tup1,tup2)
# iterator = map(lambda tu:{tu[0]:tu[1]},ret)
# print(list(iterator))



# ret1 = min(1,2,3,4,5)
# print(ret1)
# ret2 = min([2,3,-4,5],key=lambda n: n%4)
# dic = {'a':1,'b':0}
# ret3 = min(dic,key=lambda k:dic[k])
# # [1,0]
# print(ret3)

# 排序 : sorted
# l = [23,-45,43,-66,11,-22]
# ret = sorted(l)
# ret = sorted(l,reverse=True,key= lambda n:n%10)
# print(ret)
# for i in l:
#     print(i%10)

# [{'age':28},{'age':18},{'age':20}]
# l = [{'age':18},{'age':20},{'age':28}]
# lst = sorted(l,key= lambda n:n['age'])
# print(lst)


# 匿名函数/lambda:
    # 内置 :filter map sorted min max



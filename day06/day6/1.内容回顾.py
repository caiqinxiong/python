# 定义函数 调用函数
# 传参数 接受返回值

# 内容回顾
# 内置函数
    # open 文件操作
    # print\input
    # dir(数据) :显示这个数据能调用的方法
    # sum abs chr enumerate zip
# 必须要记住的5个有python特色的内置函数:
    # max min sorted 正常就是根据循环的每一项排序,
                  # 如果有特殊的条件key参数写一个函数逻辑,就根据返回值求最大\最小\排序
    # filter map 正常就必须先传function,返回值都是可迭代的
                # filter 是筛选符合function中条件的
                # map是统一对可迭代类型中每一个值进行加工处理的
# ret = max([1,23,43,6])
# # print(ret)
# 循环列表中的每一项,for循环出来的每一项是什么,在这里拿到的每一项就是什么
# 对这些拿到的值进行逐个比较
    # 1
    # max_num = 1
    # 23
    # 23 > max_num
    # max_num = 23
    # 43 > max_num
    # max_num = 43
    # 6  < max_num
    # max_num = 43

# dic = {'a':100,'b':10}
# ret = max(dic,key=lambda k:dic[k])
# print(ret)
# 循环字典
# 'a'
# lambda 'a':dic['a'] = 100
# max_num = dic['a']
# 'b'
# lambda 'b':dic['b'] = 10
# dic['a']  > dic['b']
# max_num = 'a'

# lst = [[1,2],[3,4],[1,9]]
# ret = max(lst,key=lambda item:sum(item))
# print(ret)

# ret = sorted([1,3,2,45,12,-1])
# print(ret)
# d = {'alex':[84,50],'wusir':[73,60]}
# ret = sorted(d,key=lambda k:d[k][1],reverse=True)
# print(ret)

# # 筛选符合条件的项 条件是: n>10
# ret = filter(lambda n:n>10,[1,5,12,30])
# print(ret)  # 迭代器
# for i in ret:
#     print(i)
#
# #对每一个元素进行加工,将加工之后的内容返回放在迭代器中
# ret= map(lambda n:n**2,[1,5,10])
# print(ret)   # 迭代器
# for i in ret:
#     print(i)

# dic = {'apple':[1,2,3],'banana':['a','b']}
# for index,k in enumerate(dic,1):
#     print(index,k)

# lst = [1,2,3]
# lst2 = ['a','b','c']
# ret = zip(lst,lst2)
# for i in ret:
#     print(i)

# 第一: 10个 用心的能记下来
# 第二: 如果后面用到了新的 还会在介绍的

# 递归 :
    # 自己调用自己,通过返回值return可控制递归的结束,
    # 通过参数来修改递归的逻辑和范围
    # 适合解决 大规模的某一件事,内部拆分出来的小规模的计算和大规模的逻辑完全一致
    # 大字典-套着小字典,小字典的处理逻辑和大字典一模一样
    # 学完os模块 留练习中午写(两种思路),下午讲

# 模块
    # random : randint randrange choice sample shuffle
    # re:
        # ret = findall(正则,待匹配的字符串) 找所有\
            # ret直接就是返回的所有结果
        # ret = search(正则,带匹配的字符串) 只找一个
            # ret
                # 如果匹配到了,返回一个自定义的正则的结果,通过ret.group()取值
                # 如果没有匹配到,返回None

# 晚上的时候播报 积分的结果和奖励
# 没交作业罚50 迟到的罚30
# 第8周的时候 所有全勤 全栈面试题
                # 发朋友圈20个赞


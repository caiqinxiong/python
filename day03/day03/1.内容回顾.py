# 格式化输出
    # name = input()
    # '你好，%s'%name

    # a = input()
    # b = input()
    # '%s * %s = %s'%(a,b,float(a)*float(b))
# 运算符
    # + - * / // % **
    # > < >= <= == !=
    # = += -= *= \+ %=
        # a+=2   a=a+2
    # () not and or
    # is 、is not
        # a is b 判断内存地址的
        # a == b 判断值的
# 字符编码
    # ascii码  只支持英文
    # unicode  万国码
    # utf-8    可变长的数据类型
    # GBK      中文编码
# 字节类型 = '你好'.encode('utf-8')
# print(字节类型)
    # str --> unicode
    # str转utf-8  字节类型 = '你好'.encode('utf-8')
    # utf-8转str  字符串   = b'\xe4\xbd\xa0\xe5\xa5\xbd'.decode('utf-8')
# 基础数据类型
    # 字符串
        # 索引 从0开始
        # 切片 [start:end:step]  顾头不顾尾 'abcd'[1:3] ==> 'bc'
        # strip (去掉两端的空白符 \t \n)
        # split (根据某一个指定字符进行切割)
        # join  ('|'.join(['1','2','3']=拼接结果=>'1|2|3'))
        # replace ('abcd'.replace('a','A',n)，将abcd字符串中的前n个'a'替换成'A')
        # upper 和 lower
        # isdigit isalpha
        # startswith endswith
    # 字典
        # d = {'k':'v'}
        # 增加 : d['kk'] = 'value'
        # 删除 : d.pop('k')    del d['kk']
        # 修改 : d['k'] = 'new value'
        # 查看 : print(d['k2'])  print(d.get('k2'))
        # 循环 :
            # for k in d:
               # print(k)
               # print(d[k])
    # 列表
        # [1,True,'abc',{'k':'v'},(1,2,3),[1,2,3]]
        # 索引
        # 切片
        # 增 ：append
        # 删 ：pop  remove('alex')
        # 改 : l[2] = 'alex_sb'
        # 查 : print(l[3])
        # 判断某个值是否在列表中 : True or False = 'alex' in lst
        # for i in lst:
            # print('列表中的每一项')
    # 元组 不可变的列表
        # (1,)
        # (1,[],{}) 元组中不可变数据类型都不能发生改变，但是如果是可变数据类型，内部内容可以变化
        # 索引
        # 切片
        # 查
# for
    # for i in 有多个元素的数据类型:
        # 在循环的时候，数据类型有多少个元素，就循环多少次
        # 这个缩进内部的代码就执行多少次
        # 且每一次循环，这个i会依次被赋值为这个数据类型中的元素
        # break
        # continue
    # else 当整个for循环没有被break的时候，就执行这句话
# 深浅拷贝

# 练习题难
# 大量的逻辑、循环、判断

# 补充内容：
    # 嵌套的for循环 99乘法表
    # 在for循环的过程中进行修改循环的对象
        # 在for循环一个列表、字典、元组，永远不要对这个列表、元组、字典进行修改
            # lst = ['alex','alexander','alex_li','wusir','eric','yuan']
            # del_l = []
            # for i in lst:
            #     if i.startswith('a'):
            #         del_l.append(i)
            # print(del_l)
            # for di in del_l:
            #     lst.remove(di)
    # 深浅拷贝和赋值
        # 赋值
        # a = []
        # b = a   # 赋值 a和b指的是同一个列表
        # a.append(1)
        # 列表发生变化  ab都能感知
        # a记录的是老王家地址，b也记录了老王家的地址

        # 浅拷贝 : 第一层发生的变化所有的列表互不干涉，如果是某个可变类型元素内部值变化，所有的对象共享
        # 1.切片 lst = lst1[:]
        # 2.lst2 = lst1.copy()
        # 3.import copy
          # lst3 = copy.copy(lst1)
        # 有一个列表
          # lst1 = [5,2,3,[1,2,4,{'k':'vvvv'}]]
          # 作业本
          # lst1 = [1,2,3]

        # 深拷贝
            # 不管这几个变量有多少层，只要互相是深拷贝的，那么这些数据永远没有交集
            # 互相之间的改变都不发生互相的影响
            # lst1 = [5,2,3,[1,2,4,{'k':'vvvv'}]]
            # lst2 = [5,3,3,[1,8,4,{'k':'vvvv','k2':'v2'}]]

# 集合 : 集合中所有的元素约束都和字典的key相同
    # 1.求多个集合之间的关系，并集 交集 差集(补集)
    #     linux = ['老王','老刘','小汤','小周']
    #     python = ['老王','老刘','小汤','老李']
        # 既学习linux也学习python
    # linux = {'老王','老刘','小汤','小周'}   # --> {'key':'value'}
    # python = {'老王','老刘','小汤','老李'}
    # print(linux&python)  # 交集
    # print(linux|python)  # 并集 去重
    # print(python-linux)  # 差集

    # 2.去除重复的内容
    # lst = [1,1,3,4]
    # s = set(lst)
    # print(s)

# 在不改变原顺序的情况下，去除一个列表当中重复的项 —— 不能用set集合来完成（答案在分享里）


# 基础数据类型分类记忆一
    # 数字类型 : bool int float
    # 序列类型 : str tuple list -- 索引 切片
    # 散列类型 : dict set       -- 无序的 并且元素、key必须可hash

# 基础数据类型分类记忆二
    # 可变数据类型 : list dict set
    # 不可变数据类型 :bool int float str tuple


# 一个练习题
# 求100以内的素数和
# 从2开始算，除了1和自己本身不能再被其他数整除 就是素数（质数）
# sum_num = 0
# for i in range(2,101):
#     for j in range(2,i//2+1):
#         if i%j == 0:break
#     else:
#         sum_num += i
#         print('%s是素数'%i)
# print(sum_num)

# 思考题
# 求1000以内的数
    # a + b + c == 1000
    # a + b == c





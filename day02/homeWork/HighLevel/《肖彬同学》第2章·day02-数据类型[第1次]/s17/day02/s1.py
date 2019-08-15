#!/usr/bin/python
# -*- coding:utf-8 -*-

# f = open('log','r',encoding='utf-8')
# data = f.read()
# f.close()
# print(data)

# f = open('log','rb')
# data = f.read()
# f.close()
# print(data)


# str
# name1 = "huangzhong1" str类的对象,
# name1.split()
# name1.strip()
#
# name2 = "huangzhong2"
# name2.split()
# name2.strip()
# name3 = "huangzhong3"
# name3.split()
# name3.strip()

# int
# num = 19

# list
# li = [1,2,3,43]

# dict
# dic = {'k1': 'v1'}

# ########################################## str 字符串 ##########################################
# name = 'alex' # str类的对象
# 1. capitalize 字符串首字母大写
# 自身不变，会生成一个新的值
# v = name.capitalize() # 自动找到name关联的str类，执行其中的capitalize技能
# print(name)
# print(v)

# 2. 将所有大小变小写，casefold牛逼，德语...
# name = 'AleX'
# v = name.casefold() # 跟牛逼，德语...
# print(name)
# print(v)

# 3. 将所有大小变小写
# name = 'AleX'
# v = name.lower()
# print(v)

# 4. 文本居中
# 参数1: 表示总长度
# 参数2：空白处填充的字符（长度为1）
# name = 'alex'
# v = name.center(20)
# print(v)
# v = name.center(20,'行')
# print(v)

# 5. 表示传入之在字符串中出现的次数
# 参数1： 要查找的值（子序列）
# 参数2： 起始位置（索引）
# 参数3： 结束位置（索引）
# name = "alexasdfdsafsdfasdfaaaaaaaa"
# v = name.count('a')
# print(v)
# v = name.count('df')
# print(v)

# v = name.count('df',12)
# print(v)
# v = name.count('df',0,15)
# print(v)

# 6. 是否以xx结尾
# name = 'alex'
# v1 = name.endswith('ex')
# print(v1)

# 7. 是否以xx开头
# name = 'alex'
# v2 = name.startswith('al')
# print(v2)

# 8. encode欠

# 9. 找到制表符\t,进行替换（包含前面的值）
# PS: \n
# name = "al\te\tx\nalex\tuu\tkkk"
# v = name.expandtabs(20)
# print(v)

# 10. 找到指定子序列的索引位置：不存在返回-1
# name = 'alex'
# v = name.find('o')
# print(v)
# v = name.index('o')
# print(v)

# 11.字符串格式化

# tpl = "我是:%s;年龄:%s;性别:%s"

# tpl = "我是:{0};年龄:{1};性别:{2}"
# v = tpl.format("李杰",19,'都行')
# print(v)

# tpl = "我是:{name};年龄:{age};性别:{gender}"
# v = tpl.format(name='李杰',age=19,gender='随意')
# print(v)

# tpl = "我是:{name};年龄:{age};性别:{gender}"
# v = tpl.format_map({'name':"李杰",'age':19,'gender':'中'})
# print(v)


# 12. 是否是数字、汉子.
# name  = 'alex8汉子'
# v = name.isalnum() # 字,数字
# print(v) # True
# v2 = name.isalpha()#
# print(v2)# False

# 13. 判断是否是数字
# num = '②'
# v1 = num.isdecimal() # '123'
# v2 = num.isdigit()   # '123'，'②'
# v3 = num.isnumeric() # '123'，'二'，'②'
# print(v1,v2,v3)


# 14. 是否是表示符
# n = 'name'
# v = n.isidentifier()
# print(v)

# 15.是否全部是小写
# name = "ALEX"
# v = name.islower()
# print(v)
# v = name.isupper()
# print(v)

# 16,.全部变大写，
# name = 'alex'
# v = name.upper()  # lower()
# print(v)

# 17.是否包含隐含的xx
# name = "钓鱼要钓刀鱼，\n刀鱼要到岛上钓"
# v = name.isprintable()
# print(v)


# 18.是否全部是空格
# name = '    '
# v = name.isspace()
# print(v)



# 19.元素拼接（元素字符串） *****
# name = 'alex'

# v = "_".join(name) # 内部循环每个元素
# print(v)

# name_list = ['海峰','杠娘','李杰','李泉']
# v = "搞".join(name_list)
# print(v)

# 20. 左右填充
# center,rjust,ljust
# name = 'alex'
# v = name.rjust(20,'*')
# print(v)


# 21. 对应关系 + 翻译
# m = str.maketrans('aeiou','12345') # 对应关系
#
# name = "akpsojfasdufasdlkfj8ausdfakjsdfl;kjer09asdf"
# v = name.translate(m)
# print(v)

# 22. 分割，保留分割的元素
# content = "李泉SB刘康SB刘一"
# v = content.partition('SB') # partition
# print(v)

# 23. 替换
# content = "李泉SB刘康SB刘浩SB刘一"
# v = content.replace('SB','Love')
# print(v)
# v = content.replace('SB','Love',1)
# print(v)

# 24，移除空白,\n,\t，自定义
# name = 'alex\t'
# v = name.strip() # 空白,\n,\t
# print(v)

# 25. 大小写转换
# name = "Alex"
# v = name.swapcase()
# print(v)

# 26. 填充0
# name = "alex"
# v = name.zfill(20)
# print(v)

# v1 = 'alex'
# v2 = 'eric'
#
# v = v1 + v2 # 执行v1的__add__功能
# print(v)


###### 字符串功能总结：
# name = 'alex'
# name.upper()
# name.lower()
# name.split()
# name.find()
# name.strip()
# name.startswith()
# name.format()
# name.replace()
# "alex".join(["aa",'bb'])


###### 额外功能：
# name = "alex"
# name[0]
# name[0:3]
# name[0:3:2]
# len(name)
# for循环，每个元素是字符


# 练习题
# name = "aleX"
# a
# v = name.strip()
# print(v)
# b
# v = name.startswith('al')
# print(v)
# v = name.replace('l','p')
# print(v)

# v = name.split('l')
# print(v) # 列表

# **** 转换成字节 ****
# name = "李杰"
# v1 = name.encode(encoding='utf-8') # 字节类型
# print(v1)
# v2 = name.encode(encoding='gbk') # 字节类型
# print(v2)


# ########################################## int 整数 ##########################################

# 1. 当前整数的二进制表示，最少位数
# age = 4 # 100
# print(age.bit_length())

# 2. 获取当前数据的字节表示
# age = 15
# v = age.to_bytes(10,byteorder='big')
# v = age.to_bytes(10,byteorder='little')
# print(v)
# 00000000 00001111 -> 15

# ########################################## bool 布尔值 ##########################################
# v = 0 # 1,-1
# v = ""
# v = []
# --> 空内容：False

# ########################################## list 列表 ##########################################
# ## int=xx; str='xxx'  list='xx'
# user_list = ['李泉','刘一','刘康','豆豆','小龙'] # 可变类型
# PS:
    # name = 'alex'
# 执行功能；
# 1.追加
# user_list = ['李泉','刘一','刘康','豆豆','小龙'] # 可变类型
# user_list.append('刘铭')
# print(user_list)
# 2. 清空
# user_list = ['李泉','刘一','刘康','豆豆','小龙'] # 可变类型
# user_list.clear()
# print(user_list)

# 3. 拷贝(浅拷贝)
# user_list = ['李泉','刘一','刘康','豆豆','小龙'] # 可变类型
# v = user_list.copy()
# print(v)
# print(user_list)

# 4. 计数
# user_list = ['李泉','刘一','李泉','刘康','豆豆','小龙'] # 可变类型
# v = user_list.count('李泉')
# print(v)

# 5. 扩展原列表
# user_list = ['李泉','刘一','李泉','刘康','豆豆','小龙'] # 可变类型
# user_list.extend(['郭少龙','郭少霞'])
# print(user_list)

# 6. 查找元素索引，没有报错
# user_list = ['李泉','刘一','李泉','刘康','豆豆','小龙'] # 可变类型
# v = user_list.index('李海')
# print(v)

# 7. 删除并且获取元素 - 索引
# user_list = ['李泉','刘一','李泉','刘康','豆豆','小龙'] # 可变类型
# v = user_list.pop(1)
# print(v)
# print(user_list)

# 8. 删除 - 值
# user_list = ['李泉','刘一','李泉','刘康','豆豆','小龙'] # 可变类型
# user_list.remove('刘一')
# print(user_list)

# 9. 翻转
# user_list = ['李泉','刘一','李泉','刘康','豆豆','小龙'] # 可变类型
# user_list.reverse()
# print(user_list)

# 10. 排序： 欠参数
# nums = [11,22,3,3,9,88]
# print(nums)
# 排序，从小到大
# nums.sort()
# print(nums)
# 从大到小
# nums.sort(reverse=True)
# print(nums)

######  额外：
# user_list = ['李泉','刘一','李泉','刘康','豆豆','小龙']
# user_list[0]
# user_list[1:5:2]
# del user_list[3]
# for i in user_list:
#     print(i)
# user_list[1] = '姜日天'
# user_list = ['李泉','刘一','李泉','刘康','豆豆',['日天','日地','泰迪'],'小龙']


# li = ['eric','alex','tony']
#
# v = len(li)
# print(v)
#
# li.append('seven')
# print(li)
#
# li.insert(0,'Tony')
# print(li)
#
# li[1] = 'Kelly'
#
# li.remove('eric')
# print(list)
#
# v = li.pop(1)
# print(v)
# print(li)
#
# del li[2]


# del li[0:2] # 0 =<x < 2
# print(li)

# li.reverse()
# print(li)

# for i in li:
#     print(i)

# ######################################### 强插：range,enumrate #########################################
# 1. 请输出1-10
# 2.7: 立即生成所有数字
# range(1,11) # 生成 1,23，，4,56.10

# 3.x: 不会立即生成，只有循环迭代时，才一个一个生成
# for i in range(1,11): #
#     print(i)

# for i in range(1,11,2): #
#     print(i)

# for i in range(10,0,-1): #
#     print(i)

# 1. 3.x 不会立生成，迭代之后才一个一个创建；
"""
    - 2.7：
        range()
        xrange()  不会立生成，迭代之后才一个一个创建；
    - 3.x
        range()  不会立生成，迭代之后才一个一个创建；
"""
# 2. range: 三个参数
#
# li = ['eric','alex','tony']
# # range,len,li循环
# for i in range(0,len(li)):
#     ele = li[i]
#     print(ele)


# li = ['eric','alex','tony']
# for i in li:
#     print(i)

# for i in range(0,len(li)):
#     print(i+1,li[i])


# enumerate额外生成一列有序的数字
# li = ['eric','alex','tony']
# for i,ele in enumerate(li,1):
#     print(i,ele)
#
# v = input('请输入商品序号：')
# v = int(v)
# item = li[v-1]
# print(item)

# ######################################### tuple：元组,不可被修改的列表；不可变类型 #########################################
# user_tuple = ('alex','eric','seven','alex')
# 1. 获取个数
# v = user_tuple.count('alex')
# print(v)
# 2.获取值的第一个索引位置
# v = user_tuple.index('alex')
# print(v)

####### 额外：
# user_tuple = ('alex','eric','seven','alex')
# for i in user_tuple:
#     print(i)

# v = user_tuple[0]

# v = user_tuple[0:2]
# print(v)

# user_tuple = ('alex','eric','seven',['陈涛','刘浩','赵芬芬'],'alex')
# user_tuple[0] = 123   x
# user_tuple[3] = [11,22,33] x
# user_tuple[3][1] = '刘一'
# print(user_tuple)

# li = ['陈涛','刘浩',('alex','eric','seven'),'赵芬芬']
# ****** 元组最后，加逗号 ******
# li = ('alex',)
# print(li)

# ######################################### dict：字典: 可变类型 #########################################

# 1. 清空、
# dic = {'k1':'v1','k2':'v2'}
# dic.clear()
# print(dic)

# 2. 浅拷贝
# dic = {'k1':'v1','k2':'v2'}
# v = dic.copy()
# print(v)

# 3. 根据key获取指定的value；不存在不报错
# dic = {'k1':'v1','k2':'v2'}
# v = dic.get('k1111',1111)
# print(v)
# v = dic['k1111']
# print(v)

# 4. 删除并获取对应的value值
# dic = {'k1':'v1','k2':'v2'}
# v = dic.pop('k1')
# print(dic)
# print(v)

# 5. 随机删除键值对，并获取到删除的键值
# dic = {'k1':'v1','k2':'v2'}
# v = dic.popitem()
# print(dic)
# print(v)

# k,v = dic.popitem() # ('k2', 'v2')
# print(dic)
# print(k,v)

# v = dic.popitem() # ('k2', 'v2')
# print(dic)
# print(v[0],v[1])

# 6. 增加，如果存在则不做操作
# dic = {'k1':'v1','k2':'v2'}
# dic.setdefault('k3','v3')
# print(dic)
# dic.setdefault('k1','1111111')
# print(dic)
# 7. 批量增加或修改
# dic = {'k1':'v1','k2':'v2'}
# dic.update({'k3':'v3','k1':'v24'})
# print(dic)


# dic = dict.fromkeys(['k1','k2','k3'],123)
# print(dic)
# dic = dict.fromkeys(['k1','k2','k3'],123)
# dic['k1'] = 'asdfjasldkf'
# print(dic)

# dic = dict.fromkeys(['k1','k2','k3'],[1,])
# {
#    k1: 123123213, # [1,2]
#    k2: 123123213, # [1,]
#    k3: 123123213, # [1,]
# }
# dic['k1'].append(222)
# print(dic)
# ########## 额外：
# - 字典可以嵌套
# - 字典key: 必须是不可变类型
# dic = {
#     'k1': 'v1',
#     'k2': [1,2,3,],
#     (1,2): 'lllll',
#     1: 'fffffffff',
#     111: 'asdf',
# }
# print(dic)
# key:
#     - 不可变
#     - True,1

# dic = {'k1':'v1'}
# del dic['k1']

# 布尔值：
# 1 True
# 0 False
#
# bool(1111)


# ##################################### set，集合，不可重复的列表；可变类型 #####################################
# s1 = {"alex",'eric','tony','李泉','李泉11'}
# s2 = {"alex",'eric','tony','刘一'}

# 1.s1中存在，s2中不存在
# v = s1.difference(s2)
# print(v)
# ####　s1中存在，s2中不存在，然后对s1清空，然后在重新复制
# s1.difference_update(s2)
# print(s1)

# 2.s2中存在，s1中不存在
# v = s2.difference(s1)
# print(v)

# 3.s2中存在，s1中不存在
# s1中存在，s2中不存在
# v = s1.symmetric_difference(s2)
# print(v)
# 4. 交集
# v = s1.intersection(s2)
# print(v)
# 5. 并集
# v = s1.union(s2)
# print(v)

# 6. 移除
# s1 = {"alex",'eric','tony','李泉','李泉11'}
# s1.discard('alex')
# print(s1)

# s1 = {"alex",'eric','tony','李泉','李泉11'}
# s1.update({'alex','123123','fff'})
# print(s1)
# ##### 额外：

# s1 = {"alex",'eric','tony','李泉','李泉11'}
# for i in s1:
#     print(i)

# s1 = {"alex",'eric','tony','李泉','李泉11',(11,22,33)}
# for i in s1:
#     print(i)

# ################################### 本周作业 ###################################
"""
# 1. 练习题两个试卷：readme
# 2. 购物系统
    - 个人账户,文件： user,pwd,3,余额
    - 商品，文件
    - 查看商品分页显示：
        li = [
            {...}
            {...}
            {...}
            {...}
            {...}
            {...}
            {...}
        ]
        p = int(input('请输入页码：'))
        start = (p -1) * 10
        end = p * 10
        v1 = li[start:end]
        for i v1:
            print(i)
    - 个人购物记录，文件
        查看：娃娃
    if "al" in "alex":
        pass
"""
open()



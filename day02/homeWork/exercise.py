# -*- coding:utf-8 -*-
# caiqinxiong 
# 2019/7/14 下午12:02

# 身份运算符
# a = 1
# b = 1
# print(a is b)
# print(a is not b)
# print(id(a))
# print(id(b))

# list_name = ['caqinxiong','lixiaoxin','somebody','anybody']
# 切片，顾头不顾尾
# print(list_name[1:3:2])
# print(list_name[-3:-1:-1]) # star:end:step
# print(list_name[-1:-3:-1]) # star:end:step
# print(list_name[::-1]) # 列表反转
#
# del lilist_namest
# print(lilist_namest)
#
# list_info = []
# name = input('input your name:')
# passwd = input('input your passwd:')
# age = input('input your age:')
# list_info.append(name)
# list_info.append(passwd)
# list_info.append(age)
# print(list_info)
#
# n = 0
# name_list = []
# while n<5:
#     name = input('input your name:')
#     if name in name_list:
#         print('名字已存在！')
#     else:
#         name_list.append(name)
#     n +=1
#     print(name_list)

'''
# 让用户输入用户名和密码
# 只要用户名和密码对上了l中的值，显示登陆成功
# 否则，显示登陆失败
'''
# l = [['alex','222'],['wusir','666'],['周老板','123456']]
# name = input('input your name:')
# passwd = input('input your passwd:')
# for username in l:
#     if name == l[l.index(username)][0] and passwd == l[l.index(username)][1]:
#         print('登录成功！')
#         break
# else:
#     print('登录失败！')
#

#
# a = [['k1',2],['k3',4]]
# for k,v in a:
#     print(k)

########################################################分割线###########################################################

'''
1、请用代码实现：利用下划线将列表的每一个元素拼接成字符串，li＝[‘alex’, ‘eric’, ‘rain’]
'''

# li = ['alex', 'eric', 'rain']
# s = '_'
# s = s.join(li)
# print(s)
#


'''
2、查找列表中元素，移除每个元素的空格，并查找以a或A开头并且以c结尾的所有元素。
    li = ["alec", " aric", "Alex", "Tony", "rain"]
    tu = ("alec", " aric", "Alex", "Tony", "rain")
    dic = {'k1': "alex", 'k2': ' aric', "k3": "Alex", "k4": "Tony"}
'''
# (1)题
# li = ["alec", " aric", "Alex", "Tony", "rain"]
# find_list = []
# for i in li:
#     i = i.strip()
#     if (i.startswith('a') or i.startswith('A') ) and i.endswith('c') :
#         find_list.append(i)
# print('以a或A开头并且以c结尾的元素为：\n%s' % find_list)

# (2)题
# tu = ("alec", " aric", "Alex", "Tony", "rain")
# find_list = []
# for i in tu:
#     i = i.strip()
#     if (i.startswith('a') or i.startswith('A') ) and i.endswith('c') :
#         find_list.append(i)
# print('以a或A开头并且以c结尾的元素为：\n%s' % find_list)

# (3)题
# dic = {'k1': "alex", 'k2': ' aric', "k3": "Alex", "k4": "Tony"}
# find_list = []
# # 方法一：
# # for key,value in dic.items():
# #     value = value.strip()
# #     if (value.startswith('a') or value.startswith('A')) and value.endswith('c'):
# #         find_list.append(value)
# # print('以a或A开头并且以c结尾的元素为：\n%s' % find_list)
#
# # 方法二：
# for name in dic:
#     name = dic[name].strip()
#     if (name.startswith('a') or name.startswith('A')) and name.endswith('c'):
#         find_list.append(name)
# print('以a或A开头并且以c结尾的元素为：\n%s' % find_list)

'''
3、写代码，有如下列表，按照要求实现每一个功能

li＝[‘alex’, ‘eric’, ‘rain’]

计算列表长度并输出
列表中追加元素“seven”，并输出添加后的列表
请在列表的第1个位置插入元素“Tony”，并输出添加后的列表
请修改列表第2个位置的元素为“Kelly”，并输出修改后的列表
请删除列表中的元素“eric”，并输出修改后的列表
请删除列表中的第2个元素，并输出删除的元素的值和删除元素后的列表
请删除列表中的第3个元素，并输出删除元素后的列表
请删除列表中的第2至4个元素，并输出删除元素后的列表
请将列表所有的元素反转，并输出反转后的列表
请使用for、len、range输出列表的索引
请使用enumrate输出列表元素和序号（序号从100开始）
请使用for循环输出列表的所有元素
'''

# li = ['alex','eric','rain']
# print('原列表值为： \n%s' % li)
# print('列表长度为：%s ' % len(li))
# li.append('seven')
# print('列表中追加元素“seven”后：\n%s' % li)
# li.insert(0,'Tony')
# print('在列表的第1个位置插入元素“Tony”后为：\n',li)
# li[1] = 'Kelly'
# print('修改列表第2个位置的元素为“Kelly”\n',li)
# li.remove('eric')
# print('删除列表中的元素“eric”\n',li)
# del_name = li.pop(1)
# print('删除的元素的值为:\n',del_name)
# print('删除列表中的第2个元素后为：\n',li)
# li.pop(2)
# print('删除列表中的第3个元素后为：\n',li)

# li = ['alex','eric','rain','caiqinxiong','lixiaoxin']
# print('原列表值为： \n%s\n' % li)
# for i in range(3):
#     # 循环删除index为1的元素，删3次。
#     li.pop(1)
# print('删除列表中的第2至4个元素后为：\n',li)

# li.reverse()
# print('列表所有的元素反转后为：\n',li)
# print('使用for、len、range输出列表的索引')
# for i in range(len(li)):
#     print(i,end=' ')

# print('请使用enumrate输出列表元素和序号（序号从100开始）')
# for k,v in enumerate(li):
#     print('列表的元素为：', v)
#     print('从100开始的序号为:',k+100)
#
# print('请使用for循环输出列表的所有元素')
# for i in li:
#     print(i,end='\t')

'''
4、写代码，有如下列表，请按照功能要求实现每一个功能

li = ["hello", 'seven', ["mon", ["h", "kelly"], 'all'], 123, 446]
请根据索引输出“Kelly”
请使用索引找到’all’元素并将其修改为“ALL”，如：li[0][1][9]…

'''

# li = ["hello", 'seven', ["mon", ["h", "kelly"], 'all'], 123, 446]
# print('请根据索引输出“Kelly”')
# print(li[2][1][1])
# print('请使用索引找到’all’元素并将其修改为“ALL”')
# li[2][2] = 'ALL'
# print(li)


'''
5、有如下变量，请实现要求的功能

tu = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11,22,33)}, 44])
讲述元组的特性
请问tu变量中的第一个元素“alex”是否可被修改？
请问tu变量中的”k2”对应的值是什么类型？是否可以被修改？如果可以，请在其中添加一个元素“Seven”
请问tu变量中的”k3”对应的值是什么类型？是否可以被修改？如果可以，请在其中添加一个元素“Seven”
'''
# 类似list，可查询，遍历元素，切片等，但是不能修改元素的值。不可用删除／增加和修改。
# tu变量中的第一个元素“alex”不可被修改
# tu变量中的”k2”对应的值是list，可以被修改
# tu = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11,22,33)}, 44])
# print(type(tu[1][2]['k2']))
# tu[1][2]['k2'].append('Seven')
# print(tu[1][2]['k2'])
# print(tu)
# tu = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11,22,33)}, 44])
# tu变量中的”k3”对应的值是tuple,可以被修改，因为字典的值可以是任意字符。
# print(type(tu[1][2]['k3']))
# tu[1][2]['k3'] = 'Seven'
# print(tu[1][2]['k3'])
# print(tu)

'''
6、转换

将字符串s = “alex”转换成列表
将字符串s = “alex”转换成元祖
将列表li = [“alex”, “seven”]转换成元组
将元组tu = (‘Alex’, “seven”)转换成列表
将列表li = [“alex”, “seven”]转换成字典且字典的key按照10开始向后递增
'''
#
# s = 'alex'
# print('将字符串s = “alex”转换成列表')
# s = list(s)
# print(s)
#
# print('将字符串s = “alex”转换成元祖')
# s = 'alex'
# s = tuple(s)
# print(s)
#
# print('将元组tu = (‘Alex’, “seven”)转换成列表')
# tu = ('Alex', "seven")
# tu = list(tu)
# print(tu)

print('将列表li = [“alex”, “seven”]转换成字典且字典的key按照10开始向后递增')
li = ['Alex','seven']
li = dict(li)
print(li)
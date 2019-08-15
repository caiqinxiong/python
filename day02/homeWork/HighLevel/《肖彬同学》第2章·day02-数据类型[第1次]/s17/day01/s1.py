#!/usr/bin/python
# -*- coding:utf-8 -*-

# print('hello1') # 单行注释
# print('hello2')
"""
print('hello3')
print('hello4')
"""
# 声明变量:
# 字母
# 数字 (不能开头)
# 下划线
# 不能使用关键字 ['and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'exec', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'not', 'or', 'pass', 'print', 'raise', 'return', 'try', 'while', 'with', 'yield']
# 变量名有意义
# user_id = 123


# a9 = '钓鱼就钓刀鱼，刀鱼要到岛上钓'
# print(a9)
# print(a9)


# name = "郭少龙"
# n = name


# name = "郭少龙"
# n = "郭少龙"
# 内存中，优化机制

# name = "小亮亮"
# print(name) # "小亮亮"
# n = name
# print(n)     # "小亮亮"
# name = "金刚"
# print(name)  # "金刚"
# print(n)

# name = input("请输入姓名:") # "alex"
# print(name)

# import getpass
# pwd = getpass.getpass('请输入密码：')
# print(pwd)






# import getpass
#
# name = input("请输入姓名:")
# pwd = getpass.getpass('请输入密码：')
# age = 18
# print(name)
# print(pwd)
# print(age)

# name = 'alex'

# if 1 == 1 and 2==2:
#     print('正确')
# else:
#     print('错误')




# import getpass
#
# name = input("请输入姓名:")
# pwd = getpass.getpass('请输入密码：')
# if name == 'alex' and pwd == 'sb':
#     print('欢迎登陆')
# else:
#     print('滚蛋')

# username = input('>>>')
# if username == 'alex':
#     print('普通管理')
# elif username == 'oldboy':
#     print('超级管理')
# elif username == '郭少龙':
#     print('人')
# elif username == '刘一':
#     print('装逼犯')
# else:
#     print('再见...')
#
# print('end')


# user_type = input('请输入用户类型:')
# if user_type == '管理员':
#     username = input('输入用户名')
#     if username == 'alex':
#         print('sb')
# else:
#     print('low鸡')





"""

if 1==1:
    print('asaasfd')

if 1==1:
    pass
else:
    pass

if 1==1:
    pass
elif 1==2:
    pass
else:
    pass
"""



# while True:
#     user = input('用户名：')
#     pwd = input('密码：')
#     if user == 'alex' and pwd == 'sb':
#         print('登陆成功')
#         break # 跳出循环
#     else:
#         print('用户名或密码错误,请想想..')

# 1,2,3,4,5,6  8 9 10
# i = 1
# while True:
#     if i == 7:
#         i = i + 1
#         continue # 开始下一次循环
#     print(i)
#     i = i + 1
#     if i == 11:
#         break    # 跳出所有的循环
# i = 1
# while i < 11:
#     print(i)
#     i = i + 1
# 计算 1-100和
# value = 0
# i = 1
# while i < 101:
#     value = value + i
#     i = i + 1
# print(value)




# i = 1
# while i < 101:
#     if i % 2 == 1:
#         print(i)
#     i = i + 1

# i = 1
# while i < 101:
#     if i % 2 == 0:
#         print(i)
#     i = i + 1
# value = 0
# i = 1
# while i<100:
#     if i % 2 == 1:
#         # value = value + i
#         value += i
#     else:
#         # value = value - i
#         value -= i
#     i += 1 # i = i + 1
# print(value)



# i = 0
# while i < 3:
#     user = input('>>>')
#     pwd = input('>>>')
#     if user == 'alex' and pwd == 'sb':
#         print('登陆成功')
#         break
#     else:
#         print('用户名或密码错误,请重试')
#         i += 1

# value = 7 # 数字   "字符串"
# i = 0
# while i<3:
#     num = input('请猜数字') # 7， "7"
#     num = int(num)
#     if value == num:
#         print('拿来200块')
#         break
#     else:
#         print('再来一次')
#         i += 1


# if (1 == 1 and 1 > 2) and 1 == 4:
#     print('正确')
# else:
#     print('错误')

#
# if not True:
#     pass


# content = "Alex 前几天去泰国玩姑娘，一不小心染上了病，他的内心活动是，真该多来几个"
#
# if "前几天去" in content:
#     print('包含敏感字符')
# else:
#     print(content)

# name = " "
# v = bool(name)
# print(v)

# 占位符
# name = '我叫李杰，性别：%s,我今年%s岁，我在说谎!'
# new_str = name %('男',19,)
# print(new_str)

# name = '我叫李杰，性别：%s,我今年%s岁，我在说谎!' %('男',19,)
# print(name)

# val = " alex "
# print(val)
# new_val = val.strip() # 左右
# new_val = val.lstrip()# 左边
# new_val = val.rstrip() # 右边
# print(new_val)

# user_info = "alex sb123 9"

# v = user_info.split('|')
# v = user_info.split('|',1)
# v = user_info.rsplit(' ',1)
# print(v)

# val = input('>>>')
# i = 0
# while i < len(val):
#     print(val[i])
#     i += 1

# name = '我叫李杰，性别我今年岁，我在说谎!'
# print(name[0])
# print(name[0:2])
# print(name[5:9])
# print(name[5:])
# print(name[5:-2])
# print(name[-2:])


# user_info = "alex|sb123|9"
# v = user_info.split('|')
# print(v)


# a = ['alex','eric','狗','eric',123]
# for item in a:
#     print(item)
#     break

v = {
    'name': 'alex',
    'password': '123123'
}


# 常用操作

# 索引获取值
# n = v['name']
# print(n)
# 增加，无，增加；有，修改
# v['age'] = 19
# print(v)
# 删除
# del v['name']
# print(v)
# 循环
# for item in v.keys():
#     print(item)
# for item in v.values():
#     print(item)
# for key,val in v.items():
#     print(key,val)

# user_list = ['alex','eric',['a','b','c'],'李杰']
# user_dict = {
#     'k1': 'v1',
#     'k2': {'kk1':'vv1','kk2':'vv2'},
#     'k3': 123,
#     'k4': ['alex','eric',['a','b','c'],'李杰',{'k11':'vv1'}],
# }
# user_dict['k4'][2].append('123')
# user_dict['k4'][4]['n'] = '过啥龙'
user_list = [
    {'name':'alex','pwd':'123123','times':1},
    {'name':'eric','pwd':'123123','times':1},
    {'name':'tony','pwd':'123123','times':1},
]
user = input('用户名：')
pwd = input('密码：')
for item in user_list:
    if user == item['name'] and pwd == item['pwd']:
        print('登录成功')
        break







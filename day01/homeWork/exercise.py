# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/7/9 17:45
'''
实现用户输入用户名和密码,当用户名为 seven 且 密码为 123 时,显示登陆成功,否则登陆失败!
'''
# username = 'seven'
# password = '123'
# input_name = input('please input the name:')
# input_password = input('please input the password:')
# if username == input_name and password == input_password:
# print('登陆成功!')
# else:
#     print('登陆失败!')

'''
实现用户输入用户名和密码,当用户名为 seven 且 密码为 123 时,显示登陆成功,否则登陆失败,失败时允许重复输入三次
'''
# username = 'seven'
# password = '123'
# n = 0
# while n < 3:
#     input_name = input('please input the name:')
#     input_password = input('please input the password:')
#     if username == input_name and password == input_password:
#         print('登陆成功!')
#         break
#     else:
#         print('登陆失败!')
#     n +=1

'''
实现用户输入用户名和密码,当用户名为 seven 或 alex 且 密码为 123 时,显示登陆成功,否则登陆失败,失败时允许重复输入三次
'''
# n = 0
# while n < 3:
#     input_name = input('please input the name:')
#     input_password = input('please input the password:')
#     if ('seven' == input_name or 'alex' == input_name)  and '123' == input_password:
#         print('登陆成功!')
#         break
#     else:
#         print('登陆失败!')
#     n +=1

'''
使用while循环实现输出2-3+4-5+6...+100 的和
'''
# n = 2
# sum = 0
# while n <= 100:
#     if n % 2 == 0:
#         sum = sum + n
#     else:
#         sum = sum - n
#     n +=1
# print('2-3+4-5+6...+100的和为：',sum)

'''
使用 while 循环实现输出 1,2,3,4,5, 7,8,9, 11,12
'''
# n = 0
# while n <12:
#     n +=1
#     if n == 10 or n == 6:
#         continue
#     elif n == 12:
#         print(n,end='')
#     elif n == 5 or n == 9:
#         print(n,end=', ')
#     else:
#         print(n,end=',')

'''
 使用 while 循环实现输出 1-100 内的所有奇数
'''
# n = 0
# while n < 100:
#     n +=1
#     if n % 2 == 0:
#         continue
#     print(n,end=',')

'''
 使用 while 循环实现输出 1-100 内的所有偶数
'''
# n = 0
# while n < 100:
#     n +=1
#     if n % 2 != 0:
#         continue
#     print(n,end=',')

'''
使用while 循环输出100-50，从大到小，如100，99，98…，到50时再从0循环输出到50，然后结束
'''
# n = 100
# m = 0
# while n >= 50:
#     print(n,end=',')
#     n -=1
# print()
# while m <= 50:
#     print(m,end=',')
#     m +=1

'''
使用while,完成以下图形的输出
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''

# n = 1
# m = 0
# while n <= 10:
#     if n < 5:
#         print("* " * n)
#     else:
#         m = m + 2
#         print("* " * (n - m))
#     n = n + 1
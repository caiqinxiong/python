l = [3,2,5,7,1,9,10,11,15,17]
# print(len(l))   # length
# n = 0
# while n<len(l):
#     print(l[n])
#     n += 1

# 循环 for循环
# for n in l:
#     print(n)

# while循环和for循环的区别
# while循环是根据条件来的 结束循环的次数是不固定的
# for循环循环的次数永远等于你循环的那个列表/其他数据类型的长度

# for i in l:
#     if i ==10:
#         break
#     print(i)

# for i in l:   # 迭代
#     if i ==10:
#         continue
#     print(i)

# 小练习
l = [['alex','222'],['wusir','666'],['周老板','123456']]
# 让用户输入用户名和密码
# 只要用户名和密码对上了l中的值，显示登陆成功
# 否则，显示登陆失败

# username = input('username :')   # wusir
# password = input('password :')   # 123
# login = False
# for item in l:   # ['alex','222']  ['wusir','666']  ['周老板','123456']
#     if username == item[0] and password == item[1]:
#         print('登陆成功')
#         login = True
#         break
# if login == False:
#     print('登陆失败')


# for i in [1,2,3,4]:
#     print(i)
# else:
#     print('循环完啦')

# for i in [1,2,3,4]:
#     print(i)    # i=1  i=2  i=3  i=4
#     if i == 3:
#         break
# else:
#     print('循环完啦')

# username = input('username :')   # wusir
# password = input('password :')   # 123
# for item in l:   # ['alex','222']  ['wusir','666']  ['周老板','123456']
#     if username == item[0] and password == item[1]:
#         print('登陆成功')
#         break
# else:  # 当for循环执行结束，并且在执行过程中没有被break，执行else中的代码
#     print('登陆失败')

# i = 0
# while i<5:
#     print(i)
#     i = i+1
#     if i == 3:
#         break
# else:
#     print('执行完拉')





















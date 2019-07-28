# def make_cloth_simple(n):
#     '''
#     生成器函数,没有return 只有yield
#     :param n:
#     :return:
#     '''
#     for i in range(n):
#         yield '第%s件衣服'%i
#
# ret = make_cloth_simple(1000000)
# print(ret)   # generator 生成器 生成器的本质就是一个迭代器
# for n in range(20):
#     print(ret.__next__())
#
# print('='*50)
# for i in range(5):
#     print(ret.__next__())

# 监听文件内的输入,
# 在python中监听一个文件的输入事件,只要用户输入了新内容,就打印到屏幕中来
# f.readline + while循环
# 打开文件
# 循环
    # 读
# 关闭文件

# def listen():
#     f = open('test',mode='r',encoding='utf-8')
#     while True:   # 2000
#         content = f.readline().strip()
#         if 'error' in content:
#             yield content
#
# for content in listen():
#     print(content)


# 将来你写的所有的代码 最好都把读文件的操作写成一个生成器
# def get_user(file):
#     line_lst = []
#     with open(file,mode = 'r',encoding='utf-8') as f:
#         for line in f:
#             usr,pwd = line.strip().split('|')
#             line_lst.append((usr,pwd))
#     return line_lst
#
# def login():
#     user = input('username :')
#     passwd = input('password :')
#     print(get_user('userinfo'))
#     for usr,pwd in get_user('userinfo'):
#         if usr == user and pwd == passwd:
#             print('登录成功')
#             break
#     else:
#         print('登录失败')
#
# login()

# 登录
    # 读文件
# 注册
    # 检测是不是已经存在相同的用户名
# def get_user(file):
#     with open(file,mode = 'r',encoding='utf-8') as f:
#         for line in f:
#             usr,pwd = line.strip().split('|')
#             yield usr,pwd
#
# def login():
#     user = input('username :')
#     passwd = input('password :')
#     for usr,pwd in get_user('userinfo'):
#         if usr == user and pwd == passwd:
#             print('登录成功')
#             break
#     else:
#         print('登录失败')
#
# login()

# 所有的读文件和写文件 尽量都拆分到其他函数中
# 不要嵌到你写好的功能函数中
# 比如 登录 函数中不要写读文件的逻辑
# 比如 注册 函数中不要写读\写文件的逻辑


# def func():
#     for i in range(10):
#         yield 'a%s'%i
# g = func()
# for i in g:
#     print(i)
#
# for i in g:
#     print(i)

# def func():
#     for i in range(10):
#         yield 'a%s'%i
# for i in func():
#     print(i)
# for i in func():
#     print(i)

# def func():
#     for i in range(10):
#         yield 'a%s'%i
# g1 = g2 = func()
# for i in g1:
#     print(i)
# for i in g2:
#     print(i)

# def func():
#     for i in range(10):
#         yield 'a%s'%i
# g1 = func()
# g2 = func()
# for i in g1:
#     print(i)
# for i in g2:
#     print(i)





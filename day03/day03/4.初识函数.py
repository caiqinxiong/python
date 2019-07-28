# 函数的使用
    # 1.增强代码的可读性
    # 2.降低代码的重复性

# def 函数的名字():
#     print('写在函数里的逻辑')

# lst = [1,2,3,4]
# def mylen():
#     print('执行我啦')
#     i = 0
#     for j in lst:
#         i += 1
#     print(i)
#
# mylen()


# 写函数，有三个值a,b,c,计算a*b/c的结果并打印
# a = 1
# b = 2
# c = 3
# def abc():
#     print(a*b/c)


# 返回值的概念
# def mylen():
#     print('执行我啦')
#     i = 0
#     for j in lst:
#         i += 1
#     return i
# lst = [1,2,3,4]
# ret = mylen()
# print('-->',ret)

# a = 1
# b = 2
# c = 3
# def abc():
#     return a*b/c
# ret = abc()
# print(ret)

# 思考题
# def demo():
#     print(123)
#     return True
#     print(456)
#     return False
#
# demo()

# def demo2():
#     return 1,2,3,{'k':'v'}
# ret = demo2()
# print(ret)

# def demo3():
#     ret = 1+2+3+4+5
#     return ret
#
# print(demo3())
# return
    # 不写return
        # 所有代码执行完毕自动结束函数
        # 返回值是None
    # 只写return
        # 遇到return函数结束
        # 返回值是None
    # return 结果
        # 程序结束，返回结果
        # return 结果1,结果2,结果3
            # 会被变成元组返回给调用者

# 参数
# def mylen(seq):
#     print('执行我啦')
#     i = 0
#     for j in seq:
#         i += 1
#     return i
# str1 = input('>>>')
# str2 = input('>>>')
# ret1 = mylen(str1)
# ret2 = mylen(str2)
# print('-->',ret1)
# print('-->',ret2)

# def sum(a,b,c): # 形式参数 形参
#    return a+b+c
#
# a1 = input('>>>')
# b1 = input('>>>')
# c1 = input('>>>')
# ret = sum(int(a1),int(b1),int(c1))   # 实际参数 实参
# print(ret)

# 写一个函数，传入两个参数，比较两个参数值的大小，并返回比较大的那一个数值
# 调用
# def compare(a,b):
#    if a>b:
#       return a
#    else:
#       return b
#
# print(compare(10,50))
# print(compare(20,7))


# def choose_ball(count,max_num,ball_color):
#     n = 0
#     s = ''
#     while n < count:
#         num1 = input('请输入%s球的号码 :'%ball_color)
#         num = int(num1)
#         if num <= max_num and num >= 1:
#             print('您选择了%s球'%ball_color,num1)
#             n = n + 1
#             if n < count:
#                 s = s + num1 +','
#             else:
#                 s = s + num1
#         else:
#             print('请选择1-%s之间的数字'%max_num)
#     return s
# s1 = choose_ball(6,32,'红色')
# s2 = choose_ball(2,16,'蓝色')
# print('您选择的红球有 ：',s1)
# print('您选择的蓝球有 ：',s2)


# 列表 、元组 、字符串、字典。求两个类型的长度比，返回数据长度更长的类型
# def mylen(seq):
#     i = 0
#     for j in seq:
#         i += 1
#     return i
#
# def compare(seq1,seq2):
#     if mylen(seq1)>mylen(seq2):
#         return seq1
#     else:
#         return seq2

# 写函数要注意的
    # 1.尽量用return 而不是print来处理结果
    # 2.我们的每一个函数中的代码都要注意不要出现重复的代码
        # 保证每一个函数都是最精简的功能

# 站在实参（调用）角度上
    # 按照位置传参数
    # def func(a,b):
    #     print(a)
    #     print(b)
    #
    # func(1,2)
    # func(2,1)

    # 按照关键字传参数
    # def func(a,b):
    #     print(a)
    #     print(b)
    #
    # func(a = 1,b = 2)
    # func(b = 2,a = 1)

    # 先按照位置、再关键字传参数
    # def func(a,b,c):
    #     print(a)
    #     print(b)
    #     print(c)
    #
    # func(1,b = 10, c=20)
    # func(1,c = 10, b=20)
    # open('userinfo',encoding='utf-8',mode= 'r')

# 站在形参（定义函数）的角度上
# name score 位置参数，总是写在形参的最开始
# gender默认参数（关键字参数），总是写在位置参数之后的
# def student(name,score,gender='女'):
#     print('python27期的同学%s，性别%s，第三次作业成绩%s分'%(name,gender,score))
#
# student('老王',0)
# student('周老板',1)
# student('汤青松',2,'不详')

# 动态传参数
# def sum(*args):
#     s = 0
#     for i in args:
#         s += i
#     return s
# ret = sum(1,2)
# print(ret)
# ret = sum(1,2,3)
# print(ret)
# ret = sum(1,2,3,4)
# print(ret)
# ret = sum(1,2,3,4,5)
# print(ret)

# *args动态参数放在位置参数之后
# def demo(a,b,c,*args):
#     print(a)
#     print(b)
#     print(c)
#     print(args)
#
# demo(1,2,3,4,5)

# gender默认参数（关键字参数），总是写在位置参数之后的
# *args动态参数放在位置参数之后
# 位置参数,*args,默认参数

# def func(a,b,c,*args,d ='alex'):
#     print(a)
#     print(b)
#     print(c)
#     print(d)
#     print(args)
#
# func(1,2,3,4,5,6,7)
# func(1,2,3,4,5,6,7,d='wisur')


# 动态参数二 **kwargs
# 位置参数,*args,默认参数,**kwargs
# def func(**kwargs):
#     print(kwargs)
#
# func(a = 1,b=2,c= 3)


# def func(a,b,c):
#     print(a,b,c)

# lst = [1,2,3]
# tup = (1,2,3)
# dic = {'k1':1,'k2':2,'k3':3}
# func(*lst)   # func(1,2,3)
# func(*tup)   # func(1,2,3)
# func(*dic)   # func('k1','k2','k3')


# def func(*args):
#     print(args)
#
# func(1,2,3)
# tup = (1,2,3)
# func(*tup)   # func(1,2,3)


# def func(a,b,c):
#     print(a,b,c)

# func(a=1,b=2,c=3)
# dic = {'a': 1, 'b': 2, 'c': 3}
# func(**dic)

# def func(**kwargs):
#     print(kwargs)

# func(a=1,b=2,c=3)
# dic = {'a': 1, 'b': 2, 'c': 3}
# func(**dic)







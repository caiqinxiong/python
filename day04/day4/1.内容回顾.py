# 文件操作
    # 打开文件
        # f = open('文件的路径',mode='r',encoding='utf-8')
        # open('文件的路径',mode='w',encoding='utf-8')
        # open('文件的路径',mode='a',encoding='utf-8')
        # open('文件的路径',mode='rb')
        # open('文件的路径',mode='wb')
        # open('文件的路径',mode='ab')
    # 读写文件
        # 读
            # read()  默认读所有
            # read(n) 读n个字节/字符
            # readline() 每次读一行,不知道什么时候结束
            # for lin in f:
        # 写
            # write('想写啥写啥')
            # write(b'abc')
    # 关闭文件
        # f.close()
    # 删除和修改
        # import os
        # os.remove('文件的绝对路径')
        # os.rename('原名','目的名')
        # 修改文件
            # 读a文件,写b文件
            # 删除a,重命名b->a
# 初识函数
    # 函数的定义
       # def 函数名(形参):
       #    函数体
       #    return 返回值
    # 调用
        # 变量 = 函数名(实参)
        # 变量就是函数的返回值
    # 返回值
        # 1.不写return 默认返回None
        # 2.只写return 表示函数结束,默认返回None
        # 3.return 值  值被返回给调用者
        # 4.return 值1,值2  接收到的返回值是(值1,值2)
    # 参数
        # 站在调用者的角度上
            # 按照位置传参数
                # *可以迭代的对象(可以被for循环)
            # 按照关键字传参
                # **字典
            # 混合 :先位置,再关键字
        # 站在定义函数的角度上
            # 位置参数
            # *args 动态参数
            # 默认参数
            # **kwargs 动态参数
# def cal(a,b,c):
#     pass
# cal(1,2,3)
# cal(a = 1,b = 2,c = 3)
# cal(1,b = 2,c = 3)
# cal(1,2,c = 3)
# l = [1,2,3]
# cal(*l)   # -->cal(l[0],l[1],l[2])
# d = {'a':1,'b':2,'c':3}
# cal(**d)

# f = open('test',mode='rb')
# content = f.read()
# print(content)
# msg = content.decode('utf-8')
# print(msg)
# f.close()

# path = r'F:\python自动化27期\day4\test'
# f = open(path,encoding='utf-8')
# content = f.read()
# print(content)

# 工作目录
# 在哪个路径下执行python程序,工作目录就是哪里
# 所以 如果希望在任何一个位置执行代码都不出现文件目录找不到的情况,就要用绝对路径,而不是相对路径

# pycharm下会有很多优化的机制
# 在执行代码的时候,会自动的把当前文件所在的目录作为工作目录

# 参数的陷阱,如果默认参数的值是一个可变数据类型
# 那么所有的调用者都共享这一个数据
# 这个变量是在定义的时候创建1次,而不会在调用的过程中再次被创建了
# def func(a,l = []):
#     print(id(l))
#     l.append(a)
#     print(l)
#     return l
#
# func(1)
# l1 = func(2,[])
# func(3)
# func(4,[])   # [4]


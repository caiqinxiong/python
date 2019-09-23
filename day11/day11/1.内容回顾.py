# 下次上课时间 : 10.13号
# 直播时间 9.24 9.26
# 中间还会安排两次直播 10.9\10.10

# 代码发布系统的需求采集\自动化运维需求
# 回顾的时间 后面会逐渐减少
    # 每周四 直播里 告诉大家 你这周来上课需要掌握什么

# python基础阶段已经完整的学完了
    # 基础数据类型
    # 流程控制 if for while
    # 文件操作
    # 函数基础
    # 函数的进阶(变量的命名空间和作用域 装饰器\迭代器\生成器\生成器表达式\列表推导式)
    # 内置函数
    # 常用模块(re os sys time datetime random hashlib logging json pickle)
    # 自定义模块
    # 模块的导入,什么是包
    # 软件的开发规范
    # 面向对象(基础语法 单继承多继承)
    # 面向对象进阶(多态 私有的 property classmethod staticmethod 内置方法)
    # 反射
    # 网络编程 : 概念\协议 掌握最基础的socket cs端代码就可以
    # 并发编程 : 概念
# 评估一下自己的开发水平
    # 能够完成需求
    # 面向过程/函数/对象编程
    # 能够独立的完成哪个作业? 前面的作业\计算器\选课系统\ftp

# 复习
# 并发编程(让一个程序能同时做多件事情)
# 进程 : 开销非常大 是计算机中资源分配的最小单位(内存隔离) 能利用多个CPU 由操作系统控制 同时操作内存之外的数据会产生数据的不安全
# 线程 : 开销非常小 是操作系统可以调度的最小单位(内存共享) 能利用多个CPU 由操作系统控制 同时操作全局内存中的数据会产生数据的不安全
    # Cpython解释器下 由于GIL(全局解释器锁)的问题导致了一个进程中的多个线程无法利用多核
    # 数据不安全 += -= *= /=  多个线程同时操作全局/内存外部的变量 需要自己加锁,在+= 操作前后添加lock.acquire()和lock.release()即可
    # append pop extend 你能想到的基础数据类型自带的方法都是数据安全的
# 协程 : 开销几乎为0 不是由操作系统控制的,是由代码控制的.本质是单线程的,不能利用多个CPU 也会产生数据不安全
    # gevent模块 第三方模块 他只能识别有限的IO操作 socket time.sleep

# from threading import Thread,Lock
# n = 0
# def add():
#     global n
#     for i in range(2000000):
#         lock.acquire()
#         n +=1
#         tmp = n
#         n = tmp+1
#         lock.release()

# def sub():
#     global n
#     for i in range(2000000):
#         lock.acquire()
#         n -=1
#         lock.release()

# lock = Lock()
# t1 = Thread(target=add)
# t2 = Thread(target=sub)
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(n)

# 并发方面的视频

# 初识数据库


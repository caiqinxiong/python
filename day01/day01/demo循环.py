# 死循环
# while True:
#     print('我很好,我还活着')

# 当条件不满足的时候退出循环
# n = 0
# while n<300:
#     print('我很好,我还活着')
#     n = n+1   # n=0+1=1  n=1+1=2 n=2+1

# 强制退出循环
# 找到0-300中所有能被5整除也能被16整数的数
# n = 0
# while n<300:
#     if n%5==0 and n%16==0:
#         print('-->',n)
#         break
#     n = n+1

# n = 0
# while n <10:
#     print('你好啊',n)
#     if n == 3:
#         break   # 表示退出循环
#     n = n+1

# n = 0
# while n <10:    # 0<10  1<10 2<10
#     print('begin',n) # 0 1 2
#     n = n + 1   # n=1  n=2 n=3
#     if n==2:
#         continue # 放弃本段代码中的剩余内容,继续循环
#     print('end',n) # 1     3
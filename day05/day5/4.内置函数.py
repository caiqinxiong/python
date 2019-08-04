# locals/globals
# name = 'alex'
# def func():
#     a = 1
#     b = 2
#     print(locals())
#     print(globals())
# func()

# input/open'/eva/exec/callable/print
# s = '1+2+3+4+5'
# e = input('>>>')
# print(e)
# def func():print(123456)
# func()
# ret = eval('func')   # 把字符串组成的代码当做python代码来执行,并返回值
# print(ret)
'''
伪代码
def func(sep,符号):
    col, val = express.split(sep)
    boolean = '从文件里读出来每一行的换手率对应的值 %s val'%符号
    if eval(boolean):
        print('这一行')
    return val
express = '换手率>25'
if '>' in express:
    col, val = func('>','>')
elif '<' in express:
    col, val = func('<','<')
elif '=' in express:
    col, val = func('=','==')
'''
# exec 没有返回值
# def func():
#     print('1234')
# exec('func()')    # 没有返回值
# exec('1+2-4*4')    # 没有返回值

# eval /exec 要注意使用的安全性
    # 从文件中读出来的不要直接用eval
        # a,b,c = 1,2,3
        # with open('eval的错误用法',encoding='utf-8') as f:
        #     content = f.read()
        # eval(content)
    # 用户输入的,不要直接用eval
    # 从网络上获取的,不要直接用eval

# callable 可以被调用 名字后面可以加()
# a = 1
# print(callable(a))
# a = lambda :1
# print(callable(a))

# dir查看一个数据可以调用哪些方法
# 也可以通过查看某一个特定方法是不是在这个结果中,以此来判断这个数据的类型
# ret = dir(range(10))
# print(ret)

# print就是向屏幕所在的文件输出内容
# print(1,2,3,end = '$')
# print(2,3,4,sep = ',')
# with open('print_test','w') as f:
#     print('wahahaha',file =f)

# 9*9乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%s*%s=%2s'%(j,i,i*j),end = ' ')
#     print(i,j)
# [print('%s*%s=%2s'%(j,i,i*j)) if i==j else print('%s*%s=%2s'%(j,i,i*j),end = ' ') for i in range(1,10) for j in range(1,i+1)]
import time
# print('hellooooooo',end='',flush=True)   # 不会立即写 会等一会儿
# time.sleep(0.5)  #
# print('\rworld',end='')  # 不会立即写 会等一会儿

# import time
# for i in range(0,101,2):
#      time.sleep(0.1)
#      char_num = i//2      #打印多少个'*'
#      per_str = '\r%s%% : %s'%(i,'='*char_num)
#      print(per_str,end='', flush=True)

# 数学类的 abs divmod round pow sum min max
# ret = abs(-10)
# print(ret)

# ret= divmod(10,6)
# print(ret)

# f = 1.23956
# ret= round(f,2)
# print(ret)

# ret = pow(2,3)
# ret2 = 2**3
# print(ret,ret2)

# ret = sum([1,2,3,-43,5])
# print(ret)
# def func(lst):
#     for i in lst:
#         yield int(i)
#
# l = ['1','2','3','-43','5']
# ret = sum((int(i) for i in l))
# print(ret)
# dic = {'apple':50,'umbrella':100}
# ret = sum((dic[k] for k in dic))
# print(ret)

# ret = min([1,3,-5,7,9])
# print(ret)
# ret = max([1,3,-5,7,9])
# print(ret)

# import sys
# sys.stdout.write('wahaha')
# print('wahaha')
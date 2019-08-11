import os

# ret= os.path.getsize(r'F:\python自动化27期\day6\1.内容回顾.py')  # 获取一个文件的大小
# print(ret)
# 2993字节

# ret= os.path.getsize(r'F:\python自动化27期\day6')  # 获取一个文件的大小
# print(ret)
# 4096字节

# 计算文件夹的文件的总大小
# 一个文件夹的大小并不是这个文件夹下所有文件的大小的综合

# 判断路径是文件夹还是文件
# ret = os.path.isdir(r'F:\python自动化27期\day6\4.正则表达式.py')
# print(ret)
# ret = os.path.isfile(r'F:\python自动化27期\day6\4.正则表达式.py')
# print(ret)

# 查看当前文件夹下的所有文件
# ret = os.listdir('F:\python自动化27期')
# print(ret)

# 拼路径
# path =os.path.join('F:\python自动化27期','day4')
# print(path)

# 首先判断是文件夹还是文件
# 如果是文件夹
# listdir
    # 获取到文件夹下的所有文件和文件夹的名字
    # 把当前路径和文件和文件夹的名字拼在一起
    # 然后再判断新拼好的路径时文件还是文件夹
        # 如果是文件夹 循环上面的过程
        # 如果是文件 获取文件的size,累加到结果中

# 1.一个文件夹 下面都是文件没有其他文件夹了,求这个文件夹中文件的总大小
# 2.一个文件夹,后面套着文件夹,并且不知道套了多少层,怎么算???
    # 三级菜单 : 栈\递归
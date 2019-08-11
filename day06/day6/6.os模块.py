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

import os
# os.mkdir('dir4/dir4_son')
# os.makedirs('dir5/dir5_son/dir5_grandson')
# os.removedirs('dir5/dir5_son')
# print(os.stat(r'F:\python自动化27期\day6\1.内容回顾.py'))

# os.system('dir')  # 只执行 不关心结果
# ret = os.popen('dir')  # 执行 并返回结果
# print(ret.read())

# ret = os.path.abspath(r'F:\python自动化27期/day6\1.内容回顾.py')
# print(ret)

# path = r'F:\python自动化27期\day6'
# ret = os.path.split(path)
# print(ret)
# ret = os.path.dirname(path)
# print(ret)
# ret = os.path.basename(path)
# print(ret)
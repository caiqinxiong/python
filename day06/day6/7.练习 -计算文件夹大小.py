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
# import os
# def dir_size(path):
#     if os.path.isdir(path):
#         sum_size,dirs = 0,[path]
#         while dirs:
#             path = dirs.pop()
#             dir_lst = os.listdir(path)
#             for name in dir_lst:
#                 file_path = os.path.join(path,name)
#                 if os.path.isfile(file_path):
#                     sum_size += os.path.getsize(file_path)
#                 else:
#                     dirs.append(file_path)
#         return sum_size
#     elif os.path.isfile(path):
#         return os.path.getsize(path)
#     else:
#         print('找不到文件')
#
# path1 = r'F:\python自动化27期\day6\1.内容回顾.py'
# path2 = r'F:\python自动化27期\day6'
# path3 = r'F:\python自动化27期\day7'
#
# ret = dir_size(path1)
# print(ret)
# ret = dir_size(path2)
# print(ret)
# dir_size(path3)


# import os
# def dir_size(path):
#     if os.path.isdir(path):
#         sumsize = 0
#         name_lst = os.listdir(path) # ['move_info7 :2000','dir1','dir2','1.内容回顾.py']
#         for name in name_lst:
#             full_path = os.path.join(path,name)
#             if os.path.isfile(full_path):
#                 sumsize += os.path.getsize(full_path)  # 2000
#             else:                      # dir1
#                 ret = dir_size(full_path)    # dir_size(F:\python自动化27期\day6\dir1)
#                 sumsize += ret
#         return sumsize
#     elif os.path.isfile(path):
#         return os.path.getsize(path)
#     else:print('找不到文件')
#
# path2 = r'F:\python自动化27期\day6'
# ret = dir_size(path2)
# print(ret)

# def dir_size(path):   # F:\python自动化27期\day6\dir1
#     if os.path.isdir(path):
#         sumsize = 0
#         name_lst = os.listdir(path)    # ['dir_son1','__init__.py']
#         for name in name_lst:
#             full_path = os.path.join(path,name)
#             if os.path.isfile(full_path):
#                 sumsize += os.path.getsize(full_path)  # 50
#             else:
#                 ret = dir_size(full_path)    # dir_size(F:\python自动化27期\day6\dir1\dir_son1)
#                 sumsize += ret                         # 1200 + 50 = 1250
#         return sumsize
#     elif os.path.isfile(path):
#         return os.path.getsize(path)
#     else:print('找不到文件')
#
#
# def dir_size(path):   # F:\python自动化27期\day6\dir1\dir_son1
#     if os.path.isdir(path):
#         sumsize = 0   #
#         name_lst = os.listdir(path)   # ['demo']
#         for name in name_lst:
#             full_path = os.path.join(path,name)
#             if os.path.isfile(full_path):
#                 sumsize += os.path.getsize(full_path)   # sum_size = 0+1200 = 1200
#             else:
#                 dir_size(full_path)
#         return sumsize
#     elif os.path.isfile(path):
#         return os.path.getsize(path)
#     else:print('找不到文件')
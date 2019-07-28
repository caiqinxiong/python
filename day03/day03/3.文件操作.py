# 读文件
# f是一个文件句柄，所有和文件相关的操作都要依赖f，也可以叫做文件操作符
# f = open(
#      r'D:\PyCharmProject\py27\day03\userinfo',
#      mode = 'r',
#      encoding ='UTF-8'
#      )
# 一次读所有
# print(f.read())

# 一次读一行
# 一次性读取所有内容文件有多大，占多大的内存空间- 不好，没有占用的必要
# print(f.readline())   # 一次读一行，依次向下读，但不知道在哪里结束
# print(f.readline())
# print(f.readline())

# for循环读
# for line in f:    # 技能够一行一行的读取，又可以在读完之后自动停止
#      line = line.strip()
#      if line:print(line)

# 第二种读取方式

# f.close()
# userinfo(pycharm创建utf-8) -->
# open --> 操作系统的命令操作文件（win gbk、linux ios utf8）
# == 乱码

# 文件的写操作
# f = open(
#      r'D:\PyCharmProject\py27\day03\user',
#      mode = 'w',
#           # 以写的方式打开一个已经存在文件，相当于清空原来的文件
#           # 以写的方式打开一个不存在的文件，相当于新建一个空文件
#      encoding ='UTF-8'
#      )
# f.write('老王|abc,123\n')
# f.write('alex|1234\n')
# f.close()

# 文件的追加写操作
# f = open(
#      r'D:\PyCharmProject\py27\day03\user',
#      mode = 'a',
#           # 以写的方式打开一个已经存在文件，相当于清空原来的文件
#           # 以写的方式打开一个不存在的文件，相当于新建一个空文件
#      encoding ='UTF-8'
#      )
# f.write('wusir|666')
# f.close()

# 文件的读 写 追加写 操作
# 读文件
# {'apple':[6000,10],'鞋子':[]}

# f = open('userinfo',mode='r',encoding='utf-8')
# dic = {}
# for line in f:
#      line = line.strip()
#      if line:
#           lst = line.split('|')
#           dic[lst[0]] = [lst[1],lst[2]]
# print(dic)

# 文件的上下文管理
# {'apple':[6000,10],'鞋子':[]}
# with open('userinfo',mode='r',encoding='utf-8') as f:    #  f = open('userinfo',mode='r',encoding='utf-8')
#      dic = {}
#      for line in f:
#           line = line.strip()
#           if line:
#                lst = line.split('|')
#                dic[lst[0]] = [lst[1],lst[2]]
# print(dic)


# 文件指针
# with open('userinfo',mode='r',encoding='utf-8') as f:
#      print(f.tell())
#      print(f.readline())
#      f.seek(0)
#      for line in f:
#           print(line)

# 文件的修改
# with open('user',encoding='utf-8') as f1,\
#         open('user.bak',mode='w',encoding='utf-8') as f2:
#      for line in f1:
#           line = line.strip()
#           lst = line.split('|')
#           if lst[0] == '老王':
#                lst[1] = 'password'
#           f2.write('|'.join(lst)+'\n')
# import os
# os.remove('user')
# os.rename('user.bak','user')

# D:\PyCharmProject\py27\day03\2.内容回顾2.mp4
# import os
# size = os.path.getsize(r'D:\PyCharmProject\py27\day03\2.内容回顾2.mp4')
# with open(r'D:\PyCharmProject\py27\day03\2.内容回顾2.mp4',mode='rb') as f1,\
#     open(r'D:\PyCharmProject\py27\day03\bak.mp4',mode='wb') as f2:
#     while size>1024:   # 2049
#         content = f.read(1024)
#         f2.write(content)
#         size -= 1024   # 1
#     else:
#         content = f.read(size)
#         f2.write(content)












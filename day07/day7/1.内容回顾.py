import re
# ret = re.match('\d+','123alex')   # re模块特殊的变量 ret
# print(ret.group()) # 这个变量中封装了group方法,只能通过group获取变量中匹配到的具体值
# ret = re.search('\d+','alex123wusir667')
# print(ret.group())
# ret = re.findall('\d+','wusir73alex84') 匹配所有
# print(ret)
# 正则表达式分组命名  (?P<组名>正则表达式) 给这个分组内的正则表达式起一个名字
# 等后面匹配出完整结果之后通过.group('组名')就可以获取这个分组中匹配到的内容
# ret = re.search('\d(?P<sedn>\d)','alex3714')
# print(ret.group('sedn'))

# re模块
    # match : 从头开始如果能匹配上就返回结果
    # search : 只要字符串中包含符合条件的内容就匹配第一项
    # findall : 匹配所有符合正则规则的内容
    # split : 根据正则做切割
    # sub subn : 根据正则做替换
    # finditer : 根据正则匹配所有,返回迭代器 -- 节省内容
    # compile : 预编译 -- 节省时间
# os
    # 文件操作
        # rename remove
    # 文件夹操作
        # mkdir rmdir
        # makedirs  removedirs
        # listdir
    # 操作系统命令
        # system('linux命令')
        # ret = popen('linux命令').read()
    # 工作目录
        # getcwd()        # 获取当前的工作路径
        # chdir('目标')   # 修改当前的工作路径
    # path 路径
        # 拼接   os.path.join('c://','user','alex')
            # c://user/alex
        # 分离   ret = os.path.split('c://user/alex')
            # ret = ('c://user','alex')
        # 分离出的文件夹
            # os.path.basename
# import os
# ret = os.path.basename('F:\python自动化27期\day7')
# print(ret)
        # 分离出的路径
# import os
# ret = os.path.dirname('F:\python自动化27期\day7')
# print(ret)
            # os.path.dirname
        # 判断是否存在
            # os.path.exist('路径')  True/False
        # 是否文件
            # os.path.isfile()
        # 是否文件夹
            # os.path.isdir()
        # 是否绝对路径
            # os.path.isabs()
# sys
    # sys.modules :描述了当前解释器加载到内存中的所有模块
    # sys.path : 决定了一个模块是不是能被导入
    # sys.argv : 执行文件的时候接受的参数

# 时间模块
    # time
        # 时间戳时间 纯数字 time.time()
        # 结构化时间 可命名元组(st_year = 2019,st_month = ....)
        # 格式化时间 字符串 time.strftime('%Y %m %d %H %M %S')
            # %Y %m %d %H %M %S

# from datetime import datetime
# dt = datetime.now() #获取当前时间
# print(dt.date())
# print(dt.year)
# print(dt.month)
# print(dt.day)
# print(dt.hour)
# print(dt.minute)
# print(dt.second)
#
# dt2 = datetime(2019,6,18)
# print(dt2)
#
# print(dt-dt2)
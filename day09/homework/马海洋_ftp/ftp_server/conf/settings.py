#encoding:utf-8
#--title：'马海阳'
#--mtime：'2019/9/3'

import os

# 服务端路径
# FILE_PATH = r'D:\oldboy_learn_project\oldbaoy_python_project\day09\课下\ftp作业\ftp_server'
FILE_PATH = os.path.dirname(os.path.dirname(__file__))

# 用户登陆文件
userinfo = os.path.join(FILE_PATH, 'db', 'userinfo')

# 用户目录
home = os.path.join(FILE_PATH,'db','home')

# 服务器IP，端口
IP_PORT = ('127.0.0.1',9002)

# log存放地址
log_path = os.path.join(FILE_PATH, 'log', 'program.log')

# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/9/2 10:30
import os
import time
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# 服务器ip地址和端口
IP_PORT = ('127.0.0.1',8888)

# 默认用户磁盘配额大小为1G，化为字节
QUOTA = '1073741824'

# 数据库路径
DB_PATH = r'%s/db' % BASE_DIR
if not os.path.exists(DB_PATH):os.makedirs(DB_PATH)

# 用户信息文件
USER_FILE = r'%s/users_info'  % DB_PATH

# 用户家目录
USER_HOME = lambda name:'%s/users_home/%s' % (DB_PATH,name)

# 用户客户端目录
USER_CLIENT = lambda name:'%s/client_home' % USER_HOME(name)

# 用户服务器目录
USER_SERVER = lambda name:'%s/server_home' % USER_HOME(name)

# 日志文件路径
LOG_PATH = os.path.join(BASE_DIR,'log')
if not os.path.exists(LOG_PATH):os.makedirs(LOG_PATH)
LOG_FILE = r'%s/%s-log' % (LOG_PATH,time.strftime('%Y-%m-%d', time.localtime(time.time())))


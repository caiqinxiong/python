# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/9/2 10:30
import os
import time
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# 服务器ip地址和端口
IP_PORT = ('127.0.0.1',8888)

# 数据库路径
DB_PATH = os.path.join(BASE_DIR,'db')
if not os.path.exists(DB_PATH):os.makedirs(DB_PATH)

# 用户下载目录
DOWNLOAD = lambda name:os.path.join(DB_PATH,'%s_download') % (name)

# 日志文件路径
LOG_PATH = os.path.join(BASE_DIR,'log')
if not os.path.exists(LOG_PATH):os.makedirs(LOG_PATH)
LOG_FILE = r'%s/%s-log' % (LOG_PATH,time.strftime('%Y-%m-%d', time.localtime(time.time())))


# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
#2019/12/16 10:38
import os
import time
# 获取当前时间
DAY_TIME = time.strftime('%Y-%m-%d', time.localtime(time.time()))

# 项目根路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 爬取的网站
WEB_URL = r'https://www.autohome.com.cn/all/1/#liststart'


# 图片保存路径
IMG_PATH = os.path.join(BASE_DIR,'db','img')
if not os.path.exists(IMG_PATH):os.makedirs(IMG_PATH)

# 日志文件路径
LOG_PATH = os.path.join(BASE_DIR,'log')
if not os.path.exists(LOG_PATH):os.makedirs(LOG_PATH)
LOG_FILE = r'%s/%s-log.txt' % (LOG_PATH,DAY_TIME)
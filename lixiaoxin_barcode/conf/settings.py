# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
#2019/12/2 10:11
import os
import time

# 获取当前时间
DAY_TIME = time.strftime('%Y-%m-%d', time.localtime(time.time()))
DATA_TIME = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))

# 保存的word文件名
DOCX_NAME = '条形码'
DOCX_NAME = DOCX_NAME + '_' + DATA_TIME + '.docx'

# 创建什么格式的条形码格式对象
CODE_FORMAT = 'Code128'

# 输入文本名称
CONTENT = 'content.txt'

# 生成条形码图片的名称
BAR_NAME_LIST = ['PART_NO','PACK_NO','Quantity']

# 基目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 数据存储路径
DB_PATH = os.path.join(BASE_DIR,'db')
if not os.path.exists(DB_PATH):os.makedirs(DB_PATH)

# 输入路径
INPUT_PATH = os.path.join(DB_PATH,'input')
if not os.path.exists(INPUT_PATH):os.makedirs(INPUT_PATH)

# 输入文件
INPUT_FILE = os.path.join(INPUT_PATH,CONTENT)

# 输出路径
OUTPUT_PATH = os.path.join(DB_PATH,'output')
if not os.path.exists(OUTPUT_PATH):os.makedirs(OUTPUT_PATH)

# 图片路径
IMG_PAHT = os.path.join(DB_PATH,'img')
if not os.path.exists(IMG_PAHT):os.makedirs(IMG_PAHT)

# logo图片
LOGO_PNG = os.path.join(IMG_PAHT,'logo.png')

#输出保存文件名称
OUPUT_FILE = os.path.join(OUTPUT_PATH,DOCX_NAME)

# 日志文件路径
LOG_PATH = os.path.join(BASE_DIR,'log')
if not os.path.exists(LOG_PATH):os.makedirs(LOG_PATH)
LOG_FILE = r'%s/%s-log.txt' % (LOG_PATH,DAY_TIME)







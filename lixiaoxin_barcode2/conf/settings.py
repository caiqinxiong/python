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

# 一行生成几个条形码
BARCODE_NUM = 2

############图片大小设置##################
LOGO_W = 0.4        # logo图片宽度
LOGO_H = 1.2        # logo图片高度
PART_NO_W = 1.5     # PART NO.条形码的宽度
PART_NO_H = 0.38    # PART NO.条形码的高度
PACK_NO_W = 1.5     # PACK NO.条形码的宽度
PACK_NO_H = 0.38    # PACK NO.条形码的高度
QUANTITY_W = 1.5    # Quantity条形码的宽度
QUANTITY_H = 0.38   # Quantity条形码的高度
##########################################
# 字体大小
WORD_SIZE = 8
# 字体格式
WORD_FORM = '宋体'

# 文本内容输入的表格开始行数，索引从0开始
START_ROW = 1  # 有表头时修改

# 创建什么格式的条形码格式对象
# CODE_FORMAT = 'Code128'
CODE_FORMAT = 'Code39'

# 输入文本名称
CONTENT = 'content.xls'

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
LOGO_PNG = os.path.join(BASE_DIR, 'doc', 'logo_n.png')

# doc模板
TEM_DOC = os.path.join(BASE_DIR, 'doc', 'template.docx')

#输出保存文件名称
OUPUT_FILE = os.path.join(OUTPUT_PATH,DOCX_NAME)

# 日志文件路径
LOG_PATH = os.path.join(BASE_DIR,'log')
if not os.path.exists(LOG_PATH):os.makedirs(LOG_PATH)
LOG_FILE = r'%s/%s-log.txt' % (LOG_PATH,DAY_TIME)







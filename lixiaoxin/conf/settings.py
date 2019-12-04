# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
#2019/12/2 10:11
import os
import time

# 获取当前时间
DAY_TIME = time.strftime('%Y-%m-%d', time.localtime(time.time()))
DATA_TIME = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))

# 表格读取开始行数，索引从0开始
START_ROW = 7 # 从表格第8行开始读

# 器件编号 的列号，索引从0开始
KEGUAN = 2

# 测试时间 的列号，索引从0开始
TSTM = 3

# 测试结果 的列号，索引从0开始
TSRS = 11

# 保存的表格名称
TABLE_NAME = 'NETD测试数据汇总'
TABLE_NAME = TABLE_NAME + '_' + DATA_TIME + '.xls'

# 表格sheet页名称
SHEET_SOURCE = '原始数据整合页'
SHEET_FILTER = '筛选后的数据'
SHEET_FT = 'FT'
SHEET_TCT = 'TCT'
SHEET_EXCEPT = '异常数据'
SHEET_ONE = '器件只有一个日期'
SHEET_MORE = '器件有多个日期'

# 基目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 数据存储路径
DB_PATH = os.path.join(BASE_DIR,'db')
if not os.path.exists(DB_PATH):os.makedirs(DB_PATH)

# 输入路径
INPUT_PATH = os.path.join(DB_PATH,'input')
if not os.path.exists(INPUT_PATH):os.makedirs(INPUT_PATH)

# 输出路径
OUTPUT_PATH = os.path.join(DB_PATH,'output')
if not os.path.exists(OUTPUT_PATH):os.makedirs(OUTPUT_PATH)

#输出保存文件名称
OUPUT_FILE = os.path.join(OUTPUT_PATH,TABLE_NAME)

# 日志文件路径
LOG_PATH = os.path.join(BASE_DIR,'log')
if not os.path.exists(LOG_PATH):os.makedirs(LOG_PATH)
LOG_FILE = r'%s/%s-log.txt' % (LOG_PATH,DAY_TIME)

# 临时文件目录
TMP_DIR = os.path.join(DB_PATH,'tmp')
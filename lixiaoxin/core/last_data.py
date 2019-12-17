# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
#2019/12/17 15:58
import os
import shutil
from conf import settings as ss
from core.excel_handler import Excel as ex
from core.log import Log as log

def run():
    '''主逻辑'''
    # 1.合并表格数据
    log.readAndWrite('开始合并表格数据!')
    date_list = ex().merger_excel()

    # 2.将合并后的数据写入表格
    log.readAndWrite('开始将合并后的数据写入表格！')
    ex().write_excel(date_list, ss.SHEET_SOURCE, ss.OUPUT_FILE)

    # 3.过滤数据
    log.readAndWrite('开始过滤数据，取最新日期的数据！')
    del date_list[0:2]
    date_list = ex().get_last_data(date_list)

    # 4.将筛选后的数据写入表格
    log.readAndWrite('开始将筛选后的数据写入表格！')
    ex().write_excel(date_list, ss.SHEET_FILTER, ss.OUPUT_FILE)


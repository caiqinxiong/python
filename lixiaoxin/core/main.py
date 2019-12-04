# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
#2019/12/3 16:29
import copy
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
    log.readAndWrite('开始过滤数据！')
    tmp_list = copy.deepcopy(date_list)  # 将原始数据列表进行深拷贝
    date_list = ex().filter_date(date_list, tmp_list)

    # 4.将筛选后的数据写入表格
    log.readAndWrite('开始将筛选后的数据写入表格！')
    ex().write_excel(date_list, ss.SHEET_FILTER, ss.OUPUT_FILE)

    # 5.将数据拆分成FC和TCT
    log.readAndWrite('开始将数据拆分成第一类测试%s数据和第二类测试%s数据！' % (ss.SHEET_FT,ss.SHEET_TCT))
    ft_list, tct_list = ex().split_list(date_list)

    # 6.将第一类测试FC数据写入表格
    log.readAndWrite('开始将第一类测试%s数据写入表格！' % ss.SHEET_FT)
    ex().write_excel(ft_list, ss.SHEET_FT, ss.OUPUT_FILE)

    # 7.将第二类测试TCT数据写入表格
    log.readAndWrite('开始将第二类测试%s数据写入表格！' % ss.SHEET_TCT)
    ex().write_excel(tct_list, ss.SHEET_TCT, ss.OUPUT_FILE)
# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
#2019/12/3 16:29
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

    # 3.生成每个器件文件信息
    log.readAndWrite('开始生成器件文件信息！')
    ex().device_file(date_list)

    # 4.过滤数据
    log.readAndWrite('开始过滤数据！')
    filter_list,ft_list,tct_list,except_list,one_test_list,more_test_list = ex().filter_date()

    # 5.将筛选后的数据写入表格
    log.readAndWrite('开始将筛选后的数据写入表格！')
    ex().write_excel(filter_list, ss.SHEET_FILTER, ss.OUPUT_FILE)

    # 6.将第一类测试FT数据写入表格
    log.readAndWrite('开始将第一类测试%s数据写入表格！' % ss.SHEET_FT)
    ex().write_excel(ft_list, ss.SHEET_FT, ss.OUPUT_FILE)

    # 7.将第二类测试TCT数据写入表格
    log.readAndWrite('开始将第二类测试%s数据写入表格！' % ss.SHEET_TCT)
    ex().write_excel(tct_list, ss.SHEET_TCT, ss.OUPUT_FILE)

    # 8.将异常数据写入表格
    if except_list:
        log.readAndWrite('开始将异常数据写入表格')
        ex().write_excel(except_list,ss.SHEET_EXCEPT, ss.OUPUT_FILE)

    # 9.将只进行了一类测试数据写入表格
    if one_test_list:
        log.readAndWrite('开始将%s写入表格' % ss.SHEET_ONE)
        ex().write_excel(one_test_list, ss.SHEET_ONE, ss.OUPUT_FILE)

    # 10.将器件有多个日期
    if more_test_list:
        log.readAndWrite('开始将%s写入表格' % ss.SHEET_MORE)
        ex().write_excel(more_test_list, ss.SHEET_MORE, ss.OUPUT_FILE)

    # 11.清理临时文件
    log.readAndWrite('*'*200 + '\n' + '数据筛选完成!表格路径如下：\n%s' % ss.OUPUT_FILE + '\n' + '*'*200  )
    if os.path.exists(ss.TMP_DIR):shutil.rmtree(ss.TMP_DIR)
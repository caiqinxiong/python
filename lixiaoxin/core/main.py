# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
#2019/12/3 16:29
from conf import settings as ss
from core.log import Log as log
from core import filter_data
from core import merge_data
from core import last_data

def main():
    '''主逻辑'''
    if 0 == ss.SWITCH:
        log.readAndWrite('只获取管壳最新日期的数据!')
        last_data.run()
    elif 1 == ss.SWITCH:
        log.readAndWrite('把TCT和FT的数据过滤并分开写入表格！')
        filter_data.run()
    elif 2 == ss.SWITCH:
        log.readAndWrite('把XX_result.csv里面的结果提取出来合并到一个表格!')
        merge_data.run()
    else:
        log.error('开关选择错误！！')
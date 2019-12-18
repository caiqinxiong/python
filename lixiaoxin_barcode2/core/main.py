# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
#2019/12/18 16:36
import os,sys
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.barcode_handler import *

def run():
    '''主逻辑'''
    # 1.读取文本内容
    data_list = read_file()

    # 2.循环生成条形码图片
    for i in range(len(data_list)): create_barcode(data_list[i], ss.BAR_NAME_LIST[i])

    # 3.将条形码插入docx
    write_docx(data_list)


if __name__ == '__main__':
    run()
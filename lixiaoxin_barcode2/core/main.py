# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
#2019/12/18 16:36
import os,sys
import shutil
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.barcode_handler import *

def run():
    '''主逻辑'''
    # 1.读取文本内容
    data_list = read_excel()

    # 2.循环生成条形码图片
    for i in range(len(data_list)):
        for j in range(len(data_list[i])):
            bracode_name = str(i) + '_' + str(j)
            create_barcode(data_list[i][j], bracode_name)

    # 3.将条形码插入docx
    write_docx(data_list)

    # 4.清理生成的条形码图片
    # if os.path.exists(ss.IMG_PAHT): shutil.rmtree(ss.IMG_PAHT)

if __name__ == '__main__':
    run()
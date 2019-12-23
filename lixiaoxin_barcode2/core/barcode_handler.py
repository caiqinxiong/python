# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
#2019/12/17 10:44
# 解决pip下载速度慢的问题
# https://blog.csdn.net/wolflikeinnocence/article/details/80140064

import os
import docx
import barcode
import xlrd
from barcode.writer import ImageWriter
from docx.shared import Inches   #设置图像大小
from docx.shared import Pt    #设置像素、缩进等
from win32com import client as wc
from conf import settings as ss
from core.log import Log as log

# def doc_to_docx():
#     '''.doc文件转化为.docx文件'''
#     word = wc.Dispatch('Word.Application')
#     doc = word.Documents.Open(ss.TEM_DOC)  # 目标路径下的文件
#     doc.SaveAs(ss.OUPUT_FILE, 12, False, "", True, "", False, False, False, False)  # 转化后路径下的文件
#     doc.Close()
#     word.Quit()

def read_excel(start_row=0, end_row=0, sheet_index=0):
    '''读取表格信息'''
    date_list = []
    workbook = xlrd.open_workbook(ss.INPUT_FILE)
    # 选择第1个sheet表，索引从0开始
    sheet = workbook.sheet_by_index(sheet_index)
    if not end_row:end_row = sheet.nrows
    # 从表格中读取数据，追加到列表中
    log.readAndWrite('从表格中读取数据，追加到列表中,跳过表头从%s行开始读取数据，共%s行数据！' % (start_row, sheet.nrows - start_row))
    for i in range(start_row,end_row):
        date_list.append(sheet.row_values(i))
    else:
        log.readAndWrite('数据读取完成！')
    return date_list

def create_barcode(content,bracode_name):
    '''条形码生成'''
    EAN = barcode.get_barcode_class(ss.CODE_FORMAT)  # 创建Code128格式的条形码格式对象
    ean = EAN(content, writer=ImageWriter())  # 创建条形码对象，内容为content参数传入
    bracode_name = os.path.join(ss.IMG_PAHT,bracode_name)
    log.readAndWrite('内容为%s的条形码%s生成ok' % (content,bracode_name))
    return ean.save(bracode_name, {'write_text': False})  # 保存条形码图片，并返回保存路径。图片格式为png,{'write_text': False}为不要底下的文字内容

def wirte_barcode(document,data_list,i,n,m):
    '''写入条形码'''
    # 写入logo
    table = document.tables[0].cell(n, m).paragraphs[0].add_run()
    table.add_picture(ss.LOGO_PNG, width=Inches(0.4), height=Inches(1.2))
    # 写入条形码
    table = document.tables[0].cell(n, m+1).paragraphs[0].add_run()
    table.text = ' ' + data_list[i][0] + '\t\t\n'
    name = str(i) + '_0.png'
    table.add_picture(os.path.join(ss.IMG_PAHT, name), width=Inches(1.5), height=Inches(0.38))
    table = document.tables[0].cell(n, m+1).paragraphs[0].add_run()
    table.text = '\n ' + data_list[i][1] + ' \t\t\n'
    name = str(i) + '_1.png'
    table.add_picture(os.path.join(ss.IMG_PAHT, name), width=Inches(1.5), height=Inches(0.38))
    table = document.tables[0].cell(n, m+1).paragraphs[0].add_run()
    table.text = '\n ' + data_list[i][2] + ' \t\t\n'
    name = str(i) + '_2.png'
    table.add_picture(os.path.join(ss.IMG_PAHT, name), width=Inches(1.5), height=Inches(0.38))
    DATE = '\n ' + 'DATE:' + ss.DAY_TIME + ' \t'
    table = document.tables[0].cell(n, m+1).paragraphs[0].add_run()
    table.text = DATE  # 写入当前日期

def write_docx(data_list):
    '''将条形码写入docx'''
    document=docx.Document(ss.TEM_DOC)   # 打开模板
    document.styles['Normal'].font.name = '宋体'  # 设置西文字体
    document.styles['Normal'].font.size = Pt(8)  # 设置字号
    document.styles['Normal'].paragraph_format.space_after = Pt(0)  # 设置段后间距
    n = 0;m = 0
    for i in range(len(data_list)):
        # 写入条形码
        wirte_barcode(document, data_list, i, n, m)
        m = m+2
        if m > 4:m = 0;n = n+1
    else:
        log.readAndWrite('文档内容填写完成，地址为：\n%s' % ss.OUPUT_FILE)

    # 保存docx文档
    return  document.save(ss.OUPUT_FILE)
    





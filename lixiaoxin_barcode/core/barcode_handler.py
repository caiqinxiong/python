# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
#2019/12/17 10:44
import os
import docx
import barcode
from barcode.writer import ImageWriter
from docx import Document
from docx.enum.text import WD_LINE_SPACING
from docx.enum.text import WD_TAB_ALIGNMENT,WD_TAB_LEADER  #设置制表符等
from docx.shared import Inches   #设置图像大小
from docx.shared import Pt    #设置像素、缩进等
from docx.shared import RGBColor    #设置字体颜色
from docx.shared import Length    #设置宽度
from conf import settings as ss

def read_file():
    '''读取文本信息'''
    data_list = []
    with open(ss.INPUT_FILE,mode='r') as f:
        for line in f:
            line = line.strip()
            if line:data_list.append(line)
    return data_list

def create_barcode(content,bracode_name):
    '''条形码生成'''
    EAN = barcode.get_barcode_class(ss.CODE_FORMAT)  # 创建Code128格式的条形码格式对象
    ean = EAN(content, writer=ImageWriter())  # 创建条形码对象，内容为content参数传入
    bracode_name = os.path.join(ss.IMG_PAHT,bracode_name)
    return ean.save(bracode_name, {'write_text': False})  # 保存条形码图片，并返回保存路径。图片格式为png,{'write_text': False}为不要底下的文字内容

def get_barcode():
    '''获取条形码图片地址'''
    barcode_list = []
    for i in ss.BAR_NAME_LIST:
        name = i + '.png'
        name = os.path.join(ss.IMG_PAHT,name)
        barcode_list.append(name)
    return barcode_list

def write_docx(data_list):
    '''将条形码写入docx'''
    barcode_list = get_barcode() # 获取条形码图片地址
    document=docx.Document()   # 创建一个空白文档
    table=document.add_table(rows=4,cols=2)
    run = document.tables[0].cell(0, 0).paragraphs[0].add_run()
    run.add_picture(ss.LOGO_PNG)
    for i in range(len(data_list)):
        cell = table.cell(i, 1)
        cell.text = data_list[i]
        run = document.tables[0].cell(i, 1).paragraphs[0].add_run()
        run.add_picture(barcode_list[i],width=Inches(2.0), height=Inches(0.5))
        document.tables[0].cell(i, 1).paragraphs[0].add_run()
    DATE = 'DATE:' + ss.DAY_TIME
    cell = table.cell(3, 1)
    cell.text = DATE
    document.save(ss.OUPUT_FILE)

def main():
    '''主逻辑'''
    # 1.读取文本内容
    data_list = read_file()
    
    # 2.循环生成条形码图片
    for i in range(len(data_list)):create_barcode(data_list[i],ss.BAR_NAME_LIST[i])

    # 3.将条形码插入docx
    write_docx(data_list)

main()
# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/12/6 10:45
import os
import xlrd
import xlwt
import csv
from xlutils.copy import copy as xl_copy
from conf import settings as ss
from core.log import Log as log

def read_excel(excel, date_list):
    '''读取表格信息'''
    with open(excel) as csvfile:
        csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
        table_header = next(csv_reader)  # 读取第一行每一列的标题
        table_header.insert(0, '器件编号')
        if table_header not in date_list: date_list.insert(0, table_header)
        for row in csv_reader:  # 将csv 文件中的数据保存到birth_data中
            date_list.append(row)
    return date_list

def background_color():
    '''设置表格背景颜色'''
    # pattern = xlwt.Pattern()
    # pattern.pattern = xlwt.Pattern.SOLID_PATTERN
    # # 背景颜色: 17 = Dark Green, 18 = Dark Blue, 19 = Dark Yellow , almost brown), 20 = Dark Magenta, 21 = Teal, 22 = Light Gray, 23 = Dark Gray
    # pattern.pattern_fore_colour = 3
    # style.pattern = pattern
    # # 字体加粗
    # style = xlwt.easyxf('font: bold on')
    # 样式合并
    style = xlwt.easyxf('pattern: pattern solid, fore_colour ice_blue; font: bold on')
    return style


def table_style(sheet,flag):
    '''设置表格格式'''
    # 创建一个样式对象，初始化样式
    style = xlwt.XFStyle()  # Create style
    if flag == 0 : style = background_color()
    # 设置列宽
    col_wide = sheet.col(0)  # 设置 器件编号 列宽
    col_wide.width = 256 * 20  # 256为衡量单位，20表示20个字符宽度
    col_wide = sheet.col(1)  # 设置 平均响应率 列宽
    col_wide.width = 256 * 18
    col_wide = sheet.col(2)  # 设置 平均噪声 列宽
    col_wide.width = 256 * 18
    col_wide = sheet.col(3)  # 设置 平均NETD 列宽
    col_wide.width = 256 * 15
    col_wide = sheet.col(4)  # 设置 坏点数量 列宽
    col_wide.width = 256 * 13
    borders = xlwt.Borders()  # Create borders
    borders.top = xlwt.Borders.THIN  # 添加上边框
    borders.bottom = xlwt.Borders.THIN  # 添加下边框
    borders.right = xlwt.Borders.THIN  # 添加右边框
    borders.left = xlwt.Borders.THIN  # 添加左边框
    # borders.left_colour = 0x90  # 边框上色
    # borders.right_colour = 0x90
    # borders.top_colour = 0x90
    # borders.bottom_colour = 0x90
    style.borders = borders  # Add borders to style

    al = xlwt.Alignment()
    al.horz = 0x02  # 设置水平居中
    al.vert = 0x01  # 设置垂直居中
    style.alignment = al

    return style

def write_excel(date_list, sheet_name, save_path):
    '''将数据写入新的表格'''
    if os.path.exists(save_path):
        # 表格已存在，直接打开
        rb = xlrd.open_workbook(save_path, formatting_info=True)
        workbook = xl_copy(rb)  # 从打开的xlrd的Book变量中，拷贝出一份，成为新的xlwt的Workbook变量
    else:
        # 创建工作簿
        log.readAndWrite('创建表格%s' % save_path)
        workbook = xlwt.Workbook(encoding='utf-8')
    # 创建一个sheet表
    log.readAndWrite('添加sheet页“%s”' % sheet_name)
    sheet = workbook.add_sheet(sheet_name, cell_overwrite_ok=True)
    log.readAndWrite('开始往“%s”中写入数据，共%s行!' % (sheet_name, len(date_list)))
    for i in range(len(date_list)):
        for j in range(len(date_list[i])):
            style = table_style(sheet,i)  # 设置表格格式
            sheet.write(i, j, date_list[i][j],style)
    else:
        log.readAndWrite('“%s”数据填写完成！' % sheet_name)
    # 将数据写入表格
    return workbook.save(save_path)

def merger_excel(path, date_list):
    '''将原始数据整合'''
    # 循环获取目录下的所有表格
    # log.readAndWrite('循环获取input目录下的所有XXX%s表格！' % ss.RESULT_CSV)
    guanke = os.path.basename(path)
    guanke_txt = '_' + guanke + '.txt'
    if os.path.isdir(path) and not guanke.find('_') < 0:
        for i in os.listdir(path):
            file_path = os.path.join(path, i)
            if os.path.isfile(file_path) and file_path.endswith(ss.RESULT_CSV):
                log.readAndWrite('读取表格%s的信息' % file_path)
                date_list = read_excel(file_path, date_list)
            elif os.path.isfile(file_path) and file_path.endswith(guanke_txt):
                guanke_name = os.path.basename(file_path).split(guanke_txt)[0]  # 获取器件编号
                date_list[-1].insert(0, guanke_name)  # 将器件编号插入对应的列表中
    elif os.path.isfile(path):
        pass  # 执行到文件就结束递归
    else:
        for i in os.listdir(path):
            file_path = os.path.join(path, i)
            merger_excel(file_path, date_list)
    return date_list

def run():
    '''主逻辑'''
    # 初始化
    path = ss.CSV_INPUT  # 输入路径
    date_list = []  # 数据存储列表
    date_list = merger_excel(path, date_list)
    write_excel(date_list,ss.CSV_SHEET,ss.CSV_NAME)


# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
#2019/12/2 10:07
import os
import xlrd
import xlwt
from xlutils.copy import copy as xl_copy
from conf import settings as ss
from core.log import Log as log


class Excel:

    def read_excel(self,excel,date_list,start_row=0,sheet_index=0):
        '''读取表格信息'''
        workbook = xlrd.open_workbook(excel)
        # 选择第1个sheet表，索引从0开始
        sheet = workbook.sheet_by_index(sheet_index)
        # 从表格中读取数据，追加到列表中
        log.readAndWrite('从表格中读取数据，追加到列表中,跳过表头从%s行开始读取数据，共%s行数据！' % (start_row,sheet.nrows-start_row))
        for i in range(start_row,sheet.nrows):
            date_list.append(sheet.row_values(i))
        else:
            log.readAndWrite('数据读取完成！')
        return date_list

    def write_excel(self,date_list,sheet_name,save_path):
        '''将数据写入新的表格'''
        if os.path.exists(save_path):
            # 表格已存在，直接打开
            rb = xlrd.open_workbook(save_path, formatting_info=True)
            workbook = xl_copy(rb) # 从打开的xlrd的Book变量中，拷贝出一份，成为新的xlwt的Workbook变量
        else:
            # 创建工作簿
            log.readAndWrite('创建表格%s' % save_path)
            workbook = xlwt.Workbook(encoding='utf-8')
        # 创建一个sheet表
        log.readAndWrite('添加sheet页“%s”' % sheet_name)
        sheet = workbook.add_sheet(sheet_name,cell_overwrite_ok=True)
        log.readAndWrite('开始往“%s”中写入数据，共%s行!' % (sheet_name,len(date_list)))
        for i in range(len(date_list)):
            for j in range(len(date_list[i])):
                sheet.write(i,j,date_list[i][j])
        else:
            log.readAndWrite('“%s”数据填写完成！' % sheet_name)
        # 将数据写入表格
        return  workbook.save(save_path)

    def merger_excel(self):
        '''将原始数据整合'''
        path = ss.INPUT_PATH
        date_list = []
        # 循环获取目录下的所有表格
        log.readAndWrite('循环获取input目录下的所有表格！')
        for i in os.listdir(path):
            file_path = os.path.join(path, i)
            if file_path.endswith('.xlsx') or file_path.endswith('.xls'):
                log.readAndWrite('读取表格%s的信息' % file_path)
                date_list = self.read_excel(file_path,date_list,ss.START_ROW)
        else:
            log.readAndWrite('数据获取完成！')
        return date_list


    def filter_date(self,date_list,tmp_list):
        '''剔除多余数据'''
        log.readAndWrite('开始筛选数据！')
        for i in (range(1,len(tmp_list))):
            if tmp_list[i-1][ss.KEGUAN] == tmp_list[i][ss.KEGUAN] and tmp_list[i-1][ss.TSTM].split()[0] == tmp_list[i][ss.TSTM].split()[0]:
                if tmp_list[i-1][ss.TSRS] == tmp_list[i][ss.TSRS]:
                    # log.readAndWrite('测试结果都是“通过”或者“不通过”的情况，保留最新日期的数据！')
                    date = tmp_list[i-1] if tmp_list[i-1][ss.TSTM].split()[1] < tmp_list[i][ss.TSTM].split()[1] else tmp_list[i]
                else:
                    # log.readAndWrite('测试结果有“通过”和“不通过的情况，保留通过的数据！')
                    date = tmp_list[i-1] if tmp_list[i-1][ss.TSRS] == '不通过' else tmp_list[i]
                # 剔除列表中多余数据
                # log.readAndWrite('删除数据%s' % date)
                if date in date_list:del date_list[date_list.index(date)] # 可能上次循环已经删除，所以要判断一下数据是否还在列表中
        return date_list

    def split_list(self,date_list):
        '''数据列表拆分，把第一类测试和第二类测试数据分开'''
        # 第一类测试
        ft_list = []
        # 第二类测试
        tct_list = []
        for i in range(len(date_list)):
            if i % 2 != 0:
                ft_list.append(date_list[i])
            else:
                tct_list.append(date_list[i])
        else:
            log.readAndWrite('数据列表拆分，把第一类测试和第二类测试数据分开!')
        return ft_list,tct_list






















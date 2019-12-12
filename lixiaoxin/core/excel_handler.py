# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/12/2 10:07
import os
import xlrd
import xlwt
# import openpyxl
import json
import shutil
import copy
import datetime
from xlutils.copy import copy as xl_copy
from conf import settings as ss
from core.log import Log as log


class Excel:

    def read_excel(self, excel, date_list, start_row=0, end_row=0, sheet_index=0):
        '''读取表格信息'''
        workbook = xlrd.open_workbook(excel)
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

    def table_style(self,sheet,flag):
        '''设置表格格式'''
        # 创建一个样式对象，初始化样式
        style = xlwt.XFStyle()  # Create style
        if flag <2: style = self.background_color()
        # 设置列宽
        qijian_col = sheet.col(ss.KEGUAN)  # 设置器件列宽
        qijian_col.width = 256 * 18  # 256为衡量单位，18表示18个字符宽度
        time_col = sheet.col(ss.TSTM)  # 设置时间列宽
        time_col.width = 256 * 20
        for i in range(4,13):# 4到12列的宽度
            mk_col = sheet.col(i)
            mk_col.width = 256 * 15
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

    def background_color(self):
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


    def write_excel(self, date_list, sheet_name, save_path):
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
        # style = self.table_style(sheet) # 设置表格格式
        # 插入表头数据
        for i in ss.HEAD_LIST:date_list.insert(0,i)
        log.readAndWrite('开始往“%s”中写入数据，共%s行!' % (sheet_name, len(date_list)))
        for i in range(len(date_list)):
            style = self.table_style(sheet, i)  # 设置表格格式
            for j in range(len(date_list[i])):
                if i == 0:
                    if j == 4:# 表头合并单元格
                        sheet.write_merge(i,i,j,j+8,date_list[i][j], style)
                    else:
                        sheet.write_merge(i,i+1,j,j,date_list[i][j], style)
                elif i == 1:
                    sheet.write_merge(i, i, j, j, date_list[i][j], style)
                else:
                    sheet.write(i, j, date_list[i][j], style)
        else:
            log.readAndWrite('“%s”数据填写完成！' % sheet_name)
        # 将数据写入表格
        return workbook.save(save_path)

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
                date_list = self.read_excel(file_path, date_list, ss.START_ROW)
        else:
            log.readAndWrite('数据获取完成！')
        return date_list

    def device_file(self, date_list):
        '''生成每个器件文件'''
        if os.path.exists(ss.TMP_DIR):shutil.rmtree(ss.TMP_DIR)# 清理tmp目录
        os.makedirs(ss.TMP_DIR)  # 创建临时存储文件目录
        # 循环列表，生成每个器件的文件信息
        for i in date_list:
            file = os.path.join(ss.TMP_DIR, i[ss.KEGUAN])
            conten = json.dumps(i, ensure_ascii=False)
            with open(file, mode='a', encoding='utf-8') as f:
                f.write(conten + '\n')
        else:
            log.readAndWrite('生成器件文件信息完成！')
        return date_list


    def eliminate_date(self, file_list, tmp_list, ft_time, TSRS):
        '''剔除多余数据'''
        date = []
        for i in (range(1, len(tmp_list))):
            if TSRS == '通过': # TCT均为通过
                # 1.1 FT测试中有通过和不通过的情况，则认为FT测试通过，取通过的最新数据
                if ft_time == tmp_list[i][ss.TSTM].split()[0] and tmp_list[i][ss.TSRS] == '不通过':
                    date = tmp_list[i] # 直接删除不通过的数据
                # 1.2 FT均为通过，取通过的最新数据
                elif tmp_list[i - 1][ss.TSTM].split()[0] == tmp_list[i][ss.TSTM].split()[0] and tmp_list[i -1][ss.TSRS] == tmp_list[i][ss.TSRS]: # 同一类测试比较
                    t1 = datetime.datetime.strptime(tmp_list[i - 1][ss.TSTM].split()[1], '%H:%M:%S')
                    t2 = datetime.datetime.strptime(tmp_list[i][ss.TSTM].split()[1], '%H:%M:%S')
                    t = t1 - t2
                    date = tmp_list[i - 1] if t.seconds < 0 else tmp_list[i]
            else:# TCT均为不通过
                # 2.1 FT测试中有通过有不通过情况，则认为FT测试不通过，取不通过的最新数据
                if ft_time == tmp_list[i][ss.TSTM].split()[0] and tmp_list[i][ss.TSRS] == '通过':
                    date = tmp_list[i] # 直接删除通过的数据
                # 2.3 FT测试均不通过，取不通过的最新数据
                elif tmp_list[i - 1][ss.TSTM].split()[0] == tmp_list[i][ss.TSTM].split()[0] and tmp_list[i -1][ss.TSRS] == tmp_list[i][ss.TSRS]: # 同一类测试比较
                    t1 = datetime.datetime.strptime(tmp_list[i - 1][ss.TSTM].split()[1], '%H:%M:%S')
                    t2 = datetime.datetime.strptime(tmp_list[i][ss.TSTM].split()[1], '%H:%M:%S')
                    t = t1 - t2
                    date = tmp_list[i - 1] if t.seconds < 0 else tmp_list[i]
                # 剔除列表中多余数据
            if date in file_list: del file_list[file_list.index(date)]  # 可能上次循环已经删除，所以要判断一下数据是否还在列表中
        return file_list


    def split_list(self, file_list,tct_list,ft_list,tct_time,ft_time):
        '''数据列表拆分，把第一类测试和第二类测试数据分开'''
        for i in file_list:
            if tct_time == i[ss.TSTM].split()[0]:
                tct_list.append(i)
            elif ft_time == i[ss.TSTM].split()[0]:
                ft_list.append(i)
            else:
                log.error(i)
        return tct_list,ft_list

    def read_file(self,file_path):
        '''读取每个器件文件信息'''
        file_list = []
        with open(file_path, mode='r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    content = json.loads(line)
                    file_list.append(content)
        return file_list

    def get_test_time(self,file_list):
        '''获取测试时间'''
        time_list = []  # 测试时间
        for t in file_list:
            if t[ss.TSTM].split()[0] not in time_list: time_list.append(t[ss.TSTM].split()[0])
        return time_list


    def ft_tct_time(self,time_list):
        '''获取FT和TCT的日期'''
        t1 = datetime.datetime.strptime(time_list[0], '%Y/%m/%d')
        t2 = datetime.datetime.strptime(time_list[1], '%Y/%m/%d')
        t = t1 - t2
        tct_time = time_list[0] if t.days > 0 else time_list[1]
        ft_time = time_list[0] if t.days < 0 else time_list[1]
        return tct_time,ft_time

    def test_results(self,file_list,tct_time,ft_time):
        '''获取测试结果信息'''
        tct_pass_list = []
        tct_nopass_list = []
        ft_pass_list = []
        ft_nopass_list = []
        for d in file_list:
            if tct_time == d[ss.TSTM].split()[0] and d[ss.TSRS] == '通过':
                tct_pass_list.append(d)
            elif tct_time == d[ss.TSTM].split()[0] and d[ss.TSRS] == '不通过':
                tct_nopass_list.append(d)
            elif ft_time == d[ss.TSTM].split()[0] and d[ss.TSRS] == '通过':
                ft_pass_list.append(d)
            elif ft_time == d[ss.TSTM].split()[0] and d[ss.TSRS] == '不通过':
                ft_nopass_list.append(d)
            else:
                log.error(d)
        return tct_pass_list,tct_nopass_list,ft_pass_list,ft_nopass_list

    def append_to_list(self,file_list,date_list):
        '''列表数据添加'''
        for i in file_list:
            date_list.append(i)
        return date_list

    def filter_ft_tct(self,time_list,file_list,except_list,filter_list,tct_list,ft_list):
        '''数据筛选主逻辑'''
        # 获取TCT测试时间
        tct_time, ft_time = self.ft_tct_time(time_list)
        # 获取测试结果信息
        tct_pass_list, tct_nopass_list, ft_pass_list, ft_nopass_list = self.test_results(file_list,tct_time,ft_time)
        tmp_list = copy.deepcopy(file_list)
        # TCT全部通过
        if 0 != len(tct_pass_list) and 0 == len(tct_nopass_list):
            if 0 != len(ft_nopass_list) and 0 == len(ft_pass_list):  # TCT均为通过,FT均不通过，异常
                except_list = self.append_to_list(file_list, except_list)
            else:  # TCT均为通过,FT有通过
                file_list = self.eliminate_date(file_list, tmp_list, ft_time, TSRS = '通过')
                filter_list = self.append_to_list(file_list, filter_list)
                tct_list, ft_list = self.split_list(file_list, tct_list, ft_list, tct_time, ft_time)
        # TCT有通过，有不通过，则将该器件的FT和TCT测试数据均挑出，为异常数据
        elif 0 != len(tct_pass_list) and 0 != len(tct_nopass_list):
            except_list = self.append_to_list(file_list, except_list)
        # TCT均不通过
        elif 0 == len(tct_pass_list) and 0 != len(tct_nopass_list):
            if 0 == len(ft_nopass_list) and 0 != len(ft_pass_list):  # 2.2 TCT均不通过, FT测试均通过，异常，加入异常数据表
                except_list = self.append_to_list(file_list, except_list)
            else:  # TCT均为不通过（不管几次），FT测试中有通过有不通过，则认为FT测试不通过，以最后一次FT测试结果为准。FT取不通过的结果
                file_list = self.eliminate_date(file_list, tmp_list, ft_time, TSRS = '不通过')
                filter_list = self.append_to_list(file_list, filter_list)
                tct_list, ft_list = self.split_list(file_list, tct_list, ft_list, tct_time, ft_time)
        else:
            log.error('*****************')
        return except_list,filter_list,tct_list,ft_list


    def filter_date(self):
        '''数据筛选入口函数'''
        path = ss.TMP_DIR
        filter_list = [] # 筛选后的数据
        ft_list = [] # 第一类测试
        tct_list = [] # 第二类测试
        except_list = []  # 异常数据
        one_test_list = []  # 只进行一类测试
        more_test_list = [] # 器件有多个日期
        log.readAndWrite('循环读取每个器件文件的信息')
        for i in os.listdir(path):
            file_path = os.path.join(path, i)
            file_list = self.read_file(file_path)
            time_list = self.get_test_time(file_list)
            if 1 == len(time_list):
                one_test_list = self.append_to_list(file_list, one_test_list)
            elif 2 == len(time_list):
                except_list, filter_list, tct_list, ft_list = self.filter_ft_tct(time_list,file_list,except_list,filter_list,tct_list,ft_list)
            else:
                more_test_list = self.append_to_list(file_list,more_test_list)

        return filter_list,ft_list,tct_list,except_list,one_test_list,more_test_list

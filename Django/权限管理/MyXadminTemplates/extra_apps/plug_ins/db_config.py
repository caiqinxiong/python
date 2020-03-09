__author__ = 'Luzaofa'
__date__ = '2018/9/12 19:57'

import sqlite3
from datetime import datetime


class DB_helper(object):

    def __init__(self):
        self.conn = sqlite3.connect('../MyXadminTemplates/db.sqlite3')

        self.cursor = self.conn.cursor()

    def select_menu_1(self, name, starttime, endtime, nowtime):

        now_ = datetime.now().strftime('%Y-%m-%d')

        # 根据名称查询(全部填写)
        if nowtime == '' and name != '' and starttime != '' and endtime != '':
            sql = """
                select date, productname, stunum, grade from XXX
                where name = '%s' and t1.date >= '%s' and t1.date <= '%s'
            """ % (name, starttime, endtime)
        # 根据名称查询（无开始、结束日期）
        elif nowtime == '' and name != '' and starttime == '' and endtime == '':
            sql = """
                select date, productname, stunum, grade from XXX
                where name = '%s'
            """ % (name)

        self.cursor.execute(sql)
        values = self.cursor.fetchall()
        value = []
        for V in values:
            value.append(V)
        return value

    def select_menu_2(self, name, starttime, endtime, nowtime):

        sql = """select * from XXX where XXX"""
        pass

    def select_menu_3(self, name, starttime, endtime, nowtime):

        sql = """select * from XXX where XXX"""
        pass

# -*- coding:utf-8 -*-
# Author:caiqinxiong
import pymysql

# 创建连接
conn = pymysql.connect(host='172.16.219.139', port=3306, user='root', passwd='root', db='cai')
# 创建游标
cursor = conn.cursor()

# 执行SQL，并返回收影响行数
effect_row = cursor.execute("select * from stutant")

#print(cursor.fetchone())
#print(cursor.fetchall()) # 接着读取后面的所有

date = [
    ('caiqinxiong',29,'2018-08-19'),
    ('cai',28,'2018-08-20'),
    ('xin',31,'2018-08-18'),
    ]
cursor.executemany('insert into stutant (name,age,registe_date) VALUES (%s,%s,%s) ', date)
# 提交，不然无法保存新建或者修改的数据
conn.commit()
print(cursor.fetchone())
print(cursor.fetchall()) # 接着读取后面的所有

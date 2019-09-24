# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/9/23 11:15

# 作业链接：https://www.cnblogs.com/Eva-J/articles/11074845.html
'''
# 0.建表book，并向表中插入数据
'''
# 创建book表
# create table book(书名 char(20) not null unique, 作者 char(20) not null, 出版社 char(30) not null, 价格 int not null, 出版日期 date not null) charset = utf8;
# 查看表结构
# desc book;
# +--------------+----------+------+-----+---------+-------+
# | Field        | Type     | Null | Key | Default | Extra |
# +--------------+----------+------+-----+---------+-------+
# | 书名          | char(20) | NO   | PRI | NULL    |       |
# | 作者          | char(20) | NO   |     | NULL    |       |
# | 出版社        | char(30) | NO   |     | NULL    |       |
# | 价格          | int(11)  | NO   |     | NULL    |       |
# | 出版日期       | date     | NO   |     | NULL    |       |
# +--------------+----------+------+-----+---------+-------+
# 5 rows in set (0.01 sec)

# 向book表插入7条数据
'''

insert into book values
('倚天屠龙记','egon','北京工业地雷出版社', 70,20190701),
('九阳神功','alex','人民音乐不好听出版社',5,20180704),
('九阴真经', 'yuan','北京工业地雷出版社',62,20170712),
('九阴白骨爪','jinxin','人民音乐不好听出版社',40,20190807),
('独孤九剑','alex','北京工业地雷出版社', 12,20170901),
('降龙十巴掌','egon','知识产权没有用出版社',20,20190705),
('葵花宝典','yuan','知识产权没有用出版社',33,20190802);

'''
# 查询book表所有数据
# mysql> select * from book;
# +-----------------+--------+--------------------------------+------
# | 书名           | 作者    | 出版社            | 价格 |   出版日期     |
# +-----------------+--------+--------------------------------+------
# | 九阳神功        | alex   | 人民音乐不好听出版社 |   5 | 2018-07-04   |
# | 九阴白骨爪      | jinxin | 人民音乐不好听出版社 |  40 | 2019-08-07   |
# | 九阴真经        | yuan   | 北京工业地雷出版社  |  62 | 2017-07-12   |
# | 倚天屠龙记      | egon   | 北京工业地雷出版社   | 70 | 2019-07-01   |
# | 独孤九剑        | alex   | 北京工业地雷出版社   | 12 | 2017-09-01   |
# | 葵花宝典        | yuan   | 知识产权没有用出版社 | 33 | 2019-08-02   |
# | 降龙十巴掌      | egon   | 知识产权没有用出版社 | 20 | 2019-07-05   |
# +-----------------+--------+--------------------------------+----
# 7 rows in set (0.00 sec)

'''
1.查询egon写的所有书和价格
'''
#mysql> select 书名,价格 from book where 作者='egon';
# +-----------------+--------+
# | 书名            | 价格    |
# +-----------------+--------+
# | 倚天屠龙记       |     70 |
# | 降龙十巴掌       |     20 |
# +-----------------+--------+
# 2 rows in set (0.00 sec)

'''
2.找出最贵的图书的价格
'''
# mysql> select max(价格) from book;
# +-------------+
# | max(价格)    |
# +-------------+
# |          70 |
# +-------------+
# 1 row in set (0.00 sec)


'''
3.求所有图书的均价
'''
# mysql> select avg(价格) from book;
# +-------------+
# | avg(价格)    |
# +-------------+
# |     34.5714 |
# +-------------+
# 1 row in set (0.00 sec)

'''
4.将所有图书按照出版日期排序
'''
# mysql> select * from book order by 出版日期 asc;
# +-----------------+--------+--------------------------------+--------+--------------+
# | 书名        | 作者   | 出版社              | 价格    | 出版日期      |
# +-----------------+--------+--------------------------------+--------+--------------+
# | 九阴真经    | yuan   | 北京工业地雷出版社    |     62 | 2017-07-12   |
# | 独孤九剑    | alex   | 北京工业地雷出版社    |     12 | 2017-09-01   |
# | 九阳神功    | alex   | 人民音乐不好听出版社   |      5 | 2018-07-04   |
# | 倚天屠龙记   | egon   | 北京工业地雷出版社    |     70 | 2019-07-01   |
# | 降龙十巴掌   | egon   | 知识产权没有用出版社  |     20 | 2019-07-05   |
# | 葵花宝典     | yuan   | 知识产权没有用出版社  |     33 | 2019-08-02   |
# | 九阴白骨爪   | jinxin | 人民音乐不好听出版社   |     40 | 2019-08-07   |
# +-----------------+--------+--------------------------------+--------+--------------+
# 7 rows in set (0.00 sec)

'''
5.查询alex写的所有书的平均价格
'''
# mysql> select avg(价格) from book where 作者='alex' group by 作者 ;
# +-------------+
# | avg(价格)    |
# +-------------+
# |      8.5000 |
# +-------------+
# 1 row in set (0.00 sec)

'''
6.查询人民音乐不好听出版社出版的所有图书
'''
# mysql> select * from book where 出版社='人民音乐不好听出版社' group by 出版社;
# +--------------+--------+--------------------------------+--------+--------------+
# | 书名    | 作者    | 出版社            | 价格    | 出版日期       |
# +--------------+--------+--------------------------------+--------+--------------+
# | 九阳神功 | alex   | 人民音乐不好听出版社 |      5 | 2018-07-04   |
# +--------------+--------+--------------------------------+--------+--------------+
# 1 row in set (0.00 sec)

'''
7.查询人民音乐出版社出版的alex写的所有图书和价格
'''
#按人民音乐出不好听版社搜索到0条结果
# mysql> select 书名,价格 from book where 出版社='人民音乐出不好听版社' and 作者='alex';
# Empty set (0.00 sec)
#
# 按人民音乐不好听出版社搜索到1条结果
# mysql> select 书名,价格 from book where 出版社='人民音乐不好听出版社' and 作者='alex';
# +--------------+--------+
# | 书名    | 价格 |
# +--------------+--------+
# | 九阳神功 |   5 |
# +--------------+--------+
# 1 row in set (0.00 sec)

'''
8.找出出版图书均价最高的作者
'''
# mysql> select 作者,avg(价格) from book group by 作者 order by avg(价格) desc limit 1;
# +--------+-------------+
# | 作者    | avg(价格)    |
# +--------+-------------+
# | yuan   |     47.5000 |
# +--------+-------------+
# 1 row in set (0.00 sec)

'''
9.找出最新出版的图书的作者和出版社
'''
# mysql> select 作者,出版社 from book order by 出版日期 desc limit 1;
# +--------+--------------------------------+
# | 作者    | 出版社            |
# +--------+--------------------------------+
# | jinxin | 人民音乐不好听出版社 |
# +--------+--------------------------------+
# 1 row in set (0.00 sec)


'''
10.显示各出版社出版的所有图书
'''
# mysql> select 出版社,group_concat(书名) from book group by 出版社;
# +--------------------------------+-------------------------------------------+
# | 出版社             | group_concat(书名)            |
# +--------------------------------+-------------------------------------------+
# | 人民音乐不好听出版社 | 九阳神功,九阴白骨爪              |
# | 北京工业地雷出版社   | 九阴真经,倚天屠龙记,独孤九剑      |
# | 知识产权没有用出版社 | 葵花宝典,降龙十巴掌              |
# +--------------------------------+-------------------------------------------+
# 3 rows in set (0.00 sec)

'''
11.查找价格最高的图书，并将它的价格修改为50元
'''
# mysql> select max(价格) from book;
# mysql> update book set 价格=50 where 价格=70;

'''
12.删除价格最低的那本书对应的数据
'''
# mysql> select min(价格) from book;
# mysql> delete from book where 价格=5;

'''
13.将所有alex写的书作者修改成alexsb
'''
# mysql> update book set 作者='alexsb' where 作者='alex';

'''
14.select year(publish_date) from book
自己研究上面sql语句中的year函数的功能，完成需求：
将所有2017年出版的图书从数据库中删除
'''
# mysql> delete from book where year(出版日期)=2017;

'''
15.有文件如下，请根据链接自学pymysql模块，使用python写代码将文件中的数据写入数据库
学python从开始到放弃|alex|人民大学出版社|50|2018-7-1
学mysql从开始到放弃|egon|机械工业出版社|60|2018-6-3
学html从开始到放弃|alex|机械工业出版社|20|2018-4-1
学css从开始到放弃|wusir|机械工业出版社|120|2018-5-2
学js从开始到放弃|wusir|机械工业出版社|100|2018-7-30
'''
import pymysql
conn = pymysql.connect(host='127.0.0.1', user='caiqinxiong', password="cai",database='school')
cur = conn.cursor()
sql = "insert into book values (%s,%s,%s,%s,%s)"
with open('book',mode='r',encoding='utf-8') as f:
    for line in f:
        book_name, author, press, price, date = line.strip().split('|')
        try:
            cur.execute(sql,(book_name, author, press, price, date)) # 执行插入数据sql语句，以元组的方式传入参数，字符拼接必须在execute中，防止sql注入。
            conn.commit() # 修改、插入、删除操作的sql语句在内存中，需要提交才能真正写入数据库
        except:
            conn.rollback()# 如果发生错误则回滚
cur.close()
conn.close()

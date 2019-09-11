# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/9/9 10:28

# 创建数据库
# mysql> create database school;

# 查看数据库
# mysql> show databases;

# 切换到school库
# mysql> use school;

# 创建class表
# mysql> create table class (id int,caption char(20));

# 查看表结构
# mysql> desc class;
# +---------+----------+------+-----+---------+-------+
# | Field   | Type     | Null | Key | Default | Extra |
# +---------+----------+------+-----+---------+-------+
# | id      | int(11)  | YES  |     | NULL    |       |
# | caption | char(20) | YES  |     | NULL    |       |
# +---------+----------+------+-----+---------+-------+
# 2 rows in set (0.00 sec)

#在class表中插入3条数据
# mysql> insert into class (id,caption) values (1,'三年级二班'),(2,'一年级三班'),(3,'三年级一班');

# 查看class表中的所有数据
# mysql> select * from class;
# +------+-----------------+
# | id   | caption         |
# +------+-----------------+
# |    1 | 三年级二班        |
# |    2 | 一年级三班        |
# |    3 | 三年级一班        |
# +------+-----------------+
# 3 rows in set (0.00 sec)

# 创建student表
# mysql> create table student (sid int, sname char(20), gender enum('男','女'), class_id int);

# 查看student表结构
# mysql> desc student;
# +----------+-------------------+------+-----+---------+-------+
# | Field    | Type              | Null | Key | Default | Extra |
# +----------+-------------------+------+-----+---------+-------+
# | sid      | int(11)           | YES  |     | NULL    |       |
# | sname    | char(20)          | YES  |     | NULL    |       |
# | gender   | enum('男','女')    | YES  |     | NULL    |       |
# | class_id | int(11)           | YES  |     | NULL    |       |
# +----------+-------------------+------+-----+---------+-------+
# 4 rows in set (0.00 sec)

# 在student表中插入3条数据
# mysql> insert into student values (1,'钢蛋','女',1),(2,'铁锤','女',1),(3,'山炮','男',2);

# 查看student表中所有的数据
# mysql> select * from student;
# +------+--------+--------+----------+
# | sid  | sname  | gender | class_id |
# +------+--------+--------+----------+
# |    1 | 钢蛋    | 女     |    1     |
# |    2 | 铁锤    | 女     |    1     |
# |    3 | 山炮    | 男     |    2     |
# +------+--------+--------+----------+
# 3 rows in set (0.00 sec)

# 创建teacher表
# mysql> create table teacher (tid int, tname char(20));

# 查看teacher表结构
# mysql> desc teacher;
# +-------+----------+------+-----+---------+-------+
# | Field | Type     | Null | Key | Default | Extra |
# +-------+----------+------+-----+---------+-------+
# | tid   | int(11)  | YES  |     | NULL    |       |
# | tname | char(20) | YES  |     | NULL    |       |
# +-------+----------+------+-----+---------+-------+
# 2 rows in set (0.00 sec)

# 在teacher表里插入3条数据
# mysql> insert into teacher values (1,'波多'),(2,'苍空'),(3,'饭岛');

# 查看teacher表里所有数据
# mysql> select * from teacher;
# +------+--------+
# | tid  | tname  |
# +------+--------+
# |    1 | 波多    |
# |    2 | 苍空    |
# |    3 | 饭岛    |
# +------+--------+
# 3 rows in set (0.00 sec)

# 创建course表
# mysql> create table course (cid int, cname char(20), teacher_id int);

# 查看course表结构
# mysql> desc course;
# +------------+----------+------+-----+---------+-------+
# | Field      | Type     | Null | Key | Default | Extra |
# +------------+----------+------+-----+---------+-------+
# | cid        | int(11)  | YES  |     | NULL    |       |
# | cname      | char(20) | YES  |     | NULL    |       |
# | teacher_id | int(11)  | YES  |     | NULL    |       |
# +------------+----------+------+-----+---------+-------+
# 3 rows in set (0.00 sec)

# 在course表中插入3条数据
# mysql> insert into course values (1,'生物',1),(2,'体育',1),(3,'物理',2);

# 查看course表中所有数据
# mysql> select * from course;
# +------+--------+------------+
# | cid  | cname  | teacher_id |
# +------+--------+------------+
# |    1 | 生物    |          1 |
# |    2 | 体育    |          1 |
# |    3 | 物理    |          2 |
# +------+--------+------------+
# 3 rows in set (0.00 sec)

# 创建score表
# mysql> create table score (sid int, student_id int, course_id int, number int);

# 查看score表结构
# mysql> desc score;
# +------------+---------+------+-----+---------+-------+
# | Field      | Type    | Null | Key | Default | Extra |
# +------------+---------+------+-----+---------+-------+
# | sid        | int(11) | YES  |     | NULL    |       |
# | student_id | int(11) | YES  |     | NULL    |       |
# | course_id  | int(11) | YES  |     | NULL    |       |
# | number     | int(11) | YES  |     | NULL    |       |
# +------------+---------+------+-----+---------+-------+
# 4 rows in set (0.00 sec)

# 在score表中插入3条数据
# mysql> insert into score values (1,1,1,60),(2,1,2,59),(3,2,2,100);

# 查看score表中所有数据
# mysql> select * from score;
# +------+------------+-----------+--------+
# | sid  | student_id | course_id | number |
# +------+------------+-----------+--------+
# |    1 |          1 |         1 |     60 |
# |    2 |          1 |         2 |     59 |
# |    3 |          2 |         2 |    100 |
# +------+------------+-----------+--------+
# 3 rows in set (0.00 sec)

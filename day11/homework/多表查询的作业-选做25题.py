# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/9/25 15:22
# 多表查询的作业 : https://www.cnblogs.com/Eva-J/articles/9688383.html
'''
1、查询没有学全所有课的同学的学号、姓名；
'''
# 1、先查询一共有几门课程
# mysql> select count(cid) from course;
# +------------+
# | count(cid) |
# +------------+
# |          4 |
# +------------+
# 1 row in set (0.00 sec)

# 2、在分数表中根据学生进行分组，获取每一个学生选课数量，如果数量等于总课程数量，说明已经选择了所有课程
# mysql> select student_id,sname from score inner join student on score.student_id = student.sid group by student_id having count(course_id)=(select count(cid) from course);
# +------------+--------+
# | student_id | sname  |
# +------------+--------+
# |          3 | 张三 |
# |          4 | 张一 |
# |          5 | 张二 |
# |          6 | 张四 |
# |          7 | 铁锤 |
# |          8 | 李三 |
# |          9 | 李一 |
# |         10 | 李二 |
# |         11 | 李四 |
# |         12 | 如花 |
# +------------+--------+
# 10 rows in set (0.00 sec)

'''
2、查询和“002”号的同学学习的课程完全相同的其他同学学号和姓名；
'''
# 1、先查找2号同学学习了哪些课程
# mysql> select * from score where student_id = 2;
# +-----+------------+-----------+-----+
# | sid | student_id | course_id | num |
# +-----+------------+-----------+-----+
# |   6 |          2 |         1 |   8 |
# |   8 |          2 |         3 |  68 |
# |   9 |          2 |         4 |  99 |
# +-----+------------+-----------+-----+
# 3 rows in set (0.01 sec)
#
# 2、统计2号同学一共学了几门课程
# mysql> select count(course_id) from score where student_id = 2;
# +------------------+
# | count(course_id) |
# +------------------+
# |                3 |
# +------------------+
# 1 row in set (0.00 sec)
#
# 3、找出和2号同学学习课程数量一样的同学id
# mysql> select student_id from score  where student_id != 2 group by student_id having count(course_id)=(select count(course_id) from score where student_id = 2);
# +------------+
# | student_id |
# +------------+
# |          1 |
# +------------+
# 1 row in set (0.00 sec)

# 4、最后找出既课程数量和2号同学一样的并且选课也一样的
# mysql> select student_id,sname from score inner join student on score.student_id = student.sid where student_id in (select student_id from score  where student_id != 2 group by student_id having count(course_id) = (select count(course_id) from score where student_id = 2)) and course_id in (select course_id from score where student_id = 2) group by student_id having count(course_id) =(select count(course_id) from score where student_id = 2);
# Empty set (0.00 sec)

# 没有和2号同学选课一样的，改成3号同学看看效果
# mysql> select student_id,sname from score inner join student on score.student_id = student.sid where student_id in (select student_id from score  where student_id != 3 group by student_id having count(course_id) = (select count(course_id) from score where student_id = 3)) and course_id in (select course_id from score where student_id = 3) group by student_id having count(course_id) =(select count(course_id) from score where student_id = 3);
# +------------+--------+
# | student_id | sname  |
# +------------+--------+
# |          4 | 张一 |
# |          5 | 张二 |
# |          6 | 张四 |
# |          7 | 铁锤 |
# |          8 | 李三 |
# |          9 | 李一 |
# |         10 | 李二 |
# |         11 | 李四 |
# |         12 | 如花 |
# +------------+--------+
# 9 rows in set (0.00 sec)

'''
3、删除学习“李平”老师课的SC表记录；
'''
# 1、查出李平老师的课程id号
# mysql> select * from course inner join teacher on course.teacher_id = teacher.tid where tname = '李平老师';
# +-----+--------+------------+-----+--------------+
# | cid | cname  | teacher_id | tid | tname        |
# +-----+--------+------------+-----+--------------+
# |   2 | 物理 |          2 |   2 | 李平老师 |
# |   4 | 美术 |          2 |   2 | 李平老师 |
# +-----+--------+------------+-----+--------------+
# 2 rows in set (0.00 sec)
#
# 2、在成绩表中删除掉李平老师相关的课程
# mysql> delete from score where course_id in (select cid from course inner join teacher on course.teacher_id = teacher.tid where tname = '李平老师');
# Query OK, 23 rows affected (0.14 sec)

'''
4、向SC表中插入一些记录，这些记录要求符合以下条件：①没有上过编号“002”课程的同学学号；②插入“002”号课程的平均成绩；
'''
# 表插入数据方法一
# insert into 表名(字段名) values (值);
# 方法二
# inset into t1(a,b) select c,d from t2; # t2中选择两个字段的值插入到t1，数据类型必须一致。
# 1、查看score表的字段约束，发现sid是自动增长的，所以，只需要插入student_id, course_id, num三个字段的值就行了,而且course_id=2
# mysql> desc score;
# +------------+---------+------+-----+---------+----------------+
# | Field      | Type    | Null | Key | Default | Extra          |
# +------------+---------+------+-----+---------+----------------+
# | sid        | int(11) | NO   | PRI | NULL    | auto_increment |
# | student_id | int(11) | NO   | MUL | NULL    |                |
# | course_id  | int(11) | NO   | MUL | NULL    |                |
# | num        | int(11) | NO   |     | NULL    |                |
# +------------+---------+------+-----+---------+----------------+
# 4 rows in set (0.00 sec)
#
# 2、获取002的平均成绩
# mysql> select avg(num) from score where course_id = 2;
# +----------+
# | avg(num) |
# +----------+
# |   0.0000 |
# +----------+
# 1 row in set (0.01 sec)

# 3、获取所有没上过002课的所有同学
# mysql> select student_id from score where course_id = 2;
# +------------+
# | student_id |
# +------------+
# |          1 |
# |          2 |
# |          3 |
# |          4 |
# |          5 |
# |          6 |
# |          7 |
# |          8 |
# |          9 |
# |         10 |
# |         11 |
# |         12 |
# |         13 |
# |         14 |
# |         15 |
# |         16 |
# +------------+
# 16 rows in set (0.00 sec)

# 4、将这些满足条件的sql语句进行整合，插入数据到score表。
# mysql> insert into score(student_id, course_id, num) select sid,2,(select avg(num) from score where course_id = 2) from student where sid not in ( select student_id from score where course_id = 2);
# Query OK, 16 rows affected, 16 warnings (0.59 sec)
# Records: 16  Duplicates: 0  Warnings: 16

'''
5、按平均成绩从低到高显示所有学生的“生物”、“物理”、“体育”三门的课程成绩，按如下形式显示： 学生ID,生物,物理,体育,有效课程数,有效平均分；
'''
# 按平均成绩从低到高显示有效课程数,有效平均分
# mysql> select student_id,count(course_id),avg(num) from score group by student_id order by avg(num) asc;
# +------------+------------------+----------+
# | student_id | count(course_id) | avg(num) |
# +------------+------------------+----------+
# |         14 |                1 |   0.0000 |
# |         15 |                1 |   0.0000 |
# |         16 |                1 |   0.0000 |
# |          1 |                2 |   5.0000 |
# |          6 |                3 |  25.3333 |
# |          7 |                3 |  25.3333 |
# |          8 |                3 |  25.3333 |
# |          2 |                3 |  25.3333 |
# |         13 |                2 |  43.5000 |
# |         10 |                3 |  44.3333 |
# |         11 |                3 |  44.3333 |
# |         12 |                3 |  44.3333 |
# |          4 |                3 |  48.6667 |
# |          5 |                3 |  48.6667 |
# |          9 |                3 |  52.6667 |
# |          3 |                3 |  54.6667 |
# +------------+------------------+----------+
# 16 rows in set (0.00 sec)

# 求出生物的成绩
# mysql> select student_id,num from score left join course on course_id = cid where cname = "生物";
# +------------+-----+
# | student_id | num |
# +------------+-----+
# |          1 |  10 |
# |          2 |   8 |
# |          3 |  77 |
# |          4 |  79 |
# |          5 |  79 |
# |          6 |   9 |
# |          7 |   9 |
# |          8 |   9 |
# |          9 |  91 |
# |         10 |  90 |
# |         11 |  90 |
# |         12 |  90 |
# +------------+-----+
# 12 rows in set (0.00 sec)

# 将前面两张表整合
# mysql> select sc.student_id,(select num from score left join course on score.course_id = course.cid where course.cname = "生物" and score.student_id=sc.student_id ) as 生物,count(course_id),avg(sc.num) from score as sc group by student_id order by avg(sc.num) asc;
# +------------+--------+------------------+-------------+
# | student_id | 生物    | count(course_id) | avg(sc.num) |
# +------------+--------+------------------+-------------+
# |         15 |   NULL |                1 |      0.0000 |
# |         16 |   NULL |                1 |      0.0000 |
# |         14 |   NULL |                1 |      0.0000 |
# |          1 |     10 |                2 |      5.0000 |
# |          6 |      9 |                3 |     25.3333 |
# |          7 |      9 |                3 |     25.3333 |
# |          2 |      8 |                3 |     25.3333 |
# |          8 |      9 |                3 |     25.3333 |
# |         13 |   NULL |                2 |     43.5000 |
# |         10 |     90 |                3 |     44.3333 |
# |         11 |     90 |                3 |     44.3333 |
# |         12 |     90 |                3 |     44.3333 |
# |          4 |     79 |                3 |     48.6667 |
# |          5 |     79 |                3 |     48.6667 |
# |          9 |     91 |                3 |     52.6667 |
# |          3 |     77 |                3 |     54.6667 |
# +------------+--------+------------------+-------------+
# 16 rows in set (0.00 sec)
#
# 以此类推，加上物理和体育的成绩进行整合
# mysql> select sc.student_id as 学生ID,(select num from score inner join course on score.course_id = course.cid where course.cname = "生物" and score.student_id=sc.student_id) as 生物,(select num from score inner join course on score.course_id = course.cid where course.cname = "物理" and score.student_id=sc.student_id) as 物理,(select num from score inner join course on score.course_id = course.cid where course.cname = "体育" and score.student_id=sc.student_id) as 体育,count(sc.course_id) as 有效课程数,avg(sc.num) as 有效平均分 from score as sc group by student_id order by avg(sc.num) asc;
# +----------+--------+--------+--------+-----------------+-----------------+
# | 学生ID    | 生物    | 物理   | 体育    | 有效课程数        | 有效平均分        |
# +----------+--------+--------+--------+-----------------+-----------------+
# |       14 |   NULL |      0 |   NULL |               1 |          0.0000 |
# |       15 |   NULL |      0 |   NULL |               1 |          0.0000 |
# |       16 |   NULL |      0 |   NULL |               1 |          0.0000 |
# |        1 |     10 |      0 |   NULL |               2 |          5.0000 |
# |        7 |      9 |      0 |     67 |               3 |         25.3333 |
# |        8 |      9 |      0 |     67 |               3 |         25.3333 |
# |        2 |      8 |      0 |     68 |               3 |         25.3333 |
# |        6 |      9 |      0 |     67 |               3 |         25.3333 |
# |       13 |   NULL |      0 |     87 |               2 |         43.5000 |
# |       11 |     90 |      0 |     43 |               3 |         44.3333 |
# |       12 |     90 |      0 |     43 |               3 |         44.3333 |
# |       10 |     90 |      0 |     43 |               3 |         44.3333 |
# |        4 |     79 |      0 |     67 |               3 |         48.6667 |
# |        5 |     79 |      0 |     67 |               3 |         48.6667 |
# |        9 |     91 |      0 |     67 |               3 |         52.6667 |
# |        3 |     77 |      0 |     87 |               3 |         54.6667 |
# +----------+--------+--------+--------+-----------------+-----------------+
# 16 rows in set (0.00 sec)

'''
6、查询各科成绩最高和最低的分：以如下形式显示：课程ID，最高分，最低分；
'''
# mysql> select course_id as 课程ID, max(num) as 最高分, min(num) as 最低分 from score group by course_id;
# +----------+-----------+-----------+
# | 课程ID    | 最高分     | 最低分     |
# +----------+-----------+-----------+
# |        1 |        91 |         8 |
# |        2 |         0 |         0 |
# |        3 |        87 |        43 |
# +----------+-----------+-----------+
# 3 rows in set (0.00 sec)


'''
7、按各科平均成绩从低到高和及格率的百分数从高到低顺序；
'''
# mysql> select course_id, avg(num) as 平均分,sum(case when score.num > 60 then 1 else 0 end)/count(1)*100 as 及格率 from score group by course_id order by 平均分 asc,及格率 desc;
# +-----------+-----------+-----------+
# | course_id | 平均分     | 及格率     |
# +-----------+-----------+-----------+
# |         2 |    0.0000 |    0.0000 |
# |         1 |   53.4167 |   58.3333 |
# |         3 |   64.4167 |   75.0000 |
# +-----------+-----------+-----------+
# 3 rows in set (0.00 sec)

'''
8、查询各科成绩前三名的记录:(不考虑成绩并列情况)
'''

# mysql> SELECT s1.cid AS 课程ID,s1.cname AS 课程, (SELECT num FROM score AS s2 WHERE s2.course_id=s1.cid GROUP BY num ORDER BY num DESC LIMIT 0,1) AS 第一, (SELECT num FROM score AS s2 WHERE s2.course_id=s1.cid GROUP BY num ORDER BY num DESC LIMIT 1,1) AS 第二,(SELECT num FROM score AS s2 WHERE s2.course_id=s1.cid GROUP BY num ORDER BY num DESC LIMIT 2,1) AS 第三 FROM course AS s1;
# +----------+--------+--------+--------+--------+
# | 课程ID | 课程 | 第一 | 第二 | 第三 |
# +----------+--------+--------+--------+--------+
# |        1 | 生物 |     91 |     90 |     79 |
# |        2 | 物理 |      0 |   NULL |   NULL |
# |        3 | 体育 |     87 |     68 |     67 |
# |        4 | 美术 |   NULL |   NULL |   NULL |
# +----------+--------+--------+--------+--------+
# 4 rows in set (0.00 sec)

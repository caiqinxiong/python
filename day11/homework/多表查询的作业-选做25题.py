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

'''
9、查询每门课程被选修的学生数；
'''
# mysql> select cid,cname,count(student_id) from course left join score on course_id = cid group by course_id;
# +-----+--------+-------------------+
# | cid | cname  | count(student_id) |
# +-----+--------+-------------------+
# |   4 | 美术 |                 0 |
# |   1 | 生物 |                12 |
# |   2 | 物理 |                16 |
# |   3 | 体育 |                12 |
# +-----+--------+-------------------+
# 4 rows in set (0.00 sec)

'''
10、查询同名同姓学生名单，并统计同名人数；
'''
# mysql> select sname,count(sname) from student group by sname;
# +--------+--------------+
# | sname  | count(sname) |
# +--------+--------------+
# | 刘一 |            1 |
# | 刘三 |            1 |
# | 刘二 |            1 |
# | 刘四 |            1 |
# | 如花 |            1 |
# | 张一 |            1 |
# | 张三 |            1 |
# | 张二 |            1 |
# | 张四 |            1 |
# | 李一 |            1 |
# | 李三 |            1 |
# | 李二 |            1 |
# | 李四 |            1 |
# | 理解 |            1 |
# | 钢蛋 |            1 |
# | 铁锤 |            1 |
# +--------+--------------+
# 16 rows in set (0.00 sec)

'''
11、查询每门课程的平均成绩，结果按平均成绩升序排列，平均成绩相同时，按课程号降序排列；
'''
# mysql> select cid,cname,avg(if(isnull(num), 0 ,num)) as 平均分 from course left join score on course_id = cid group by course_id order by avg(num) asc,cid desc;
# +-----+--------+-----------+
# | cid | cname  | 平均分 |
# +-----+--------+-----------+
# |   4 | 美术 |    0.0000 |
# |   2 | 物理 |    0.0000 |
# |   1 | 生物 |   53.4167 |
# |   3 | 体育 |   64.4167 |
# +-----+--------+-----------+
# 4 rows in set (0.00 sec)

'''
12、查询平均成绩大于85的所有学生的学号、姓名和平均成绩；
'''
# 1、先查询所有学生的平均成绩
# mysql> select student_id,sname,avg(num) from student left join score on student_id = student.sid group by student_id;
# +------------+--------+----------+
# | student_id | sname  | avg(num) |
# +------------+--------+----------+
# |          1 | 理解 |   5.0000 |
# |          2 | 钢蛋 |  25.3333 |
# |          3 | 张三 |  54.6667 |
# |          4 | 张一 |  48.6667 |
# |          5 | 张二 |  48.6667 |
# |          6 | 张四 |  25.3333 |
# |          7 | 铁锤 |  25.3333 |
# |          8 | 李三 |  25.3333 |
# |          9 | 李一 |  52.6667 |
# |         10 | 李二 |  44.3333 |
# |         11 | 李四 |  44.3333 |
# |         12 | 如花 |  44.3333 |
# |         13 | 刘三 |  43.5000 |
# |         14 | 刘一 |   0.0000 |
# |         15 | 刘二 |   0.0000 |
# |         16 | 刘四 |   0.0000 |
# +------------+--------+----------+
# 16 rows in set (0.00 sec)

# 2、过滤出平均成绩大于85分的，没有大于85分的同学
# mysql> select student_id,sname,avg(num) from student left join score on student_id = student.sid group by student_id having avg(num)>85;
# Empty set (0.00 sec)

'''
13、查询课程名称为“生物”，且分数低于60的学生姓名和分数
'''
# 方法一
# mysql> select sname,num from student left join score on student_id = student.sid where course_id = ( select cid from course where cname='生物') and num<60;
# +--------+------+
# | sname  | num  |
# +--------+------+
# | 理解 |   10 |
# | 钢蛋 |    8 |
# | 张四 |    9 |
# | 铁锤 |    9 |
# | 李三 |    9 |
# +--------+------+
# 5 rows in set (0.00 sec)

# 方法二（3个左连接并用）
# mysql> SELECT student.sid AS 学号,student.sname AS 姓名,score.num AS 成绩 FROM score LEFT JOIN course ON score.course_id=course.cid LEFT JOIN student ON score.student_id= student.sid  WHERE course.cname="生物" AND score.num<60;
# +--------+--------+--------+
# | 学号 | 姓名 | 成绩 |
# +--------+--------+--------+
# |      1 | 理解 |     10 |
# |      2 | 钢蛋 |      8 |
# |      6 | 张四 |      9 |
# |      7 | 铁锤 |      9 |
# |      8 | 李三 |      9 |
# +--------+--------+--------+
# 5 rows in set (0.00 sec)

'''
14、查询课程编号为003且课程成绩在80分以上的学生的学号和姓名；
'''
# mysql> select student_id,sname from student left join score on student_id = student.sid where course_id=3 and num >80;
# +------------+--------+
# | student_id | sname  |
# +------------+--------+
# |          3 | 张三 |
# |         13 | 刘三 |
# +------------+--------+
# 2 rows in set (0.00 sec)

'''
15、求选了课程的学生人数
'''
# 方法一
# mysql> select count(t1.student_id) as 选课总人数 from (select student_id from score group by student_id) as t1;
# +-----------------+
# | 选课总人数 |
# +-----------------+
# |              16 |
# +-----------------+
# 1 row in set (0.00 sec)
#
# 方法二
# mysql>   select count(distinct student_id) as 选课总人数 from score;
# +-----------------+
# | 选课总人数 |
# +-----------------+
# |              16 |
# +-----------------+
# 1 row in set (0.01 sec)

'''
16、查询选修“张磊老师”所授课程的学生中，成绩最高的学生姓名及其成绩；
'''
# 方法一
# mysql> select sname,num from score left join student on score.student_id = student.sid  where score.course_id in (select course.cid from course left join teacher on course.teacher_id = teacher.tid where tname='张磊老师') order by num desc limit 1;
# +--------+-----+
# | sname  | num |
# +--------+-----+
# | 李一 |  91 |
# +--------+-----+
# 1 row in set (0.00 sec)

# 方法二（3个左连接并用）
# mysql> SELECT student.sid AS 学号,student.sname AS 姓名,num AS 成绩 FROM score  LEFT JOIN course ON score.course_id=course.cid LEFT JOIN student ON score.student_id=student.sid LEFT JOIN teacher ON course.teacher_id=teacher.tid  WHERE teacher.tname = "张磊老师" ORDER BY num DESC LIMIT 1;
# +--------+--------+--------+
# | 学号 | 姓名 | 成绩 |
# +--------+--------+--------+
# |      9 | 李一 |     91 |
# +--------+--------+--------+
# 1 row in set (0.00 sec)

# 方法三（多个子查询套用）
# mysql> select sname,num from student left join score on student_id = student.sid where course_id in (select cid from course where teacher_id = ( select tid from teacher where tname='张磊老师')) order by num desc limit 1;
# +--------+------+
# | sname  | num  |
# +--------+------+
# | 李一 |   91 |
# +--------+------+
# 1 row in set (0.00 sec)

'''
17、查询各个课程及相应的选修人数；
'''
# mysql> select cid,cname,count(student_id) from course left join score on course_id = cid group by course_id;
# +-----+--------+-------------------+
# | cid | cname  | count(student_id) |
# +-----+--------+-------------------+
# |   4 | 美术 |                 0 |
# |   1 | 生物 |                12 |
# |   2 | 物理 |                16 |
# |   3 | 体育 |                12 |
# +-----+--------+-------------------+
# 4 rows in set (0.00 sec)
#

'''
18、查询不同课程但成绩相同的学生的学号、课程号、学生成绩；
'''
# 利用同一张表重命名成两张表，再比较。
# mysql> select distinct s1.course_id,s2.course_id,s1.num from score as s1, score as s2 where s1.num = s2.num and s1.course_id != s2.course_id;
# Empty set (0.00 sec)
# 没有不同课程一样成绩的同学，手动修改某个同学的成绩查看效果
# mysql> update score set num = 8  where sid=8;
# Query OK, 1 row affected (0.07 sec)
# Rows matched: 1  Changed: 1  Warnings: 0
#
# mysql> select distinct s1.course_id,s2.course_id,s1.num from score as s1, score as s2 where s1.num = s2.num and s1.course_id != s2.course_id;
# +-----------+-----------+-----+
# | course_id | course_id | num |
# +-----------+-----------+-----+
# |         3 |         1 |   8 |
# |         1 |         3 |   8 |
# +-----------+-----------+-----+
# 2 rows in set (0.00 sec)

'''
19、查询每门课程成绩最好的前两名；
'''
# mysql> SELECT cid AS 课程ID,cname AS 课程,(SELECT num FROM score AS s2 WHERE s2.course_id=s1.cid GROUP BY num ORDER BY num DESC LIMIT 0,1) AS 第一,(SELECT num FROM score AS s2 WHERE s2.course_id=s1.cid GROUP BY num ORDER BY num DESC LIMIT 1,1) AS 第二  FROM course AS s1;
# +----------+--------+--------+--------+
# | 课程ID | 课程 | 第一 | 第二 |
# +----------+--------+--------+--------+
# |        1 | 生物 |     91 |     90 |
# |        2 | 物理 |      0 |   NULL |
# |        3 | 体育 |     87 |     68 |
# |        4 | 美术 |   NULL |   NULL |
# +----------+--------+--------+--------+
# 4 rows in set (0.00 sec)
#

'''
20、检索至少选修两门课程的学生学号；
'''
# mysql> select student_id from score group by student_id having count(course_id)>=2;
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
# +------------+
# 13 rows in set (0.00 sec)

'''
21、查询全部学生都选修的课程的课程号和课程名；
'''
# mysql> select course_id,cname from course inner join score on course_id = cid group by course_id having count(course_id)=(select count(sid) from student);
# +-----------+--------+
# | course_id | cname  |
# +-----------+--------+
# |         2 | 物理 |
# +-----------+--------+
# 1 row in set (0.00 sec)

'''
22、查询没学过“李平”老师讲授的任一门课程的学生姓名；
'''
# 方法一 （多个子查询套用）
# mysql> select student_id,sname from student left join score on student.sid=student_id where course_id not in (select cid from course where teacher_id = (select tid from teacher where tname='李平老师')) group by student_id;
# +------------+--------+
# | student_id | sname  |
# +------------+--------+
# |          1 | 理解 |
# |          2 | 钢蛋 |
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
# |         13 | 刘三 |
# +------------+--------+
# 13 rows in set (0.00 sec)

# 方法二（利用左连接）
# mysql> select student_id,student.sname from score left join student on score.student_id = student.sid where score.course_id not in (select cid from course left join teacher on course.teacher_id = teacher.tid where tname = '李平老师') group by student_id;
# +------------+--------+
# | student_id | sname  |
# +------------+--------+
# |          1 | 理解 |
# |          2 | 钢蛋 |
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
# |         13 | 刘三 |
# +------------+--------+
# 13 rows in set (0.00 sec)

'''
23、查询两门以上不及格课程的同学的学号及其平均成绩；
'''
# mysql> select student_id,avg(num) from score where student_id in ( select student_id from score where num<60 group by student_id having count(course_id)>=2) group by student_id;
# +------------+----------+
# | student_id | avg(num) |
# +------------+----------+
# |          1 |   5.0000 |
# |          2 |  25.3333 |
# |          6 |  25.3333 |
# |          7 |  25.3333 |
# |          8 |  25.3333 |
# |         10 |  44.3333 |
# |         11 |  44.3333 |
# |         12 |  44.3333 |
# +------------+----------+
# 8 rows in set (0.00 sec)


'''
24、检索“004”课程分数小于60，按分数降序排列的同学学号；
'''
# mysql> select student_id from score where course_id=4 and num<60 order by num desc;
# Empty set (0.00 sec)
# “004”课程没有同学，改成查询1号课程看一下效果
# mysql> select student_id from score where course_id=1 and num<60 order by num desc;
# +------------+
# | student_id |
# +------------+
# |          1 |
# |          6 |
# |          7 |
# |          8 |
# |          2 |
# +------------+
# 5 rows in set (0.00 sec)

'''
25、删除“002”同学的“001”课程的成绩；
'''
# mysql>  delete from score where course_id = 1 and student_id = 2;
# Query OK, 1 row affected (0.08 sec)

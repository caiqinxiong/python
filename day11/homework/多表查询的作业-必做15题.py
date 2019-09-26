# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
# 2019/9/24 14:26
# 多表查询的作业 : https://www.cnblogs.com/Eva-J/articles/9688383.html

'''
1、查询男生、女生的人数；
'''
# mysql> select gender,count(gender) from student group by gender;
# +--------+---------------+
# | gender | count(gender) |
# +--------+---------------+
# | 女     |             6 |
# | 男     |            10 |
# +--------+---------------+
# 2 rows in set (0.00 sec)

'''
2、查询姓“张”的学生名单；
'''
# mysql> select * from student where sname like '张%';
# +-----+--------+----------+--------+
# | sid | gender | class_id | sname  |
# +-----+--------+----------+--------+
# |   3 | 男    |        1 | 张三 |
# |   4 | 男    |        1 | 张一 |
# |   5 | 女    |        1 | 张二 |
# |   6 | 男    |        1 | 张四 |
# +-----+--------+----------+--------+
# 4 rows in set (0.00 sec)


'''
3、课程平均分从高到低显示
'''
# mysql> select course_id,avg(num) from score group by course_id order by avg(num) desc;
# +-----------+----------+
# | course_id | avg(num) |
# +-----------+----------+
# |         4 |  85.2500 |
# |         2 |  65.0909 |
# |         3 |  64.4167 |
# |         1 |  53.4167 |
# +-----------+----------+
# 4 rows in set (0.00 sec)

# mysql> select cname,avg(num) from course,score where course_id = cid group by course_id order by avg(num) desc;
# +--------+----------+
# | cname  | avg(num) |
# +--------+----------+
# | 美术    |  85.2500 |
# | 物理    |  65.0909 |
# | 体育    |  64.4167 |
# | 生物    |  53.4167 |
# +--------+----------+
# 4 rows in set (0.00 sec)

'''
4、查询有课程成绩小于60分的同学的学号、姓名；
'''
# mysql> select student_id,sname from student inner join score on student_id = student.sid where num <60;
# +------------+--------+
# | student_id | sname  |
# +------------+--------+
# |          1 | 理解 |
# |          1 | 理解 |
# |          2 | 钢蛋 |
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
# 12 rows in set (0.00 sec)
#
# mysql> select student_id,sname,num from student inner join score on student_id = student.sid where num <60;
# +------------+--------+-----+
# | student_id | sname  | num |
# +------------+--------+-----+
# |          1 | 理解 |  10 |
# |          1 | 理解 |   9 |
# |          2 | 钢蛋 |   8 |
# |          4 | 张一 |  11 |
# |          5 | 张二 |  11 |
# |          6 | 张四 |   9 |
# |          7 | 铁锤 |   9 |
# |          8 | 李三 |   9 |
# |          9 | 李一 |  22 |
# |         10 | 李二 |  43 |
# |         11 | 李四 |  43 |
# |         12 | 如花 |  43 |
# +------------+--------+-----+
# 12 rows in set (0.01 sec)

'''
5、查询至少有一门课与学号为1的同学所学课程相同的同学的学号和姓名；
'''
# 学号为1的同学所学课程
# mysql> select course_id from score where student_id = 1;
# +-----------+
# | course_id |
# +-----------+
# |         1 |
# |         2 |
# |         4 |
# +-----------+
# 3 rows in set (0.00 sec)

# mysql> select distinct student_id,sname from student inner join score on student.sid = student_id where course_id in (select course_id from score where student_id = 1);
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
# +------------+--------+
# 12 rows in set (0.00 sec)

'''
6、查询出只选修了一门课程的全部学生的学号和姓名；
'''
# mysql> select student_id,sname from student inner join score on student_id = student.sid group by student_id having count(course_id)=1 ;
# +------------+--------+
# | student_id | sname  |
# +------------+--------+
# |         13 | 刘三    |
# +------------+--------+
# 1 row in set (0.00 sec)

'''
7、查询各科成绩最高和最低的分：以如下形式显示：课程ID，最高分，最低分；
'''
# mysql> select course_id as 课程ID, max(num) as 最高分, min(num) as 最低分 from score group by course_id;
# +----------+-----------+-----------+
# | 课程ID    | 最高分     | 最低分     |
# +----------+-----------+-----------+
# |        1 |        91 |         8 |
# |        2 |       100 |         9 |
# |        3 |        87 |        43 |
# |        4 |       100 |        22 |
# +----------+-----------+-----------+
# 4 rows in set (0.00 sec)

'''
8、查询课程编号“2”的成绩比课程编号“1”课程低的所有同学的学号、姓名；
'''
# mysql> select student.sid,sname from student  where ( (select num from score where student_id = student.sid and course_id=2) < (select num from score where student_id = student.sid and course_id=1) );
# +-----+--------+
# | sid | sname  |
# +-----+--------+
# |   1 | 理解 |
# |   3 | 张三 |
# |   4 | 张一 |
# |   5 | 张二 |
# |   9 | 李一 |
# |  10 | 李二 |
# |  11 | 李四 |
# |  12 | 如花 |
# +-----+--------+
# 8 rows in set (0.00 sec)

'''
9、查询“生物”课程比“物理”课程成绩高的所有学生的学号；
'''
# 1、先将课程表的名称和成绩表的课程id对应起来
# select * from score inner join course on course_id = course.cid;
#2、再分别找出“生物”课程和“物理”课程的信息
# mysql> select * from score inner join course on course_id = course.cid where cname='生物';
# +-----+------------+-----------+-----+-----+--------+------------+
# | sid | student_id | course_id | num | cid | cname  | teacher_id |
# +-----+------------+-----------+-----+-----+--------+------------+
# |   1 |          1 |         1 |  10 |   1 | 生物 |          1 |
# |   6 |          2 |         1 |   8 |   1 | 生物 |          1 |
# |  10 |          3 |         1 |  77 |   1 | 生物 |          1 |
# |  14 |          4 |         1 |  79 |   1 | 生物 |          1 |
# |  18 |          5 |         1 |  79 |   1 | 生物 |          1 |
# |  22 |          6 |         1 |   9 |   1 | 生物 |          1 |
# |  26 |          7 |         1 |   9 |   1 | 生物 |          1 |
# |  30 |          8 |         1 |   9 |   1 | 生物 |          1 |
# |  34 |          9 |         1 |  91 |   1 | 生物 |          1 |
# |  38 |         10 |         1 |  90 |   1 | 生物 |          1 |
# |  42 |         11 |         1 |  90 |   1 | 生物 |          1 |
# |  46 |         12 |         1 |  90 |   1 | 生物 |          1 |
# +-----+------------+-----------+-----+-----+--------+------------+

# mysql> select * from score inner join course on course_id = course.cid where cname='物理';
# +-----+------------+-----------+-----+-----+--------+------------+
# | sid | student_id | course_id | num | cid | cname  | teacher_id |
# +-----+------------+-----------+-----+-----+--------+------------+
# |   2 |          1 |         2 |   9 |   2 | 物理 |          2 |
# |  11 |          3 |         2 |  66 |   2 | 物理 |          2 |
# |  15 |          4 |         2 |  11 |   2 | 物理 |          2 |
# |  19 |          5 |         2 |  11 |   2 | 物理 |          2 |
# |  23 |          6 |         2 | 100 |   2 | 物理 |          2 |
# |  27 |          7 |         2 | 100 |   2 | 物理 |          2 |
# |  31 |          8 |         2 | 100 |   2 | 物理 |          2 |
# |  35 |          9 |         2 |  88 |   2 | 物理 |          2 |
# |  39 |         10 |         2 |  77 |   2 | 物理 |          2 |
# |  43 |         11 |         2 |  77 |   2 | 物理 |          2 |
# |  47 |         12 |         2 |  77 |   2 | 物理 |          2 |
# +-----+------------+-----------+-----+-----+--------+------------+
# 11 rows in set (0.00 sec)

# 3、把这两个查询出来的信息当做两张表组合成一张表

# mysql> select * from (select * from score inner join course on course_id = course.cid where cname='生物') as t1 inner join (select * from score inner join course on course_id = course.cid where cname='物理') as t2 on t1.student_id = t2.student_id;
# +-----+------------+-----------+-----+-----+--------+------------+-----+------------+-----------+-----+-----+--------+------------+
# | sid | student_id | course_id | num | cid | cname  | teacher_id | sid | student_id | course_id | num | cid | cname  | teacher_id |
# +-----+------------+-----------+-----+-----+--------+------------+-----+------------+-----------+-----+-----+--------+------------+
# |   1 |          1 |         1 |  10 |   1 | 生物 |          1 |   2 |          1 |         2 |   9 |   2 | 物理 |          2 |
# |  10 |          3 |         1 |  77 |   1 | 生物 |          1 |  11 |          3 |         2 |  66 |   2 | 物理 |          2 |
# |  14 |          4 |         1 |  79 |   1 | 生物 |          1 |  15 |          4 |         2 |  11 |   2 | 物理 |          2 |
# |  18 |          5 |         1 |  79 |   1 | 生物 |          1 |  19 |          5 |         2 |  11 |   2 | 物理 |          2 |
# |  22 |          6 |         1 |   9 |   1 | 生物 |          1 |  23 |          6 |         2 | 100 |   2 | 物理 |          2 |
# |  26 |          7 |         1 |   9 |   1 | 生物 |          1 |  27 |          7 |         2 | 100 |   2 | 物理 |          2 |
# |  30 |          8 |         1 |   9 |   1 | 生物 |          1 |  31 |          8 |         2 | 100 |   2 | 物理 |          2 |
# |  34 |          9 |         1 |  91 |   1 | 生物 |          1 |  35 |          9 |         2 |  88 |   2 | 物理 |          2 |
# |  38 |         10 |         1 |  90 |   1 | 生物 |          1 |  39 |         10 |         2 |  77 |   2 | 物理 |          2 |
# |  42 |         11 |         1 |  90 |   1 | 生物 |          1 |  43 |         11 |         2 |  77 |   2 | 物理 |          2 |
# |  46 |         12 |         1 |  90 |   1 | 生物 |          1 |  47 |         12 |         2 |  77 |   2 | 物理 |          2 |
# +-----+------------+-----------+-----+-----+--------+------------+-----+------------+-----------+-----+-----+--------+------------+
# 11 rows in set (0.00 sec)

# 4、再比较查询“生物”课程比“物理”课程成绩高的所有学生的学号
# mysql> select t1.student_id,t1.num as 生物,t2.num as 物理 from (select * from score inner join course on course_id = course.cid where cname='生物') as t1 inner join (select * from score inner join course on course_id = course.cid where cname='物理') as t2 on t1.student_id = t2.student_id where t1.num > t2.num;
# +------------+--------+--------+
# | student_id | 生物    | 物理    |
# +------------+--------+--------+
# |          1 |     10 |      9 |
# |          3 |     77 |     66 |
# |          4 |     79 |     11 |
# |          5 |     79 |     11 |
# |          9 |     91 |     88 |
# |         10 |     90 |     77 |
# |         11 |     90 |     77 |
# |         12 |     90 |     77 |
# +------------+--------+--------+
# 8 rows in set (0.00 sec)

'''
10、查询平均成绩大于60分的同学的学号和平均成绩;
'''
# mysql> select student_id,avg(num) from score group by student_id having avg(num)>60;
# +------------+----------+
# | student_id | avg(num) |
# +------------+----------+
# |          3 |  82.2500 |
# |          4 |  64.2500 |
# |          5 |  64.2500 |
# |          6 |  69.0000 |
# |          7 |  66.0000 |
# |          8 |  66.0000 |
# |          9 |  67.0000 |
# |         10 |  74.2500 |
# |         11 |  74.2500 |
# |         12 |  74.2500 |
# |         13 |  87.0000 |
# +------------+----------+
# 11 rows in set (0.01 sec)

'''
11、查询所有同学的学号、姓名、选课数、总成绩；
'''
# mysql> select student_id,sname,count(course_id),sum(num) from student inner join score on student.sid = student_id group by student_id;
# +------------+--------+------------------+----------+
# | student_id | sname  | count(course_id) | sum(num) |
# +------------+--------+------------------+----------+
# |          1 | 理解 |                3 |       85 |
# |          2 | 钢蛋 |                3 |      175 |
# |          3 | 张三 |                4 |      329 |
# |          4 | 张一 |                4 |      257 |
# |          5 | 张二 |                4 |      257 |
# |          6 | 张四 |                4 |      276 |
# |          7 | 铁锤 |                4 |      264 |
# |          8 | 李三 |                4 |      264 |
# |          9 | 李一 |                4 |      268 |
# |         10 | 李二 |                4 |      297 |
# |         11 | 李四 |                4 |      297 |
# |         12 | 如花 |                4 |      297 |
# |         13 | 刘三 |                1 |       87 |
# +------------+--------+------------------+----------+
# 13 rows in set (0.00 sec)

'''
12、查询姓“李”的老师的个数；
'''
# mysql>  select count(tname) from teacher where tname like '李%';
# +--------------+
# | count(tname) |
# +--------------+
# |            2 |
# +--------------+
# 1 row in set (0.00 sec)

'''
13、查询没学过“张磊老师”课的同学的学号、姓名；
'''
# 方法一
# 1、先找到张磊老师所教课程
# mysql> select * from course inner join teacher on teacher_id=tid where tname='张磊老师';
# +-----+--------+------------+-----+--------------+
# | cid | cname  | teacher_id | tid | tname        |
# +-----+--------+------------+-----+--------------+
# |   1 | 生物 |          1 |   1 | 张磊老师 |
# +-----+--------+------------+-----+--------------+
# 1 row in set (0.00 sec)

# 2、找出选了张磊老师课程的学生
# mysql> select * from score where course_id = (select cid from course inner join teacher on teacher_id=tid where tname='张磊老师');
# +-----+------------+-----------+-----+
# | sid | student_id | course_id | num |
# +-----+------------+-----------+-----+
# |   1 |          1 |         1 |  10 |
# |   6 |          2 |         1 |   8 |
# |  10 |          3 |         1 |  77 |
# |  14 |          4 |         1 |  79 |
# |  18 |          5 |         1 |  79 |
# |  22 |          6 |         1 |   9 |
# |  26 |          7 |         1 |   9 |
# |  30 |          8 |         1 |   9 |
# |  34 |          9 |         1 |  91 |
# |  38 |         10 |         1 |  90 |
# |  42 |         11 |         1 |  90 |
# |  46 |         12 |         1 |  90 |
# +-----+------------+-----------+-----+
# 12 rows in set (0.00 sec)

# 3、最后反选一下所有学生中不包含选了张磊老师的课的学生就行
# mysql> select sid,sname from student where sid not in (select student_id from score where course_id = (select cid from course inner join teacher on teacher_id=tid where tname='张磊老师'));
# +-----+--------+
# | sid | sname  |
# +-----+--------+
# |  13 | 刘三 |
# |  14 | 刘一 |
# |  15 | 刘二 |
# |  16 | 刘四 |
# +-----+--------+
# 4 rows in set (0.00 sec)

# 方法二，直接用多个子查询套用
# mysql> select sid,sname from student where sid not in (select student_id from score where course_id = (select cid from course where teacher_id = (select tid from teacher where tname = '张磊老师')));
# +-----+--------+
# | sid | sname  |
# +-----+--------+
# |  13 | 刘三 |
# |  14 | 刘一 |
# |  15 | 刘二 |
# |  16 | 刘四 |
# +-----+--------+
# 4 rows in set (0.00 sec)

'''
14、查询学过“1”并且也学过编号“2”课程的同学的学号、姓名；
'''
# 方法一
# 1、先找出学过课程1的同学
# mysql> select * from student inner join score on student_id = student.sid where course_id=1 ;
# +-----+--------+----------+--------+-----+------------+-----------+-----+
# | sid | gender | class_id | sname  | sid | student_id | course_id | num |
# +-----+--------+----------+--------+-----+------------+-----------+-----+
# |   1 | 男    |        1 | 理解 |   1 |          1 |         1 |  10 |
# |   2 | 女    |        1 | 钢蛋 |   6 |          2 |         1 |   8 |
# |   3 | 男    |        1 | 张三 |  10 |          3 |         1 |  77 |
# |   4 | 男    |        1 | 张一 |  14 |          4 |         1 |  79 |
# |   5 | 女    |        1 | 张二 |  18 |          5 |         1 |  79 |
# |   6 | 男    |        1 | 张四 |  22 |          6 |         1 |   9 |
# |   7 | 女    |        2 | 铁锤 |  26 |          7 |         1 |   9 |
# |   8 | 男    |        2 | 李三 |  30 |          8 |         1 |   9 |
# |   9 | 男    |        2 | 李一 |  34 |          9 |         1 |  91 |
# |  10 | 女    |        2 | 李二 |  38 |         10 |         1 |  90 |
# |  11 | 男    |        2 | 李四 |  42 |         11 |         1 |  90 |
# |  12 | 女    |        3 | 如花 |  46 |         12 |         1 |  90 |
# +-----+--------+----------+--------+-----+------------+-----------+-----+
# 2、再找出学过课程2的同学
# mysql> select * from student inner join score on student_id = student.sid where course_id=2;
# +-----+--------+----------+--------+-----+------------+-----------+-----+
# | sid | gender | class_id | sname  | sid | student_id | course_id | num |
# +-----+--------+----------+--------+-----+------------+-----------+-----+
# |   1 | 男    |        1 | 理解 |   2 |          1 |         2 |   9 |
# |   3 | 男    |        1 | 张三 |  11 |          3 |         2 |  66 |
# |   4 | 男    |        1 | 张一 |  15 |          4 |         2 |  11 |
# |   5 | 女    |        1 | 张二 |  19 |          5 |         2 |  11 |
# |   6 | 男    |        1 | 张四 |  23 |          6 |         2 | 100 |
# |   7 | 女    |        2 | 铁锤 |  27 |          7 |         2 | 100 |
# |   8 | 男    |        2 | 李三 |  31 |          8 |         2 | 100 |
# |   9 | 男    |        2 | 李一 |  35 |          9 |         2 |  88 |
# |  10 | 女    |        2 | 李二 |  39 |         10 |         2 |  77 |
# |  11 | 男    |        2 | 李四 |  43 |         11 |         2 |  77 |
# |  12 | 女    |        3 | 如花 |  47 |         12 |         2 |  77 |
# +-----+--------+----------+--------+-----+------------+-----------+-----+
# 11 rows in set (0.00 sec)
#
# 3、把前面找出来的信息再组合成新的一张表，就可以找出既选择1课程又选择2课程学生了
# mysql> select t1.student_id,t1.sname from (select student_id,sname,course_id from student inner join score on student_id = student.sid where course_id=1) as t1 inner join ( select student_id,sname,course_id from student inner join score on student_id = student.sid where course_id=2) as t2 on t1.student_id = t2.student_id;
# +------------+--------+
# | student_id | sname  |
# +------------+--------+
# |          1 | 理解 |
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
# 11 rows in set (0.00 sec)

# 方法二
# mysql> select sid,sname from student where sid in (select t1.student_id from (select student_id from score where course_id = 1)  t1 inner join (select student_id from score where course_id = 2) t2 on t1.student_id = t2.student_id);
# +-----+--------+
# | sid | sname  |
# +-----+--------+
# |   1 | 理解 |
# |   3 | 张三 |
# |   4 | 张一 |
# |   5 | 张二 |
# |   6 | 张四 |
# |   7 | 铁锤 |
# |   8 | 李三 |
# |   9 | 李一 |
# |  10 | 李二 |
# |  11 | 李四 |
# |  12 | 如花 |
# +-----+--------+
# 11 rows in set (0.00 sec)

'''
15、查询学过“李平老师”所教的所有课的同学的学号、姓名；
'''
# 方法一
# 1、先找到'李平老师'对应的tid号
# mysql> select * from teacher where tname='李平老师';
# +-----+--------------+
# | tid | tname        |
# +-----+--------------+
# |   2 | 李平老师 |
# +-----+--------------+
# 1 row in set (0.00 sec)
#
# 2、通过tid号找到'李平老师'所教的课程对应的cid号
# mysql> select * from course where teacher_id = (select tid from teacher where tname='李平老师');
# +-----+--------+------------+
# | cid | cname  | teacher_id |
# +-----+--------+------------+
# |   2 | 物理 |          2 |
# |   4 | 美术 |          2 |
# +-----+--------+------------+
# 2 rows in set (0.00 sec)
#
# 3、统计'李平老师'一共教了几门课程
# mysql>  select count(cid) from course where teacher_id in (select tid from teacher where tname ='李平老师');
# +------------+
# | count(cid) |
# +------------+
# |          2 |
# +------------+
# 1 row in set (0.00 sec)

# 3、将选择了'李平老师'所教的两门课程的学生查询出来。
# mysql> select  student_id,sname from student inner join score on student_id = student.sid where course_id in (select cid from course where teacher_id = (select tid from teacher where tname='李平老师')) group by sname having count(sname)=(select count(cid) from course where teacher_id in (select tid from teacher where tname ='李平老师'));
# +------------+--------+
# | student_id | sname  |
# +------------+--------+
# |         12 | 如花 |
# |          4 | 张一 |
# |          3 | 张三 |
# |          5 | 张二 |
# |          6 | 张四 |
# |          9 | 李一 |
# |          8 | 李三 |
# |         10 | 李二 |
# |         11 | 李四 |
# |          1 | 理解 |
# |          7 | 铁锤 |
# +------------+--------+
# 11 rows in set (0.01 sec)

# 方法二
# mysql> select sid,sname from student where sid in (  select  student_id from (  select student_id,count(course_id) course_count from score where course_id in ( select cid from course where teacher_id in (select tid from teacher where tname ='李平老师')) group by student_id) t1  where t1.course_count =  (select count(cid) from course where teacher_id in (select tid from teacher where tname ='李平老师'))  );
# +-----+--------+
# | sid | sname  |
# +-----+--------+
# |   1 | 理解 |
# |   3 | 张三 |
# |   4 | 张一 |
# |   5 | 张二 |
# |   6 | 张四 |
# |   7 | 铁锤 |
# |   8 | 李三 |
# |   9 | 李一 |
# |  10 | 李二 |
# |  11 | 李四 |
# |  12 | 如花 |
# +-----+--------+
# 11 rows in set (0.00 sec)


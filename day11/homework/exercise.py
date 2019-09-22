# -*- coding:utf-8 -*-
# caiqinxiong 
# 2019/9/22 上午9:19
# 创建class表
# create table class (cid int primary key auto_increment, caption char(20) not null);
# mysql> desc class;
# +---------+----------+------+-----+---------+----------------+
# | Field   | Type     | Null | Key | Default | Extra          |
# +---------+----------+------+-----+---------+----------------+
# | cid     | int(11)  | NO   | PRI | NULL    | auto_increment |
# | caption | char(20) | NO   |     | NULL    |                |
# +---------+----------+------+-----+---------+----------------+
# 2 rows in set (0.00 sec)

# insert into class (caption) values ('三年二班'),('一年三班'),('三年一班');
# mysql> select * from class;
# +-----+--------------+
# | cid | caption      |
# +-----+--------------+
# |   1 | 三年二班     |
# |   2 | 一年三班     |
# |   3 | 三年一班     |
# +-----+--------------+
# 3 rows in set (0.00 sec)

#  create table student ( sid int primary key auto_increment, sname char(20) not null, gender enum('male','female') default 'male', class_id int, foreign key(class_id) references class(cid) on update cascade on delete cascade);
# mysql> desc student;
# +----------+-----------------------+------+-----+---------+----------------+
# | Field    | Type                  | Null | Key | Default | Extra          |
# +----------+-----------------------+------+-----+---------+----------------+
# | sid      | int(11)               | NO   | PRI | NULL    | auto_increment |
# | sname    | char(20)              | NO   |     | NULL    |                |
# | gender   | enum('male','female') | YES  |     | male    |                |
# | class_id | int(11)               | YES  | MUL | NULL    |                |
# +----------+-----------------------+------+-----+---------+----------------+
# 4 rows in set (0.01 sec)

# mysql> show create table student \G;
# *************************** 1. row ***************************
#        Table: student
# Create Table: CREATE TABLE `student` (
#   `sid` int(11) NOT NULL AUTO_INCREMENT,
#   `sname` char(20) NOT NULL,
#   `gender` enum('male','female') DEFAULT 'male',
#   `class_id` int(11) DEFAULT NULL,
#   PRIMARY KEY (`sid`),
#   KEY `class_id` (`class_id`),
#   CONSTRAINT `student_ibfk_1` FOREIGN KEY (`class_id`) REFERENCES `class` (`cid`) ON DELETE CASCADE ON UPDATE CASCADE
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8
# 1 row in set (0.01 sec)






# create table employee(
# id int not null unique auto_increment,
# emp_name varchar(20) not null,
# sex enum('male','female') not null default 'male', #大部分是男的
# age int(3) unsigned not null default 28,
# hire_date date not null,
# post varchar(50),
# post_comment varchar(100),
# salary double(15,2),
# office int, #一个部门一个屋子
# depart_id int
# );
#
# insert into employee(emp_name,sex,age,hire_date,post,salary,office,depart_id) values
# ('egon','male',18,'20170301','老男孩驻沙河办事处外交大使',7300.33,401,1), #以下是教学部
# ('alex','male',78,'20150302','teacher',1000000.31,401,1),
# ('wupeiqi','male',81,'20130305','teacher',8300,401,1),
# ('yuanhao','male',73,'20140701','teacher',3500,401,1),
# ('liwenzhou','male',28,'20121101','teacher',2100,401,1),
# ('jingliyang','female',18,'20110211','teacher',9000,401,1),
# ('jinxin','male',18,'19000301','teacher',30000,401,1),
# ('成龙','male',48,'20101111','teacher',10000,401,1),
#
# ('歪歪','female',48,'20150311','sale',3000.13,402,2),#以下是销售部门
# ('丫丫','female',38,'20101101','sale',2000.35,402,2),
# ('丁丁','female',18,'20110312','sale',1000.37,402,2),
# ('星星','female',18,'20160513','sale',3000.29,402,2),
# ('格格','female',28,'20170127','sale',4000.33,402,2),
#
# ('张野','male',28,'20160311','operation',10000.13,403,3), #以下是运营部门
# ('程咬金','male',18,'19970312','operation',20000,403,3),
# ('程咬银','female',18,'20130311','operation',19000,403,3),
# ('程咬铜','male',18,'20150411','operation',18000,403,3),
# ('程咬铁','female',18,'20140512','operation',17000,403,3)
# ;

# select concat('<名字:',emp_name,'>') as name ,concat('<薪资:',salary,'>') as salary from employee;
# select distinct post from employee;
# select emp_name,salary*12 as annual_year from employee;

# select emp_name,age from employee where post = 'teacher';
# select emp_name,age from employee where post = 'teacher' and age > 30;
# select emp_name,age,salary from employee where post = 'teacher' and salary between 9000 and 10000;
# select emp_name,age,salary from employee where post = 'teacher' and salary in (9000,10000,30000);
# select emp_name,age,salary from employee where post = 'teacher' and salary not in (9000,10000,30000);
# select emp_name,salary*12 from employee where post = 'teacher' and emp_name like 'jin%';

# select post,count(emp_name) from employee group by post;
# select sex,count(emp_name) from employee group by sex;
# select post,avg(salary) from employee group by post;
# select post,max(salary) from employee group by post;
# select post,min(salary) from employee group by post;
# select sex,avg(salary) from employee group by sex;

# select emp_name,age,hire_date from employee order by age asc ,hire_date desc;
# select post,avg(salary) from employee group by post having avg(salary)>1000 order by avg(salary) asc;
# select post,avg(salary) from employee group by post having avg(salary)>1000 order by avg(salary) desc;

# create table department(
# id int,
# name varchar(20)
# );
#
# create table emp(
# id int primary key auto_increment,
# name varchar(20),
# sex enum('male','female') not null default 'male',
# age int,
# dep_id int
# );
#
# #插入数据
# insert into department values
# (200,'技术'),
# (201,'人力资源'),
# (202,'销售'),
# (203,'运营');
#
# insert into emp(name,sex,age,dep_id) values
# ('egon','male',18,200),
# ('alex','female',48,201),
# ('wupeiqi','male',38,201),
# ('yuanhao','female',28,202),
# ('liwenzhou','male',18,200),
# ('jingliyang','female',18,204)
# ;


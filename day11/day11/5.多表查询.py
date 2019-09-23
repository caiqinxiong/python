# 什么叫连表
# create table t1(a int,b int);
# insert into t1 values(1,2),(3,4),(5,6);
# create table t2(c int,d int,e int);
# insert into t2 values(1,1,1),(2,2,2),(3,3,3);

'''
# 数据准备
create table department(
id int,
name varchar(20)
) charset = utf8;

create table emp(
id int primary key auto_increment,
name varchar(20),
sex enum('male','female') not null default 'male',
age int,
dep_id int
) charset = utf8;

#插入数据
insert into department values
(200,'技术'),
(201,'人力资源'),
(202,'销售'),
(203,'运营');

insert into emp(name,sex,age,dep_id) values
('egon','male',18,200),
('alex','female',48,201),
('wupeiqi','male',38,201),
('yuanhao','female',28,202),
('liwenzhou','male',18,200),
('jingliyang','female',18,204)
;
'''

# 连表查询 = 内连接
# select * from 表1,表2 where 连接条件
# select * from emp,department where dep_id = department.id;
# select * from emp,department as dep where dep_id = dep.id;

# select * from 表1 inner join 表2 on 条件
# 内连接 inner join 保留两表中所有匹配条件的数据
# select * from emp inner join department on dep_id = department.id;
# 外连接
    # 左外连接 left join  保留左表中所有数据
    # select * from emp left join department on dep_id = department.id;
    # 右外连接 right join 保留右表中所有数据
    # select * from emp right join department on dep_id = department.id;
    # 全外连接 保留左表右表中所有数据
    # select * from emp left join department on dep_id = department.id
    # union
    # select * from emp right join department on dep_id = department.id;

# 1.基于两张表找到每个人的名字和所属的部门,左外连接
# select emp.name from emp left join department on dep_id = department.id;
# select emp.name,department.name from emp left join department on dep_id = department.id;
# select emp.name,dep.name from emp left join department as dep on dep_id = dep.id;

# 2.找到"技术"部的所有人
# 方法一:
# select * from emp inner join department on dep_id = department.id where department.name='技术';
# 方法二:
# select * from emp,department where dep_id = department.id and department.name='技术';

# 3.以内连接的方式查询employee和department表，
# 并且employee表中的age字段值必须大于25,即找出年龄大于25岁的员工以及员工所在的部门
# select * from emp inner join department on dep_id = department.id
# select emp.name,department.name from emp inner join department on dep_id = department.id where age>25;

# 4.以内连接的方式查询employee和department表，并且以age字段的升序方式显示
# select emp.name,department.name from emp inner join department on dep_id = department.id

# 子查询
# 1.查询平均年龄在25岁以上的部门名
    # 找到了平均年龄在25岁以上的部门id
        # select dep_id from emp group by dep_id having avg(age)>25;
    # 根据部门id找到部门名
        # select * from department where id in (201,202);
   #  select * from department where id in (select dep_id from emp group by dep_id having avg(age)>25);

# 查看技术部员工姓名
    # select id from department where name = '技术';
    # select * from emp where dep_id = 200;
    # select * from emp where dep_id = (select id from department where name = '技术');

# 当连表和子查询都可以出结果的时候,连表的效率高

# F:\python自动化27期\day11\day27.sql
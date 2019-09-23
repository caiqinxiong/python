# mysql数据库
# 存储引擎
    # innodb 默认的存储方式(存储引擎)
        # 支持事务 外键 行级锁 表级锁
        # 存储为两个文件:一个用来存表结构 一个用来存数据
    # myisam
        # 支持表级锁
# 基础的数据类型
    # int tinyint float(m,n)
    # char(n) varchar(n)
    # datetime date time
    # enum('选项1','选项2') set('选项'...)
# 约束
# create table student6(id int unique auto_increment,name char(12) not null unique,phone char(11) unique,gender enum('male','female') default 'male');
# create table student7(name char(12) not null unique,id int unique auto_increment,phone char(11) unique,gender enum('male','female') default 'male');
# id name phone gender
    # 非空 not null
    # 默认 default
    # 唯一 unique
    # 自增 auto_increment = unique + not null + 自增效果
        # 1.依赖于唯一约束的
        # 2.自带一个not null约束
    # 主键 primary key = 第一个(非空 + 唯一)=这张表的主键
        # pri == primary key 主键
        # 每张表只能有一个主键
        # create table student8(name char(12) not null unique,id int primary key auto_increment,phone char(11) unique,gender enum('male','female') default 'male')
    # 联合唯一(常用)\联合主键(不常用)
        # create table server_info2(id int primary key auto_increment, name char(20), ip char(15) not null,port int(5) not null,unique(ip,port));
        # create table server_info2(id int unique auto_increment, name char(20), ip char(15),port int(5),primary key(ip,port));
    # 外键 foreign key
        # create table stu2(id int,name char(12),class_id int,foreign key(class_id) references class2(cid));
        # create table class2(cid int primary key,classname char(12));

        # 级联更新
        # create table stu3(id int,name char(12),class_id int,foreign key(class_id) references class3(cid) on update cascade);
        # create table class3(cid int primary key,classname char(12));

# 表的删除 drop table 表名;
# 表的修改 alter table
    # 增加字段 删除字段 修改字段名 修改约束 修改数据类型 修改长度 修改表名
# 表的查看
    # desc 表名;
    # show create table 表名;

# 数据操作
# 增 insert
    # insert into 表名 values(值,值2,值3),(值,值2,值3),...,.;
    # insert into 表名(指定字段名1,指定字段2) values(值1,值2),...,.;
    # insert into 表名 select 语句;   # 把查出来的数据都添加到对应的表名中
        # 表1 : id name age      select * from 表1
        # 表二 : id name gender
            # insert into 表2(id,name) select id,name from 表1;
# 删 delete
    # delete from 表名 where 条件   # 删除所有符合条件的行
# 改 update
    # update 表名 set 字段名=值,字段2=值2 where 条件;

# 查 select
    # 单表查询
    # 多表查询

# 增删改
# 查询
    # 单表查询
    # 多表查询
# 其他知识点 :
    # 数据库的备份 mysqldump
        # 恢复数据 mysql> source xxx.sql
    # 事务
'''
mysql> begin;
Query OK, 0 rows affected (0.00 sec)

mysql> select a from t1 where b = 2 for update;
+------+
| a    |
+------+
|    1 |
+------+
1 row in set (0.00 sec)

mysql> update t1 set a=2 where b = 2;
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> commit;
Query OK, 0 rows affected (0.03 sec)
'''
# pymysql模块
    #
    
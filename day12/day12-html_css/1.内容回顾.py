# 课程安排
# 13\20\27 前端的内容
# 13 html + css
# 20 js bom dom
# 27 jq bootstrap

# 数据库
# 什么是关系型数据库 非关系型数据库(no-sql)
# mysql oracle       redis mongodb

# 数据库的操作
    # 创建库 create database 库的名字
    # 切换到库下 use 库名
    # 修改库的编码 alter database charset=utf8
    # 查看当前有哪些库 show databases
# 数据表的操作
    # 存储引擎 : Innodb Myisam
    # 创建表 create table
        # 基本数据类型 数字(int,float,tinyint) 字符串(char,varchar)
            # 时间(datetime date time) set和enum
        # 约束条件 非空not null,默认default,唯一unique,auto_increment自增
                #  主键primary key,外键 foreign key
    # 删除表 drop table
    # 查看表 desc 表名 / show create table 表名
    # 修改表 alter table
# 数据的操作
    # 增 insert into 表名(字段1,字段2) values(值1,值2),(第二行的数据1,line2data2)
    # 删 delete from 表 where 条件
    # 改 update 表名 set 字段1=新的值,字段2=新的值 where 条件
    # 查
        # 单表查询 : select distinct 字段 from 表 where 条件 group by 字段 having 过滤条件 order by 排序 limit n;
        # 多表查询 :
            # 连表
                # where / select * from 表1 inner join 表2 on 表1.字段 = 表2.字段
                # left join
                # right join
            # 子查询
                # select * from 表 where 字段 = (select ...)
    # 聚合函数 : count sum avg max min
# 数据库的备份\还原
    # mysqldump -u用户名 -p密码 数据库名 > 地址/xxx.sql
    # 进数据库,source 地址/xxx.sql
# python操作数据库
    # pymysql
    # 先建立链接
    # 获取游标
    # 执行sql
    # 获取结果
    # 关闭游标和链接
# 事务\锁\索引
    # begin;
    # select * from 表 where id <5 for update;
    # update 表 set age= age+1 where id <5;
    # commit;

    # 索引 : 会加速查询 会拖慢写的速度 索引不要建立不合适的索引
    # 创建索引 : create index 索引名 on 表名(字段名)  给字段创建一个叫做(索引名)的索引
    # 删除索引 : drop index 索引名 on 表名
    # 主键 和 唯一 是自带索引的
    # 我们自己创建索引 :除了主键 和 唯一约束之外的,区分度比较大的,经常被作为条件查询的
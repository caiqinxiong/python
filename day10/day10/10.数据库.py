# 安装数据库 server端

# 启动数据库
    # server端
    # net start mysql 启动服务端
    # net stop mysql  关闭服务端

# mysql客户端
    # 执行mysql.exe可以启动客户端,连接上server端

# mysql> select user();  # 查看当前登录的用户是谁
    # ;是sql语句的结束符,写任何代码之后都应该自己添加;表示一句指令的结束
# mysql> exit 表示退出客户端

# cmd命令行直接输入 mysql -u用户名 -p密码
# mysql -uroot -p123  表示以root用户登录 密码是123
# 设置密码 set password = password('新密码')

# mysql(开源 互联网公司) oracle(金融公司 事业单位) sqlserver db2 postgresql sqllite
# mongodb redis memcache hbase
# 名词
    # DBMS数据库管理系统
    # DBA数据库管理员
    # 什么是库 DB
    # 什么是表 table
    # 什么是数据 data

# 数据库的操作
    # 创建库 : create database; 数据库的名字
        # 相当于创建了一个文件夹
    # 查看库 : show databases;
    # 使用库 : use py27
        # 切换到对应的文件夹下
    # 查看当前库有哪些表 : show tables;
    # 删除库 : drop database py27;

# 数据表的操作
    # 创建表
        # 语法 create table 表名(字段名 类型(长度) 约束,字段名 类型(长度) 约束...);
        # create table score(id int(8),name char(20),num int(4)) charset=utf8;
    # 修改表
    # 查看表结构 :
                # desc score;                更直观
                # show create table score;   更全面: 查看表的编码 存储引擎
                # mysql5.6以上版本 默认innodb
                    # 支持事务
                    # 行级锁 表锁 数据修改频繁
                    # 外键约束
    # 删除表 : drop table 表名;
# 数据的操作
    # 增
        # insert into 表名(字段名) values (值);
        # insert into score(id,name,num) values (1,'alex',0);
        # insert into score values (2,'wusir',60);
        # insert into score values (2,'wusir',60),(2,'wusir',60),(2,'wusir',60);
        # insert into score(name,num) values ('松松',100);
        # insert into score(name,num) values ('松松',100),('立立',99);
    # 删
        # delete from 表名 where 条件;
        # delete from score where id = 2;
    # 改
        # update 表 set 字段名='新的值' where 条件
        # update score set id=4 where name = '松松'
    # 查
        # select * from 表

# 类型 和 约束
# 类型
    # 数字 :
        # 整型 :长度的约束都是无效的,它能够表示的大小只和它存储的字节数相关
            # 年龄 : tinyint 1bytes 不算符号最多可以存到255 算上符号127
            #  smallint 2bytes
            #  mediumint 3bytes
            # int 4bytes 2**32  整数
            # bigint 8字节 2**64
                # create table t1(age1 tinyint(2),age2 tinyint,age3 tinyint unsigned);
                # create table t1(age int unsigned);
        # 浮点型
            # float(m,n) 单精度
                # m 表示一共有多少位
                # n 表示小数部分占其中的多少
                # float(5,2)
                # create table t2(salary float(5,2))
            # double(m,n) 双精度  能够表示的小数点之后的位数更精准
            # 薪资
    # 字符串 :
        # char(255) : 用户名\密码\手机号\身份证号
            # char(20)定长存储
                # 存储 'alex                ' 浪费空间
                # 操作节省时间
        # varchar(65535) : 评论 微博 微信朋友圈 论坛
            # varchar(255)变长存储
                # 存储 'alex4'  节省空间
                # 更加浪费时间
        # create table t4(username char(20),password char(32))
    # 时间 :
        # datetime 年月日时分秒
            # 登陆时间
            # 修改时间
            # 出生日期
            # 跑步计时
        # date 年月日
            # 注册时间
        # time 时分秒
        # timestamp 时间戳4字节 1970-2038-xx-xx
        # year 年
        # create table t5(dt datetime,d date,t time,ts timestamp,y year);
        # create table t6(dt datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,d date,t time,ts timestamp,y year);
    # 单选和多选 : 性别 爱好
        # enum单选和set多选并去重
        # create table t7(gender enum('男','女'),hobby set('抽烟','喝酒','烫头','洗脚'));
        # insert into t7 values('男','抽烟')


# 约束
# 数据的查询
    # 单表查询
    # 连表查询
# html











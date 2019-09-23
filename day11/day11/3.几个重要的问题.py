# mysql -u用户名 -p密码 -h主机地址
# mysql> 在这里你什么位置都没有,既不在任何一个数据库中,也不能直接操作某个库的表
# mysql> use 数据库名; # 先要选择你要去的数据库(前提是有这样一个库,如果没有需要先创建)
# mysql> 才能开始创建表或者操作表和数据

# 关于编码
    # 数据库有一些默认的配置
    # 查看默认的配置们
    # mysql> show variables;
    # mysql> show variables like '%charac%';
    # mysql> set character_set_server = utf8;
        # 在内存中临时设置server端默认的编码,重启会失效
        # 也可以直接把character_set_server = utf8;写到my.ini文件中,永久生效

    # create table 如果不指定就是用默认的编码
    # 指定字符编码也可以创建表,编码的设置只对这张表生效
    # create table 表名(字段 数据类型 约束) charset = utf8;


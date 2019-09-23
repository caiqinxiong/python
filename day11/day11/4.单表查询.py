# select * from 表;
# 百分之99.9999999的概率是需要从表中筛选数据显示的
# 筛选数据 -> 条件

# select
    # select 后面永远跟着的是列的名字;
    # select 筛选字段的名字来指定你要查询的字段
    # select id,emp_name from employee;
    # 四则运算 select emp_name,salary*12 from employee;
    # 重命名 select emp_name as name,salary*12 from employee;
    # 重命名 select emp_name as name,salary*12 as annual_salary from employee;
    # 重命名 select emp_name name,salary*12 annual_salary from employee;
    # 拼接函数 select concat('abc','|||','cde');
        # select concat(emp_name,':',salary) from employee;
    # 去重 distinct
        # select distinct post from employee;
        # select distinct age,post from employee;

# where条件的筛选 根据值/范围约束
    # 根据数值范围查询 > < >= <= != <> = between a and b
    # select * from employee where age=18
    # select * from employee where age='18'  # 可以但是效率差
        # 年龄小于25的
        # select * from employee where age<25;
        # 薪资大于8000的
        # select * from employee where salary>8000;
        # 薪资在10000到20000之间
        # select * from employee where salary between 10000 and 20000;
    # 根据精准的范围查询 in
        # 25 28 78
        # select * from employee where age in (25,28,78);
    # 模糊查询 - like
        # 通配符 % 表示任意长度任意内容
            # select * from employee where emp_name like '程%'
        # 通配符 _ 表示任意1个字符的任意内容
            # select * from employee where emp_name like '程__'
            # select * from employee where emp_name like '程_'
    # 模糊查询 - 正则查询 regexp
        # select * from employee where emp_name regexp '^程';
# 条件的组合 与或非
    #  and 与
        # 找到年龄在25岁以上的所有老师
        # select * from employee where age>25 and post='teacher';
        # 找到年龄在25岁以上的所有老师的姓名
        # select emp_name from employee where age>25 and post='teacher';
    #  or  或
        # 找到所有的女性或者年龄小于20岁的人
        # select * from employee where sex = 'female' or age<20;
    #  not 非
        # 找到年龄不是18,78岁的人
        # select * from employee where age not in (18,78)
# NULL是mysql中的一个关键字
    # NULL不能用 = !=判断
    # 需要用is /is not判断
# 练习讲解:
# 4. 查看岗位描述不为NULL的员工信息
# select * from employee where post_comment is not null;

# 5.查看岗位是teacher且薪资是10000或9000或30000的员工姓名、年龄、薪资
# select * from employee where salary =9000 or salary =10000 or salary = 30000
# select emp_name,age,salary from employee where salary in (30000,9000,10000) and post = 'teacher'

# 聚合函数
    # avg求平均 sum求和 min求最小 max求最大 count计数
    # select avg(salary) from employee;

# 分组 group by 分组之后数据只和被分组的字段有关系,和具体的每一条数据没有关系
    # select * from employee group by post;
    # 求每个部门的人的平均工资
    # select post,avg(salary) from employee group by post;

# 练习
# 查询岗位名以及岗位包含的所有员工名字
    # select * from employee group by post;
    # select post,group_concat(emp_name) from employee group by post;

# 找到employee表中,各部门年龄大于20的平均薪资是多少
# select post,avg(salary) from employee where age>20 group by post

# HAVING 过滤 总是在分组之后才执行过滤条件
# 求平均年龄大于30岁的部门
# select post,avg(age)  from employee group by post having avg(age)>30
# 求平均薪资大于1w的部门
# select post,avg(salary) from employee group by post having avg(salary)>10000;

# order by 排序
# 将选出来的数据根据某一个字段排序,默认是升序(从小到大),desc是倒序
# select * from 表 order by age;  # 升序
# select * from 表 order by age asc;  # 升序
# select * from 表 order by age desc;  # 降序

# limit 取前n个
# select * from 表 order by age limit 3;
# select * from 表 order by age desc limit 3;

# 从m开始,取n个
# select * from 表 order by age limit 9,3;
    # 是从第10条开始,取3条,第10,11,12条会被取出来
# select * from 表 order by age limit 3 offset 9;
    # 是从第10条开始,取3条,第10,11,12条会被取出来

# select
# distinct
# from
# where
# group by
# having
# order by
# limit
# offset
import pymysql

# 获取用户输入
username = input("输入用户名：")
pwd = input("请输入密码：")


# 连接数据库检索有没有该用户
conn = pymysql.connect(
    host="localhost",
    port=3306,
    database="userinfo",
    user="root",
    password="123456",
    charset="utf8"
)

cursor = conn.cursor()  # 获取光标
# 拼接要执行的SQL语句
sql = "select * from info where username='%s' and password='%s'" % (username, pwd)
print(sql)
print("=" * 120)
# 执行SQL语句
ret = cursor.execute(sql)
if ret:
    print("登录成功")
else:
    print("登录失败！")
# 关闭光标对像
cursor.close()
# 关闭连接
conn.close()

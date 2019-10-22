import pymysql

conn = pymysql.connect(
    host="localhost",
    port=3306,
    database="userinfo",
    user="root",
    password="123456",
    charset="utf8"
)

cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 指定返回的数据格式为字典格式

sql = "select * from info"

cursor.execute(sql)  # 返回的不是具体的数据而是受影响的行数
# ret = cursor.fetchall()  # 返回所有的数据
# ret = cursor.fetchone()  # 返回第一条的数据
# print(ret)
# ret = cursor.fetchone()  # 返回一条的数据
# print(ret)
# ret = cursor.fetchone()  # 返回一条的数据
# print(ret)
# ret = cursor.fetchone()  # 返回一条的数据
# print(ret)
# ret = cursor.fetchone()  # 返回一条的数据
# print(ret)
# ret = cursor.fetchone()  # 返回一条的数据
# print(ret)
# ret = cursor.fetchone()  # 返回一条的数据
# print(ret)

ret = cursor.fetchmany(3)  # 查询具体多少条数据
print(ret)
# cursor.scroll(0, mode="absolute")  # 绝对移动，写多少就是移到多少
cursor.scroll(-1, mode="relative")
ret = cursor.fetchall()
print(ret)
cursor.close()
conn.close()

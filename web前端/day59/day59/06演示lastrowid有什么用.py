import pymysql

conn = pymysql.connect(
    host="localhost",
    port=3306,
    database="userinfo",
    user="root",
    password="123456",
    charset="utf8"
)

cursor = conn.cursor()
# 创建班级的sql语句
sql1 = "insert into class (name) VALUES (%s)"
# 创建学生的sql语句
sql2 = "insert into student (name, cid) VALUES (%s, %s)"


cursor.execute(sql1, "全栈9期")
new_id = cursor.lastrowid  # 获取刚插入数据的ID值
cursor.execute(sql2, ["小东北", new_id])

conn.commit()
cursor.close()
conn.close()

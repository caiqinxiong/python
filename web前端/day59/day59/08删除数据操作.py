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

# sql = "delete from info WHERE username=%s"
sql = "delete from info WHERE id=%s"

cursor.execute(sql,8)

conn.commit()
cursor.close()
conn.close()

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

sql = "update info set password=%s where username=%s"

cursor.execute(sql,["123456", "小东北"])

conn.commit()
cursor.close()
conn.close()

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
sql = "insert into info (username, password) VALUES (%s, %s)"

data = [("alex1", "dashabi"), ("污Sir1",), ("xiaoyima1", "nvshen")]
try:
    cursor.executemany(sql, data)  # 内部实现for循环，批量执行插入语句
    # for i in data:
    #     cursor.execute(sql, i)
    conn.commit()  # 提交一次
except Exception as e:
    print("错啦！")
    conn.rollback()

cursor.close()
conn.close()

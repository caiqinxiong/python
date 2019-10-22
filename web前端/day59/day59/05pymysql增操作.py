"""
pymysql增操作
"""

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

# 拼接语句
sql = "insert into info (username, password)VALUES (%s, %s)"
# 执行
try:
    cursor.execute(sql, ["大旭",])
    # 自己写个for循环 (今天作业自己试下)
    conn.commit()
except Exception as e:
    print("报错啦：",str(e))
    conn.rollback()  # 回滚
# 对数据库做写操作一定要记得提交assword

cursor.close()
conn.close()



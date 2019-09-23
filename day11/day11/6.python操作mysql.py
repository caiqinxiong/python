import pymysql

# conn = pymysql.connect(host='127.0.0.1', user='root', password="123456",
#                  database='py27_day11')
# cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
# cur = conn.cursor()
# cur.execute('select * from emp')
# print(cur.fetchone())
# print(cur.fetchone())
# print(cur.fetchone())
# print(cur.fetchone())  # 如果没有了就为None

# ret = cur.fetchmany(2)
# print(ret)

# ret = cur.fetchall()
# print(ret)
# cur.close()
# conn.close()

# 修改或者写入数据
# conn = pymysql.connect(host='127.0.0.1', user='root', password="123456",
#                  database='py27_day11')
# cur = conn.cursor()
# cur.execute('insert into t1 values (111,222)')
# conn.commit()  # insert update delete 提交数据才能生效
# cur.close()
# conn.close()

# num1 = input('num1>')
# sql = 'select * from t1 where a=%s and b =%s'
# conn = pymysql.connect(host='127.0.0.1', user='root', password="123456",
#                 database='py27_day11')
# cur = conn.cursor()
# cur.execute(sql,(num1,2))
# print(cur.fetchall())
# cur.close()
# conn.close()
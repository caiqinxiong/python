import pymysql

username = input("输入用户名：")
pwd = input("请输入密码：")

# if username == "erge" and pwd == "dashabi":
#     print("登陆成功！")
# else:
#     print("滚~")

# 拿到用户输入的用户名密码

# 去数据库里面判断用户名和密码是否正确
# 1. 连接数据库
conn = pymysql.connect(
    host="localhost",
    port=3306,  # 端口号是数字类型
    database="userinfo",  # 写自己本地的数据库名字
    user="root",
    password="123456",
    charset="utf8"   # 千万记得没有-
)

cursor = conn.cursor()  # 获取输入SQL语句的光标对象
sql = "select * from info;"
ret = cursor.execute(sql)
print(ret)
# 关闭连接
cursor.close()
conn.close()


# 2. 判断 --> 只需要把检索条件写到sql语句中，去数据库执行就可以了

# with open("userinfo.txt", "r", encoding="utf-8") as f:
#     for line in f:
#         # print(line.strip())
#         u, p = line.strip().split("|")
#         if u == username and p == pwd:
#             print("登陆成功！")
#             break
#     else:
#         print("go out~")

username = input("输入用户名：")
pwd = input("请输入密码：")

# if username == "erge" and pwd == "dashabi":
#     print("登陆成功！")
# else:
#     print("滚~")


with open("userinfo.txt", "r", encoding="utf-8") as f:
    for line in f:
        # print(line.strip())
        u, p = line.strip().split("|")
        if u == username and p == pwd:
            print("登陆成功！")
            break
    else:
        print("go out~")

# -*- coding: utf-8 -*-
product_list = [["1 电脑",1999],["2 鼠标",10],["3 键盘",20],["4 滑板鞋", 998],["5 肉松饼", 3]] #定义一个商品清单列表
purchased_list = [] #已经购买的列表
recharge_amount = input("请输入充值金额: ")
if not recharge_amount.isdigit():   #判断输入的金额是否为数字形式
    exit()
salary = int(recharge_amount)
yuer = salary #余额
for i in product_list:      #打印输出商品列表
    print(i)

buyindex = ""   #创建一个空的字符串，存储输入
while True:
    buy = input("请输入选择商品的序号,'q'是退出,'n'是结算: ")

    if buy.isdigit():
        buyindex = int(buy)
        if buyindex < 1 or buyindex > len(product_list):
            print("输入有误，请重新输入.")
            continue
    elif buy.upper() == "Q":  ##将输入的字符大写，满足用户可以随意输入大小写
            print("退出程序")
            print("----------------购物车结算-------------------")
            for j in purchased_list:
                print(j)
            spend = salary - yuer  ##计算用户消费多少钱了
            print("你已经购买了以上的商品。您本次总共消费:%f元，剩余金额为：%f元" % (spend, yuer))
            exit()

    elif buy.upper() == "N":
        print("----------------购物车结算-------------------")
        for j in purchased_list:
            print(j)
        spend = salary - yuer
        print("你已经购买了以上的商品。您本次总共消费:%f元，剩余金额为：%f元" % (spend, yuer))
        exit()
    else:
        print("输入有误，请重新输入")
        continue
    price = product_list[buyindex - 1][1]  #取出用户选择商品的价格
    if (price > yuer):  ##增加输出打印当前已购买商品，方便用户选择
        print("您的余额不够，剩余：%f，请删除商品." % yuer)
        print("----------------购物车清单-------------------")
        for j in purchased_list:
            print(j)
        spend = salary - yuer
        print("你已经购买了以上的商品。目前总共消费:%f元，剩余金额为：%f元" % (spend, yuer))
        delnumber = input("请输入你要删除的商品序号: ")

        if delnumber.isdigit():
            delnumber = int(delnumber)
            if product_list[delnumber - 1] in purchased_list:
                price = product_list[delnumber - 1][1]    #取出用户选择删除商品的价格
                yuer = yuer + price
                purchased_list.remove(product_list[delnumber - 1]) ##从购物车中删除用户选择的商品
                print("删除成功，删除商品为: \n" + (product_list[delnumber - 1][0]))
                continue

            else:
                print("输入的商品序号出错，或者你的购物车里没有此商品，请重新购物")


    elif (price <= yuer):
        yuer = yuer - price
        purchased_list.append(product_list[buyindex - 1])   ##从商品列表中添加用户选择的商品到购物车中
        print("购买成功，购买商品为：\n" + product_list[buyindex - 1][0])


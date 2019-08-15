#!/usr/bin/env python
# coding:utf-8
# Auto :lijincheng
#  shopping
goods = [
    ("笔记本电脑", 10000),
    ("iphone x",8000 ),
    ("显示器", 3000),
    ("耳机", 1200),
    ("音响", 1500),
    ("鼠标", 200)
]
global leng
leng = len(goods)

while True:
    money = input("请输入您要充值的金额： ")
    shopping_cart = []  # 初始化购物车
    if len(money) == 0:
        print("你输入的金额为空，请输入充值金额： ")
        break
    elif not money.isdigit():
        print("你输入金额不合法，请重新输入： ")
        break
    else:
        print("你的账号余额为：%s" % (money))
        print("===== 商品清单列表 =====： ")
        print("序号  商品名称   价格 ")
        for x, y in enumerate(goods):
            print(x, y[0], y[1])

    while True:
        num = input("请选择购买商品的序号，结算商品请输入n,退出购物请输入exit：").strip()
        if num == "n":
            print(shopping_cart)
        elif num == "exit":
            break
        elif int(num) > (leng-1):
            print("您输入的序号超过范围，请重新输入：")
        else:
            # num = int(num)
            money = int(money)
            # shop = goods[int(num)]
            if int(num) == 0 and money > int(goods[int(num)][1]):
                shopping_cart.append(goods[int(num)])
                print(shopping_cart)
                money -= goods[int(num)][1]
                print("你的账号余额为：%s"% (money))

            elif int(num) == 1 and money > int(goods[int(num)][1]):
                shopping_cart.append(goods[int(num)])
                print(shopping_cart)
                money -= goods[int(num)][1]
                print("你的账号余额为：%s" % (money))

            elif int(num) == 2 and money > int(goods[int(num)][1]):
                shopping_cart.append(goods[int(num)])
                print(shopping_cart)
                money -= goods[int(num)][1]
                print("你的账号余额为：%s" % (money))

            elif int(num) == 3 and money > int(goods[int(num)][1]):
                shopping_cart.append(goods[int(num)])
                print(shopping_cart)
                money -= goods[int(num)][1]
                print("你的账号余额为：%s" % (money))

            elif int(num) == 4 and money > int(goods[int(num)][1]):
                shopping_cart.append(goods[int(num)])
                print(shopping_cart)
                money -= goods[int(num)][1]
                print("你的账号余额为：%s" % (money))

            elif int(num) == 5 and money > int(goods[int(num)][1]):
                shopping_cart.append(goods[int(num)])
                print(shopping_cart)
                money -= goods[int(num)][1]
                print("你的账号余额为：%s" % (money))

            elif num =="n":
                print(shopping_cart)

            elif (num == "q") or (num == "Q"):
                break

            else:
                print("\033[30;42m你的余额不足了,好好工作，努力挣钱吧.\033[0m")
                print( "您的余额还剩下:\033[30;41m %s\033[0m"% (money))

    break
print("=======您所购的商品如下=======")
print("商品名称  价格  数量")
for x, y in enumerate(shopping_cart):
    print(y[0], y[1], y[0].count(y[0]))
print("\033[30;43m欢迎再次光临.\033[0m")